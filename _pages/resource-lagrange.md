---
title: "Lagrange Multipliers: Optimisation with Constraints"
permalink: /resources/lagrange-multipliers/
author_profile: true
---

*Teaching resource for Mathematics, Sciences Po Paris.*

Most economic problems are not "maximise this function". They are "maximise this function given that you cannot spend more than you have". The Lagrangian turns the second problem into the first. If the first-order conditions here look unfamiliar, start with [Derivatives](/resources/derivatives/).

---

## 1. The problem

You want to maximise *f(x, y)* subject to a constraint *g(x, y) = c*. The objective is usually utility, profit or output. The constraint is a budget, a technology or a resource you cannot exceed.

The naive approach is to solve the constraint for *y*, substitute it into *f*, and maximise in one variable. That works, and for simple problems it is faster. It stops working as soon as the constraint cannot be solved cleanly for one variable, or as soon as you have three choice variables and two constraints. The Lagrangian always works, and it hands you a piece of economics for free.

## 2. The intuition

At the optimum, the level curve of *f* is tangent to the constraint. If it were not, the two curves would cross, and you could slide along the constraint onto a higher level curve.

Tangency means the two gradients point in the same direction:

<div class="math-display">
\[ \nabla f(x^*, y^*) \;=\; \lambda \, \nabla g(x^*, y^*) \]
</div>

That is the whole theorem. The multiplier *λ* is whatever number makes the two gradients match in length once they already match in direction.

## 3. The recipe

Write the Lagrangian:

<div class="math-display">
\[ \mathcal{L}(x, y, \lambda) \;=\; f(x,y) \;-\; \lambda \big( g(x,y) - c \big) \]
</div>

Then set all three partial derivatives to zero:

<div class="math-display">
\[ \frac{\partial \mathcal{L}}{\partial x} = f_x - \lambda g_x = 0, \qquad
   \frac{\partial \mathcal{L}}{\partial y} = f_y - \lambda g_y = 0, \qquad
   \frac{\partial \mathcal{L}}{\partial \lambda} = c - g(x,y) = 0 \]
</div>

The third condition is just the constraint, which is why you never have to remember it separately. Dividing the first condition by the second one kills *λ* and leaves the tangency condition:

<div class="math-display">
\[ \frac{f_x}{f_y} \;=\; \frac{g_x}{g_y} \]
</div>

Two equations, tangency and the constraint, and two unknowns. Solve.

## 4. Worked example: the consumer problem

Maximise *U(x, y) = xᵃ y¹⁻ᵃ* subject to *pₓx + p_y y = m*, with *0 < a < 1*.

<div class="math-display">
\[ \mathcal{L} = x^{a} y^{1-a} - \lambda \big( p_x x + p_y y - m \big) \]
</div>

The first-order conditions in *x* and *y*:

<div class="math-display">
\[ a\, x^{a-1} y^{1-a} = \lambda p_x, \qquad (1-a)\, x^{a} y^{-a} = \lambda p_y \]
</div>

Divide the first by the second:

<div class="math-display">
\[ \frac{a\,y}{(1-a)\,x} \;=\; \frac{p_x}{p_y} \]
</div>

The left-hand side is the marginal rate of substitution, so tangency says MRS equals the price ratio: the rate at which you are willing to trade *y* for *x* equals the rate at which the market lets you. Rearranging gives *p_y y = ((1−a)/a)·pₓx*, and substituting that into the budget constraint:

<div class="math-display">
\[ x^* = \frac{a\,m}{p_x}, \qquad y^* = \frac{(1-a)\,m}{p_y} \]
</div>

With Cobb-Douglas preferences the consumer spends a fixed share *a* of income on *x*, whatever the prices are. That is a strong prediction, and it is why this utility function turns up in every problem set.

## 5. What λ actually is

*λ* is not algebraic debris to be discarded. It is the shadow price of the constraint: the rate at which the best attainable value of the objective improves when you relax the constraint by one unit. If *V(c)* is the maximum of *f* given constraint level *c*, then

<div class="math-display">
\[ \frac{dV}{dc} \;=\; \lambda \]
</div>

This is the envelope theorem, and it saves a lot of work. It says you can ignore how *x\** and *y\** themselves move when *c* changes, because those effects cancel at the optimum.

In the example above, put the solutions back into the utility function:

<div class="math-display">
\[ V(m) = m \left( \frac{a}{p_x} \right)^{a} \left( \frac{1-a}{p_y} \right)^{1-a} \;=\; \lambda \, m \]
</div>

So here *λ* is the marginal utility of income: one more euro of budget buys *λ* more utils. Reading the units always tells you what *λ* means. In a cost-minimisation problem, where you minimise *wL + rK* subject to producing at least *q*, the multiplier comes out in euros per unit of output, and it is marginal cost.

## 6. Inequality constraints

Budgets are usually "no more than", not "exactly". For *max f(x)* subject to *g(x) ≤ c*, the Karush-Kuhn-Tucker conditions add two requirements to the same first-order conditions:

<div class="math-display">
\[ \lambda \ge 0, \qquad g(x) \le c, \qquad \lambda \big( g(x) - c \big) = 0 \]
</div>

The last line is complementary slackness, and it says that one of two things must hold. Either the constraint binds, *g(x) = c*, and the multiplier is positive. Or the constraint is slack and *λ = 0*, in which case the constraint was irrelevant and you could have ignored it. A constraint that does not bind has no shadow price.

In practice: guess which constraints bind, solve, then check that your solution really satisfies the ones you assumed slack and that every *λ* came out non-negative. If it did not, guess again.

## 7. Common mistakes

1. Reading the sign of *λ* as meaningful in itself. Writing *L = f + λ(c − g)* flips it. What matters is keeping one convention and interpreting the magnitude.
2. Forgetting the third first-order condition. The derivative with respect to *λ* is the constraint. Drop it and you have two equations and three unknowns.
3. Stopping at the tangency condition. MRS equal to the price ratio is only half the answer: it is a ratio, not a quantity. You still need the constraint to pin down levels.
4. Assuming an interior solution. With perfect substitutes, or when one good is far too expensive, tangency has no valid solution and the optimum sits at a corner.
5. Treating a critical point as a maximum. First-order conditions only produce candidates. You need a concave objective and a convex feasible set, or a second-order check.
6. Rescaling the constraint and expecting *λ* to survive. Writing the budget as *2pₓx + 2p_y y = 2m* halves *λ*, because the shadow price is defined per unit of the constraint as you wrote it.

---

## Practice

1. Maximise *f(x, y) = xy* subject to *x + y = 10*. Find *x\**, *y\** and *λ*, then redo it with *x + y = 11* and check that the change in the optimal value is *λ*.
2. Minimise *x² + y²* subject to *x + 2y = 5*. Interpret *λ*.
3. A consumer has *U(x, y) = ln x + 2 ln y* and income *m* at prices *pₓ, p_y*. Find the demands and the expenditure shares.
4. Maximise *U = x^(1/3) y^(2/3)* subject to *4x + 2y = 60*. Then raise income to 61 and check that utility rises by roughly *λ*.
5. A firm minimises *wL + rK* subject to *√(LK) = q*. Find the conditional factor demands and show that *λ* is marginal cost.

Found a mistake, or want another topic here? [Email me](mailto:maximiliano.moreno-lopez@psemail.eu).
