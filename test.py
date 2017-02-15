#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

d = pq("""
<div class="al_txt">
            <p>塔罗牌是西方的智慧占卜方法，旨在探讨宇宙和生命的变化，本文与各位塔罗牌占卜爱好者共同分享塔罗牌牌意解释，希望在塔罗占卜时能够给予您有益的启发。</p>
<p>塔罗牌占卜充满着西方艺术和文化的风貌，通过塔罗占卜能预测你的人生、爱情和未来，也可以深入一个人的内心，挖掘其心理和精神的隐秘发展方向，还可以揭开神秘的精神层面，透过塔罗牌的象征图案打开潜意识之门。 </p>
<p>据说，可以通过塔罗牌的神秘暗示，寻求自己的力量、超越或限制，指引自己的思想、行动朝着更积极的光明一面，使内心和外在世界充满和谐与平衡。</p>

<li><a href="/xingzuo/taluopai/31378.html" target="_blank">塔罗牌五角星国王解释，塔罗牌解释【五角星国王】</a></li>
<li><a href="/xingzuo/taluopai/31377.html" target="_blank">塔罗牌五角星皇后解释，塔罗牌解释【五角星皇后】</a></li>
<li><a href="/xingzuo/taluopai/31376.html" target="_blank">塔罗牌五角星骑士解释，塔罗牌解释【五角星骑士】</a></li>
<li><a href="/xingzuo/taluopai/31375.html" target="_blank">塔罗牌五角星侍卫解释，塔罗牌解释【五角星侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31373.html" target="_blank">塔罗牌五角星10解释，塔罗牌解释【五角星10】</a></li>
<li><a href="/xingzuo/taluopai/31372.html" target="_blank">塔罗牌五角星9解释，塔罗牌解释【五角星9】</a></li>
<li><a href="/xingzuo/taluopai/31371.html" target="_blank">塔罗牌五角星8解释，塔罗牌解释【五角星8】</a></li>
<li><a href="/xingzuo/taluopai/31370.html" target="_blank">塔罗牌五角星7解释，塔罗牌解释【五角星7】</a></li>
<li><a href="/xingzuo/taluopai/31369.html" target="_blank">塔罗牌五角星6解释，塔罗牌解释【五角星6】</a></li>
<li><a href="/xingzuo/taluopai/31368.html" target="_blank">塔罗牌五角星5解释，塔罗牌解释【五角星5】</a></li>
<li><a href="/xingzuo/taluopai/31367.html" target="_blank">塔罗牌五角星4解释，塔罗牌解释【五角星4】</a></li>
<li><a href="/xingzuo/taluopai/31366.html" target="_blank">塔罗牌五角星3解释，塔罗牌解释【五角星3】</a></li>
<li><a href="/xingzuo/taluopai/31365.html" target="_blank">塔罗牌五角星2解释，塔罗牌解释【五角星2】</a></li>
<li><a href="/xingzuo/taluopai/31364.html" target="_blank">塔罗牌五角星1解释，塔罗牌解释【五角星1】</a></li>
<li><a href="/xingzuo/taluopai/31363.html" target="_blank">塔罗牌宝剑国王解释，塔罗牌解释【宝剑国王】</a></li>
<li><a href="/xingzuo/taluopai/31362.html" target="_blank">塔罗牌宝剑皇后解释，塔罗牌解释【宝剑皇后】</a></li>
<li><a href="/xingzuo/taluopai/31360.html" target="_blank">塔罗牌宝剑骑士解释，塔罗牌解释【宝剑骑士】</a></li>
<li><a href="/xingzuo/taluopai/31359.html" target="_blank">塔罗牌宝剑侍卫解释，塔罗牌解释【宝剑侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31358.html" target="_blank">塔罗牌宝剑10解释，塔罗牌解释【宝剑10】</a></li>
<li><a href="/xingzuo/taluopai/31357.html" target="_blank">塔罗牌宝剑9解释，塔罗牌解释【宝剑9】</a></li>
<li><a href="/xingzuo/taluopai/31356.html" target="_blank">塔罗牌宝剑8解释，塔罗牌解释【宝剑8】</a></li>
<li><a href="/xingzuo/taluopai/31355.html" target="_blank">塔罗牌宝剑7解释，塔罗牌解释【宝剑7】</a></li>
<li><a href="/xingzuo/taluopai/31352.html" target="_blank">塔罗牌宝剑6解释，塔罗牌解释【宝剑6】</a></li>
<li><a href="/xingzuo/taluopai/31351.html" target="_blank">塔罗牌宝剑5解释，塔罗牌解释【宝剑5】</a></li>
<li><a href="/xingzuo/taluopai/31350.html" target="_blank">塔罗牌宝剑4解释，塔罗牌解释【宝剑4】</a></li>
<li><a href="/xingzuo/taluopai/31349.html" target="_blank">塔罗牌宝剑3解释，塔罗牌解释【宝剑3】</a></li>
<li><a href="/xingzuo/taluopai/31348.html" target="_blank">塔罗牌宝剑2解释，塔罗牌解释【宝剑2】</a></li>
<li><a href="/xingzuo/taluopai/31347.html" target="_blank">塔罗牌宝剑1解释，塔罗牌解释【宝剑1】</a></li>
<li><a href="/xingzuo/taluopai/31346.html" target="_blank">塔罗牌圣杯国王解释，塔罗牌解释【圣杯国王】</a></li>
<li><a href="/xingzuo/taluopai/31345.html" target="_blank">塔罗牌圣杯皇后解释，塔罗牌解释【圣杯皇后】</a></li>
<li><a href="/xingzuo/taluopai/31344.html" target="_blank">塔罗牌圣杯骑士解释，塔罗牌解释【圣杯骑士】</a></li>
<li><a href="/xingzuo/taluopai/31343.html" target="_blank">塔罗牌圣杯侍卫解释，塔罗牌解释【圣杯侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31342.html" target="_blank">塔罗牌圣杯10解释，塔罗牌解释【圣杯10】</a></li>
<li><a href="/xingzuo/taluopai/31341.html" target="_blank">塔罗牌圣杯9解释，塔罗牌解释【圣杯9】</a></li>
<li><a href="/xingzuo/taluopai/31340.html" target="_blank">塔罗牌圣杯8解释，塔罗牌解释【圣杯8】</a></li>
<li><a href="/xingzuo/taluopai/31339.html" target="_blank">塔罗牌圣杯7解释，塔罗牌解释【圣杯7】</a></li>
<li><a href="/xingzuo/taluopai/31338.html" target="_blank">塔罗牌圣杯6解释，塔罗牌解释【圣杯6】</a></li>
<li><a href="/xingzuo/taluopai/31337.html" target="_blank">塔罗牌圣杯5解释，塔罗牌解释【圣杯5】</a></li>
<li><a href="/xingzuo/taluopai/31336.html" target="_blank">塔罗牌圣杯4解释，塔罗牌解释【圣杯4】</a></li>
<li><a href="/xingzuo/taluopai/31335.html" target="_blank">塔罗牌圣杯3解释，塔罗牌解释【圣杯3】</a></li>
<li><a href="/xingzuo/taluopai/31334.html" target="_blank">塔罗牌圣杯2解释，塔罗牌解释【圣杯2】</a></li>
<li><a href="/xingzuo/taluopai/31333.html" target="_blank">塔罗牌圣杯1解释，塔罗牌解释【圣杯1】</a></li>
<li><a href="/xingzuo/taluopai/31332.html" target="_blank">塔罗牌权杖国王解释，塔罗牌解释【权杖国王】</a></li>
<li><a href="/xingzuo/taluopai/31331.html" target="_blank">塔罗牌权杖皇后解释，塔罗牌解释【权杖皇后】</a></li>
<li><a href="/xingzuo/taluopai/31330.html" target="_blank">塔罗牌权杖骑士解释，塔罗牌解释【权杖骑士】</a></li>
<li><a href="/xingzuo/taluopai/31329.html" target="_blank">塔罗牌权杖侍卫解释，塔罗牌解释【权杖侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31328.html" target="_blank">塔罗牌权杖10解释，塔罗牌解释【权杖10】</a></li>
<li><a href="/xingzuo/taluopai/31327.html" target="_blank">塔罗牌权杖9解释，塔罗牌解释【权杖9】</a></li>
<li><a href="/xingzuo/taluopai/31326.html" target="_blank">塔罗牌权杖8解释，塔罗牌解释【权杖8】</a></li>
<li><a href="/xingzuo/taluopai/31325.html" target="_blank">塔罗牌权杖7解释，塔罗牌解释【权杖7】</a></li>
<li><a href="/xingzuo/taluopai/31324.html" target="_blank">塔罗牌权杖6解释，塔罗牌解释【权杖6】</a></li>
<li><a href="/xingzuo/taluopai/31323.html" target="_blank">塔罗牌权杖5解释，塔罗牌解释【权杖5】</a></li>
<li><a href="/xingzuo/taluopai/31322.html" target="_blank">塔罗牌权杖4解释，塔罗牌解释【权杖4】</a></li><li><a href="/xingzuo/taluopai/31378.html" target="_blank">塔罗牌五角星国王解释，塔罗牌解释【五角星国王】</a></li>
<li><a href="/xingzuo/taluopai/31377.html" target="_blank">塔罗牌五角星皇后解释，塔罗牌解释【五角星皇后】</a></li>
<li><a href="/xingzuo/taluopai/31376.html" target="_blank">塔罗牌五角星骑士解释，塔罗牌解释【五角星骑士】</a></li>
<li><a href="/xingzuo/taluopai/31375.html" target="_blank">塔罗牌五角星侍卫解释，塔罗牌解释【五角星侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31373.html" target="_blank">塔罗牌五角星10解释，塔罗牌解释【五角星10】</a></li>
<li><a href="/xingzuo/taluopai/31372.html" target="_blank">塔罗牌五角星9解释，塔罗牌解释【五角星9】</a></li>
<li><a href="/xingzuo/taluopai/31371.html" target="_blank">塔罗牌五角星8解释，塔罗牌解释【五角星8】</a></li>
<li><a href="/xingzuo/taluopai/31370.html" target="_blank">塔罗牌五角星7解释，塔罗牌解释【五角星7】</a></li>
<li><a href="/xingzuo/taluopai/31369.html" target="_blank">塔罗牌五角星6解释，塔罗牌解释【五角星6】</a></li>
<li><a href="/xingzuo/taluopai/31368.html" target="_blank">塔罗牌五角星5解释，塔罗牌解释【五角星5】</a></li>
<li><a href="/xingzuo/taluopai/31367.html" target="_blank">塔罗牌五角星4解释，塔罗牌解释【五角星4】</a></li>
<li><a href="/xingzuo/taluopai/31366.html" target="_blank">塔罗牌五角星3解释，塔罗牌解释【五角星3】</a></li>
<li><a href="/xingzuo/taluopai/31365.html" target="_blank">塔罗牌五角星2解释，塔罗牌解释【五角星2】</a></li>
<li><a href="/xingzuo/taluopai/31364.html" target="_blank">塔罗牌五角星1解释，塔罗牌解释【五角星1】</a></li>
<li><a href="/xingzuo/taluopai/31363.html" target="_blank">塔罗牌宝剑国王解释，塔罗牌解释【宝剑国王】</a></li>
<li><a href="/xingzuo/taluopai/31362.html" target="_blank">塔罗牌宝剑皇后解释，塔罗牌解释【宝剑皇后】</a></li>
<li><a href="/xingzuo/taluopai/31360.html" target="_blank">塔罗牌宝剑骑士解释，塔罗牌解释【宝剑骑士】</a></li>
<li><a href="/xingzuo/taluopai/31359.html" target="_blank">塔罗牌宝剑侍卫解释，塔罗牌解释【宝剑侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31358.html" target="_blank">塔罗牌宝剑10解释，塔罗牌解释【宝剑10】</a></li>
<li><a href="/xingzuo/taluopai/31357.html" target="_blank">塔罗牌宝剑9解释，塔罗牌解释【宝剑9】</a></li>
<li><a href="/xingzuo/taluopai/31356.html" target="_blank">塔罗牌宝剑8解释，塔罗牌解释【宝剑8】</a></li>
<li><a href="/xingzuo/taluopai/31355.html" target="_blank">塔罗牌宝剑7解释，塔罗牌解释【宝剑7】</a></li>
<li><a href="/xingzuo/taluopai/31352.html" target="_blank">塔罗牌宝剑6解释，塔罗牌解释【宝剑6】</a></li>
<li><a href="/xingzuo/taluopai/31351.html" target="_blank">塔罗牌宝剑5解释，塔罗牌解释【宝剑5】</a></li>
<li><a href="/xingzuo/taluopai/31350.html" target="_blank">塔罗牌宝剑4解释，塔罗牌解释【宝剑4】</a></li>
<li><a href="/xingzuo/taluopai/31349.html" target="_blank">塔罗牌宝剑3解释，塔罗牌解释【宝剑3】</a></li>
<li><a href="/xingzuo/taluopai/31348.html" target="_blank">塔罗牌宝剑2解释，塔罗牌解释【宝剑2】</a></li>
<li><a href="/xingzuo/taluopai/31347.html" target="_blank">塔罗牌宝剑1解释，塔罗牌解释【宝剑1】</a></li>
<li><a href="/xingzuo/taluopai/31346.html" target="_blank">塔罗牌圣杯国王解释，塔罗牌解释【圣杯国王】</a></li>
<li><a href="/xingzuo/taluopai/31345.html" target="_blank">塔罗牌圣杯皇后解释，塔罗牌解释【圣杯皇后】</a></li>
<li><a href="/xingzuo/taluopai/31344.html" target="_blank">塔罗牌圣杯骑士解释，塔罗牌解释【圣杯骑士】</a></li>
<li><a href="/xingzuo/taluopai/31343.html" target="_blank">塔罗牌圣杯侍卫解释，塔罗牌解释【圣杯侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31342.html" target="_blank">塔罗牌圣杯10解释，塔罗牌解释【圣杯10】</a></li>
<li><a href="/xingzuo/taluopai/31341.html" target="_blank">塔罗牌圣杯9解释，塔罗牌解释【圣杯9】</a></li>
<li><a href="/xingzuo/taluopai/31340.html" target="_blank">塔罗牌圣杯8解释，塔罗牌解释【圣杯8】</a></li>
<li><a href="/xingzuo/taluopai/31339.html" target="_blank">塔罗牌圣杯7解释，塔罗牌解释【圣杯7】</a></li>
<li><a href="/xingzuo/taluopai/31338.html" target="_blank">塔罗牌圣杯6解释，塔罗牌解释【圣杯6】</a></li>
<li><a href="/xingzuo/taluopai/31337.html" target="_blank">塔罗牌圣杯5解释，塔罗牌解释【圣杯5】</a></li>
<li><a href="/xingzuo/taluopai/31336.html" target="_blank">塔罗牌圣杯4解释，塔罗牌解释【圣杯4】</a></li>
<li><a href="/xingzuo/taluopai/31335.html" target="_blank">塔罗牌圣杯3解释，塔罗牌解释【圣杯3】</a></li>
<li><a href="/xingzuo/taluopai/31334.html" target="_blank">塔罗牌圣杯2解释，塔罗牌解释【圣杯2】</a></li>
<li><a href="/xingzuo/taluopai/31333.html" target="_blank">塔罗牌圣杯1解释，塔罗牌解释【圣杯1】</a></li>
<li><a href="/xingzuo/taluopai/31332.html" target="_blank">塔罗牌权杖国王解释，塔罗牌解释【权杖国王】</a></li>
<li><a href="/xingzuo/taluopai/31331.html" target="_blank">塔罗牌权杖皇后解释，塔罗牌解释【权杖皇后】</a></li>
<li><a href="/xingzuo/taluopai/31330.html" target="_blank">塔罗牌权杖骑士解释，塔罗牌解释【权杖骑士】</a></li>
<li><a href="/xingzuo/taluopai/31329.html" target="_blank">塔罗牌权杖侍卫解释，塔罗牌解释【权杖侍卫】</a></li>
<li><a href="/xingzuo/taluopai/31328.html" target="_blank">塔罗牌权杖10解释，塔罗牌解释【权杖10】</a></li>
<li><a href="/xingzuo/taluopai/31327.html" target="_blank">塔罗牌权杖9解释，塔罗牌解释【权杖9】</a></li>
<li><a href="/xingzuo/taluopai/31326.html" target="_blank">塔罗牌权杖8解释，塔罗牌解释【权杖8】</a></li>
<li><a href="/xingzuo/taluopai/31325.html" target="_blank">塔罗牌权杖7解释，塔罗牌解释【权杖7】</a></li>
<li><a href="/xingzuo/taluopai/31324.html" target="_blank">塔罗牌权杖6解释，塔罗牌解释【权杖6】</a></li>
<li><a href="/xingzuo/taluopai/31323.html" target="_blank">塔罗牌权杖5解释，塔罗牌解释【权杖5】</a></li>
<li><a href="/xingzuo/taluopai/31322.html" target="_blank">塔罗牌权杖4解释，塔罗牌解释【权杖4】</a></li>
<li><a href="/xingzuo/taluopai/31321.html" target="_blank">塔罗牌权杖3解释，塔罗牌解释【权杖3】</a></li>
<li><a href="/xingzuo/taluopai/31320.html" target="_blank">塔罗牌权杖2解释，塔罗牌解释【权杖2】</a></li>
<li><a href="/xingzuo/taluopai/31319.html" target="_blank">塔罗牌权杖1解释，塔罗牌解释【权杖1】</a></li>
<li><a href="/xingzuo/taluopai/31318.html" target="_blank">塔罗牌世界解释，塔罗牌解释【世界】</a></li>
<li><a href="/xingzuo/taluopai/31317.html" target="_blank">塔罗牌审判解释，塔罗牌解释【审判】</a></li>
<li><a href="/xingzuo/taluopai/31316.html" target="_blank">塔罗牌太阳解释，塔罗牌解释【太阳】</a></li>
<li><a href="/xingzuo/taluopai/31315.html" target="_blank">塔罗牌月亮解释，塔罗牌解释【月亮】</a></li>
<li><a href="/xingzuo/taluopai/31314.html" target="_blank">塔罗牌星星解释，塔罗牌解释【星星】</a></li>
<li><a href="/xingzuo/taluopai/31313.html" target="_blank">塔罗牌高塔解释，塔罗牌解释【高塔】</a></li>
<li><a href="/xingzuo/taluopai/31310.html" target="_blank">塔罗牌恶魔解释，塔罗牌解释【恶魔】</a></li>
<li><a href="/xingzuo/taluopai/31309.html" target="_blank">塔罗牌节制解释，塔罗牌解释【节制】</a></li>
<li><a href="/xingzuo/taluopai/31308.html" target="_blank">塔罗牌死神解释，塔罗牌解释【死神】</a></li>
<li><a href="/xingzuo/taluopai/31307.html" target="_blank">塔罗牌悬吊者解释，塔罗牌解释【悬吊者】</a></li>
<li><a href="/xingzuo/taluopai/31306.html" target="_blank">塔罗牌正义解释，塔罗牌解释【正义】</a></li>
<li><a href="/xingzuo/taluopai/31305.html" target="_blank">塔罗牌命运之轮解释，塔罗牌解释【命运之轮】</a></li>
<li><a href="/xingzuo/taluopai/31304.html" target="_blank">塔罗牌隐士解释，塔罗牌解释【隐士】</a></li>
<li><a href="/xingzuo/taluopai/31303.html" target="_blank">塔罗牌力量解释，塔罗牌解释【力量】</a></li>
<li><a href="/xingzuo/taluopai/31302.html" target="_blank">塔罗牌战车解释，塔罗牌解释【战车】</a></li>
<li><a href="/xingzuo/taluopai/31301.html" target="_blank">塔罗牌恋人解释，塔罗牌解释【恋人】</a></li>
<li><a href="/xingzuo/taluopai/31300.html" target="_blank">塔罗牌教皇解释，塔罗牌解释【教皇】</a></li>
<li><a href="/xingzuo/taluopai/31299.html" target="_blank">塔罗牌皇帝解释，塔罗牌解释【皇帝】</a></li>
<li><a href="/xingzuo/taluopai/31298.html" target="_blank">塔罗牌女皇解释，塔罗牌解释【女皇】</a></li>
<li><a href="/xingzuo/taluopai/31297.html" target="_blank">塔罗牌女教皇解释，塔罗牌解释【女教皇】</a></li>
<li><a href="/xingzuo/taluopai/31296.html" target="_blank">塔罗牌魔术师解释，塔罗牌解释【魔术师】</a></li>
<li><a href="/xingzuo/taluopai/31295.html" target="_blank">塔罗牌愚人解释，塔罗牌解释【愚人】</a></li>
<li><a href="/xingzuo/taluopai/31321.html" target="_blank">塔罗牌权杖3解释，塔罗牌解释【权杖3】</a></li>
<li><a href="/xingzuo/taluopai/31320.html" target="_blank">塔罗牌权杖2解释，塔罗牌解释【权杖2】</a></li>
<li><a href="/xingzuo/taluopai/31319.html" target="_blank">塔罗牌权杖1解释，塔罗牌解释【权杖1】</a></li>
<li><a href="/xingzuo/taluopai/31318.html" target="_blank">塔罗牌世界解释，塔罗牌解释【世界】</a></li>
<li><a href="/xingzuo/taluopai/31317.html" target="_blank">塔罗牌审判解释，塔罗牌解释【审判】</a></li>
<li><a href="/xingzuo/taluopai/31316.html" target="_blank">塔罗牌太阳解释，塔罗牌解释【太阳】</a></li>
<li><a href="/xingzuo/taluopai/31315.html" target="_blank">塔罗牌月亮解释，塔罗牌解释【月亮】</a></li>
<li><a href="/xingzuo/taluopai/31314.html" target="_blank">塔罗牌星星解释，塔罗牌解释【星星】</a></li>
<li><a href="/xingzuo/taluopai/31313.html" target="_blank">塔罗牌高塔解释，塔罗牌解释【高塔】</a></li>
<li><a href="/xingzuo/taluopai/31310.html" target="_blank">塔罗牌恶魔解释，塔罗牌解释【恶魔】</a></li>
<li><a href="/xingzuo/taluopai/31309.html" target="_blank">塔罗牌节制解释，塔罗牌解释【节制】</a></li>
<li><a href="/xingzuo/taluopai/31308.html" target="_blank">塔罗牌死神解释，塔罗牌解释【死神】</a></li>
<li><a href="/xingzuo/taluopai/31307.html" target="_blank">塔罗牌悬吊者解释，塔罗牌解释【悬吊者】</a></li>
<li><a href="/xingzuo/taluopai/31306.html" target="_blank">塔罗牌正义解释，塔罗牌解释【正义】</a></li>
<li><a href="/xingzuo/taluopai/31305.html" target="_blank">塔罗牌命运之轮解释，塔罗牌解释【命运之轮】</a></li>
<li><a href="/xingzuo/taluopai/31304.html" target="_blank">塔罗牌隐士解释，塔罗牌解释【隐士】</a></li>
<li><a href="/xingzuo/taluopai/31303.html" target="_blank">塔罗牌力量解释，塔罗牌解释【力量】</a></li>
<li><a href="/xingzuo/taluopai/31302.html" target="_blank">塔罗牌战车解释，塔罗牌解释【战车】</a></li>
<li><a href="/xingzuo/taluopai/31301.html" target="_blank">塔罗牌恋人解释，塔罗牌解释【恋人】</a></li>
<li><a href="/xingzuo/taluopai/31300.html" target="_blank">塔罗牌教皇解释，塔罗牌解释【教皇】</a></li>
<li><a href="/xingzuo/taluopai/31299.html" target="_blank">塔罗牌皇帝解释，塔罗牌解释【皇帝】</a></li>
<li><a href="/xingzuo/taluopai/31298.html" target="_blank">塔罗牌女皇解释，塔罗牌解释【女皇】</a></li>
<li><a href="/xingzuo/taluopai/31297.html" target="_blank">塔罗牌女教皇解释，塔罗牌解释【女教皇】</a></li>
<li><a href="/xingzuo/taluopai/31296.html" target="_blank">塔罗牌魔术师解释，塔罗牌解释【魔术师】</a></li>
<li><a href="/xingzuo/taluopai/31295.html" target="_blank">塔罗牌愚人解释，塔罗牌解释【愚人】</a></li>

<p>本文地址：http://www.8s8s.com/xingzuo/taluopai/31311.html</p>
		</div>

	""")

from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TaroSmall(Base):
    __tablename__ = 'taro_small'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)
    meaning = Column(String)
    love0 = Column(String)
    love1 = Column(String)
    health0 = Column(String)
    health1 = Column(String)
    work0 = Column(String)
    work1 = Column(String)
    wealth0 = Column(String)
    wealth1 = Column(String)
    person0 = Column(String)
    person1 = Column(String)
    look0 = Column(String)
    look1 = Column(String)
    img = Column(String)

class TaroBig (Base):
    __tablename__ = 'taro_big'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)
    meaning = Column(String)
    love0 = Column(String)
    love1 = Column(String)
    work0 = Column(String)
    work1 = Column(String)
    wealth0 = Column(String)
    wealth1 = Column(String)
    person0 = Column(String)
    person1 = Column(String)
    img = Column(String)
    card= Column(String)
    xingzuo = Column(String)
    yuansu = Column(String)

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/mywebsite')

DBSession = sessionmaker(bind=engine)
session = DBSession()


l = 0
names=[]
for i in d('li > a'):
    print l

    print d(i).attr('href')
    d = pq('http://www.8s8s.com/%s' % d(i).attr('href'))
    table = d('body > div.astro > div.als > div.al_txt > table')
    name = table.find('tr:nth-child(1) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    key = table.find('tr:nth-child(2) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    meaning = table.find('tr:nth-child(3) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    love0 = table.find('tr:nth-child(5) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    love1 = table.find('tr:nth-child(12) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    health0 = table.find('tr:nth-child(9) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    health1 = table.find('tr:nth-child(16) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    work0 = table.find('tr:nth-child(7) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    work1 = table.find('tr:nth-child(14) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    wealth0 = table.find('tr:nth-child(6) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    wealth1 = table.find('tr:nth-child(13) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    person0 = table.find('tr:nth-child(4) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    person1 = table.find('tr:nth-child(11) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    look0 = table.find('tr:nth-child(8) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    look1 = table.find('tr:nth-child(15) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk','ignore').encode('utf-8')
    img = ''
    if not name in names:
        l += 1
        print len(key)
        if len(key)!=3:
            newTaro = TaroSmall( name=name,key=key,meaning=meaning,love0=love0,love1=love1,health0=health0,health1=health1,work0=work0,
                    work1=work1,wealth0=wealth0,wealth1=wealth1,person0=person0,person1=person1,look0=look0,look1=look1)
        else:
            name = table.find('tr:nth-child(1) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                            'ignore').encode(
                'utf-8')
            yuansu = table.find('tr:nth-child(2) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                           'ignore').encode(
                'utf-8')
            card = table.find('tr:nth-child(3) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                           'ignore').encode(
                'utf-8')
            xingzuo = table.find('tr:nth-child(4) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                           'ignore').encode(
                'utf-8')
            key = table.find('tr:nth-child(6) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                           'ignore').encode(
                'utf-8')
            meaning = table.find('tr:nth-child(5) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                               'ignore').encode(
                'utf-8')
            love0 = table.find('tr:nth-child(8) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                             'ignore').encode(
                'utf-8')
            love1 = table.find('tr:nth-child(12) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                              'ignore').encode(
                'utf-8')

            work0 = table.find('tr:nth-child(10) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                             'ignore').encode(
                'utf-8')
            work1 = table.find('tr:nth-child(14) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                              'ignore').encode(
                'utf-8')
            wealth0 = table.find('tr:nth-child(9) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                               'ignore').encode(
                'utf-8')
            wealth1 = table.find('tr:nth-child(13) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                                'ignore').encode(
                'utf-8')
            person0 = table.find('tr:nth-child(7) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                               'ignore').encode(
                'utf-8')
            person1 = table.find('tr:nth-child(11) > td:nth-child(2)').text().encode('latin1', 'ignore').decode('gbk',
                                                                                                                'ignore').encode(
                'utf-8')

            img = ''
            newTaro = TaroBig( name=name,key=key,meaning=meaning,love0=love0,love1=love1,work0=work0,
                    work1=work1,wealth0=wealth0,wealth1=wealth1,person0=person0,person1=person1,card=card,yuansu=yuansu,xingzuo=xingzuo)

        session.add(newTaro)
        session.commit()
        names.append(name)
session.close()


    # r=requests.get('http://home.so-net.net.tw/wwlcom/02/%s' % d(i).attr('href'))
    # tree = etree.HTML(r.text.encode('latin1', 'ignore').decode('big5').encode('utf-8'))
    # nodes = tree.xpath("/html/body/table[4]/tr/td/div/dd[5]/table/tr[2]/td[2]")
    # print nodes
    # print 'A'
    # name = d(d('font')[0]).text().encode('latin1', 'ignore').decode('big5').encode('utf-8').split(' ')[0]
    # subName = d(d('font')[0]).text().encode('latin1', 'ignore').decode('big5').encode('utf-8').split(' ')[1][1:-1]
    # eName = d(d('font')[3]).text().encode('latin1', 'ignore').decode('big5').encode('utf-8')
    # key = d(d('font')[4]).text().encode('latin1', 'ignore').decode('big5').encode('utf-8')
    # meaning = d(d('font')[5]).text().encode('latin1', 'ignore').decode('big5').encode('utf-8')
    # if d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(2) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8'):
    #     love0 =  d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(2) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     love1 =  d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(2) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     health0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(3) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     health0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(3) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     work0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(4) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     work1 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(4) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     fun0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(5) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     fun1 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(5) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     other0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(6) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     other1 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(6) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     result0 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(7) > td:nth-child(2) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')
    #     result1 = d('body > table:nth-child(4) > tr > td > div').find('table > tr:nth-child(7) > td:nth-child(3) > font').text()\
    #     .encode('latin1', 'ignore').decode('big5').encode('utf-8')

    # print result1