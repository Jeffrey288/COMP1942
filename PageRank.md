
## **$r=Mr$**
The stochastic matrix $M$ is
\
$\begin{aligned}\begin{matrix}&\!\!\!\!\!\!&\begin{matrix}\text{x}&\text{y}&\text{z}\\\end{matrix}\\&\begin{matrix}\text{x}\\\text{y}\\\text{z}\\\end{matrix}\!\!\!\!\!\!&\begin{pmatrix}0&1&0.5\\0.5&0&0.5\\0.5&0&0\\\end{pmatrix}\\\end{matrix}\end{aligned}$
  
The page ranks are given by $r=Mr=\begin{pmatrix}0&1&0.5\\0.5&0&0.5\\0.5&0&0\\\end{pmatrix}r$. Initializing r by $\begin{pmatrix}1\\1\\1\\\end{pmatrix}$ and by iteration, we obtain<table border="0" ><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
1</td>
<td style="vertical-align:center;text-align:center;">
2</td>
<td style="vertical-align:center;text-align:center;">
3</td>
<td style="vertical-align:center;text-align:center;">
4</td>
<td style="vertical-align:center;text-align:center;">
5</td>
<td style="vertical-align:center;text-align:center;">
6</td>
<td style="vertical-align:center;text-align:center;">
7</td>
<td style="vertical-align:center;text-align:center;">
8</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.5\\1\\0.5\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.25\\1\\0.75\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.375\\1\\0.625\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.312\\1\\0.688\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.344\\1\\0.656\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.328\\1\\0.672\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.336\\1\\0.664\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

<table border="0" ><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
9</td>
<td style="vertical-align:center;text-align:center;">
10</td>
<td style="vertical-align:center;text-align:center;">
11</td>
<td style="vertical-align:center;text-align:center;">
12</td>
<td style="vertical-align:center;text-align:center;">
13</td>
<td style="vertical-align:center;text-align:center;">
14</td>
<td style="vertical-align:center;text-align:center;">
15</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.332\\1\\0.668\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.334\\1\\0.666\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

Summarizing, the page ranks are $\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}=\begin{pmatrix}1.333\\1\\0.667\\\end{pmatrix}$.
## **$r=pMr+c$**

  
  
  
  
  
  
  
  The stochastic matrix $M$ is
\
$\begin{aligned}\begin{matrix}&\!\!\!\!\!\!&\begin{matrix}\text{x}&\text{y}&\text{z}\\\end{matrix}\\&\begin{matrix}\text{x}\\\text{y}\\\text{z}\\\end{matrix}\!\!\!\!\!\!&\begin{pmatrix}0&1&0.5\\0.5&0&0.5\\0.5&0&0\\\end{pmatrix}\\\end{matrix}\end{aligned}$
  
The page ranks are given by $r=0.8Mr+c=0.8\begin{pmatrix}0&1&0.5\\0.5&0&0.5\\0.5&0&0\\\end{pmatrix}r+\begin{pmatrix}0.2\\0.2\\0.2\\\end{pmatrix}$. Initializing r by $\begin{pmatrix}1\\1\\1\\\end{pmatrix}$ and by iteration, we obtain<table border="0" ><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
1</td>
<td style="vertical-align:center;text-align:center;">
2</td>
<td style="vertical-align:center;text-align:center;">
3</td>
<td style="vertical-align:center;text-align:center;">
4</td>
<td style="vertical-align:center;text-align:center;">
5</td>
<td style="vertical-align:center;text-align:center;">
6</td>
<td style="vertical-align:center;text-align:center;">
7</td>
<td style="vertical-align:center;text-align:center;">
8</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.4\\1\\0.6\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.24\\1.0\\0.76\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.304\\1\\0.696\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.278\\1\\0.722\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.289\\1\\0.711\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.285\\1\\0.715\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.286\\1\\0.714\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

<table border="0" ><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
9</td>
<td style="vertical-align:center;text-align:center;">
10</td>
<td style="vertical-align:center;text-align:center;">
11</td>
<td style="vertical-align:center;text-align:center;">
12</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.286\\1.0\\0.714\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.286\\1\\0.714\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.286\\1\\0.714\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.286\\1\\0.714\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

Summarizing, the page ranks are $\begin{pmatrix}r(\text{x})\\r(\text{y})\\r(\text{z})\\\end{pmatrix}=\begin{pmatrix}1.286\\1\\0.714\\\end{pmatrix}$.