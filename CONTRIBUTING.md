# Contributing to SiMath

Welcome to the **MMC SiMath** project! We're excited to have you contribute to our collection of mathematical simulations and visualizations.

## 🎯 Project Overview

SiMath is a collaborative repository that aims to collect scripts (mainly in Python 3) that visually illustrate mathematical concepts, theorems, and algorithms. Our goal is to create an educational resource for students, educators, and math enthusiasts.

## 📋 Contribution Guidelines

### 🔧 Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/simath.git
   cd simath
   ```
3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux:
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### 📁 Project Structure

When adding a new algorithm, follow this structure:

```
algorithms/
├── YourAlgorithmName/
│   ├── YourAlgorithmName.py      # Main implementation
│   ├── YourAlgorithmName.md      # Documentation
│   ├── config.yaml               # Configuration (if needed)
│   └── __init__.py              # Python package file
```

And add corresponding simulation scripts:

```
simulations/
├── linux/
│   └── YourAlgorithmName.bash    # Linux launcher
└── windows/
    └── YourAlgorithmName.bat     # Windows launcher
```

### 🐍 Python Code Standards

1. **Python Version**: Use Python 3.8 or higher
2. **Dependencies**: Add new dependencies to `requirements.txt`. If the library is already listed, ensure compatibility and avoid duplicates or changes in versions
3. **Configuration**: Use `config.yaml` files for algorithm parameters
4. **Visualization**: Include real-time or step-by-step visualizations when possible
5. **Documentation**: Add clear docstrings and comments

### 📚 Documentation Requirements

Each algorithm must include a `.md` file with:

1. **Mathematical Background**: Explain the concept/theorem
2. **Algorithm Description**: How it works step-by-step
3. **Code Overview**: Key features and usage
4. **Educational Value**: What readers can learn
5. **Code Snippet**: Show the core algorithm logic

### 🎨 Visualization Guidelines

- Include **step-by-step visualization** when applicable
- Add **color coding** to highlight different elements
- Use **real-time updates** for educational effect
- Make visualizations **clear and educational**

### 🧪 Testing Your Contribution

Before submitting:

1. **Test on both platforms** (if possible):
   ```bash
   # Windows
   simulations\windows\YourAlgorithm.bat
   
   # Linux
   bash simulations/linux/YourAlgorithm.bash
   ```

2. **Verify configuration loading** works correctly
3. **Check that visualizations display properly**
4. **Ensure code follows Python standards**

### 📤 Submitting Your Contribution

1. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-algorithm-name
   ```

2. **Commit your changes** with clear messages:
   ```bash
   git add .
   git commit -m "Add [AlgorithmName]: Brief description"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-algorithm-name
   ```

4. **Create a Pull Request** on GitHub with:
   - Clear title describing the algorithm
   - Description of what the algorithm demonstrates
   - Screenshots or GIFs of the visualization (if possible)
   - Any special dependencies or requirements

### ✅ Pull Request Checklist

- [ ] Algorithm follows the project structure
- [ ] Includes both `.py` and `.md` files
- [ ] Configuration file (`config.yaml`) if needed
- [ ] Platform-specific launchers (`.bat` and `.bash`)
- [ ] Clear documentation with educational value
- [ ] Code includes comments and docstrings
- [ ] Visualization is educational and clear
- [ ] No unnecessary dependencies added

### 🆘 Getting Help

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Reach out to the MMC community

### 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to mathematical education! 🧮✨**