
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>WEB1</title>
 </head>
 <body>

<?php

if(@$_GET['flag'] == "iphone_flag")
	echo "<center><h3>Ура! Ты всё таки купил Iphone 7! Поздравляю!</h3>
	<img src=iphone7.jpg style='height:400px;'/>
	<h1>А вот и флаг: InnoCTF{1ph0ne7_w45_5ucc35fu11y_buy3d}</h1>";
else 
	echo "<p>Логин или пароль введены не верно!</p>  <a href=./> Вернуться назад</a>";
?>
</body></html>
