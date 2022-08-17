
--- question ---

---
legend: Question 2 of 3
---

The code below uses a `for` loop to call the animation `tree_fall()` **5 times**. The `tree_fall()` animation has **2 frames**, each frame is displayed for **1 second**. 

What will be the **total run time** of the animation?

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 
---
for i in range(5): # Repeat 5 times
  tree_fall() # Run a 2 second animation
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
