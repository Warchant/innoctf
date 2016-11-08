
<html>
<head>
<meta charset="utf-8">

</head>
<body>
<br /><br />
<br>

<center>
<?php

$model = 'IPHONE7';

if(isset($_GET['submit'])){
	if($model == strtoupper($_GET['model'])){
		//redirect
		header('Location: admin.php?flag=iphone_flag');
		
	} 
	else
	{
		switch(@$_GET['model'])
		{
			case "alcatel":
				$img = "alcatel";
				break;
			case "motorola":
				$img = "motorola";
				break;
			case "nokia":
				$img = "nokia";
				break;
			case "texet":
				$img = "texet";
				break;
			case "sony_ericsson":
				$img = "se";
				break;
			case "siemens":
				$img = "siemens";
				break;
			default:
				$img = "b15da768f414";
		}
		echo "<b>Ну вот, ты купил совсем не то что нужно. А теперь представь лицо своей девушки, когда она увидит это: </b><br>
		<br />
		<img src=".$img.".jpg style='height:300px;'/>
		";
	}
}
else {

?>
<b>Это - мобильный телефон твоей девушки! Но она хочет Iphone7, так купи же его!</b><br>
<br />
<img src=b15da768f414.jpg width=359px height=252px />

<?php
}
?>

</center>
<br />
<center>
		<center>Мобилки:
		<form action="" method="get">
			    <input value="russian" name="language" type="hidden" />
			    <input value="19424" name="cost" type="hidden" />
			    <input value="innoctf" name="contest" type="hidden" />
			    <input value="today" name="time" type="hidden" />
			    <input value="web3" name="task" type="hidden" />
			<p><select name="model">
			    <option value="alcatel" selected>Alcatel OT310</option>
			    <option value="motorola">Motorola L6</option>
			    <option value="nokia">Nokia 3310</option>
			    <option value="texet">Texet</option>
			    <option value="sony_ericsson">Sony Ericsson K500i</option>
			    <option value="siemens">Siemens A55</option>
			    <input value="Купить!" name="submit" type="submit" /></td>
			   </select></p>
			    <input value="true" name="buy" type="hidden" />
			    <input value="working" name="server" type="hidden" />
		</form>
</center>
			<br />

</body>
</html>
