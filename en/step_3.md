## Code your animation

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will write the code that detects nearby colours and activates your animation.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open the [ambient art starter project](https://trinket.io/library/trinkets/4e77300dfc){:target="_blank"}.

--- /task ---

--- task ---

Find the comment `# Colour palette` and enter the code for your colour palette.

[[[sh-colour-palette]]]

[[[generic-theory-simple-colours]]]

--- /task ---

### Frame 1

--- task ---

Copy the design for your first frame into the tool below. 

<iframe src="https://trinket.io/embed/html/d017077cff?outputOnly=true" width="100%" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /task ---

--- task ---

**Create** a blank list to store your colour variables. 

--- code ---
---
language: python
filename: main.py
line_numbers: 
line_number_start: 
line_highlights: 
---
frame_1 = [

  ]
--- /code ---

--- /task ---

--- task ---

Highlight the values in the image creation tool above. 

Copy and paste them inside your blank list. 

<mark>Add a gif to demo this</mark>

**Tip**: To copy and paste you can highlight the text and then right click (tap and hold on mobile) and choose 'Copy'. Then click on the empty line inside the `frame_1` list, right click anc choose 'Paste'.

--- /task ---

--- task ---

Enter code for displaying the colour values from your `frame_1` list onto your SenseHAT LED matrix. 

[[[sh-show-pixels]]]

--- /task ---

--- task ---

Add a `sleep` to make sure that the frame pauses to give you time to see the image.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
sleep(1) # Pause for 1 second
--- /code ---

--- /task ---

--- task ---

**Test** your code by clicking Run.

You should see the first frame of your animation on the LED matrix. 

--- /task ---


--- save ---
