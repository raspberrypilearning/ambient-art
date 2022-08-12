
--- question ---

---
legend: Question 2 of 3
---

The code below creates an animation that has **2 frames**. Each frame will be displayed for **1 second**. The frames are inside a `for` loop which **repeats 5 times**.

What will be the total run time of the animation?

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
for i in range(5):
  f = sense.colour.colour[0:3] # Store the sensor readings
  tree_full = [
   b, b, l, l, f, l, b, b,
   b, l, f, l, l, l, f, b,
   b, l, l, l, f, l, l, b,
   b, f, l, l, l, l, l, b,
   b, b, l, f, l, f, b, b,
   b, b, b, t, t, b, b, b,
   b, b, b, t, t, b, b, b,
   g, g, g, g, g, g, g, g,
  ]
  sense.set_pixels(tree_full)
  sleep(1)
  fruit_fall1 = [
   b, b, l, l, l, l, b, b,
   b, l, l, l, f, l, l, b,
   b, l, f, l, l, l, l, b,
   b, l, l, l, f, l, f, b,
   b, f, l, l, l, l, b, b,
   b, b, b, f, t, f, b, b,
   b, b, b, t, t, b, b, b,
   g, g, g, g, g, g, g, g,
  ]
  sense.set_pixels(fruit_fall1)
  sleep(1)
--- /code ---

--- choices ---

- ( ) 2 seconds

  --- feedback ---

Almost. A **single** loop of the animation will take **2 seconds**. However, this animation is repeated **5 times**. 

  --- /feedback ---

- (x) 10 seconds

  --- feedback ---

Excellent! **2 seconds** x **5 loops** = **10 seconds**

  --- /feedback ---

- ( ) 5 seconds

  --- feedback ---

Not quite. The animation will repeat **5 times** but each loop takes **2 seconds**. 

  --- /feedback ---

--- /choices ---

--- /question ---
