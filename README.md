# Monte Carlo Approximation of π (Random Sampling + Live Visualization)

This project estimates the value of **π** using a **Monte Carlo simulation** and visualizes the process in real time. Random points are generated inside a square \([-1, 1] \times [-1, 1]\). The fraction of points that fall inside the unit circle \(x^2 + y^2 \le 1\) is used to approximate π.

---

## What this project does

- Randomly samples points \((x, y)\) uniformly in the square \([-1,1] \times [-1,1]\)
- Classifies each point as:
  - **inside** the unit circle (colored **red**)
  - **outside** the unit circle (colored **blue**)
- Uses the ratio of points inside the circle to estimate π:
  \[
  \pi \approx 4 \cdot \frac{N_{\text{inside}}}{N}
  \]
- Updates two live plots:
  - **Left plot:** the random points (red/blue)
  - **Right plot:** convergence of the π estimate over time

---

## Mathematical idea

### Why the factor of 4 appears
- Area of square \([-1,1] \times [-1,1]\) is:
  \[
  A_{\text{square}} = 2 \times 2 = 4
  \]
- Area of the unit circle is:
  \[
  A_{\text{circle}} = \pi \cdot 1^2 = \pi
  \]
- The probability that a uniformly random point in the square lies in the circle is:
  \[
  P(\text{inside}) = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4}
  \]
- Rearranging gives:
  \[
  \pi \approx 4P(\text{inside}) \approx 4 \cdot \frac{N_{\text{inside}}}{N}
  \]

---

## Visualization details

The code uses **Matplotlib** in an efficient way:

- The scatter plot is created **once**:
  - `scatter = axis[0].scatter([], [], ...)`
- The line plot is created **once**:
  - `plot, = axis[1].plot([], [], ...)`
- During the simulation, these objects are **updated** rather than re-created:
  - `scatter.set_offsets(...)` updates point positions
  - `scatter.set_facecolors(...)` updates point colors
  - `plot.set_data(...)` updates the π estimate curve
- The animation effect is produced using:
  - `plt.pause(0.01)`

The plots update every 100 samples:
```python
if N % 100 == 0:
    ...
