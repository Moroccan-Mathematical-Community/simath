# Gauss Pivot Algorithm

## What is Gaussian Elimination?
Gaussian elimination is a fundamental algorithm in linear algebra used to solve systems of linear equations. Named after Carl Friedrich Gauss, this method transforms a system of equations into an upper triangular form using elementary row operations, making it easy to solve by back substitution.

## How Does the Algorithm Work?
The Gauss Pivot algorithm works through systematic elimination:

1. **Find a pivot** (non-zero element) in the current column.
2. **Swap rows if needed** to bring the pivot to the diagonal position.
3. **Eliminate** all elements below the pivot by subtracting appropriate multiples of the pivot row.
4. **Move to the next column** and repeat until the matrix is in upper triangular form.

## About the Code
- The matrix and vector are loaded from `config.yaml` for easy customization.
- The code includes helper functions for matrix operations (sum, product, row operations).
- Real-time visualization shows each step of the elimination process with color coding.
- The algorithm handles pivot selection and row swapping automatically.

## Key Code Snippet
```python
def GaussPivot(M, B):
    row = 0
    col = 0
    n = len(M)
    m = len(M[0])
    while (row < n) and (col < m):
        if M[row][col] != 0:  # Found pivot
            # Eliminate elements below pivot
            for j in range(row + 1, n):
                factor = -M[j][col] / M[row][col]
                # Apply row operations...
        else:
            # Find non-zero element to swap
            # or move to next column
```

## Visual Features
- **🔴 Red**: Current pivot element
- **🟢 Light Green**: Pivot row
- **🟠 Light Orange**: Pivot column  
- **🟡 Yellow**: Modified matrix cells
- **🩷 Light Pink**: Modified vector values
- **Step-by-step animation** showing the transformation process

## Educational Value
- Demonstrates systematic approach to solving linear systems.
- Shows the importance of pivot selection in numerical stability.
- Visualizes row operations and their effects on the matrix.
- Easy to experiment with different matrices and observe the elimination process.

---
**Master the fundamentals of linear algebra through visualization!**