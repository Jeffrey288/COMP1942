Initially,  
|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$0.7$|$0.7$|$0.7$|
## **Iteration 1**
<table border="0"><tr><td style="vertical-align:top">

$\begin{aligned}    (x_1,x_2,d) = (170,90,1)    \end{aligned}$

$\begin{aligned}    \text{net} &=  w_1x_1+w_2x_2+b \\                 &=  0.7\times170+0.7\times90+ 0.7 \\                 &=  182.7    \end{aligned}$

$\begin{aligned}y&=\tanh{(\text{net})}\\&=\tanh(182.7)\\&=1.0\end{aligned}$

Correct!
</td>
<td style="vertical-align:top">

$\begin{aligned}w_1&\leftarrow w_1+\alpha(d-y)x_1 \\            &=0.7+0.3\times(1-            1.0)\times170 \\            &=0.7            \end{aligned}$

$\begin{aligned}w_2&\leftarrow w_2+\alpha(d-y)x_2 \\            &=0.7+0.3\times(1-            1.0)\times90 \\            &=0.7            \end{aligned}$

$\begin{aligned}b&\leftarrow b+\alpha(d-y) \\        &=0.7+0.3\times(1-        1.0) \\        &=0.7        \end{aligned}$
</td>
</tr>
</table>

|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$0.7$|$0.7$|$0.7$|
## **Iteration 2**
<table border="0"><tr><td style="vertical-align:top">

$\begin{aligned}    (x_1,x_2,d) = (190,95,-1)    \end{aligned}$

$\begin{aligned}    \text{net} &=  w_1x_1+w_2x_2+b \\                 &=  0.7\times190+0.7\times95+ 0.7 \\                 &=  200.2    \end{aligned}$

$\begin{aligned}y&=\tanh{(\text{net})}\\&=\tanh(200.2)\\&=1.0\end{aligned}$

Incorrect!
</td>
<td style="vertical-align:top">

$\begin{aligned}w_1&\leftarrow w_1+\alpha(d-y)x_1 \\            &=0.7+0.3\times(-1-            1.0)\times190 \\            &=-113.3            \end{aligned}$

$\begin{aligned}w_2&\leftarrow w_2+\alpha(d-y)x_2 \\            &=0.7+0.3\times(-1-            1.0)\times95 \\            &=-56.3            \end{aligned}$

$\begin{aligned}b&\leftarrow b+\alpha(d-y) \\        &=0.7+0.3\times(-1-        1.0) \\        &=0.1        \end{aligned}$
</td>
</tr>
</table>

|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$-113.3$|$-56.3$|$0.1$|
## **Iteration 3**
<table border="0"><tr><td style="vertical-align:top">

$\begin{aligned}    (x_1,x_2,d) = (160,50,-1)    \end{aligned}$

$\begin{aligned}    \text{net} &=  w_1x_1+w_2x_2+b \\                 &=  -113.3\times160+-56.3\times50+ 0.1 \\                 &=  -20942.9    \end{aligned}$

$\begin{aligned}y&=\tanh{(\text{net})}\\&=\tanh(-20942.9)\\&=-1.0\end{aligned}$

Incorrect!
</td>
<td style="vertical-align:top">

$\begin{aligned}w_1&\leftarrow w_1+\alpha(d-y)x_1 \\            &=-113.3+0.3\times(-1-            -1.0)\times160 \\            &=-113.3            \end{aligned}$

$\begin{aligned}w_2&\leftarrow w_2+\alpha(d-y)x_2 \\            &=-56.3+0.3\times(-1-            -1.0)\times50 \\            &=-56.3            \end{aligned}$

$\begin{aligned}b&\leftarrow b+\alpha(d-y) \\        &=0.1+0.3\times(-1-        -1.0) \\        &=0.1        \end{aligned}$
</td>
</tr>
</table>

|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$-113.3$|$-56.3$|$0.1$|
## **Iteration 4**
<table border="0"><tr><td style="vertical-align:top">

$\begin{aligned}    (x_1,x_2,d) = (180,70,-1)    \end{aligned}$

$\begin{aligned}    \text{net} &=  w_1x_1+w_2x_2+b \\                 &=  -113.3\times180+-56.3\times70+ 0.1 \\                 &=  -24334.9    \end{aligned}$

$\begin{aligned}y&=\tanh{(\text{net})}\\&=\tanh(-24334.9)\\&=-1.0\end{aligned}$

Incorrect!
</td>
<td style="vertical-align:top">

$\begin{aligned}w_1&\leftarrow w_1+\alpha(d-y)x_1 \\            &=-113.3+0.3\times(-1-            -1.0)\times180 \\            &=-113.3            \end{aligned}$

$\begin{aligned}w_2&\leftarrow w_2+\alpha(d-y)x_2 \\            &=-56.3+0.3\times(-1-            -1.0)\times70 \\            &=-56.3            \end{aligned}$

$\begin{aligned}b&\leftarrow b+\alpha(d-y) \\        &=0.1+0.3\times(-1-        -1.0) \\        &=0.1        \end{aligned}$
</td>
</tr>
</table>

|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$-113.3$|$-56.3$|$0.1$|
## **Iteration 5**
<table border="0"><tr><td style="vertical-align:top">

$\begin{aligned}    (x_1,x_2,d) = (170,90,1)    \end{aligned}$

$\begin{aligned}    \text{net} &=  w_1x_1+w_2x_2+b \\                 &=  -113.3\times170+-56.3\times90+ 0.1 \\                 &=  -24327.9    \end{aligned}$

$\begin{aligned}y&=\tanh{(\text{net})}\\&=\tanh(-24327.9)\\&=-1.0\end{aligned}$

Incorrect!
</td>
<td style="vertical-align:top">

$\begin{aligned}w_1&\leftarrow w_1+\alpha(d-y)x_1 \\            &=-113.3+0.3\times(1-            -1.0)\times170 \\            &=-11.3            \end{aligned}$

$\begin{aligned}w_2&\leftarrow w_2+\alpha(d-y)x_2 \\            &=-56.3+0.3\times(1-            -1.0)\times90 \\            &=-2.3            \end{aligned}$

$\begin{aligned}b&\leftarrow b+\alpha(d-y) \\        &=0.1+0.3\times(1-        -1.0) \\        &=0.7        \end{aligned}$
</td>
</tr>
</table>

|$w_1$|$w_2$|$b$|
|:-:|:-:|:-:|
|$-11.3$|$-2.3$|$0.7$|
