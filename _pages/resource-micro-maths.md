---
title: "Maths for Intermediate Microeconomics"
permalink: /resources/micro-maths/
---

*Tutorial 1 companion, Intermediate Microeconomics, Sciences Po Paris.*

Several of you wrote after the first tutorial asking for material to go over the maths and for exercises to practise. This page is that answer. It follows the order of the Tutorial 1 slides (which are on Moodle) and, for each topic, gives you the essentials in a few lines, a note that explains it properly, and exercises with solutions you can reveal one by one. You do not need all of it at once. Work through the parts you found hardest, and email me when something does not click.

---

## 1. Derivatives in one variable

The core of everything else. You need the rules by heart and the chain rule until it is automatic.

<div class="math-display">
\[ (u+v)' = u' + v' \qquad (uv)' = u'v + uv' \qquad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2} \]
\[ (x^{\alpha})' = \alpha x^{\alpha - 1} \qquad (e^{u})' = u' e^{u} \qquad (\ln u)' = \frac{u'}{u} \qquad \big(f(g(x))\big)' = f'(g(x))\,g'(x) \]
</div>

- Read: [Derivatives: A Refresher](/resources/derivatives/), especially section 3 on the chain rule.
- Practise: [Starter](/resources/derivatives-warmup/) (24, the basic rules), [Intermediate](/resources/derivatives-100/) (100, product and quotient rules), [Upper intermediate](/resources/derivatives-second/) (20, chain rule and second derivatives).

The slide exercise *f(x) = 3(ln x)²* is a chain rule: outer *3u²*, inner *ln x*, so *f′ = 6 ln x · (1/x)*.

## 2. Logarithms and exponentials

The rules you will use in every problem set:

<div class="math-display">
\[ \ln(uv) = \ln u + \ln v \qquad \ln\frac{u}{v} = \ln u - \ln v \qquad \ln(u^{\alpha}) = \alpha \ln u \qquad e^{\ln u} = u \]
\[ u^{\alpha} u^{\beta} = u^{\alpha+\beta} \qquad \frac{u^{\alpha}}{u^{\beta}} = u^{\alpha-\beta} \qquad (u^{\alpha})^{\beta} = u^{\alpha\beta} \qquad u^{-\alpha} = \frac{1}{u^{\alpha}} \]
</div>

Two traps from the slides: *(ln u)^α* is not *α ln u*, and *u^α + u^β* does not simplify. Also, *ln* is only defined for positive numbers, and *ln 1 = 0*.

Why we care: taking logs turns a Cobb-Douglas utility *x^a y^b* into *a ln x + b ln y*, which is easier to differentiate and describes the same preferences, since ln is increasing. And a coefficient in a log-log regression is an elasticity.

## 3. Partial derivatives

When a function has several variables, differentiate with respect to one while treating the others as constants. Marginal utility, marginal product and the MRS are all partial derivatives:

<div class="math-display">
\[ U = x^{a} y^{b}: \qquad U_x = a x^{a-1} y^{b}, \qquad U_y = b x^{a} y^{b-1}, \qquad MRS = \frac{U_x}{U_y} = \frac{a}{b}\cdot\frac{y}{x} \]
</div>

- Read: [Partial Derivatives and Optimisation in Two Variables](/resources/partial-derivatives/).
- Practise: [Partial Derivatives Practice](/resources/partial-derivatives-practice/), 22 exercises in three levels, the last ones built on Problem Set 1.

## 4. Unconstrained optimisation

One variable: set *f′(x) = 0* and solve; *f″ < 0* means a maximum, *f″ > 0* a minimum. Two variables: set both partials to zero and solve the system; then compute

<div class="math-display">
\[ D = f_{xx} f_{yy} - f_{xy}^2 \]
</div>

and read: *D > 0* with *f_xx < 0* is a maximum, *D > 0* with *f_xx > 0* a minimum, *D < 0* a saddle. The slide example *f(y, z) = y² − 2y + z²* has its critical point at *(1, 0)* with *D = 4 > 0* and *f_yy = 2 > 0*: a minimum.

Problem 3 of Problem Set 1 is this in one variable with parameters: *V(τ, y_i)* is concave in *τ* because *∂²V/∂τ² = −2ȳ < 0*, so the first-order condition gives each agent's preferred tax rate. Sections 5 and 6 of the [partial derivatives note](/resources/partial-derivatives/) work through it.

## 5. Constrained optimisation: the Lagrangian

The consumer problem, max *U(x₁, x₂)* subject to *p₁x₁ + p₂x₂ = R*. Form the Lagrangian, take the partials, and the first two conditions give MRS = price ratio:

<div class="math-display">
\[ \mathcal{L} = U(x_1, x_2) + \lambda\,\big(R - p_1 x_1 - p_2 x_2\big) \qquad\Longrightarrow\qquad \frac{U_{x_1}}{U_{x_2}} = \frac{p_1}{p_2} \]
</div>

- Read: [Lagrange Multipliers: Optimisation with Constraints](/resources/lagrange-multipliers/). It also explains what *λ* means, which the exam likes to ask.
- Practise: [Lagrange Multipliers: Practice](/resources/lagrange-practice/), 20 problems from numbers-only to Kuhn-Tucker. The slide problem, max *x₁x₂* subject to *2x₁ + 3x₂ = 6*, is the same structure as the first ones.

A note on the sign of *λ*: the slides write *+λ(R − g)*, my notes write *−λ(g − c)*. They are the same thing; keep whichever you like and be consistent.

## 6. Probability and expectation

A random variable takes values with probabilities. Its expectation is the probability-weighted average:

<div class="math-display">
\[ E[X] = \sum_i p_i\, x_i \qquad\qquad X \sim \mathcal{U}[a, b] \text{ (continuous)}: \quad E[X] = \frac{a+b}{2} \]
</div>

The slide exercises: a fair 5-sided die has *E[X] = (1+2+3+4+5)/5 = 3*; the lottery ticket has *E[X] = −10 · 0.99 + 1000 · 0.01 = 0.1 > 0*; a uniform variable on *[0, 1]* has mean *1/2*, which is exactly why average income *ȳ = 1/2* in Problem Set 1.

## 7. Integrals

Integration reverses differentiation, and a definite integral is the area under the curve:

<div class="math-display">
\[ \int x^{\alpha}\,dx = \frac{x^{\alpha+1}}{\alpha+1} \quad (\alpha \neq -1) \qquad \int \frac{u'}{u}\,dx = \ln u \qquad \int u' e^{u}\,dx = e^{u} \]
\[ \int_2^3 x^3\,dx = \left[\frac{x^4}{4}\right]_2^3 = \frac{81 - 16}{4} = 16.25 \qquad\qquad \int_0^5 e^{3x}\,dx = \left[\frac{e^{3x}}{3}\right]_0^5 = \frac{e^{15} - 1}{3} \]
</div>

You will meet integrals when a model has a continuum of agents, as in Problem Set 1 where income is spread over *[0, 1]*: average income is *∫₀¹ y dy = 1/2*.

---

## How to use this before the midterm

1. Do the derivatives [Starter](/resources/derivatives-warmup/) sheet in one sitting. If you get fewer than 20 of 24, read the refresher first.
2. Do the [Intermediate](/resources/derivatives-100/) sheet in pieces, ten a day. It is about speed and confidence, not difficulty.
3. Read the [partial derivatives note](/resources/partial-derivatives/) and do its practice sheet through the Intermediate level.
4. Read the [Lagrange note](/resources/lagrange-multipliers/) and do the Starter and Intermediate problems.
5. Redo Problem Set 1, Problem 3, with the book closed.

If you get stuck anywhere, [email me](mailto:maximiliano.moreno-lopez@psemail.eu) with the exercise number and what you tried. That is much more useful to both of us than "I don't understand derivatives" :')
