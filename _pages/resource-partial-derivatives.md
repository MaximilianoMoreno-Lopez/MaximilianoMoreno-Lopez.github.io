---
title: "Partial Derivatives and Optimisation in Two Variables"
permalink: /resources/partial-derivatives/
---

*Teaching resource for Intermediate Microeconomics (Tutorial 1) and Mathematics, Sciences Po Paris.*

Almost nothing in microeconomics depends on one variable. Utility depends on several goods, output on several inputs, a voter's payoff on the tax rate and on her income. Partial derivatives are how you take a derivative when there is more than one variable in the room, and they are the whole engine behind marginal utility, the MRS, marginal products and first-order conditions. This note assumes you can differentiate in one variable; if not, start with the [derivatives refresher](/resources/derivatives/).

---

## 1. What a partial derivative is

Take *f(x, y)*. The partial derivative of *f* with respect to *x* asks: if I nudge *x* a little and hold *y* exactly fixed, how much does *f* move? It is written *∂f/∂x* or *f_x*.

<div class="math-display">
\[ \frac{\partial f}{\partial x} \;=\; \lim_{h \to 0} \frac{f(x + h,\, y) - f(x,\, y)}{h} \]
</div>

Geometrically, *f(x, y)* is a surface. Slicing it with a vertical plane at a fixed *y* gives a one-variable curve, and *f_x* is the slope of that curve. There is one partial derivative per variable, and together they form the gradient *∇f = (f_x, f_y)*.

## 2. How to compute one

**Rule.** To differentiate with respect to *x*, treat every other variable as if it were a number. Then use the ordinary one-variable rules.

The example from the Tutorial 1 slides, *g(x₁, x₂) = x₁x₂² − 3x₁*:

<div class="math-display">
\[ \frac{\partial g}{\partial x_1} = x_2^2 - 3 \qquad\qquad \frac{\partial g}{\partial x_2} = 2x_1 x_2 \]
</div>

For *∂g/∂x₁*, the factor *x₂²* is a constant multiplying *x₁*, so it survives, and *−3x₁* gives *−3*. For *∂g/∂x₂*, the term *−3x₁* is a constant and disappears, and *x₁x₂²* is a constant times *x₂²*.

Three more that you will meet constantly:

<div class="math-display">
\[ U = x^{a} y^{b}: \qquad U_x = a\,x^{a-1} y^{b}, \qquad U_y = b\,x^{a} y^{b-1} \]
\[ U = \ln x + \ln y: \qquad U_x = \frac1x, \qquad U_y = \frac1y \]
\[ f = e^{2x} \ln y: \qquad f_x = 2e^{2x} \ln y, \qquad f_y = \frac{e^{2x}}{y} \]
</div>

The chain rule works exactly as before: in the last example the factor 2 comes from differentiating *2x* inside the exponential.

## 3. Reading them as economics

- **Marginal utility.** *U_x = ∂U/∂x* is the extra utility from one more unit of *x*, holding *y* fixed. Diminishing marginal utility is *U_xx < 0*.
- **Marginal product.** For *Q(K, L)*, *Q_L* is the marginal product of labour. For Cobb-Douglas *Q = A K^α L^β*, *Q_L = β Q/L*: the exponent is the output elasticity.
- **Marginal rate of substitution.** The slope of an indifference curve is *−U_x/U_y*; the MRS is the ratio *U_x/U_y*. For *U = x^a y^b* it is *(a/b)(y/x)*. This ratio is what you set equal to the price ratio in a consumer problem.
- **Elasticities.** *(∂Q/∂p)(p/Q)* is a partial derivative made unit-free. For *Q = A p^{−2} m*, the price elasticity is *−2* and the income elasticity is *1*: the exponents.

**Why the MRS is a ratio of partials.** Along an indifference curve *U(x, y) = c*, the total change is zero:

<div class="math-display">
\[ dU = U_x\,dx + U_y\,dy = 0 \quad\Longrightarrow\quad \frac{dy}{dx} = -\frac{U_x}{U_y} \]
</div>

That is the total differential, and it gives the slope of any level curve *F(x, y) = c* as *−F_x/F_y* without ever solving for *y*. On the circle *x² + y² = 25* at *(3, 4)* the slope is *−3/4*.

## 4. Second-order partials

Differentiate a partial derivative again and you get four second-order partials: *f_xx*, *f_yy*, and the two cross partials *f_xy* (differentiate *f_x* with respect to *y*) and *f_yx*. For any function you will meet in this course the cross partials are equal, *f_xy = f_yx* (Young's theorem). Use that as a free check on your algebra.

For *f = x³y − 2xy² + y*: *f_x = 3x²y − 2y²*, *f_y = x³ − 4xy + 1*, so

<div class="math-display">
\[ f_{xx} = 6xy, \qquad f_{yy} = -4x, \qquad f_{xy} = f_{yx} = 3x^2 - 4y \]
</div>

## 5. Unconstrained optimisation in two variables

**First-order conditions.** At a maximum or minimum the surface is flat in every direction, so every partial derivative is zero. That gives a system of as many equations as variables:

<div class="math-display">
\[ f_x(x^*, y^*) = 0, \qquad f_y(x^*, y^*) = 0 \]
</div>

**Second-order conditions.** A flat point can be a hilltop, a valley bottom or a saddle (up one way, down the other). Compute

<div class="math-display">
\[ D \;=\; f_{xx}\, f_{yy} - \big(f_{xy}\big)^2 \]
</div>

at the critical point, and read:

| | |
|---|---|
| *D > 0* and *f_xx > 0* | minimum |
| *D > 0* and *f_xx < 0* | maximum |
| *D < 0* | saddle point |
| *D = 0* | the test is silent; look at the function directly |

The slide example, *f(y, z) = y² − 2y + z²*: the conditions *2y − 2 = 0* and *2z = 0* give *(1, 0)*; then *f_yy = 2*, *f_zz = 2*, *f_yz = 0*, so *D = 4 > 0* with *f_yy > 0*: a minimum. Completing the square confirms it: *f = (y − 1)² + z² − 1*.

A saddle for contrast, *f(x, y) = x² − y² + 2x*: the critical point is *(−1, 0)*, but *D = (2)(−2) − 0 = −4 < 0*. The first-order conditions found a flat point that is neither a maximum nor a minimum. This is why the second-order check is not optional.

When the two first-order conditions involve both variables, solve them as a system. A firm with profit *π = 20q₁ + 30q₂ − q₁² − q₂² − q₁q₂* has *π₁ = 20 − 2q₁ − q₂* and *π₂ = 30 − 2q₂ − q₁*; solving gives *q₁ = 10/3*, *q₂ = 40/3*, and *D = 4 − 1 = 3 > 0* with *π₁₁ < 0* confirms a maximum.

## 6. One variable, but with parameters: the Problem Set 1 model

Often you differentiate with respect to one variable while others sit in the formula as parameters. That is a partial derivative too, and it is exactly what Problem 3 of Problem Set 1 asks for. An agent with income *y_i* gets

<div class="math-display">
\[ V(\tau, y_i) = (1 - \tau)\,y_i + (\tau - \tau^2)\,\bar y \]
</div>

from a tax rate *τ*. Here *y_i* and *ȳ* are parameters; *τ* is the variable.

<div class="math-display">
\[ \frac{\partial V}{\partial \tau} = -y_i + (1 - 2\tau)\,\bar y, \qquad \frac{\partial^2 V}{\partial \tau^2} = -2\bar y < 0 \]
</div>

The second derivative is negative, so *V* is strictly concave in *τ*: single-peaked preferences, one best tax rate per agent. Setting the first derivative to zero:

<div class="math-display">
\[ \tau_i^* = \frac12\left(1 - \frac{y_i}{\bar y}\right) \]
</div>

for *y_i ≤ ȳ*, and zero for anyone richer than average. Now differentiate the *answer* with respect to the *parameter*: *∂τ_i\*/∂y_i = −1/(2ȳ) < 0*. Richer agents prefer lower taxes. That last step, differentiating a solution with respect to a parameter to see how the solution moves, is called comparative statics, and you will do it in every part of this course.

## 7. Common mistakes

1. Forgetting that the other variable is a constant. In *∂(x²y)/∂x* the answer is *2xy*, not *2x*: the *y* stays.
2. Dropping a term that does contain the variable. In *∂(x₁x₂² − 3x₁)/∂x₁* both terms contain *x₁*, so both contribute.
3. Confusing *f_xy* with *f_xx f_yy*. The cross partial is a single second derivative, taken in *x* then in *y*.
4. Stopping at the first-order conditions. Without *D* you do not know whether you found a maximum, a minimum or a saddle.
5. Evaluating *D* in general when it depends on the point. Plug in each critical point separately; the sign can differ from one to the next.
6. Treating the parameter as the variable in Problem Set 1. You differentiate *V* with respect to *τ*, not *y_i*; *y_i* only comes back when you ask how *τ_i\** changes with it.

---

## Practice

Five to check yourself. The [full practice sheet](/resources/partial-derivatives-practice/) has twenty-two more, in three levels.

<div class="practice practice--long" id="practice">
<ol class="practice-list practice-list--long">
<li class="practice-item"><span class="practice-n">1.</span>
<div class="practice-q">Compute both partials of \( f(x, y) = x^2 y^3 + e^{y} - 4x \).</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ f_x = 2xy^3 - 4, \qquad f_y = 3x^2 y^2 + e^{y} \]
<p>For \( f_x \), \( e^y \) is a constant and vanishes; for \( f_y \), \( -4x \) vanishes.</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">2.</span>
<div class="practice-q">For \( U(x, y) = x^{1/4} y^{3/4} \), find the MRS and evaluate it at \( (1, 3) \).</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ MRS = \frac{U_x}{U_y} = \frac{\tfrac14 x^{-3/4} y^{3/4}}{\tfrac34 x^{1/4} y^{-1/4}} = \frac{y}{3x} \]
<p>At \( (1, 3) \) the MRS is \( 1 \). General pattern for \( x^a y^b \): \( MRS = \frac{a}{b}\cdot\frac{y}{x} \).</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">3.</span>
<div class="practice-q">Find the slope of the level curve \( xy = 12 \) at \( (3, 4) \) using partial derivatives.</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ \frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{y}{x} = -\frac43 \]
<p>Check by solving explicitly: \( y = 12/x \), \( y' = -12/x^2 = -12/9 = -4/3 \). Same answer, but the partial-derivative route works even when you cannot solve for \( y \).</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">4.</span>
<div class="practice-q">Find and classify the critical point of \( f(x, y) = -2x^2 - y^2 + 8x + 2y \).</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ f_x = -4x + 8 = 0 \Rightarrow x = 2, \qquad f_y = -2y + 2 = 0 \Rightarrow y = 1 \]
\[ f_{xx} = -4, \quad f_{yy} = -2, \quad f_{xy} = 0, \qquad D = 8 > 0 \]
<p>\( D > 0 \) and \( f_{xx} < 0 \): a maximum at \( (2, 1) \), where \( f = -8 - 1 + 16 + 2 = 9 \).</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">5.</span>
<div class="practice-q">In the Problem Set 1 model, suppose average income is \( \bar y = 0.5 \). Which agents prefer a tax rate of at least \( 0.25 \)? What does the median voter choose if median income is \( 0.4 \)?</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ \tau_i^* = \frac12\left(1 - \frac{y_i}{0.5}\right) = \frac12 - y_i \geq 0.25 \quad\Longleftrightarrow\quad y_i \leq 0.25 \]
<p>Agents with income up to \( 0.25 \), half the average, want \( \tau \geq 0.25 \). The median voter with \( y_m = 0.4 \) chooses \( \tau^* = 0.5 - 0.4 = 0.1 \): a positive tax, because the median is below the mean. In the problem set the distribution was uniform, median equal to mean, and the tax was zero.</p>
</div></details></li>
</ol>
</div>

{% include practice-reveal.html %}

Constrained problems, where a budget or a technology limits the choice, are the next step: [Lagrange multipliers](/resources/lagrange-multipliers/).

Found a mistake, or want another topic here? [Email me](mailto:maximiliano.moreno-lopez@psemail.eu).
