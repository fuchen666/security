@echo off
title windows信息收集
echo [+] windows信息收集
set "hostname=>null&&hostname"
set "whoami=>null&&whoami"
set "whoamiall=>null&&whoami /all"
set "systeminfo=>null&&systeminfo"
set "ipconfig=>null&&ipconfig /all"
set "route=>null&&route print"
set "netstat=>null&&netstat -ano"
set "paths=>null&&path"
set "users=>null&&net users"
set "domain=>null&&net user /domain"
set "localgroup=>null&&net localgroup"
set "administratosgroup=>null&&net localgroup Administrators"
set "accounts=>null&&net accounts"
set "arp=>null&&arp -a"
set "view=>null&&net view"
set "tasklist=>null&&tasklist /svc"
set "netsh=>null&&netsh firewall show config"
pause
echo ^<html^> >> save.html
echo ^<head^> >> save.html
echo ^<style^> >> save.html 
echo ^.divcss5^{ border:0px solid #00F; height:120px; width:200px;word-wrap:break-word^} >> save.html
echo ^</style^> >> save.html
echo ^<title^> >> save.html
echo 信息收集的结果 >> save.html
echo ^</title^> >> save.html 
echo ^<body^> >> save.html
echo ^<h3^> >> save.html
echo %hostname% >> save.html
echo 收集的结果 >> save.html
echo ^</h3^> >> save.html
echo ^<div class="divcss5"^> >> save.html 
echo ^<table border="1" style="background:gray"^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 主机名 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %hostname% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 当前用户 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %whoami% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 当前用户、群组和权限 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %whoamiall% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 一般系统的信息 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %systeminfo% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo IP和网络 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %ipconfig% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 路由表 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %route% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 网络连接信息 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %netstat% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 路径 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %paths% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 用户 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %users% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 在域内的用户 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %doamin% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 组名 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %localgroup% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 管理员组里的用户 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %administratosgroup% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 名单的密码政策locahost >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %accounts% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo ARP表 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %arp% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 网络里的共享主机 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %view% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 正在执行任务 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %tasklist% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^<tr^> >> save.html
echo ^<td^> >> save.html
echo 防火墙配置 >> save.html
echo ^</td^> >> save.html
echo ^<td^> >> save.html
echo %netsh% >> save.html
echo ^</td^> >> save.html
echo ^</tr^> >> save.html
echo ^</table^> >> save.html
echo ^</div^> >> save.html
echo ^</body^> >> save.html
echo ^</html^> >> save.html
