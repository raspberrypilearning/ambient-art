## Code your animation

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will set up your frames for the animation. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open the [ambient art starter project](https://trinket.io/library/trinkets/4e77300dfc){:target="_blank"}.

--- /task ---

--- task ---

Find the comment `# Colour palette` and add variables for each of the colours in your animation design: 

--- code ---
---
language: python
filename: main.py
line_numbers: 
line_number_start: 1
line_highlights: 2-5
---
# Colour palette
i = (0, 128, 128) # Teal
o = (128, 128, 0) # Olive
w = (255, 192, 203) # Pink
y = (153, 50, 204) # DarkOrchid
--- /code ---

[[[ambient-colours]]]

[[[generic-theory-simple-colours]]]

--- /task ---

### Frame 1

--- task ---

Copy the design for your first frame into the tool below. 

**Tip:** Make sure you colour all the squares, even if they are 'white' in your design. 

<iframe src="https://trinket.io/embed/html/d017077cff?outputOnly=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /task ---

--- task ---

Find the comment `# Animation`

**Create** a blank list to store your colour variables. 

--- code ---
---
language: python
filename: main.py
line_numbers: 
line_number_start: 1
line_highlights: 2-4
---
# Animation
frame_1 = [

          ]
--- /code ---

--- /task ---

--- task ---

**Highlight** the values in the image creation tool above. 

**Copy** and **paste** them inside your blank list. 

<mark>Add a gif to demo this</mark>

You code should like this this, with your own colour variables inside.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 
---
# Animation
frame_1 = [
  b, b, l, l, f, l, b, b,
  b, l, f, l, l, l, f, b,
  b, l, l, l, f, l, l, b,
  b, f, l, l, l, l, l, b,
  b, b, l, f, l, f, b, b,
  b, b, b, t, t, b, b, b,
  b, b, b, t, t, b, b, b,
  g, g, g, g, g, g, g, g,
  ]
--- /code ---

**Tip**: To copy and paste you can highlight the text and then right click (tap and hold on mobile) and choose 'Copy'. Then click on the empty line inside the `frame_1` list, right click and choose 'Paste'.

**Tip**: If you are using Firefox then you will need to add in the line spaces to format your grid code.

--- /task ---

--- task ---

Underneath your `frame_1` list, enter the code for displaying the colour values from your `frame_1` list onto your SenseHAT LED matrix and make it `sleep` for 1 second.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 11-12
---
frame_1 = [
  b, b, l, l, f, l, b, b,
  b, l, f, l, l, l, f, b,
  b, l, l, l, f, l, l, b,
  b, f, l, l, l, l, l, b,
  b, b, l, f, l, f, b, b,
  b, b, b, t, t, b, b, b,
  b, b, b, t, t, b, b, b,
  g, g, g, g, g, g, g, g,
  ]
sense.set_pixels(frame_1)
sleep(1) # Pause for 1 second
--- /code ---

--- /task ---

--- task ---

**Test** your code by clicking Run.

You should see the first frame of your animation on the LED matrix. 

![The first frame appearing on the LED matrix showing a tree with fruit.](images/tree_frame_1.png)

**Debug**:

I have a syntax error in my code!
+ Check that you have separated each variable with a comma in your list
+ Check that you code matches the examples given

--- /task ---

### Create the remaining frames

<iframe src="https://trinket.io/embed/html/d017077cff?outputOnly=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- task ---

Use the tool below to make the remaining frames for your animation then add your code for the remaining frames. 

Add the next frame of your animation to your code, and display the frame and pause.

**Repeat** this for `frame_2`, `frame_3` and `frame_4`. 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 3-14
---
sense.set_pixels(frame_1) 
sleep(1)
frame_2 = [
   b, b, l, l, l, l, b, b,
   b, l, l, l, f, l, l, b,
   b, l, f, l, l, l, l, b,
   b, l, l, l, f, l, f, b,
   b, f, l, l, l, l, b, b,
   b, b, b, f, t, f, b, b,
   b, b, b, t, t, b, b, b,
   g, g, g, g, g, g, g, g,
  ]
sense.set_pixels(frame_2) 
sleep(1)
--- /code ---

--- /task ---

--- save ---
