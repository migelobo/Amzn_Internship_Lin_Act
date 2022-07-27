<!DOCTYPE html>
<html lang="en">
<head>
	<title>Stepper Motor Breathing Simulation</title>
	<link rel="stylesheet" type="text/css" href='/static/styles/mystyle1.css'>
	<script>
	function show_breath_to_take(){
			if(document.getElementById('breathe').checked){
				document.getElementById('number_breaths').style.display='block';
				document.getElementById('breath_label').style.display='block';
			}else{
				document.getElementById('number_breaths').style.display='none';
				document.getElementById('breath_label').style.display='none';
			}
	}	
	</script>
</head>
<body>
	<h1> Stepper Simulations</h1>
	<p style="text-align:center;">This project takes in user input for steps, RPM, and step size to move a stepper motor. Please fill in all areas before submitting</p>
	
	<section class="container">
	<div class="one">
		<form action="/Stepper_motor", method="post" target="_blank">
	 
		<label for="steps">Steps:</label>
			<input type="text" id="steps" name="steps"><br><br>

		 <label for="rpm">RPM:</label>
			<input type="text" id="rpm" name="rpm"><br><br>
		 
		 <label>Select your step type</label><br>
			<input type="radio" id="full_step" name="step_type" value="1">
			<label for="full_step" >Full-step</label><br>
			<input type="radio" id="half_step" name="step_type" value="0">
			<label for="half_step" >Half-step</label><br><br>
		 
		 <label>Select a direction</label><br>
			<input type="radio" id="forward" name="direction" value="1">
			<label for="forward" >Forward</label><br>
			<input type="radio" id="backward" name="direction" value="0">
			<label for="backward">Backward</label><br><br>
		 
		 
		<input type="checkbox" id="breathe" name="breathe" value="True" onclick="show_breath_to_take()">
		<label for="breathe" >Enable Breathing </label><br>
		
		<label for="number_breaths" id="breath_label" style="display:none;" >Number of breaths:</label>
			<input type="text" id="number_breaths" style="display:none;" name="number_breaths"><br>
			
		 <input type="submit" class="myButton" value="Submit"><br>
		
		</form>
		<br>
	</div>
	</section>
	
	<section class="container">
	<div class="two">
		<table>
			<tr>
				<th>Breathing Pattern</th>
				<th>Steps</th>
				<th>RPM</th>
				<th>Step Type</th>
			</tr>
			<tr>
				<td>Adult</td>
				<td>50</td>
				<td>5</td>
				<td>Full-step</td>
			</tr>
			<tr>
				<td>Stressed Adult</td>
				<td>60</td>
				<td>8</td>
				<td>Full-step</td>
			</tr>
			<tr>
				<td>Elder</td>
				<td>30</td>
				<td>3</td>
				<td>Half-step</td>				
			</tr>
			<tr>
				<td>Child</td>
				<td>10</td>
				<td>1</td>
				<td>Half-step</td>
			</tr>
		</table><br>
		<label>Time Lapsed: {{time_lapse}} </label><br><br>
</body>
</html>
