
## **Step 1:**

$\begin{aligned}\newcommand\arraystretch{2.0}\text{Mean vector} = \begin{pmatrix}\dfrac{6+9+4+10}4\\\dfrac{6+10+11+5}4\\\end{pmatrix}=\renewcommand\arraystretch{1}\begin{pmatrix}7.25\\8\\\end{pmatrix}\end{aligned}$

For data $(6,6)$, difference from mean vector 
    $=\begin{pmatrix}6-7.25\\6-8\\\end{pmatrix} = \begin{pmatrix}-1.25\\-2\\\end{pmatrix}$  
        For data $(9,10)$, difference from mean vector 
    $=\begin{pmatrix}9-7.25\\10-8\\\end{pmatrix} = \begin{pmatrix}1.75\\2\\\end{pmatrix}$  
        For data $(4,11)$, difference from mean vector 
    $=\begin{pmatrix}4-7.25\\11-8\\\end{pmatrix} = \begin{pmatrix}-3.25\\3\\\end{pmatrix}$  
        For data $(10,5)$, difference from mean vector 
    $=\begin{pmatrix}10-7.25\\5-8\\\end{pmatrix} = \begin{pmatrix}2.75\\-3\\\end{pmatrix}$  
        
## **Step 2:**

$\begin{aligned}Y=\begin{pmatrix}-1.25&1.75&-3.25&2.75\\-2&2&3&-3\\\end{pmatrix}\end{aligned}$

$\Sigma=0.25YY^T=0.25\begin{pmatrix}-1.25&1.75&-3.25&2.75\\-2&2&3&-3\\\end{pmatrix}\begin{pmatrix}-1.25&-2\\1.75&2\\-3.25&3\\2.75&-3\\\end{pmatrix}\newcommand\arraystretch{2.0}=\begin{pmatrix}5.6875&-3\\-3&6.5\\\end{pmatrix}$
## **Step 3:**


$\begin{aligned}\newcommand\arraystretch{2.0}\begin{vmatrix}5.6875-\lambda&-3\\-3&6.5-\lambda\\\end{vmatrix}=0\end{aligned}$

$\begin{aligned}\left(5.6875-\lambda\right)\left(6.5-\lambda\right)-\left(-3\right)\left(-3\right)=0\end{aligned}$

Solving, we obtain the eigenvalues $\lambda = 3.0664$ and $\lambda = 9.1211$.
<table border="0"><tr><td style="vertical-align:top">

For $\lambda = 3.0664$,  
  
$\begin{aligned}    \newcommand\arraystretch{2.0}\begin{pmatrix}5.6875-3.0664&-3\\-3&6.5-3.0664\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    \newcommand\arraystretch{2.4}\begin{pmatrix}2.6211&-3\\-3&3.4336\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    \newcommand\arraystretch{1}\begin{pmatrix}1&-1.1445\\-1.1445&1.31\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    x_1=1.1445x_2    \end{aligned}$

Choosing the eigenvector with unit length, we have $\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}-0.7531\\-0.658\\\end{pmatrix}$.</td>
<td style="vertical-align:top">

For $\lambda = 9.1211$,  
  
$\begin{aligned}    \newcommand\arraystretch{2.0}\begin{pmatrix}5.6875-9.1211&-3\\-3&6.5-9.1211\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    \newcommand\arraystretch{2.4}\begin{pmatrix}-3.4336&-3\\-3&-2.6211\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    \newcommand\arraystretch{1}\begin{pmatrix}1&0.8737\\0.8737&0.7634\\\end{pmatrix}\renewcommand\arraystretch{1}\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0\\0\\\end{pmatrix}\\    x_1=-0.8737x_2    \end{aligned}$

Choosing the eigenvector with unit length, we have $\begin{pmatrix}x_1\\x_2\\\end{pmatrix}=\begin{pmatrix}0.658\\-0.7531\\\end{pmatrix}$.</td>
</tr>
</table>


## **Step 4:**

$\begin{aligned}\Phi=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}\end{aligned}$

## **Step 5:**

$\begin{aligned}Y=\Phi^TX=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}X\end{aligned}$

For data $(6,6)$, 
    $Y=\Phi^TX=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}\begin{pmatrix}6\\6\\\end{pmatrix}=\begin{pmatrix}-0.5706\\-8.4661\\\end{pmatrix}$  
        For data $(9,10)$, 
    $Y=\Phi^TX=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}\begin{pmatrix}9\\10\\\end{pmatrix}=\begin{pmatrix}-1.609\\-13.3571\\\end{pmatrix}$  
        For data $(4,11)$, 
    $Y=\Phi^TX=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}\begin{pmatrix}4\\11\\\end{pmatrix}=\begin{pmatrix}-5.6518\\-10.2497\\\end{pmatrix}$  
        For data $(10,5)$, 
    $Y=\Phi^TX=\begin{pmatrix}0.658&-0.7531\\-0.7531&-0.658\\\end{pmatrix}\begin{pmatrix}10\\5\\\end{pmatrix}=\begin{pmatrix}2.8143\\-10.8203\\\end{pmatrix}$  
        
$\begin{aligned}\newcommand\arraystretch{2.0}\text{Mean vector} = \begin{pmatrix}\dfrac{(-0.5706)+(-1.609)+(-5.6518)+2.8143}4\\\dfrac{(-8.4661)+(-13.3571)+(-10.2497)+(-10.8203)}4\\\end{pmatrix}=\renewcommand\arraystretch{1}\begin{pmatrix}-1.2543\\-10.7233\\\end{pmatrix}\end{aligned}$

For data $(6,6)$, final transformed vector
    $=\begin{pmatrix}-0.5706-(-1.2543)\\-8.4661-(-10.7233)\\\end{pmatrix} = \begin{pmatrix}0.6837\\2.2572\\\end{pmatrix}$  
        For data $(9,10)$, final transformed vector
    $=\begin{pmatrix}-1.609-(-1.2543)\\-13.3571-(-10.7233)\\\end{pmatrix} = \begin{pmatrix}-0.3547\\-2.6338\\\end{pmatrix}$  
        For data $(4,11)$, final transformed vector
    $=\begin{pmatrix}-5.6518-(-1.2543)\\-10.2497-(-10.7233)\\\end{pmatrix} = \begin{pmatrix}-4.3975\\0.4736\\\end{pmatrix}$  
        For data $(10,5)$, final transformed vector
    $=\begin{pmatrix}2.8143-(-1.2543)\\-10.8203-(-10.7233)\\\end{pmatrix} = \begin{pmatrix}4.0685\\-0.097\\\end{pmatrix}$  
        
## **Step 6:**
Thus,    
  $(6,6)$ is reduced to $(0.6837)$;   
   $(9,10)$ is reduced to $(-0.3547)$;   
   $(4,11)$ is reduced to $(-4.3975)$;   
   $(10,5)$ is reduced to $(4.0685)$;   
   