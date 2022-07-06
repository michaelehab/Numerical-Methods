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
## Differentiation
## Integration
## Regression
## ODE
## Eigenvalues
## Non-Linear Equations
