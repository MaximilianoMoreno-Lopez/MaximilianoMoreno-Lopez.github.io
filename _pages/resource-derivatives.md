---
title: "Derivatives: A Refresher"
permalink: /resources/derivatives/
redirect_from:
  - /teaching/resources/derivatives/
---

*Teaching resource for Mathematics, Sciences Po Paris.*

A derivative tells you how much the output of a function moves when you nudge the input. Everything below is either a way of computing that number or a way of reading it.

---

## 1. The definition

The derivative of a function *f* at a point *x* is the limit of the average rate of change as the nudge goes to zero:

<div class="math-display">
\[ f'(x) \;=\; \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \]
</div>

Geometrically, *f′(x)* is the slope of the tangent line to the graph of *f* at *x*. Read it as a rate per unit of *x*: if *x* is measured in tonnes and *f* in euros, then *f′(x)* is euros per tonne.

If that limit does not exist, *f* is not differentiable at *x*. That happens at kinks (like |x| at 0), at jumps, and where the tangent is vertical. Every differentiable function is continuous, but plenty of continuous functions are not differentiable.

## 2. The rules

| Rule | Statement |
|---|---|
| Constant | (c)′ = 0 |
| Power | (xⁿ)′ = n·xⁿ⁻¹ |
| Constant multiple | (c·f)′ = c·f′ |
| Sum | (f ± g)′ = f′ ± g′ |
| Product | (f·g)′ = f′g + fg′ |
| Quotient | (f/g)′ = (f′g − fg′)/g² |
| Chain | (f(g(x)))′ = f′(g(x))·g′(x) |

The functions you will meet most often:

<div class="math-display">
\[ (e^x)' = e^x \qquad (\ln x)' = \frac{1}{x} \qquad (a^x)' = a^x \ln a \]
\[ (\sin x)' = \cos x \qquad (\cos x)' = -\sin x \]
</div>

## 3. The chain rule, properly

The chain rule is the one that costs marks, so it gets its own section. It handles any function built by putting one function inside another: *e* raised to something, the log of something, something to a power.

**The idea.** Think of the function as layers. In *e^{3x²}* the outer layer is "*e* to the power of" and the inner layer is *3x²*. A small change in *x* changes the inside; the change in the inside then changes the outside. The two effects multiply, so the derivative is the derivative of the outside, evaluated at the inside, times the derivative of the inside:

<div class="math-display">
\[ \frac{d}{dx} f\big(g(x)\big) \;=\; f'\big(g(x)\big)\cdot g'(x) \]
</div>

**The routine.** Call the inside *u*. Differentiate the outer function with respect to *u* as if *u* were a plain variable, leave *u* exactly as it is, then multiply by *du/dx*. Four outer functions cover almost every case:

<div class="math-display">
\[ (e^{u})' = e^{u}\, u' \qquad (\ln u)' = \frac{u'}{u} \qquad (u^{n})' = n u^{n-1}\, u' \qquad (\sqrt{u})' = \frac{u'}{2\sqrt{u}} \]
</div>

**Three examples, one more layer each.**

*One layer.* *f(x) = (3x² + 1)⁵*. Inside *u = 3x² + 1*, so *u′ = 6x*. Outer rule: *(u⁵)′ = 5u⁴ u′*.

<div class="math-display">
\[ f'(x) = 5(3x^2 + 1)^4 \cdot 6x = 30x\,(3x^2+1)^4 \]
</div>

*Exponential inside.* *f(x) = e^{−x²}*. Inside *u = −x²*, *u′ = −2x*.

<div class="math-display">
\[ f'(x) = e^{-x^2} \cdot (-2x) = -2x\,e^{-x^2} \]
</div>

*Two layers.* *f(x) = ln(√(x² + 1))*. Work from the outside in: the log of something, then the square root of something, then *x² + 1*.

<div class="math-display">
\[ f'(x) = \frac{1}{\sqrt{x^2+1}} \cdot \frac{1}{2\sqrt{x^2+1}} \cdot 2x = \frac{x}{x^2+1} \]
</div>

(A shortcut here: *ln √v = ½ ln v*, so *f = ½ ln(x² + 1)* and the answer follows in one step. Simplifying before differentiating is often the smart move.)

**How to know you need it.** If the thing being raised, logged or exponentiated is anything other than a bare *x*, you need the chain rule. *e^x* does not; *e^{2x}* does. *ln x* does not; *ln(x² + 1)* does. The most common mistake in the whole course is writing *(e^{2x})′ = e^{2x}* and forgetting the factor 2.

## 4. Worked examples

**(a) Product and chain together.** Let *f(x) = x² ln x*.

<div class="math-display">
\[ f'(x) = 2x \ln x + x^2 \cdot \frac{1}{x} = 2x\ln x + x \]
</div>

**(b) Quotient.** Let *f(x) = (x + 1)/(x − 2)*, with *x ≠ 2*.

<div class="math-display">
\[ f'(x) = \frac{1 \cdot (x-2) - (x+1) \cdot 1}{(x-2)^2} = \frac{-3}{(x-2)^2} \]
</div>

The derivative is negative everywhere the function is defined, so *f* is decreasing on both sides of the asymptote.

**(c) Nested chain.** Let *f(x) = ln(1 + e²ˣ)*. Peel the layers from the outside in:

<div class="math-display">
\[ f'(x) = \frac{1}{1+e^{2x}} \cdot e^{2x} \cdot 2 = \frac{2e^{2x}}{1+e^{2x}} \]
</div>

## 5. Reading the sign and the curvature

- *f′(x) > 0* on an interval means *f* is increasing there.
- *f′(x) < 0* means *f* is decreasing.
- *f′(x) = 0* gives a critical point: a candidate maximum, minimum or inflection.

The second derivative tells you the shape:

- *f″(x) > 0* means *f* is convex (curving up), so a critical point there is a minimum.
- *f″(x) < 0* means *f* is concave (curving down), so a critical point there is a maximum.

That is all of unconstrained optimisation: solve *f′(x) = 0* for the first-order condition, then check *f″* for the second-order condition. Check the boundaries of the domain too. The maximum of a function on [0, 10] can sit at 0 or at 10, where the derivative need not be zero.

## 6. Why economists care

Almost every marginal object in economics is a derivative.

**Marginal cost.** If *C(q)* is the total cost of producing *q* units, marginal cost is *C′(q)*. A price-taking firm maximises profit *π(q) = p·q − C(q)*, so:

<div class="math-display">
\[ \pi'(q) = p - C'(q) = 0 \quad\Longrightarrow\quad p = C'(q) \]
</div>

Price equals marginal cost. The second-order condition *π″(q) = −C″(q) < 0* says that marginal cost has to be increasing at the optimum.

**Marginal utility and the MRS.** With utility *U(x, y)*, the partial derivatives *∂U/∂x* and *∂U/∂y* are marginal utilities. Their ratio is the marginal rate of substitution, which is the slope of the indifference curve.

**Elasticity.** An elasticity is a derivative made unit-free, so you can compare a market measured in litres with one measured in kilowatt-hours:

<div class="math-display">
\[ \varepsilon \;=\; \frac{dQ}{dP} \cdot \frac{P}{Q} \;=\; \frac{d \ln Q}{d \ln P} \]
</div>

The second form is why we regress logs on logs so often: the coefficient you estimate is the elasticity.

**Growth rates.** For a variable *X(t)* over time, the growth rate is the derivative of its log:

<div class="math-display">
\[ g_X \;=\; \frac{\dot{X}(t)}{X(t)} \;=\; \frac{d \ln X(t)}{dt} \]
</div>

## 7. Common mistakes

1. Forgetting the inner derivative. The derivative of *e³ˣ* is *3e³ˣ*, not *e³ˣ*.
2. Differentiating a product term by term. (f·g)′ is not f′·g′.
3. Sign slips in the quotient rule. The numerator is f′g − fg′, in that order, and it is not symmetric.
4. Treating every critical point as a maximum. Check the second derivative, or the sign of *f′* on either side.
5. Ignoring the domain. ln(x) only exists for *x > 0*, so a critical point outside the domain is not a solution.
6. Dropping units. A derivative carries units: output units per input unit. If the units come out wrong, so did the answer.

---

## Practice

Differentiate, then state where each function is increasing. Open the solution to check.

<div class="practice practice--long" id="practice">
<ol class="practice-list practice-list--long">
<li class="practice-item"><span class="practice-n">1.</span>
<div class="practice-q">\( f(x) = 3x^4 - 8x^3 + 6x^2 \)</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ f'(x) = 12x^3 - 24x^2 + 12x = 12x\,(x-1)^2 \]
<p>The factor \( (x-1)^2 \) is never negative, so the sign is the sign of \( x \): \( f \) is decreasing for \( x < 0 \) and increasing for \( x > 0 \). At \( x = 1 \) the derivative touches zero without changing sign, so that is a flat point, not a turning point.</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">2.</span>
<div class="practice-q">\( f(x) = x\,e^{-x} \)</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
<p>Product rule, with the chain rule on \( e^{-x} \):</p>
\[ f'(x) = e^{-x} + x \cdot (-e^{-x}) = e^{-x}(1 - x) \]
<p>Since \( e^{-x} > 0 \) always, \( f \) is increasing for \( x < 1 \) and decreasing for \( x > 1 \). The maximum is at \( x = 1 \), where \( f = 1/e \).</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">3.</span>
<div class="practice-q">\( f(x) = \ln(x^2 + 1) \)</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
<p>Chain rule with inside \( u = x^2 + 1 \), \( u' = 2x \):</p>
\[ f'(x) = \frac{2x}{x^2 + 1} \]
<p>The denominator is positive, so \( f \) is increasing for \( x > 0 \) and decreasing for \( x < 0 \), with a minimum at \( x = 0 \). The domain is all real numbers because \( x^2 + 1 > 0 \).</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">4.</span>
<div class="practice-q">\( f(x) = \dfrac{2x - 5}{x^2 + 1} \)</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
<p>Quotient rule:</p>
\[ f'(x) = \frac{2(x^2+1) - (2x-5)\,2x}{(x^2+1)^2} = \frac{-2x^2 + 10x + 2}{(x^2+1)^2} = \frac{-2\,(x^2 - 5x - 1)}{(x^2+1)^2} \]
<p>The sign is the sign of \( -(x^2 - 5x - 1) \). The roots of \( x^2 - 5x - 1 = 0 \) are \( x = \tfrac{5 \pm \sqrt{29}}{2} \), about \( -0.19 \) and \( 5.19 \). So \( f \) is increasing between them and decreasing outside.</p>
</div></details></li>
<li class="practice-item"><span class="practice-n">5.</span>
<div class="practice-q">A firm has \( C(q) = q^3 - 6q^2 + 15q \). Find marginal cost, the output at which it is lowest, and the price at which a price-taking firm would choose that output.</div>
<details class="practice-sol"><summary>Solution</summary><div class="practice-a tex2jax_ignore">
\[ MC(q) = C'(q) = 3q^2 - 12q + 15 \]
<p>Marginal cost is lowest where its own derivative is zero: \( MC'(q) = 6q - 12 = 0 \), so \( q = 2 \), and \( MC''(q) = 6 > 0 \) confirms a minimum. There \( MC(2) = 12 - 24 + 15 = 3 \).</p>
<p>A price-taking firm produces where \( p = MC(q) \), so it would choose \( q = 2 \) at a price of \( 3 \). Note that at exactly this point marginal cost is flat, so the second-order condition holds only weakly; for any price above 3 the firm picks the larger root of \( 3q^2 - 12q + 15 = p \), on the rising part of the curve.</p>
</div></details></li>
</ol>
</div>

{% include practice-reveal.html %}

### Practice sheets

Three levels, every solution one click away:

- [Starter](/resources/derivatives-warmup/): 24 exercises on the definition and the basic rules.
- [Intermediate](/resources/derivatives-100/): 100 exercises on the product and quotient rules, almost no chain rule.
- [Upper intermediate](/resources/derivatives-second/): 20 exercises with the chain rule and second derivatives.

Once these are comfortable, the next step is [Lagrange multipliers](/resources/lagrange-multipliers/), which is how you optimise when a budget or a technology gets in the way.

Found a mistake, or want another topic here? [Email me](mailto:maximiliano.moreno-lopez@psemail.eu).
