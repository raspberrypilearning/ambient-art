## Sense the colour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Sense the ambient colour of the environment and use this to adapt your animation. Use a `for` loop to repeat your animation.
</div>
<div>
![An animation of a tree with fruit falling down on the SenseHAT LED matrix. The colour sensor value is changed and this is replicated in the image.](images/step-four-output.gif){:width="300px"}
</div>
</div>

--- task ---

**Choose** Decide which of your colours you want to change to match the ambient colour. 

--- /task ---

--- task ---

**Find** your animation function under the `# Animation based on the colour sensor` comment and add code to update **your chosen** ambient colour to the colour sensed by the SenseHAT colour sensor. 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 4
---
# Animation based on the colour sensor
def painting():
  
  e = sense.colour.colour[0:3] # Store the sensor readings
  
  # Frame 1
  frame_1 = [
    a, a, a, a, u, u, a, a, 
    a, a, a, u, u, u, a, a, 
    a, a, u, u, u, a, a, a, 
    a, a, u, u, a, a, a, a, 
    q, q, a, a, a, a, a, a, 
    q, q, a, a, a, a, a, a, 
    e, e, a, a, a, a, a, a, 
    a, a, a, a, a, a, a, a
  ]
 
--- /code ---

**Tip** In the example above, the `e` variable will be the colour that changes based on the colour sensor reading. 

--- /task ---

--- task ---

**Test** Update the **Colour picker** tool on your SenseHAT emulator then run your code. Check that your animation uses the sensed colour. 

Change the **Colour picker** colour and run your project a couple of times to make sure the colour changes in your animation. 

**Debug**:
I have a syntax error!
+ Double check that your code matches the code in the example above

--- collapse ---
---
title: I'm running my code on a physical Sense HAT
---
You can alter the readings from the colour sensor by using coloured transparent plastic. Even using coloured felt tip pens on a small piece of [cling film](https://en.wikipedia.org/wiki/Plastic_wrap) will work.

--- /collapse ---

--- /task ---

A better way to change your animation to match the ambient colour is to loop your animation multiple times and check for a change in colour each run.

--- task ---

**Find** the `# Looped animation` comment add a line of code to loop your animation `10` times. 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 2
---
# Looped animation 
for i in range(10):
painting()
 
--- /code ---

--- /task ---

--- task ---

You now need to indent your function call so that it sits **inside** the `for` loop.

To do this, Use the **Tab** character on your keyboard. 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1 
line_highlights: 3
---
# Looped animation 
for i in range(10):
  painting()
 
--- /code ---

--- /task ---

--- task ---

**Test** Run your code and change the colour picker several times as your project is running. Check that your animation updates to use the sensed colour on it's next run of the animation. 

![An animation of a tree with fruit falling down on the SenseHAT LED matrix. The colour sensor value is changed and this is replicated in the image.](images/step-four-output.gif){:width="300px"}

**Debug**:
I have a syntax error!
+ Double check that your code matches the code in the example above
+ Make sure all the code to be repeated is indented  

--- /task ---

--- save ---