# Box Packing Optimizer

A Python application that computes the optimal rectangular box dimensions to hold a set of user-provided items using symbolic optimization. The tool uses Lagrange multipliers to minimize surface area under a volume constraint and visualizes results in 3D.

## Status

**Archived / Refactored**

## Features

- Interactive CLI for entering box weight capacity and item specifications
- Symbolic optimization using SymPy to minimize surface area under volume constraints
- Lagrange multiplier method for constrained optimization
- Numerical evaluation of optimal dimensions
- 3D visualization of the container and individual item boxes using Matplotlib

## Project Structure

```
box-packing-optimizer/
├── main.py              # Main entry point script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── LICENSE              # MIT License
├── CONTRIBUTING.md      # Contribution guidelines
├── CHANGELOG.md         # Version history
├── .editorconfig        # Editor configuration
└── .gitignore           # Git ignore rules
```

## Requirements

- Python 3.9+
- sympy
- numpy
- matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ApatheticMioz/mt1008-project-a.git
   cd mt1008-project-a
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python main.py
```

Follow the interactive prompts to:

1. Enter the box weight capacity
2. Specify the number of items
3. For each item, enter its weight and volume

The script will:
- Validate that total item weight doesn't exceed capacity
- Calculate optimal box dimensions using Lagrange multipliers
- Display the solution (x, y, z dimensions)
- Generate 3D visualizations of the container and item arrangement

## How It Works

The optimizer uses Lagrange multipliers to solve the following constrained optimization problem:

- **Objective**: Minimize surface area: `f = 2xy + 2xz + 2yz`
- **Constraint**: Fixed total volume: `g = xyz - V = 0`

The solution yields cubic dimensions (x = y = z) for the optimal box shape.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.
