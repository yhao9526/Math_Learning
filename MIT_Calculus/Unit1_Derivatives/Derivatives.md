# Unit 1 Derivatives
****
## Lecture 1: What is a derivative?

**1. The derivative is the limit of the secant line approaching the tangent line:**
- Geometric interpretation:
![Geometric interpretation](Images/Figure_1.png)
- Algebraic Explanation:
![Algebraic Explanation](Images/Figure_2.png)
$$
\lim _{\Delta x \rightarrow 0} \frac{\Delta f}{\Delta x}=\lim _{\Delta x \rightarrow 0} \frac{f\left(x_0+\Delta x\right)-f\left(x_0\right)}{\Delta x}=f^{\prime}\left(x_0\right)
$$

**2. Example:**

$ f(x)=\frac{1}{x} $ **proof:**
$$
\begin{aligned}
\frac{\Delta f}{\Delta x} & =\frac{\frac{1}{(x+\Delta x)}-\frac{1}{x}}{\Delta x} \\
& =\frac{-\Delta x}{\Delta x \cdot x \cdot(x+\Delta x)} \\
& =\frac{-1}{x \cdot(x+\Delta x)} \\
f^{\prime}(x) & =\lim _{\Delta x \rightarrow 0} \frac{\Delta t}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{-1}{x \cdot(x+\Delta x)} \\
& =-\frac{1}{x^2}
\end{aligned}
$$

$ f(x)=x^n $ **proof:**
$$
\begin{aligned}
\frac{\Delta f}{\Delta x} & =\frac{(x+\Delta x)^n-x^n}{\Delta x} \\
& =\frac{x^n+n \cdot \Delta x \cdot x^{n-1}+o\left[(\Delta x)^2\right]-x^n}{\Delta x} \\
& =n \cdot x^{n-1}+o(\Delta x) \\
f^{\prime}(x) & =\lim _{\Delta x \rightarrow 0} \frac{\Delta f}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0}\left[n \cdot x^{n-1}+o(\Delta x)\right] \\
& =n \cdot x^{n-1}
\end{aligned}
$$

**3. Note:**

Tangent Line Equation: $y-y_0=f^{\prime}\left(x_0\right)\left(x-x_0\right)$
****

## Lecture 2: Limits and Continuity

**1. Limits:**
$$
\lim _{x \rightarrow x_0} \frac{\Delta f}{\Delta x}=\lim _{x \rightarrow x_0} \frac{f\left(x_0+\Delta x\right)-f\left(x_0\right)}{\Delta x}
$$

**2. Continuity:**
$$
\lim _{x \rightarrow x_0} f(x)=f\left(x_0\right)
$$

**3. Two trigonometric limits:**
$$
\lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1 
$$

![sin](Images/Figure_3.png)
