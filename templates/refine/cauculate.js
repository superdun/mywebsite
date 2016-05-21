/**
 * Created by li on 2015/6/21.
 */
window.onload=function(){
    cauculate.init();
};
var cauculate={
    init:function(){
        $('#canvas').hide();
        draw.init()
    },
    open:function(){
        $('#inform').hide()
    },
    start:function(){
        cauculate.getvalue();
        step.init();
        cauculate.writevalue();
    },
    getvalue:function(){
        cauculate.alpha=parseFloat(document.getElementById("alpha").value);
        cauculate.f=parseFloat(document.getElementById('F').value);
        cauculate.d=parseFloat(document.getElementById('D').value);
        cauculate.w=parseFloat(document.getElementById('W').value);
        cauculate.l=parseFloat(document.getElementById('L').value);
        cauculate.v=parseFloat(document.getElementById('V').value);
        cauculate.l2=parseFloat(document.getElementById('L2').value);
        cauculate.v2=parseFloat(document.getElementById('V2').value);
        cauculate.r=parseFloat(document.getElementById('R').value);
        cauculate.q=parseFloat(document.getElementById('q').value);
        cauculate.xf=parseFloat(document.getElementById('xF').value);
        cauculate.xd=parseFloat(document.getElementById('xD').value);
        cauculate.xw=parseFloat(document.getElementById('xW').value);
        cauculate.faia=parseFloat(document.getElementById('faia').value);
        cauculate.faib=parseFloat(document.getElementById('faib').value);
        cauculate.caichulv=parseFloat(document.getElementById('caichulv').value);
        cauculate.tlyqb=parseFloat(document.getElementById('tlyqb').value);
        cauculate.jlyqb=parseFloat(document.getElementById('jlyqb').value);
        if(!cauculate.f&&!cauculate.d&&!cauculate.w){
            cauculate.f=1
        }
    },
    writevalue:function(){
        document.getElementById("alpha").value= cauculate.alpha;
        document.getElementById('F').value=cauculate.f;
        document.getElementById('D').value=cauculate.d;
        document.getElementById('W').value=cauculate.w;
        document.getElementById('L').value=cauculate.l;
        document.getElementById('V').value=cauculate.v;
        document.getElementById('L2').value=cauculate.l2;
        document.getElementById('V2').value=cauculate.v2;
        document.getElementById('R').value=cauculate.r;
        document.getElementById('q').value=cauculate.q;
        document.getElementById('xF').value=cauculate.xf;
        document.getElementById('xD').value=cauculate.xd;
        document.getElementById('xW').value=cauculate.xw;
        document.getElementById('faia').value=cauculate.faia;
        document.getElementById('faib').value=cauculate.faib;
        document.getElementById('caichulv').value=cauculate.caichulv;
        document.getElementById('tlyqb').value=cauculate.tlyqb;
        document.getElementById('jlyqb').value=cauculate.jlyqb;
        document.getElementById('jlline').value=cauculate.jlline;
        document.getElementById('tlline').value=cauculate.tlline;
        document.getElementById('qline').value=cauculate.qline;
        document.getElementById('rmin').value=cauculate.rmin;
        document.getElementById('xphline').value=cauculate.xphline;
        document.getElementById('Rmini').value=cauculate.rmin;
        document.getElementById('qaxy').value=cauculate.qax+','+cauculate.qay;

    },
    round:function(x){
        return (Math.round(x*1000))/1000;
    },
    q1:function(){
        switch (document.getElementById('condition').value){
            case '饱和蒸汽':
                cauculate.q=0;
                break;
            case '泡点进料':
                cauculate.q=1;
                break;
            case '气液混合物':
                cauculate.q=null;
                break;
            case '冷液进料':
                cauculate.q=null;
                break;
            case '过热蒸汽进料':
                cauculate.q=null;
                break;
        }
        document.getElementById("q").value=cauculate.q;
    },
    q2:function(){
        cauculate.q=parseFloat(document.getElementById('q').value);
        $('option').attr('selected',false);
        switch (true){
            case cauculate.q===1:
                document.getElementById('condition').value='泡点进料';
                break;
            case cauculate.q===0:
                document.getElementById('condition').value='饱和蒸汽';
                break;
            case cauculate.q>1:
                document.getElementById('condition').value='冷液进料';
                break;
            case cauculate.q<1&&cauculate.q>0:
                document.getElementById('condition').value='气液混合物';
                break;
            case cauculate.q<0:
                document.getElementById('condition').value='过热蒸汽进料';
                break;
        }
    }
};
var step={
    init: function () {
        step.xph();
        step.fwd();
        step.lines();
        step.rmin()
    },
    xph:function(){
        cauculate.xphline="y="+cauculate.alpha+"x/(1+"+(cauculate.alpha-1)+"x)"
    },
    fwd:function() {
        switch (true) {
            case cauculate.f>0 && cauculate.xd>0 && cauculate.xf>0&& cauculate.xw>0:
                cauculate.d = cauculate.round(cauculate.f * (cauculate.xf - cauculate.xw) / (cauculate.xd - cauculate.xw));
                cauculate.w = cauculate.round(cauculate.f - cauculate.d);
                cauculate.faia = cauculate.round(cauculate.d * cauculate.xd / (cauculate.f * cauculate.xf));
                cauculate.faib = cauculate.round(cauculate.w * (1 - cauculate.xw) / (cauculate.f * (1 - cauculate.xf)));
                cauculate.caichulv = cauculate.round((cauculate.xf - cauculate.xw) / (cauculate.xd - cauculate.xw));
                break;
            case cauculate.faia>0 && cauculate.xd>0 && cauculate.xf>0 && cauculate.f>0:
                cauculate.d =cauculate.round(cauculate.f * cauculate.faia * cauculate.xf / cauculate.xd);
                cauculate.w = cauculate.round(cauculate.f - cauculate.d);
                cauculate.xw =cauculate.round((cauculate.f * cauculate.xf - cauculate.d * cauculate.xd) / cauculate.w);
                cauculate.caichulv = cauculate.round((cauculate.xf - cauculate.xw) / (cauculate.xd - cauculate.xw));
                cauculate.faib = cauculate.round(cauculate.w * (1 - cauculate.xw) / (cauculate.f * (1 - cauculate.xf)));
                break;
            case cauculate.faib>0 && cauculate.xw>0 && cauculate.xf>0 && cauculate.f>0:
                cauculate.w = cauculate.round(cauculate.f * cauculate.faib * (1-cauculate.xf) / (1-cauculate.xw));
                cauculate.d = cauculate.round(cauculate.f - cauculate.w);
                cauculate.xd = cauculate.round((cauculate.f * cauculate.xf - cauculate.w * cauculate.xw) / cauculate.d);
                cauculate.caichulv = cauculate.round((cauculate.xf - cauculate.xw) / (cauculate.xd - cauculate.xw));
                cauculate.faia = cauculate.round(cauculate.w * (1 - cauculate.xw) / (cauculate.f * (1 - cauculate.xf)));
                break;
            case cauculate.faia>0 && cauculate.faib>0 && cauculate.xf>0:
                cauculate.w = cauculate.round(cauculate.faib * cauculate.f * (1 - cauculate.xf) + (1 - cauculate.faia) * cauculate.f * cauculate.xf);
                cauculate.d = cauculate.round(cauculate.f - cauculate.w);
                cauculate.xd = cauculate.round(cauculate.faia * cauculate.f * cauculate.xf / cauculate.d);
                cauculate.xw = cauculate.round((1 - cauculate.faia) * cauculate.f * cauculate.xf / cauculate.w);
                cauculate.caichulv = cauculate.round((cauculate.xf - cauculate.xw) / (cauculate.xd - cauculate.xw));
                break;
        }

    },
    lines:function(){
        switch (cauculate.q){
            case 1:
                cauculate.qline="x="+cauculate.xf;
                break;
            case 0:
                cauculate.qline="y="+cauculate.xf;
                break;
            default :
                if(cauculate.xf/(cauculate.q-1)>0){
                    cauculate.qline="y="+cauculate.round(cauculate.q/(cauculate.q-1))+"x-"+cauculate.round(cauculate.xf/(cauculate.q-1));
                }
                else{
                    cauculate.qline="y="+cauculate.round(cauculate.q/(cauculate.q-1))+"x+"+cauculate.round((cauculate.xf/(cauculate.q-1))*-1);
                }
        }
        if(cauculate.tlyqb>0&&!(cauculate.r>0)){
            cauculate.r=cauculate.round(((1-cauculate.tlyqb)*cauculate.q*cauculate.f+(cauculate.f-cauculate.d)*cauculate.tlyqb)/((cauculate.tlyqb-1)*cauculate.d))
        }
        if(cauculate.jlyqb>0&&!(cauculate.r>0)){
            cauculate.r=cauculate.round(cauculate.jlyqb/(1-cauculate.jlyqb))
        }
        cauculate.l=cauculate.round(cauculate.r*cauculate.d);
        cauculate.v=cauculate.l+cauculate.d;
        if(!(cauculate.jlyqb>0)){
            cauculate.jlyqb=cauculate.round(cauculate.l/cauculate.v);
        }
        cauculate.jlline="y="+cauculate.round(cauculate.l/cauculate.v)+"x+"+cauculate.round(cauculate.d*cauculate.xd/cauculate.v);
        cauculate.l2=cauculate.round(cauculate.l+cauculate.q*cauculate.f);
        cauculate.v2=cauculate.round(cauculate.v-(1-cauculate.q)*cauculate.f);
        if(!(cauculate.tlyqb>0)){
            cauculate.tlyqb=cauculate.round(cauculate.l2/cauculate.v2);
        }
        cauculate.tlline='y='+cauculate.round(cauculate.l2/cauculate.v2)+'x-'+cauculate.round(cauculate.w*cauculate.xw/cauculate.v2);
    },
    rmin:function(){
        if(cauculate.q===1){
            cauculate.rmin=cauculate.round(1/(cauculate.alpha-1)*(cauculate.xd/cauculate.xf-cauculate.alpha*(1-cauculate.xd)/(1-cauculate.xf)));
            cauculate.qax=cauculate.xf;
            cauculate.qay=cauculate.round(cauculate.alpha*cauculate.qax/(1+(cauculate.alpha-1)*cauculate.qax))
        }
        if(cauculate.q===0){
            cauculate.rmin=cauculate.round(1/(cauculate.alpha-1)*(cauculate.xd*cauculate.alpha/cauculate.xf-(1-cauculate.xd)/(1-cauculate.xf)));
            cauculate.qay=cauculate.xf;
            cauculate.qax=cauculate.round(cauculate.qay/(cauculate.alpha-cauculate.qay*(cauculate.alpha-1)))
        }
        if(cauculate.q!==1&&cauculate.q!==0){
            var a=cauculate.alpha;
            var F=cauculate.xf;
            var q=cauculate.q;
            var C=q-a*F+F;
            var D=q-1;
            var A=Math.pow(C/D-a,2)+4*F*q*(a-1)/((q-1)*(q-1));
            var B=(1-q)*Math.sqrt(A)+a*(q-1)+a*F-F-q;
            cauculate.qax=B/(2*q*(a-1));
            cauculate.qay=cauculate.round(a*cauculate.qax/(1+(a-1)*cauculate.qax));
            cauculate.rmin=cauculate.round((cauculate.xd-cauculate.qay)/(cauculate.qay-cauculate.qax));
            if(cauculate.rmin<0){
                B=(q-1)*Math.sqrt(A)+a*(q-1)+a*F-F-q;
                cauculate.qax=B/(2*q*(a-1));
                cauculate.qay=cauculate.round(a*cauculate.qax/(1+(a-1)*cauculate.qax));
                cauculate.rmin=cauculate.round((cauculate.xd-cauculate.qay)/(cauculate.qay-cauculate.qax));
            }
        }
    }
};
