---
title: "Derivatives: A Refresher"
permalink: /resources/derivatives/
author_profile: true
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

The chain rule is the one that costs marks in exams. When the variable sits inside another function, differentiate the outer layer first, leave the inside alone, then multiply by the derivative of the inside:

<div class="math-display">
\[ \frac{d}{dx}\, e^{3x^2} \;=\; e^{3x^2} \cdot 6x \]
</div>

## 3. Worked examples

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

## 4. Reading the sign and the curvature

- *f′(x) > 0* on an interval means *f* is increasing there.
- *f′(x) < 0* means *f* is decreasing.
- *f′(x) = 0* gives a critical point: a candidate maximum, minimum or inflection.

The second derivative tells you the shape:

- *f″(x) > 0* means *f* is convex (curving up), so a critical point there is a minimum.
- *f″(x) < 0* means *f* is concave (curving down), so a critical point there is a maximum.

That is all of unconstrained optimisation: solve *f′(x) = 0* for the first-order condition, then check *f″* for the second-order condition. Check the boundaries of the domain too. The maximum of a function on [0, 10] can sit at 0 or at 10, where the derivative need not be zero.

## 5. Why economists care

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

## 6. Common mistakes

1. Forgetting the inner derivative. The derivative of *e³ˣ* is *3e³ˣ*, not *e³ˣ*.
2. Differentiating a product term by term. (f·g)′ is not f′·g′.
3. Sign slips in the quotient rule. The numerator is f′g − fg′, in that order, and it is not symmetric.
4. Treating every critical point as a maximum. Check the second derivative, or the sign of *f′* on either side.
5. Ignoring the domain. ln(x) only exists for *x > 0*, so a critical point outside the domain is not a solution.
6. Dropping units. A derivative carries units: output units per input unit. If the units come out wrong, so did the answer.

---

## Practice

Differentiate, then state where each function is increasing:

1. *f(x) = 3x⁴ − 8x³ + 6x²*
2. *f(x) = x e⁻ˣ*
3. *f(x) = ln(x² + 1)*
4. *f(x) = (2x − 5)/(x² + 1)*
5. A firm has *C(q) = q³ − 6q² + 15q*. Find marginal cost, the output at which it is lowest, and the price at which a price-taking firm would choose that output.

### Practice sheets

Three levels, every solution one click away:

- [Starter](/resources/derivatives-warmup/): 24 exercises on the definition and the basic rules.
- [Intermediate](/resources/derivatives-100/): 100 exercises on the product and quotient rules, almost no chain rule.
- [Upper intermediate](/resources/derivatives-second/): 20 exercises with the chain rule and second derivatives.

Once these are comfortable, the next step is [Lagrange multipliers](/resources/lagrange-multipliers/), which is how you optimise when a budget or a technology gets in the way.

Found a mistake, or want another topic here? [Email me](mailto:maximiliano.moreno-lopez@psemail.eu).
