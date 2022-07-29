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
	 <script type="text/javascript">
		function ShowHideDiv(debug_request) {
			var debug = document.getElementById("debug");
			debug.style.display = debug_request.checked ? "block" : "none";
		}
	</script>
</head>
<body>
	<h1> Stepper Simulations</h1>
	
	<p style="text-align:center;">This project takes in user input for steps, RPM, and step size to move a stepper motor. Please fill in all areas before submitting</p>
	
	<section class="top_container">
		<div class="left">
			<h2>How to Play</h2>
			<hr />
			<label>1mm = 10 steps</label><br>
			<label>50 steps = 1 full rotation</label><br><br>
			<label><strong>Amplitude:</strong>
				<small> 
					The distance (in mm) the stepper <br>
					motor oscillates back and forth to simulate breathing
				</small></label><br><br>
			<label><strong>RPM: </strong>
				<small>
					This is known as revolutions per minute; or <br>
					how many full rotations the stepper makes in one<br>
					minute. This is how speed is modified in the simulator
				</small>
			</label><br><br>
			<label> <strong>Step Type:</strong>
				<small>
					This is changes the total amount of degrees<br>
					the shaft rotates in a given step.<br>
					<b>Full-Step:</b> Shaft rotates 1.8<sup>o</sup> each step<br>
					<b>Half-Step:</b> Shaft rotates .9<sup>o</sup> each step<br>
				</small>
			</label>
			
			<h3>Terminology/Conversions</h3>
			<label>1mm = 10 steps</label>
	
		</div>

		<div class="center">
			<form action="/Stepper_motor", method="post" target="_blank">
		
			<label for="steps">Amplitude:</label>
				<input type="text" id="steps" name="steps" size="4"> mm<br><br>

			<label for="rpm">RPM:</label>
				<input type="text" id="rpm" name="rpm" size="4"><br><br>
			
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

		<div class="right">
			<table>
				<tr>
					<th>Breathing Pattern</th>
					<th>Amplitude</th>
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
		</div>
	</section>
	<section class="bottom_container">
		<h4>Debugging</h4> <input type="checkbox" id="debug_request" style="display:none"  onclick="ShowHideDiv(this)">
		<label for=debug_request class="label1"></label>
		<div id="debug" style="display: none"><br>
			<form action="/Debug_Stepper", method="post" target="_blank">
		
				<label for="steps">Steps:</label>
					<input type="text" id="steps" name="steps" size="4">
	
				<label for="rpm">RPM:</label>
					<input type="text" id="rpm" name="rpm" size="4"><br><br>
					
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

				<input type="submit" class="myButton" value="Submit"><br>
		</div>


	</section>
</body>
</html>
