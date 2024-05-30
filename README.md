<h1>Project Title: Voice-Driven Intelligence on Wheels: A Speech-Based Smart Vehicle Powered by IoT</h1> <br>
<b>Execution Video: </b>https://youtu.be/rwGcXWfQ77Y?si=_9_4_txi6GPTQWWc
<br>
<br>
<b>Step 1: Create the python virtual environment in Raspberry Pi OS</b> <br>
python -m venv project
<br>
<br>

<b>Step 2: Activate virtual environment</b><br>
Source bin/activate
<br>
<br>
<b>Step 3: Installing all the required libraries by using pip command</b><br>
Libraries: tensorflow,librosa,jupyternotebook,numpy,pandas,gpiozero,GPIO<br>
EX: pip intall tensorflow, etc
<br>
<br>
<b>Step 4: configuring raspberry pi pins</b><br>
<table>
    <tr>
      <th>Component</th>
      <th>GPIO Pin</th>
    </tr>
    <tr>
      <td>Right Motor Forward</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Right Motor Backward</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Left Motor Forward</td>
      <td>23</td>
    </tr>
    <tr>
      <td>Left Motor Backward</td>
      <td>22</td>
    </tr>
    <tr>
      <td>Ultrasonic Sensor Echo</td>
      <td>27</td>
    </tr>
    <tr>
      <td>Ultrasonic Sensor Trigger</td>
      <td>24</td>
    </tr>
    <tr>
      <td>Front Right LED</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Front Left LED</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Back Right LED</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Back Left LED</td>
      <td>26</td>
    </tr>
    <tr>
      <td>Servo Motor</td>
      <td>21</td>
    </tr>
    <tr>
      <td>Buzzer</td>
      <td>10</td>
    </tr>
  </table>


<br>
<b>Step 5: run python code “car1.py”</b>
Python car1.py
<br>
<br>
<b>Step 6: After running code give voice input like turn right, turn left, stop, reverse, lights on, lights off, go forward, blow horn, speed up, slow down</b>
<br>
<br>
<b>Step 7: Gesture control operations in key board</b><br>
  <br>
  <table>
    <tr>
      <th>Action</th>
      <th>Gesture</th>
    </tr>
    <tr>
      <td>Go Forward</td>
      <td>Up arrow key</td>
    </tr>
    <tr>
      <td>Reverse</td>
      <td>Down arrow key</td>
    </tr>
    <tr>
      <td>Stop</td>
      <td>Release the key</td>
    </tr>
    <tr>
      <td>Turn Left</td>
      <td>Left arrow key</td>
    </tr>
    <tr>
      <td>Turn Right</td>
      <td>Right arrow key</td>
    </tr>
    <tr>
      <td>Blow Horn</td>
      <td>Key "b" or "B"</td>
    </tr>
    <tr>
      <td>Lights On</td>
      <td>Key "l" or "L"</td>
    </tr>
    <tr>
      <td>Lights Off</td>
      <td>Release key</td>
    </tr>
    <tr>
      <td>Speed Up</td>
      <td>Key "u" or "U"</td>
    </tr>
    <tr>
      <td>Slow Down</td>
      <td>Key "d" or "D"</td>
    </tr>
  </table>
<br>

<b>Step 8: press ctrl+c to stop executing the code</b>
