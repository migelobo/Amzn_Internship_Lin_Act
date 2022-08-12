<!DOCTYPE html>
<html lang="en">
<head>
	<!--title and framework of the dashboard including scripts and css-->
	<title>Stepper Motor Breathing Simulation</title>
	<link rel="stylesheet" type="text/css" href='/static/styles/mystyle1.css'>
	<!--this function was for the ability to show/hide the breathing button in a previous iteration of the dashboard
		didnt delete because im sentimental-->
	<!--<script> 
	function show_breath_to_take(){
			if(document.getElementById('breathe').checked){
				document.getElementById('number_breaths').style.display='block';
				document.getElementById('breath_label').style.display='block';
			}else{
				document.getElementById('number_breaths').style.display='none';
				document.getElementById('breath_label').style.display='none';
			}
	}	
	</script>-->
	<!--function that shows/hides the Debugging tab when the dashboard is loaded-->
	 <script type="text/javascript">
		function ShowHideDiv(debug_request) {
			var debug = document.getElementById("debug");
			debug.style.display = debug_request.checked ? "block" : "none";
		}
	</script>
	<!--this function is in charge of moving the values in the Simulation Presets table to the Breathing section by clicking on it-->
	<script>
		function moveNumbers(number){
			var Row = document.getElementById(number.toString());
			var cells = Row.getElementsByTagName("td");
			document.getElementById("amplitude").value=cells[1].innerText;
			document.getElementById("rpm").value=cells[2].innerText;
		}
	</script>
</head>
<!--start of the actual dashboard visuals-->
<body>
	<h1> Stepper Simulations</h1>
	
	<p style="text-align:center;">This project facilitates a stepper motors capabilities to test accuracy of any motion tracking chipset's ouput,<br>
	compared to the user inputed values  
	</p>
	<!--left most section of the dashboard containing information regarding termninology, functionality, and other usefull knowledge of the dashboard
		there is no real reason to change this section other than to update meaning of words, update added features -->
	<section class="top_container">
		<div class="left">
			<h2>How to Play</h2>
			<hr/>
			
			<label></label>
			
			<label><strong>Amplitude:</strong>
				<small> 
					The breath displacement (in mm) <br>
					from start position. <br>
					<b>Min/Max:</b> 1mm/210mm
				</small></label><br><br>
			<label><strong>RPM: </strong>
				<small>
					The number of total compressions the motor <br>
					will do in a minute. A compression counts as a <br>
					back and forth motion<br>
					<b>Min/Max:</b> 1/100
				</small>
			</label><br><br>
			<label><strong>Number of Breaths:</strong>
				<small>
					Total number of repeated  <br>
					motions the motor will make to simulate a "breath"<br>
				</small>
			</label><br>
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
				50 steps = 1 full rotation<br>
				<b>To run for "x" min: <br></b>
				Number of Breaths = RPM * "x" min 
				</small>
			</label><br><br>
			<label><strong>Step Type:</strong>
				<small>
					This is changes the total amount of degrees<br>
					the shaft rotates in a given step.<br>
					<b>Full-Step:</b> Shaft rotates 1.8<sup>o</sup> each step<br>
					<b>Half-Step:</b> Shaft rotates .9<sup>o</sup> each step<br><br>
				</small>
				<label style="display:none">carlos was here lol</label>
			</label>
	
		</div>
		<!-- center section of the dashboard containing both input driven sections. -->
		<div class="center">
			<h4>Breathing</h4><br>
			<hr/>
			<!--the post method is commonly used in HTML form submission. For this reason we can use the user inputs to run our python program.
				the form inputs are left blank when loaded and when submission is confirmed, the dashboards redirects to "/Stepper_motor" which is 
				the Stepper_motor funciton in main.py -->
			<form action="/Stepper_motor", method="post" target="_blank">
				<!--the following are the label and input types for all fields that are in charge of the breathing simulator. All fields are required 
					to be filled and have set limiters based on the stepper motors capabilities-->
				<label for="amplitude"><b>Amplitude:</b></label>
					<input type="number" id="amplitude" name="amplitude" min="1" max="210" required><small> <b>mm</b></small><br><br>

				<label for="rpm"><b>RPM:</b></label>
					<input type="number" step = "0.01" id="rpm" name="rpm" min="1" max="100" required> <small><b></b></small><br><br>
				
				<label for="number_breaths" id="breath_label"><b> Number of Breaths:</b></label>
					<input type="number" id="number_breaths" name="number_breaths" min="1" max="1000" required><br><br>
				
				<input type="submit" class="myButton" value="Submit">
			</form><br><br>

			<!--The Debugging section remains hidden until the "+" is pressed, the line below is making sure the proper function is utilized.
				when submission is confimed, the dashboard will redirect to "/Debug_Stepper" which is the Debug_Stepper function in main.py -->
			<h4>Debugging</h4> <input type="checkbox" id="debug_request" style="display:none"  onclick="ShowHideDiv(this)">
				<label for=debug_request class="label1"></label>
			<hr/>
			<div id="debug" style="display: none"><br>
			<form action="/Debug_Stepper", method="post" target="_blank">
				<!--the following are the label and input types for all fields that are in charge of the breathing simulator. All fields are required 
				to be filled and have set limiters based on the stepper motors capabilities-->
				<label for="steps">Steps:</label>
					<input type="number" id="steps" name="steps" min="1" max="2120" required><br><br>
	
				<label for="rpm">RPM:</label>
					<input type="number" id="rpm" name="rpm" min="1" max="100" required><br><br>
					
				<label>Select your step type</label><br>
				<input type="radio" id="full_step" name="step_type" value="1" required>
					<label for="full_step" >Full-step</label><br>
				<input type="radio" id="half_step" name="step_type" value="0">
					<label for="half_step" >Half-step</label><br><br>

				<label>Select a direction</label><br>
				<input type="radio" id="forward" name="direction" value="1" required>
					<label for="forward" >Forward</label><br>
				<input type="radio" id="backward" name="direction" value="0">
					<label for="backward">Backward</label><br><br>

				<input type="submit" class="myButton" value="Submit"><br>
		</div>
			<br>
		</div>
		<!--right most section of the dashboard, containg the simulation presets and step conversion and time lapsed variables-->
		<div class="right">
			<h4>Simulation Presets</h4>
			<hr/>
			<!--this is the start of the tables creation.
				<tr> takes care of creating new rows for the table
				<th> creates the table header sections
				<td> creates new values for each section of the table in order
				each new table entry must have a new unique id in order to allow it to be a clickable object
				follow the format below to create a new entry-->
			<table>
				<tr>
					<th>Breathing Pattern</th>
					<th>Amplitude</th>
					<th>RPM</th>
				</tr>
				<!--This entry is an example entry, please change-->
				<tr id=one onclick="moveNumbers(this.id)">
					<td>Adult</td>
					<td>5</td>
					<td>5</td>
				</tr>
				<!--This entry is an example entry, please change-->
				<tr id=two onclick="moveNumbers(this.id)">
					<td>Stressed Adult</td>
					<td>6</td>
					<td>8</td>
				</tr>
				<!--This entry is an example entry, please change-->
				<tr id=three onclick="moveNumbers(this.id)">
					<td>Elder</td>
					<td>3</td>
					<td>3</td>			
				</tr>
				<!--This entry is an example entry, please change-->
				<tr id=four onclick="moveNumbers(this.id)">
					<td>Child</td>
					<td>1</td>
					<td>1</td>
				</tr>
				<!--
					<tr> id=[next entry number] onclick="moveNumbers(this.id")>
						<td>[Breathing Pattern Name]</td>
						<td>[Amplitude]</td>
						<td>[RPM]</td>
					<tr> 
				-->
			</table><br>
			<!--variables that are in main.py to be displayed when their values are updated-->
			<label>Time Lapsed: {{time_lapse}} </label><br>
			<label>Steps: {{steps_oscillated}}</label>
		</div>
	</section>
	<!-- 
		code that was used in a previous iteration of the dashboard but left in in case of it needing to be used
		it utilizes the commented out function in the former half of the code
	-->
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
