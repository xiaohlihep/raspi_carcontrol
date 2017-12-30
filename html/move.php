<?php 

$M="";
$T=1;
$P=0.5;

if(isset($_GET['M']))
{
	$M=$_GET['M'];
}
if(isset($_GET['T']))
{
	$T=$_GET['T'];
}
if(isset($_GET['P']))
{
	$P=$_GET['P'];
}
if($M!="")
{
	$cmd='nohup sudo /usr/bin/gpio.py '.$M.' '.$T.' '.$P;
	exec($cmd);
	echo "done";
}
else
{
	echo "invalid request";
}




?>
