The adjacency matrix $M$ is
\
$\begin{aligned}\begin{matrix}&\!\!\!\!\!\!&\begin{matrix}\text{x}&\text{y}&\text{z}\\\end{matrix}\\&\begin{matrix}\text{x}\\\text{y}\\\text{z}\\\end{matrix}\!\!\!\!\!\!&\begin{pmatrix}0&1&0\\1&0&0\\1&1&0\\\end{pmatrix}\\\end{matrix}\end{aligned}$
  
The hub scores are given by $h=MM^Th=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\\\end{pmatrix}h$. Initializing h by $\begin{pmatrix}1\\1\\1\\\end{pmatrix}$ and by iteration, we obtain<table border="0"><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
1</td>
<td style="vertical-align:center;text-align:center;">
2</td>
<td style="vertical-align:center;text-align:center;">
3</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}h(\text{x})\\h(\text{y})\\h(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}2\\2\\4\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}2.25\\2.25\\4.5\\\end{pmatrix}\end{aligned}$
</td>
</tr>
<tr>
<td>

$h$   
Normalized</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}0.75\\0.75\\1.5\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}0.75\\0.75\\1.5\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

  
The authority scores are given by $a=M^TMa=\begin{pmatrix}2&1&0\\1&2&0\\0&0&0\\\end{pmatrix}a$. Initializing a by $\begin{pmatrix}1\\1\\1\\\end{pmatrix}$ and by iteration, we obtain<table border="0"><tr><td style="vertical-align:center;text-align:center;">
Iteration</td>
<td style="vertical-align:center;text-align:center;">
1</td>
<td style="vertical-align:center;text-align:center;">
2</td>
<td style="vertical-align:center;text-align:center;">
3</td>
</tr>
<tr>
<td>

$\begin{aligned}\begin{pmatrix}a(\text{x})\\a(\text{y})\\a(\text{z})\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}3\\3\\0\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}4.5\\4.5\\0\\\end{pmatrix}\end{aligned}$
</td>
</tr>
<tr>
<td>

$a$   
Normalized</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1\\1\\1\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.5\\1.5\\0\\\end{pmatrix}\end{aligned}$
</td>
<td style="vertical-align:center;text-align:center;">

$\begin{aligned}\begin{pmatrix}1.5\\1.5\\0\\\end{pmatrix}\end{aligned}$
</td>
</tr>
</table>

Summarizing, the hub scores are $\begin{pmatrix}h(\text{x})\\h(\text{y})\\h(\text{z})\\\end{pmatrix}=\begin{pmatrix}0.75\\0.75\\1.5\\\end{pmatrix}$ and the authority scores are $\begin{pmatrix}a(\text{x})\\a(\text{y})\\a(\text{z})\\\end{pmatrix}=\begin{pmatrix}1.5\\1.5\\0\\\end{pmatrix}$.