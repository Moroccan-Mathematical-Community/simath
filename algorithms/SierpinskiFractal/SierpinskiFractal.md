
# Sierpinski Triangle (Fractal) Algorithm

## What is the Sierpinski Triangle?
The Sierpinski triangle is a famous fractal named after the Polish mathematician Wacław Sierpiński. It is constructed by recursively subdividing an equilateral triangle into smaller triangles, removing the central one at each step. The result is a self-similar pattern that appears the same at any scale.

## How Does the Algorithm Work?
This script uses a simple and beautiful method called the "Chaos Game" to generate the Sierpinski triangle:

1. **Start with three points** (the triangle's vertices).
2. **Pick a random starting point** inside the triangle.
3. **Repeat for many iterations:**
   - Randomly select one of the three vertices.
   - Move halfway from the current point to the chosen vertex.
   - Plot the new point.
   - The process is repeated, and the points gradually reveal the fractal pattern.

## About the Code
- The triangle's vertices and other parameters are loaded from `config.yaml` for easy customization.
- The code uses `matplotlib` for plotting and `random` for randomness.
- Each new point is plotted in real time, so you can watch the fractal emerge step by step.

## Key Code Snippet
```python
for i in range(iterations):
	x = rd.choice(heads)  # Randomly pick a vertex
	z = [(x[0]+y[0])/2, (x[1]+y[1])/2]  # Move halfway
	plt.plot(z[0], z[1], '.')  # Plot the point
	plt.pause(pause)
	plt.title(f"iteration N°{i+1}")
	y = z  # Update current point
```

## Educational Value
- Demonstrates randomness leading to order (chaos game).
- Shows self-similarity and recursion in mathematics.
- Easy to modify for experimentation (try changing the vertices or the number of iterations!).

---
**Explore, experiment, and enjoy the beauty of fractals!**
