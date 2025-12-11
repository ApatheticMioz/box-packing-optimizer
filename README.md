# Box Packing Optimizer

A small SymPy/NumPy/Matplotlib script that computes an optimal rectangular box to hold a set of user-provided items and visualizes the result in 3D. The script asks for item weights/volumes, solves for minimal surface area given fixed total volume using Lagrange multipliers, then plots both the container box and the individual item boxes.

## Features
- Interactive CLI prompts for box weight capacity and item weights/volumes.
- Symbolic optimization with SymPy to minimize surface area under a volume constraint.
- Numerical evaluation of the optimal dimensions.
- 3D visualization of the container edges and individual item boxes using Matplotlib.

## Tech Stack
- Python
- sympy
- numpy
- matplotlib

## Installation
1. Ensure Python 3.9+ is installed.
2. Install dependencies:
   ```bash
   pip install sympy numpy matplotlib
   ```

## Usage
Run the main script from the project root:
```bash
python 232523_232577_232536_MT1008_Project_A_Code.py
```
Follow the prompts to enter box capacity, number of items, and each item's weight and volume. The script prints optimal dimensions and opens 3D plots.

## Notes
- The script currently ignores weight in the optimization and only constrains by volume; ensure provided total weight does not exceed the capacity check.
- Both provided `.py` files contain identical logic; use the `232523_232577_232536_MT1008_Project_A_Code.py` entry point.
