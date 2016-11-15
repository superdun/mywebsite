window.onload=function(){
    game.init()
};

var game = {

    init:function(){
        $('#loadLayer').show()
        $('#gameLayer').hide()
        $('#overLayer').hide()
        game.height = $(window).height()-20
        $('#cowboy').attr('height',game.height);
        $('#loadLayer').height(game.height);
        $('#overLayer').height(game.height);
        game.width = $(window).width()-20
        $('#cowboy').attr('width',game.width);
        $('#loadLayer').width(game.width);
        $('#overLayer').width(game.width);


        game.ctx=document.getElementById("cowboy").getContext("2d");
        

        loader.loadResource();
        

    },
    start:function(){
        draw.init()
        game.timer_1=setInterval(game.draw,18);
    },
    draw:function(){
        draw.bg()
    }
}

var draw = {
    init:function(){
        draw.bgY = game.bg.height
    },
    bg:function(){
        if (draw.bgY<=game.height){
            game.ctx.drawImage(game.bg,0,0,game.bg.width,draw.bgY,0,game.height-draw.bgY,game.width,draw.bgY);
            game.ctx.drawImage(game.bg,0,game.bg.height-(game.height-draw.bgY),game.bg.width,game.height-draw.bgY,0,0,game.width,game.height-draw.bgY);
            draw.bgY-=3
            if(draw.bgY<=0){
                draw.bgY = game.bg.height

            }
        }
        else{
            game.ctx.drawImage(game.bg,0,draw.bgY-game.height,game.bg.width,game.height,0,0,game.width,game.height);
            draw.bgY-=3
        }

        
    }
}


var loader = {

    loadResource:function(){
        game.loadcount = 0
        game.totalcount = 0
        game.bg=new Image();
        game.totalcount++;
        game.bg.src="{{url_for('static', filename='demos/cowboy/img/bg.jpg')}}";
        game.bg.onload=function(){
            loader.loadercount()
        };
    },
    loadercount:function(){
        game.loadcount++;
        
        $("p").html("载入中："+game.loadcount+"/"+game.totalcount);
        if(game.loadcount===game.totalcount){
            game.start();
            $("#loadLayer").hide()
            $("#gameLayer").show()
        }
    }
    
}