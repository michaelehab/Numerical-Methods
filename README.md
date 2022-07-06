# Numerical Methods implemented in Python
<div align="center">

![GitHub stars](https://img.shields.io/github/stars/michaelehab/Numerical-Methods?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/michaelehab/Numerical-Methods?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/michaelehab/Numerical-Methods?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/michaelehab/Numerical-Methods?style=plastic)
</div>

# Definition 📃(<a href="https://en.wikipedia.org/wiki/Numerical_analysis">WIKI</a>):
Numerical analysis is the study of algorithms that use numerical approximation for the problems of mathematical analysis. Numerical analysis finds application in all fields of engineering and the physical sciences, and in the 21st century also the life and social sciences, medicine, business and even the arts.

# Subjects 📘
## <a href="./interpolation.py">Interpolation</a>
### 1. Lagrange Interpolating Polynomial:
#### Example : 
<table align="center">
  <tr>
    <td>X</td> 
    <td>1.0</td>
    <td>1.3</td>
    <td>1.5</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0.841</td>
    <td>0.964</td>
    <td>0.997</td>
  </tr>
</table>

#### Using Lagrange Polynomial :
$$l_k(x)= \prod_{i=0,\, i\neq k}^{n} \frac{x-x_i}{x_k-x_i}=\frac{x-x_0}{x_k-x_0} \cdots \frac{x-x_{k-1}}{x_k-x_{k-1}} \frac{x-x_{k+1}}{x_k-x_{k+1}} \cdots \frac{x-x_{n}}{x_k-x_{n}}$$

$$l_2(1.4)=0.9854$$

### 2. Newton Divided Difference:
#### Example : 
<table align="center">
  <tr>
    <td>X</td> 
    <td>0</td>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>1</td>
    <td>5</td>
    <td>17</td>
  </tr>
</table>

#### Using Newton Divided Difference :
$$\left[\begin{array}{ccccc}
x_0=0 & f[x_0]=1  &                  & & \cr
x_1=2 & f[x_1]=5   & f[x_0,x_1]=\displaystyle\frac{5-1}{2-0} = 2& & \cr
x_2=4 & f[x_2]=17 & f[x_1,x_2]=\displaystyle\frac{17-5}{4-2}=6  &  f[x_0,x_1,x_2]=
\displaystyle\frac{6-2}{4-0}=1
  & 
\end{array}\right]$$

Then

$$\begin{array}{rcl}
P_2(x)&=&f[x_0]+f[x_0,x_1]x+f[x_0,x_1,x_2]x(x-2)\\
&=&1+2x+x(x-2)\\
&=&1+x^2
\end{array}$$

## <a href="./differentiation.py">Differentiation</a>
### 1. Forward Difference
$$f^ \prime(x) = \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

$$f^{\prime \prime}(x) = \frac{f(x + 2\Delta x) - 2f(x + \Delta x) + f(x)}{(\Delta x)^2}$$

### 2. Backward Difference
$$f^ \prime(x) = \frac{f(x) - f(x - \Delta x)}{\Delta x}$$

### 3. Centered Difference
$$f^ \prime(x) = \frac{f(x + \Delta x) - f(x - \Delta x)}{2\Delta x}$$

$$f^{\prime \prime}(x) = \frac{f(x + \Delta x) + f(x - \Delta x) - 2f(x)}{(\Delta x)^2}$$
## <a href="./integration.py">Integration</a>
### 1. Trapezoidal Rule
$$\int_{a}^b f(x)dx=\frac{h}{2}(f(a)+f(b)+2\sum_{i=0}^{n-1}f(a + ih))$$
Where:

$$h = \frac{b - a}{numberOfSegments}$$

### 2. Simpson $\frac{1}{3}$ Rule
$$\int_{a}^b f(x)dx=\frac{h}{3}(f(x)+f(x_n)+2\sum_{i(even)=0}^{n-2}f(x_i)+4\sum_{i(odd)=0}^{n-1}f(x_i))$$
Where:

$$h = \frac{b - a}{numberOfSegments}$$

### 3. 2-Points Gauss Quadrature
$$\int_{a}^b f(x)dx=\frac{b - a}{2}(f(\frac{b - a}{2} * \frac{1}{\sqrt{3}} + \frac{b + a}{2}) + f(\frac{b - a}{2} * \frac{-1}{\sqrt{3}} + \frac{b + a}{2}))$$

### 4. MidPoint Rule (One Point Gauss Quadrature)
$$\int_{a}^b f(x)dx=(b - a)f(\frac{b + a}{2})$$

## <a href="./regression.py">Regression</a>
### Linear Regression ($y = a + bx$)

$$\begin{bmatrix}
\sum_{1}^{n} 1 & \sum_{1}^{n} x_i \\
\sum_{1}^{n} x_i & \sum_{1}^{n} (x_i)^2
\end{bmatrix}
\begin{bmatrix}
a \\
b
\end{bmatrix} =
\begin{bmatrix}
\sum_{1}^{n} y_i \\
\sum_{1}^{n} x_i y_i
\end{bmatrix}$$
## <a href="./ode.py">ODE</a>
### 1. Euler Method ($y(t0) = y0$ & $f(x_i, y_i) = \frac{dy}{dx}$)
$$y_{i+1} = y_i + hf(x_i, y_i)$$

### 2. Taylor Method ($y(t0) = y0$ & $f(x_i, y_i) = \frac{dy}{dx}$)
$$y_{i+1} = y_i + hf(x_i, y_i) + \frac{h^2}{2}f^\prime(x_i, y_i)$$

### 3. Runge-Kutta 2nd Order ($y(t0) = y0$ & $f(x_i, y_i) = \frac{dy}{dx}$)
$$k_1 = f(x_i, y_i)$$

$$k_2 = f(x_i + p_1h, y_i + q_1 k_1 h)$$

$$y_{i+1} = y_i + h(a_1 k_1 + a_2 k_2)$$
#### Heun: $(a_1 = \frac{1}{2}, a_2 = \frac{1}{2}, p_1 = q_1 = 1)$
#### Midpoint: $(a_1 = 0, a_2 = 1, p_1 = q_1 = \frac{1}{2})$
#### Ralston: $(a_1 = \frac{1}{3}, a_2 = \frac{2}{3}, p_1 = q_1 = \frac{3}{4})$

### 4. Runge-Kutta 4th Order ($y(t0) = y0$ & $f(x_i, y_i) = \frac{dy}{dx}$)
$$k_1 = f(x_i, y_i)$$

$$k_2 = f(x_i + \frac{h}{2}, y_i + \frac{k_1 h}{2})$$

$$k_3 = f(x_i + \frac{h}{2}, y_i + \frac{k_2 h}{2})$$

$$k_4 = f(x_i + h, y_i + k_3 h)$$

$$y_{i+1} = y_i + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
## <a href="./eigenvalues.py">Eigenvalues</a>
### 1. Normalized Power Method
* Let $x_0$ be an initial approximation to the eigenvector.
* For $k=1,2,3,\ldots$ do
  * Compute $x_k=Ax_{k-1}$,
  * Normalize $x_k=x_k/\|x_k\|_\infty$
* Stop when tolerance is $t$
  
## <a href="./nonlinear.py">Non-Linear Equations</a>
### 1. Fixed Point
$$F(x) = 0$$

$$x = G(x)$$

$$x^{(k)} = G(x^{(k -1)})$$

### 2. Gauss Seidel
$$x^{(k)} = G(x^{(k)})$$

### 3. Newton's Method
$$-F(x^{(k - 1)}) = J(x^{(k - 1)})y^{(k - 1)}$$

$$x^{(k)} = x^{(k - 1)} + y^{(k - 1)}$$

where

$$
J =
\begin{bmatrix}
  \frac{\partial F_1}{\partial x_1} & \frac{\partial F_1}{\partial x_2} & \cdots & \frac{\partial F_1}{\partial x_n} \\
  \frac{\partial F_2}{\partial x_1} & \frac{\partial F_2}{\partial x_2} & \cdots & \frac{\partial F_2}{\partial x_n} \\
  \vdots & \vdots & \ddots & \vdots \\
  \frac{\partial F_m}{\partial x_1} & \frac{\partial F_m}{\partial x_2} & \cdots & \frac{\partial F_m}{\partial x_n} \\
\end{bmatrix}
$$

Setting the environment 🛠
--------------------------
#### 1. Make sure python v3.7 or higher is installed:

```console
* To get the version Excute:
$ python --version
Python 3.9.6
```
> if not installed watch the following [video](https://www.youtube.com/watch?v=VWgs_iTojoA)

#### 2. Make Sure Git is installed:
```console
* To get the version Excute:
$ git --version
git version 2.28.0.windows.1
```
> if not installed watch the following [video](https://www.youtube.com/watch?v=2j7fD92g-gE)

#### 3. Execute the following commands in your terminal after changing your directory to the desired path

```console
$ mkdir Numerical-Methods
$ python -m venv venv```
```
For Windows Users:
```
$ venv\Scripts\activate.bat
```
For Linux Users:
```
$ source venv/bin/activate
```
Then
```
$ git clone https://github.com/michaelehab/Numerical-Methods && cd Numerical-Methods
$ pip install -r requirements.txt
