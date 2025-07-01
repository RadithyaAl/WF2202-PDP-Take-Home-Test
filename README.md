# WF2202 – PDE & Numerical Methods: Take-Home Exam

This repository contains my full Python implementation of the **WF2202 - Partial Differential Equation and Numerical Method** take-home exam (Institut Teknologi Bandung). The MATLAB code included in the repo is provided for comparison only, as required by the instructor — the main work was completed in Python with minimal dependencies.

---

## 📘 Exam Overview

The take-home exam consists of four main numerical computation problems, each testing key topics in numerical analysis:

| No. | Topic                                    | Methodologies Implemented         |
|-----|------------------------------------------|------------------------------------|
| 1   | System of linear algebraic equations     | Gauss Elimination & Gauss-Seidel  |
| 2   | 1D Unsteady Heat Conduction              | FTCS Scheme & Analytical Solution |
| 3   | Steady-State 2D Heated Plate             | Gauss-Seidel Iteration            |
| 4   | Beam Deflection (Nonlinear ODEs)         | 2nd & 4th Order Runge-Kutta       |

---

## 🛠️ Technologies Used

- ✅ **Python 3.11**
- ✅ Pure standard libraries (`math`, `copy`) — *no third-party dependencies*
- ✅ MATLAB (minimal, comparison only)

---


## ✅ Problem Descriptions (Python Implementations)

### 1️⃣ Gauss Elimination & Gauss-Seidel
- Solves `Ax = b` where A is an `n x n` coefficient matrix.
- Accepts input from the keyboard.
- Solution is printed with convergence status.

### 2️⃣ Heat Conduction Equation
- Solves the transient 1D heat equation using the **FTCS** scheme.
- Includes comparison with analytical results.
- Allows multiple time-step values for stability testing.

### 3️⃣ Heated Plate Problem
- Applies **Gauss-Seidel** iteration to a 2D grid.
- Boundary temperatures are set based on student's NIM.
- Solution is visualized as a 2D distribution plot.

### 4️⃣ Beam Deflection with Runge-Kutta
- Solves nonlinear ODE from Bernoulli-Euler beam theory.
- Implements both **2nd Order (Modified Euler)** and **4th Order Runge-Kutta** methods.
- Plots deflection comparison.

---

## ⚠️ Academic Integrity Note

> This project was submitted as part of an academic exam. The original intellectual work belongs to the authors, and the repository is shared only for educational purposes.

---

## 📬 Contact

If you'd like to collaborate or have questions about the numerical techniques, feel free to connect.
