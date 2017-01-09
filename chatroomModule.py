# -*- coding: utf-8 -*-
from flask import session
from moduleGlobal import socketio, redis_store
from flask_socketio import emit, join_room, leave_room
import moduleTextFilter

import hashlib
import time
import random
import string
import json


@socketio.on('joined', namespace='/randomchat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.','status':'ok','name':name}, room=room)


@socketio.on('text', namespace='/randomchat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    msg = message['msg']
    filter = moduleTextFilter.Filter()
    filter.parse('static/keywords.txt')
    msg = filter.filter(msg)
    rawChatRecord = redis_store.get(room)
    if rawChatRecord:
        chatRecord=json.loads(rawChatRecord)
        chatRecord[name]['count'] = chatRecord[name]['count']+1
        redis_store.set(room,json.dumps(chatRecord))

    emit('message', {'msg':  msg,'name':name}, room=room)


@socketio.on('left', namespace='/randomchat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    # name = session.get('name')
    # redis_store.set('waitingRoom', '')
    # redis_store.delete(session.get('room'))
    # leave_room(room)
    redis_store.delete(room)
    emit('status', {'msg': u'对方下线了，页面即将刷新,找寻新的小伙伴,T__T','status':'failed'}, room=room)


@socketio.on('disconnect', namespace='/randomchat')
def disconnect():

    room = session.get('room')
    # if redis_store.get(room+'Count')==1:
    #     redis_store.delete(room)
    #     redis_store.delete(room+'Count')
    # redis_store.set('waitingRoom','')
    #
    #
    redis_store.delete(room)
    emit('status', {'msg': u'对方下线了，页面即将刷新,找寻新的小伙伴,T__T', 'status': 'failed'}, room=room)

@socketio.on('date', namespace='/randomchat')
def date(message):
    room = session.get('room')
    name = session.get('name')
    rawChatRecord = redis_store.get(room)
    if rawChatRecord:
        chatRecord=json.loads(rawChatRecord)
        ACount = chatRecord['A']['count']
        BCount = chatRecord['B']['count']

        if ACount>20 and BCount>20 :

            if chatRecord[name]['detail'] == '':
                chatRecord[name]['detail']={'realName':message['realName'],'phone':message['phone']}
                redis_store.set(room,json.dumps(chatRecord))
                if chatRecord['A']['detail'] != '' and chatRecord['B']['detail']!= '':
                    emit('dateResult', {'msg':u'你们成功交换了联系方式,对方的','A': u'名字：%s,电话：%s'%(chatRecord['A']['detail']['realName'],chatRecord['A']['detail']['phone']),
                                        'B':u'名字：%s,电话：%s'%(chatRecord['B']['detail']['realName'],chatRecord['B']['detail']['phone']),'status':'ok'} ,room=room)
                else:
                    emit('dateResult', {'msg':u'发送成功，在对方也决意交换联系方式之前，你的联系方式不会显示给对方','status':'waiting'})
            else:
                emit('dateResult', {'msg': u'您已经发送过，不要重复发送','status':'failed'})
        else:
            emit('dateResult', {'msg': u'再聊聊才能交换联系方式哦','status':'failed'})
    else:
        emit('dateResult', {'msg': u'现在就你自己，和谁交换联系方式？请耐心等待', 'status': 'failed'})


    print chatRecord[name]['detail']

def makeRoomNumber():
    md5 = hashlib.md5()
    md5.update(str(time.time()) + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)))
    return md5.hexdigest()


socket = socketio
