function xianshishuzi(){document.getElementById("shuzi").innerHTML=document.getElementById("length").value};
setInterval(xianshishuzi,10);

var girlname=['蝶','樱','莹','萤','滢','莺','璎','韵','舞','莎','姗','黛','丽','娜','瑷','妮','娥','惠','茹','香','艳','花','茉','蕊','娥','妲','馨','倩','恋','妙'];
var boyname=['漓','殇','梦','阑','雪','凪','爱','羽','魑','蔷','海','雨','悠','紫','岚','晗','薰','柊','茵','钰','雅','夏','绪','栩','珣','菀','琬','梧','霆','诗','丝','洛','温','蒂','璃','安','洁','莉','灵','血','魅','塔','利','亚','伤','瑟','薇','玫','瑰','泪','邪','儿','凡','多','姆','威','恩','影','琉','蕾','玥','曦','月','蓝','琦','凤','颜','鸢','希','玖','兮','烟','叶','兰','凝','冰','伊','如','落','心','语','凌','陌','千','优','晶','墨','阳','云','筱','残','莲','沫','渺','琴','依','然','可','黎','幽','幻','银','倾','乐','慕','文','思','清','碎','音','芊','怡','苏','城','萌','美','迷','离','白','嫩','风','霜','萝','妖','百','合','珠','喃','之','情','弥','绯','芸','茜','魂','澪','琪','欣','咝','蠫','赬','飖','呗','缈','娅','吉','拉','斯','基','柔','朵','铃','裳','纱','塲','颖','觞','蕴','燢','覮','铧','累','觷','儠','摋','孆','瞲','櫗','刿','鷡','氩','浅','趯','鸑','萦','儽','骅','糜','婺','嚻','龠','鹦','韎','麴','莳','寂','翼','巧','哀','俏','涅','盘','辰','芝','艾','柒','曼','妲','眉','御','寇','米','菲','奥','格','萨','尼','子','克','乃','湿'];
var gmname=boyname.concat(girlname)
var data1=""
function start(){
var mytr1=document.getElementById("tr1")
var mytr2=document.getElementById("tr2")
if(document.getElementById("jieguo1")){mytr1.removeChild(document.getElementById("jieguo1"));
mytr2.removeChild(document.getElementById("jieguo2"))
}

var finalname=""
if(document.getElementById("xingbie").value=="male"){finalname=boyname;
data1="汤姆苏"}
else{finalname=gmname;
data1="玛丽苏"};
var fnl=finalname.length
var namechengguo=""
if(!document.getElementById("xing").value){if(!document.getElementById("ming").value){alert("请输入您尊贵的姓和名！")}
else{alert("请输入您尊贵的姓！")}}
else{if(!document.getElementById("ming").value){alert("请输入您尊贵的名！")}
else{
	for(var i=0;i<=document.getElementById("length").value-3;i++){
	var a=Math.round(Math.random()*3)
	if(a==0){a=1}
	var namelength=finalname
	var siname=""
	for(var j=0;j<=a;j++){siname+=finalname[Math.round(Math.random()*fnl)]}
	if(i<document.getElementById("length").value-3){namechengguo+=siname+"·"}
	else{namechengguo+=siname}//去掉最后的点
	}//for
	var newtd=document.createElement("td")
    var newinput=document.createElement("td")
    newtd.setAttribute("id","jieguo1")
  	newinput.setAttribute("id","jieguo2")

	
	mytr1.appendChild(newtd)
	mytr2.appendChild(newinput)
	var name1=document.getElementById("xing").value+"·"+namechengguo+"·"+document.getElementById("ming").value
	document.getElementById("jieguo1").innerHTML="您的"+data1+"名字为："
	document.getElementById("jieguo2").innerHTML=name1

}//else
}//else
}//func