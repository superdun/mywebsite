
#华理创客空间网站
个人为华理创客空间搭建的组织网站，目标是实现信息展示，仪器实时预约，组织报名，活动报名等功能
<br><br>
##使用的基本技术
###前端：
html5,css,JavaScript为基本技术，预约报名等功能采用了AJAX技术,采用了采用了bootstrap前端框架，Jinjia2模板，提高了维护性
###后端：
python2.7的flask框架，Jinjia2模板.<br><br>
##域名：
使用花生壳内网穿透的免费二级域名，服务器搭建于树莓派（内容维护中，暂不可访问）
##使用方法
*服务器架设：python2.7环境，flask库，运行flask1.py，网站即运行于127.0.0.1：8080  

*维护信息：在static/相应文件夹，将信息图片（jpg）与信息文本（txt）命以相同文件名，信息文本中第一行输入标题，其余为内容。即可实现网站内容更新（AJAX）  
  
*报名/预约：服务器会自动将报名信息发送至设定好的管理员邮箱  
  
##效果图片   
![mahua](https://github.com/superdun/mywebsite/raw/master/exp_pics/1.jpg)
![mahua](https://github.com/superdun/mywebsite/raw/master/exp_pics/2.jpg)
![mahua](https://github.com/superdun/mywebsite/raw/master/exp_pics/3.jpg)
