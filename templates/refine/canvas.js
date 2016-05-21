var draw={
    init:function(){
        draw.ctx=document.getElementById('pic').getContext('2d');
        draw.ctx.strokeStyle='black';
        draw.ctx.strokeRect(0,0,500,500);
        draw.ctx.translate(0,500);
    },
    open:function(){
        cauculate.getvalue();
        draw.xphx=[0];
        draw.xphy=[0];
        draw.qx=[];
        draw.qy=[];
        draw.dx=0;
        draw.dy=0;
        draw.jlx=[];
        draw.jly=[];
        $('#canvas').show();
        draw.ctx.strokeStyle="red";
        draw.xphline();
        draw.ctx.strokeStyle="blue";
        draw.qline();
        draw.ctx.strokeStyle="#8E388E";
        draw.jlline();
        draw.tlline();
        draw.ctx.strokeStyle="black";
        draw.stair()
    },
    close:function(){
        $('#canvas').hide();
        draw.ctx.clearRect(0,0,500,-500)
    },
    xphline:function(){
        draw.ctx.beginPath();
        draw.ctx.moveTo(0,0);
        draw.ctx.lineTo(500,-500);
        draw.ctx.closePath();
        draw.ctx.stroke();
        for(var i=0;i<=500;i++){
            var j=Math.round(((cauculate.alpha*i/500)/(1+(cauculate.alpha-1)*i/500))*500);
            draw.xphx.push(i/500);
            var a=draw.xphy.push(j/500);
            draw.ctx.strokeStyle='red';
            draw.ctx.beginPath();
            draw.ctx.moveTo(500*draw.xphx[a-2],500*draw.xphy[a-2]*-1);
            draw.ctx.lineTo(500*draw.xphx[a-1],500*draw.xphy[a-1]*-1);
            draw.ctx.closePath();
            draw.ctx.stroke();
        }
    },
    qline:function(){
        for(var i=0;i<=500;i++){
            switch (cauculate.q){
                case 1:
                    draw.ctx.beginPath();
                    draw.ctx.moveTo(500*cauculate.xf,0);
                    draw.ctx.lineTo(500*cauculate.xf,-500);
                    draw.ctx.closePath();
                    draw.ctx.stroke();
                    break;
                case 0:
                    j=cauculate.xf*500;
                    draw.qx.push(i/500);
                    var a=draw.qy.push(j/500);
                    draw.ctx.beginPath();
                    draw.ctx.moveTo(500*draw.qx[a-2],500*draw.qy[a-2]*-1);
                    draw.ctx.lineTo(500*draw.qx[a-1],500*draw.qy[a-1]*-1);
                    draw.ctx.closePath();
                    draw.ctx.stroke();
                    break;
                default :
                    var j=Math.round(((cauculate.q/(cauculate.q-1))*i/500-cauculate.xf/(cauculate.q-1))*500);
                    draw.qx.push(i/500);
                    var a=draw.qy.push(j/500);
                    draw.ctx.beginPath();
                    draw.ctx.moveTo(500*draw.qx[a-2],500*draw.qy[a-2]*-1);
                    draw.ctx.lineTo(500*draw.qx[a-1],500*draw.qy[a-1]*-1);
                    draw.ctx.closePath();
                    draw.ctx.stroke()
            }
        }
    },
    jlline:function(){
        for(var i=0;i<=cauculate.xd*500;i++){
            var j=Math.round(((cauculate.l/cauculate.v)*i/500+cauculate.xd*cauculate.d/cauculate.v)*500);
            draw.jlx.push(i/500);
            var a=draw.jly.push(j/500);
            draw.ctx.beginPath();
            draw.ctx.moveTo(500*draw.jlx[a-2],500*draw.jly[a-2]*-1);
            draw.ctx.lineTo(500*draw.jlx[a-1],500*draw.jly[a-1]*-1);
            draw.ctx.closePath();
            draw.ctx.stroke();
            if(cauculate.q===1){
                draw.dx=cauculate.xf;
                draw.dy=Math.round(((cauculate.l/cauculate.v)*cauculate.xf+cauculate.xd*cauculate.d/cauculate.v)*500)/500;

            }
            else{
                if(Math.abs(500*draw.qy[draw.qx.indexOf(i/500)]-j)<=1){
                    draw.dx=i/500;
                    draw.dy=j/500
                }
            }
        }
    },
    tlline:function(){
        draw.ctx.beginPath();
        draw.ctx.moveTo(500*draw.dx,-500*draw.dy);
        draw.ctx.lineTo(500*cauculate.xw,-500*cauculate.xw);
        draw.ctx.closePath();
        draw.ctx.stroke()
    },
    stair:function(){
        var ax=cauculate.xd;
        var ay=cauculate.xd;
        while(ax>cauculate.xw){
            draw.ctx.moveTo(500*ax,-500*ay);
            draw.ctx.lineTo((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500,-500*ay);
            draw.ctx.closePath();
            draw.ctx.stroke();
            if(Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)<=draw.dx*500){
                draw.ctx.moveTo(Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500),-500*ay);
                draw.ctx.lineTo(Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500),-1*Math.round(((cauculate.l2/cauculate.v2)*Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500-cauculate.xw*cauculate.w/cauculate.v2)*500));
                draw.ctx.closePath();
                draw.ctx.stroke();
                ax=Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500;
                ay=Math.round(((cauculate.l2/cauculate.v2)*Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500-cauculate.xw*cauculate.w/cauculate.v2)*500)/500
            }
            else{
                draw.ctx.moveTo(Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500),-500*ay);
                draw.ctx.lineTo(Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500),-1*Math.round(((cauculate.l/cauculate.v)*Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500+cauculate.xd*cauculate.d/cauculate.v)*500));
                draw.ctx.closePath();
                draw.ctx.stroke();
                ax=Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500;
                ay=Math.round(((cauculate.l/cauculate.v)*Math.round((ay/(cauculate.alpha-ay*(cauculate.alpha-1)))*500)/500+cauculate.xd*cauculate.d/cauculate.v)*500)/500
            };console.log(ax);console.log(ay)
        }
    },
};