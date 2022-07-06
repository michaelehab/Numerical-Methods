# Numerical Methods implemented in Python
<div align="center">

![numerical analysis](https://user-images.githubusercontent.com/29122581/177538989-e1e77473-0cd3-4eb8-8c19-8ff87230ac5a.png)
![GitHub stars](https://img.shields.io/github/stars/michaelehab/Numerical-Methods?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/michaelehab/Numerical-Methods?style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/michaelehab/Numerical-Methods?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/michaelehab/Numerical-Methods?style=plastic)
</div>

# Definition (<a href="https://en.wikipedia.org/wiki/Numerical_analysis">WIKI</a>):
Numerical analysis is the study of algorithms that use numerical approximation for the problems of mathematical analysis. Numerical analysis finds application in all fields of engineering and the physical sciences, and in the 21st century also the life and social sciences, medicine, business and even the arts.

# Subjects
## <a href="./interpolation.py">Interpolation</a>
### Lagrange Interpolating Polynomial:
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

### Newton Divided Difference:
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
    <td>14</td>
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

## Differentiation
## Integration
## Regression
## ODE
## Eigenvalues
## Non-Linear Equations
