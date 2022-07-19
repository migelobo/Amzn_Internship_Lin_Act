<!DOCTYPE html>
<html lang="en">
<head>
	<title>Stepper Motor Breathing Simulation</title>
	<link rel="stylesheet" type="text/css" href='/static/styles/mystyle.css'>
</head>
<body>
	<h1> Raspberry PI Bottle Webserver Demo</h1>
	<p style="text-align:center;">This project uses CSS to improve overall gui.</p>
	
	<section class="container">
	<div class="one">
	<form action="/Stepper_motor", method="post" target="_blank">
	 <label for="steps">Steps:</label>
	 <input type="text" id="steps" name="steps"><br><br>
	 <label for="rpm">RPM:</label>
	 <input type="text" id="rpm" name="rpm"><br><br>
	 <input type="submit" class="myButton" value="Submit"><br>
	 
	</form>
	<br>
	</div>
	</section>
	
</body>
</html>
