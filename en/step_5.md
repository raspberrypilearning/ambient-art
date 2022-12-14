## Time your animation

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will adjust the timings of your animation to make sure that it is under 30 seconds long.
</div>
<div>
![An animation of a smiley face winking on the LED matrix of a SenseHAT.](images/step-five-output.gif){:width="300px"}
</div>
</div>

### The current length of your animation

--- task ---

**Look** at your code. Can you work out the total length of your animation? 

--- collapse ---
---
title: How long does your animation run for?
---

If you count the values in the brackets of the `sleep()` function calls then you can see that **1 + 1 + 1 + 1 = 4**. This means that one loop of your animation is **4 seconds** long. 

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 1
line_highlights: 2
---
# Looped animation
for i in range(10): # Loop 10 times
--- /code ---

The animation call is within a loop which repeats **10 times**. This means the total animation run time is **4 x 10 = 40** to make a **40 second** animation.

--- /collapse ---

--- /task ---

### Adjust the timings

--- task ---

**Watch** your animation closely. Are you happy with the 1 second pause between each frame? Adjust the values in your `sleep()` functions until you are happy with the outcome. 

**Tip:** The `sleep()` times between frames do not have to be equal. You could pause one frame for `1` second and another for `2` seconds. 

--- /task ---

--- task ---

**Look** at your code. Can you work out the **new** total length of your animation? 

--- collapse ---
---
title: How long does your animation run for?
---

**Count up** the `sleep()` seconds in your code.

**Multiply** the number of seconds by **10**.

The answer is the **total run time** of your animation. 

--- /collapse ---

--- /task ---

## Make your animation less than 30 seconds

Your short animation should run for less than 30 seconds in total - but not be too quick or people will not see your designs. 

--- task ---

Reduce the number of repetitions in your `for` loop until your animation is **less than 30 seconds** long.

For example,

If each loop of your animation takes **4 seconds** then you can reduce your number of repetitions from `10` to `7` to make a **28 second** animation.

**4 x 7 = 28**.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
# Looped animation
for i in range(7):
--- /code ---

--- collapse ---
---
title: I need more help with the maths
---

Here are some example scenarios. You can use these to help you with your calculations. 

1. Add together the **number of seconds** in your code used for **one** loop.
2. Find that number in the table below.
3. Change the number in the brackets of your `for` loop to match the **number of repetitions** in the table.

| Number of seconds | Number of repetitions |
| --- | ----------- |
| 1 | 29 |
| 2 | 14 |
| 3 | 9 |
| 4 | 7 |
| 5 | 5 |
| 6 | 4 |
| 7 | 4 |
| 8 | 3 |
| 9 | 3 |
| 10 | 2 |

--- /collapse ---

--- /task ---

--- task ---

**Test**: Click Run and test your code. Make sure that there are no syntax errors and that the colour detection is still working. 

![An animation of a smiley face winking on the LED matrix of a SenseHAT.](images/step-five-output.gif){:width="300px"}

You now have a completed animation!

--- /task ---


--- save ---