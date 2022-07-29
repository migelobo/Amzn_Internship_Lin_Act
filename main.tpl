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
	<script>
		function moveNumbers(number){
			var Row = document.getElementById(number.toString());
			var cells = Row.getElementsByTagName("td");
			document.getElementById("amplitude").value=cells[1].innerText;
			document.getElementById("rpm").value=cells[2].innerText;
		}
	</script>
</head>
<body>
	<h1> Stepper Simulations</h1>
	
	<p style="text-align:center;">This project facilitates a stepper motors capabilities to test accuracy of any motion tracking chipset's ouput<br>
	compared to the user inputed values  
	</p>
	
	<section class="top_container">
		<div class="left">
			<h2>How to Play</h2>
			<hr/>
			
			<label><strong>Amplitude:</strong>
				<small> 
					The distance (in mm) the motor will <br>
					will travel back and forth to simulate breathing
				</small></label><br><br>
			<label><strong>Speed: </strong>
				<small>
					Speed is esablished by how many revolutions <br>
					you want the motor to make in a minute or RPM
				</small>
			</label><br><br>
			<label><strong>Number of Breaths:</strong>
				<small>
					Total number of oscillations <br>
					the motor will make to simulate a "breath"
				</small>
			</label><br><br>
			<label><strong>Simulation Presets:</strong>
				<small>
					These are previously tested<br>
					values that simulate a specific breathing pattern.<br>
					Clicking on one will auto-fill text box and leave you <br>
					to input number of breaths
				</small>


			</label>
			
			<h3>Additional Information</h3>
			<label><strong>Debugging Tab:</strong>
				<small>
					For those familiar with stepper motor<br>
					functionality, debugging allows you to control: number of<br>
					steps, RPM, step-type, and direction of motor.
				</small>
			</label><br><br>
			<label><strong>Conversions:</strong></label><br>
				<small>1mm = 10 steps<br>
				50 steps = 1 full rotation
				</small>
			</label><br><br>
			<label><strong>Step Type:</strong>
				<small>
					This is changes the total amount of degrees<br>
					the shaft rotates in a given step.<br>
					<b>Full-Step:</b> Shaft rotates 1.8<sup>o</sup> each step<br>
					<b>Half-Step:</b> Shaft rotates .9<sup>o</sup> each step<br><br>
				</small>
			</label>
	
		</div>

		<div class="center">
			<h4>Breathing</h4><br>
			<hr/>
			<form action="/Stepper_motor", method="post" target="_blank">
		
			<label for="amplitude"><b>Amplitude:</b></label>
				<input type="text" id="amplitude" name="amplitude" size="4"><small> <b>mm</b></small><br><br>

			<label for="rpm"><b>Speed:</b></label>
				<input type="text" id="rpm" name="rpm" size="4"> <small><b>RPM</b></small><br><br>
			
			<label for="number_breaths" id="breath_label"><b>Number of Breaths:</b></label>
				<input type="text" id="number_breaths" name="number_breaths" size="5"><br><br>
			
			<input type="submit" class="myButton" value="Submit">
			</form><br><br>

			<h4>Debugging</h4> <input type="checkbox" id="debug_request" style="display:none"  onclick="ShowHideDiv(this)">
			
		<label for=debug_request class="label1"></label>
		<hr/>
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
			<br>
		</div>

		<div class="right">
			<h4>Simulation Presets</h4>
			<hr/>
			<table>
				<tr>
					<th>Breathing Pattern</th>
					<th>Amplitude</th>
					<th>RPM</th>
				</tr>
				<tr id=one onclick="moveNumbers(this.id)">
					<td>Adult</td>
					<td>50</td>
					<td>5</td>
				</tr>
				<tr id=two onclick="moveNumbers(this.id)">
					<td>Stressed Adult</td>
					<td>60</td>
					<td>8</td>
				</tr>
				<tr id=three onclick="moveNumbers(this.id)">
					<td>Elder</td>
					<td>30</td>
					<td>3</td>			
				</tr>
				<tr id=four onclick="moveNumbers(this.id)">
					<td>Child</td>
					<td>10</td>
					<td>1</td>
				</tr>
			</table><br>
			<label>Time Lapsed: {{time_lapse}} </label><br>
			<label>Steps: {{steps_oscillated}}</label>
		</div>
	</section>
	<!--
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
	-->
</body>
</html>
