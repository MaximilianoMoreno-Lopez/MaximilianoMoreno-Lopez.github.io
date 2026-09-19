---
title: "Derivatives: A Refresher"
permalink: /resources/derivatives/
author_profile: true
redirect_from:
  - /teaching/resources/derivatives/
---

*Teaching resource — Mathematics, Sciences Po Paris.*

A derivative answers one question: **if I nudge the input a little, how much does the output move?** Everything below is either a way of computing that number, or a way of reading it once you have it.

---

## 1. The definition

The derivative of a function *f* at a point *x* is the limit of the average rate of change as the nudge shrinks to zero:

<div class="math-display">
\[ f'(x) \;=\; \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \]
</div>

Geometrically, *f′(x)* is the slope of the tangent line to the graph of *f* at *x*. Read it as a **rate per unit of x**: if *x* is measured in tonnes and *f* in euros, then *f′(x)* is euros per tonne.

If that limit does not exist, *f* is not differentiable at *x*. That happens at kinks (|x| at 0), at jumps, and at vertical tangents. **Differentiable ⟹ continuous, but not the reverse.**

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

And the functions you will meet constantly:

<div class="math-display">
\[ (e^x)' = e^x \qquad (\ln x)' = \frac{1}{x} \qquad (a^x)' = a^x \ln a \]
\[ (\sin x)' = \cos x \qquad (\cos x)' = -\sin x \]
</div>

The **chain rule** is the one that costs marks. Whenever the variable sits inside something else, differentiate the outer layer first, leaving the inside untouched, then multiply by the derivative of the inside:

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

The sign is negative everywhere the function is defined, so *f* is decreasing on both sides of the asymptote.

**(c) Nested chain.** Let *f(x) = ln(1 + e²ˣ)*. Peel the layers from the outside in:

<div class="math-display">
\[ f'(x) = \frac{1}{1+e^{2x}} \cdot e^{2x} \cdot 2 = \frac{2e^{2x}}{1+e^{2x}} \]
</div>

## 4. Reading the sign and the curvature

- *f′(x) > 0* on an interval ⟹ *f* is **increasing** there.
- *f′(x) < 0* ⟹ *f* is **decreasing**.
- *f′(x) = 0* ⟹ **critical point**: a candidate maximum, minimum, or inflection.

The second derivative *f″(x)* tells you the shape:

- *f″(x) > 0* ⟹ **convex** (curving up); a critical point there is a **minimum**.
- *f″(x) < 0* ⟹ **concave** (curving down); a critical point there is a **maximum**.

That is the whole of unconstrained optimisation: set *f′(x) = 0* for the **first-order condition**, then check *f″* for the **second-order condition**. Do not forget the boundaries of the domain — the maximum of a function on [0, 10] can sit at 0 or at 10, where the derivative need not vanish.

## 5. Why economists care

Almost every "marginal" object in economics is a derivative.

**Marginal cost.** If *C(q)* is the total cost of producing *q* units, marginal cost is *C′(q)*. A price-taking firm maximises profit *π(q) = p·q − C(q)*, so:

<div class="math-display">
\[ \pi'(q) = p - C'(q) = 0 \quad\Longrightarrow\quad p = C'(q) \]
</div>

Price equals marginal cost — and the second-order condition *π″(q) = −C″(q) < 0* is exactly the requirement that marginal cost be increasing at the optimum.

**Marginal utility and the MRS.** With utility *U(x, y)*, the partial derivatives *∂U/∂x* and *∂U/∂y* are marginal utilities, and their ratio is the marginal rate of substitution — the slope of the indifference curve.

**Elasticity.** An elasticity is a derivative made unit-free, so that a market measured in litres can be compared with one measured in kilowatt-hours:

<div class="math-display">
\[ \varepsilon \;=\; \frac{dQ}{dP} \cdot \frac{P}{Q} \;=\; \frac{d \ln Q}{d \ln P} \]
</div>

The second form is why we so often regress logs on logs: the estimated coefficient *is* the elasticity.

**Growth rates.** For a variable *X(t)* over time, the growth rate is the derivative of its log:

<div class="math-display">
\[ g_X \;=\; \frac{\dot{X}(t)}{X(t)} \;=\; \frac{d \ln X(t)}{dt} \]
</div>

## 6. Common mistakes

1. **Forgetting the inner derivative.** The derivative of *e³ˣ* is *3e³ˣ*, not *e³ˣ*.
2. **Differentiating a product term by term.** (f·g)′ is *not* f′·g′.
3. **Sign slips in the quotient rule.** The numerator is f′g − fg′, in that order. It is not symmetric.
4. **Treating every critical point as a maximum.** Check the second derivative, or the sign of *f′* on each side.
5. **Ignoring the domain.** ln(x) exists only for *x > 0*; a critical point outside the domain is not a solution.
6. **Dropping units.** A derivative always carries units: output units per input unit. If the units of your answer make no sense, neither does the answer.

---

## Practice

Differentiate, then state where each function is increasing:

1. *f(x) = 3x⁴ − 8x³ + 6x²*
2. *f(x) = x e⁻ˣ*
3. *f(x) = ln(x² + 1)*
4. *f(x) = (2x − 5)/(x² + 1)*
5. A firm has *C(q) = q³ − 6q² + 15q*. Find marginal cost, the output at which it is lowest, and the price at which a price-taking firm would choose that output.

Found an error, or want another topic covered here? [Email me](mailto:maximiliano.moreno-lopez@psemail.eu).
