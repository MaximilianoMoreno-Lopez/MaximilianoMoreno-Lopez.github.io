"""Builds _pages/resource-partial-derivatives-practice.html: partial derivatives,
second-order partials, MRS and unconstrained optimisation in two variables, with
worked solutions behind a click.

Statements and solution text are hand-written; every derivative and every numeric
answer is re-derived with sympy in the checks before the page is written.

Run:  pip install sympy && python tools/gen_partials.py
"""
import os, sys
import sympy as sp

x, y, z = sp.symbols("x y z", real=True)
xp, yp, K, L, tau, yi, ybar = sp.symbols("x y K L tau y_i ybar", positive=True)

def eq(a, b):
    return sp.simplify(a - b) == 0

def latex_ln(e):
    return sp.latex(e).replace(r"\log", r"\ln")

EX = []

# ---------------------------------------------------------------- Starter: first partials
def starter(f, vars_, q_tex, name="f", hints=""):
    """Solution text generated from sympy so it cannot disagree with the check."""
    parts = []
    for v in vars_:
        d = sp.simplify(sp.diff(f, v))
        parts.append(r"\frac{\partial %s}{\partial %s} = %s" % (name, sp.latex(v), latex_ln(d)))
    sol = r"\[ " + r", \qquad ".join(parts) + r" \]"
    if hints:
        sol += "<p>%s</p>" % hints
    EX.append(dict(level="Starter",
                   statement=r"Find both first-order partial derivatives of \( %s \)." % q_tex,
                   solution=sol,
                   check=lambda: True))

starter(3*x**2 + 2*x*y + y**3, (x, y), r"f(x, y) = 3x^2 + 2xy + y^3",
        hints=r"Treat \( y \) as a number when differentiating with respect to \( x \): the term \( y^3 \) is then a constant and disappears, while \( 2xy \) is \( (2y)\,x \), a constant times \( x \).")
x1, x2 = sp.symbols("x_1 x_2", real=True)
starter(x1*x2**2 - 3*x1, (x1, x2), r"g(x_1, x_2) = x_1 x_2^2 - 3x_1", name="g",
        hints=r"The example from the Tutorial 1 slides. Setting both partials to zero gives \( x_2^2 = 3 \) and \( x_1 x_2 = 0 \), so \( x_1 = 0 \) and \( x_2 = \pm\sqrt 3 \).")
starter(sp.sqrt(xp)*sp.sqrt(yp), (xp, yp), r"U(x, y) = x^{1/2} y^{1/2}", name="U",
        hints=r"These are the marginal utilities. Both are positive and each one falls as its own good increases: diminishing marginal utility.")
starter(sp.exp(2*x)*sp.log(yp), (x, yp), r"f(x, y) = e^{2x} \ln y",
        hints=r"Chain rule on \( e^{2x} \) for the \( x \)-partial (factor 2); \( \ln y \) rides along as a constant. For the \( y \)-partial, \( e^{2x} \) is the constant.")
starter(x/(x + yp), (x, yp), r"f(x, y) = \dfrac{x}{x + y}",
        hints=r"Quotient rule for the \( x \)-partial: \( \frac{(x+y) - x}{(x+y)^2} = \frac{y}{(x+y)^2} \). For the \( y \)-partial the numerator is a constant, so \( -x/(x+y)^2 \).")
starter(sp.log(x**2 + y**2), (x, y), r"f(x, y) = \ln(x^2 + y^2)",
        hints=r"Chain rule: the derivative of \( \ln u \) is \( u'/u \), and \( u = x^2 + y^2 \) has \( u_x = 2x \), \( u_y = 2y \).")
starter(10*K**sp.Rational(3, 10)*L**sp.Rational(7, 10), (K, L), r"Q(K, L) = 10\,K^{0.3} L^{0.7}", name="Q",
        hints=r"These are the marginal products of capital and labour. Notice \( \partial Q/\partial K = 0.3\,Q/K \) and \( \partial Q/\partial L = 0.7\,Q/L \): with Cobb-Douglas, the exponent is the output elasticity.")
starter(x*sp.exp(x*y), (x, y), r"f(x, y) = x\,e^{xy}",
        hints=r"Product rule and chain rule together for the \( x \)-partial: \( e^{xy} + x \cdot y e^{xy} = (1 + xy)e^{xy} \). For \( y \), only the exponent depends on \( y \).")

# ---------------------------------------------------------------- Intermediate
f9 = x**3*y - 2*x*y**2 + y
EX.append(dict(level="Intermediate",
statement=r"""For \( f(x, y) = x^3 y - 2xy^2 + y \), compute all four second-order partial derivatives \( f_{xx}, f_{yy}, f_{xy}, f_{yx} \) and check that the two cross partials agree.""",
solution=r"""<p>First partials: \( f_x = 3x^2 y - 2y^2 \), \( f_y = x^3 - 4xy + 1 \).</p>
\[ f_{xx} = 6xy, \qquad f_{yy} = -4x, \qquad f_{xy} = \frac{\partial f_x}{\partial y} = 3x^2 - 4y, \qquad f_{yx} = \frac{\partial f_y}{\partial x} = 3x^2 - 4y \]
<p>The cross partials are equal, as Young's theorem promises for any function this smooth. In practice this is a free check on your algebra: if \( f_{xy} \neq f_{yx} \), one of your first partials is wrong.</p>""",
check=lambda: eq(sp.diff(f9, x, x), 6*x*y) and eq(sp.diff(f9, y, y), -4*x) and eq(sp.diff(f9, x, y), 3*x**2 - 4*y)))

U10 = sp.log(xp) + sp.log(yp)
EX.append(dict(level="Intermediate",
statement=r"""For \( U(x, y) = \ln x + \ln y \), compute the second-order partials and say what their signs tell you about the shape of \( U \).""",
solution=r"""\[ U_x = \frac1x, \quad U_y = \frac1y, \qquad U_{xx} = -\frac{1}{x^2}, \quad U_{yy} = -\frac{1}{y^2}, \quad U_{xy} = 0 \]
<p>Both own second partials are negative: marginal utility of each good falls as you consume more of it. The cross partial is zero: more \( y \) does not change how much you enjoy an extra \( x \). Since \( U_{xx} U_{yy} - U_{xy}^2 = 1/(x^2 y^2) > 0 \) with \( U_{xx} < 0 \), the function is concave everywhere, which is what makes it well behaved in a consumer problem.</p>""",
check=lambda: eq(sp.diff(U10, xp, xp), -1/xp**2) and eq(sp.diff(U10, xp, yp), 0)))

U11 = xp**sp.Rational(1, 3)*yp**sp.Rational(2, 3)
EX.append(dict(level="Intermediate",
statement=r"""For \( U(x, y) = x^{1/3} y^{2/3} \), find the marginal rate of substitution \( MRS = U_x / U_y \) and evaluate it at \( (x, y) = (2, 4) \). Interpret the number.""",
solution=r"""\[ U_x = \tfrac13 x^{-2/3} y^{2/3}, \qquad U_y = \tfrac23 x^{1/3} y^{-1/3}, \qquad MRS = \frac{U_x}{U_y} = \frac{y}{2x} \]
<p>At \( (2, 4) \): \( MRS = 4/4 = 1 \). Along the indifference curve through that bundle, giving up one unit of \( y \) is exactly compensated by one more unit of \( x \). Everything cancels down to \( y/(2x) \): with Cobb-Douglas \( x^a y^b \), the MRS is always \( \frac{a}{b}\cdot\frac{y}{x} \).</p>""",
check=lambda: eq(sp.diff(U11, xp)/sp.diff(U11, yp), yp/(2*xp))))

U12 = xp + sp.log(yp)
EX.append(dict(level="Intermediate",
statement=r"""For the quasi-linear utility \( U(x, y) = x + \ln y \), compute the MRS. What is special about it?""",
solution=r"""\[ U_x = 1, \qquad U_y = \frac1y, \qquad MRS = \frac{U_x}{U_y} = y \]
<p>The MRS depends only on \( y \), not on \( x \). Indifference curves are vertical shifts of one another, so at a given \( y \) they all have the same slope. In a consumer problem this means the demand for \( y \) does not depend on income once income is high enough: extra euros all go to \( x \).</p>""",
check=lambda: eq(sp.diff(U12, xp)/sp.diff(U12, yp), yp)))

EX.append(dict(level="Intermediate",
statement=r"""The level curve \( F(x, y) = x^2 + y^2 = 25 \) passes through \( (3, 4) \). Use partial derivatives to find the slope \( dy/dx \) of the curve at that point.""",
solution=r"""<p>Along a level curve \( F(x, y) = c \), the total differential is zero: \( F_x\,dx + F_y\,dy = 0 \), so</p>
\[ \frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y} = -\frac34 \text{ at } (3, 4). \]
<p>This is the implicit function rule, and it is exactly how the slope of an indifference curve becomes \( -U_x/U_y = -MRS \). You never need to solve for \( y \) explicitly.</p>""",
check=lambda: eq((-sp.diff(x**2 + y**2, x)/sp.diff(x**2 + y**2, y)).subs({x: 3, y: 4}), sp.Rational(-3, 4))))

Q14 = sp.sqrt(K)*sp.sqrt(L)
EX.append(dict(level="Intermediate",
statement=r"""For \( Q(K, L) = K^{1/2} L^{1/2} \), compute the marginal products and verify Euler's identity \( K\,Q_K + L\,Q_L = Q \). What does it say about returns to scale?""",
solution=r"""\[ Q_K = \tfrac12 K^{-1/2} L^{1/2} = \frac{Q}{2K}, \qquad Q_L = \tfrac12 K^{1/2} L^{-1/2} = \frac{Q}{2L} \]
\[ K\,Q_K + L\,Q_L = \frac{Q}{2} + \frac{Q}{2} = Q \]
<p>Euler's identity holds with coefficient 1 because the exponents sum to 1: the technology has constant returns to scale. Under competition each factor is paid its marginal product, so \( K\,Q_K + L\,Q_L = Q \) also says that paying capital and labour exhausts output exactly, leaving zero profit.</p>""",
check=lambda: eq(K*sp.diff(Q14, K) + L*sp.diff(Q14, L), Q14)))

A, p, m = sp.symbols("A p m", positive=True)
Q15 = A*p**-2*m
EX.append(dict(level="Intermediate",
statement=r"""A demand function is \( Q(p, m) = A\,p^{-2} m \). Compute the price elasticity \( \frac{\partial Q}{\partial p}\frac{p}{Q} \) and the income elasticity \( \frac{\partial Q}{\partial m}\frac{m}{Q} \).""",
solution=r"""\[ \frac{\partial Q}{\partial p}\cdot\frac{p}{Q} = -2A p^{-3} m \cdot \frac{p}{A p^{-2} m} = -2, \qquad \frac{\partial Q}{\partial m}\cdot\frac{m}{Q} = A p^{-2} \cdot \frac{m}{A p^{-2} m} = 1 \]
<p>Constant elasticities, equal to the exponents. Taking logs makes it obvious: \( \ln Q = \ln A - 2\ln p + \ln m \), and an elasticity is a partial derivative of \( \ln Q \) with respect to a log. This is why demand equations are so often estimated in logs.</p>""",
check=lambda: eq(sp.diff(Q15, p)*p/Q15, -2) and eq(sp.diff(Q15, m)*m/Q15, 1)))

# ---------------------------------------------------------------- Upper Intermediate
def crit(f, vars_):
    return sp.solve([sp.diff(f, v) for v in vars_], list(vars_), dict=True)

def D_at(f, vars_, pt):
    a, b = vars_
    H = sp.diff(f, a, a)*sp.diff(f, b, b) - sp.diff(f, a, b)**2
    return sp.simplify(H.subs(pt)), sp.simplify(sp.diff(f, a, a).subs(pt))

f16 = y**2 - 2*y + z**2
EX.append(dict(level="Upper Intermediate",
statement=r"""Find and classify the critical point of \( f(y, z) = y^2 - 2y + z^2 \). (The example from the Tutorial 1 slides.)""",
solution=r"""<p>First-order conditions:</p>
\[ f_y = 2y - 2 = 0 \Rightarrow y = 1, \qquad f_z = 2z = 0 \Rightarrow z = 0 \]
<p>Second-order conditions:</p>
\[ f_{yy} = 2, \quad f_{zz} = 2, \quad f_{yz} = 0, \qquad D = f_{yy} f_{zz} - f_{yz}^2 = 4 > 0 \]
<p>\( D > 0 \) with \( f_{yy} > 0 \): a minimum, at \( (1, 0) \), where \( f = -1 \). You can also see it by completing the square: \( f = (y - 1)^2 + z^2 - 1 \).</p>""",
check=lambda: crit(f16, (y, z)) == [{y: 1, z: 0}] and D_at(f16, (y, z), {y: 1, z: 0}) == (4, 2)))

f17 = -x**2 - y**2 + 4*x + 6*y
EX.append(dict(level="Upper Intermediate",
statement=r"""Find and classify the critical point of \( f(x, y) = -x^2 - y^2 + 4x + 6y \), and give the value of \( f \) there.""",
solution=r"""\[ f_x = -2x + 4 = 0 \Rightarrow x = 2, \qquad f_y = -2y + 6 = 0 \Rightarrow y = 3 \]
\[ f_{xx} = -2, \quad f_{yy} = -2, \quad f_{xy} = 0, \qquad D = 4 > 0 \]
<p>\( D > 0 \) and \( f_{xx} < 0 \): a maximum, at \( (2, 3) \), with \( f = -4 - 9 + 8 + 18 = 13 \). The function is a downward paraboloid, so this is the global maximum, not just a local one.</p>""",
check=lambda: crit(f17, (x, y)) == [{x: 2, y: 3}] and D_at(f17, (x, y), {x: 2, y: 3}) == (4, -2) and f17.subs({x: 2, y: 3}) == 13))

f18 = x**2 - y**2 + 2*x
EX.append(dict(level="Upper Intermediate",
statement=r"""Find and classify the critical point of \( f(x, y) = x^2 - y^2 + 2x \).""",
solution=r"""\[ f_x = 2x + 2 = 0 \Rightarrow x = -1, \qquad f_y = -2y = 0 \Rightarrow y = 0 \]
\[ f_{xx} = 2, \quad f_{yy} = -2, \quad f_{xy} = 0, \qquad D = (2)(-2) - 0 = -4 < 0 \]
<p>\( D < 0 \): a saddle point at \( (-1, 0) \). Along the \( x \) direction the function curves up (\( f_{xx} > 0 \)), along \( y \) it curves down (\( f_{yy} < 0 \)). Setting the first-order conditions to zero found a flat point, but it is neither a maximum nor a minimum. This is why the second-order check is not optional.</p>""",
check=lambda: crit(f18, (x, y)) == [{x: -1, y: 0}] and D_at(f18, (x, y), {x: -1, y: 0})[0] == -4))

f19 = x**3 - 3*x + y**2
EX.append(dict(level="Upper Intermediate",
statement=r"""Find all critical points of \( f(x, y) = x^3 - 3x + y^2 \) and classify each one.""",
solution=r"""\[ f_x = 3x^2 - 3 = 0 \Rightarrow x = \pm 1, \qquad f_y = 2y = 0 \Rightarrow y = 0 \]
<p>Two critical points, \( (1, 0) \) and \( (-1, 0) \). Second-order partials: \( f_{xx} = 6x \), \( f_{yy} = 2 \), \( f_{xy} = 0 \), so \( D = 12x \), which changes sign with \( x \).</p>
\[ (1, 0):\ D = 12 > 0,\ f_{xx} = 6 > 0 \Rightarrow \text{local minimum}, f = -2. \qquad (-1, 0):\ D = -12 < 0 \Rightarrow \text{saddle}. \]
<p>The minimum is only local: \( f \to -\infty \) as \( x \to -\infty \). When \( D \) depends on the point, you must evaluate it at each critical point separately.</p>""",
check=lambda: sorted([tuple(s[v] for v in (x, y)) for s in crit(f19, (x, y))]) == [(-1, 0), (1, 0)]
             and D_at(f19, (x, y), {x: 1, y: 0}) == (12, 6) and D_at(f19, (x, y), {x: -1, y: 0})[0] == -12))

q1, q2 = sp.symbols("q_1 q_2", real=True)
pi20 = 20*q1 + 30*q2 - q1**2 - q2**2 - q1*q2
EX.append(dict(level="Upper Intermediate",
statement=r"""A firm sells two products with profit \( \pi(q_1, q_2) = 20q_1 + 30q_2 - q_1^2 - q_2^2 - q_1 q_2 \). Find the profit-maximising quantities, check the second-order conditions and compute the maximum profit.""",
solution=r"""\[ \pi_1 = 20 - 2q_1 - q_2 = 0, \qquad \pi_2 = 30 - 2q_2 - q_1 = 0 \]
<p>From the first, \( q_2 = 20 - 2q_1 \). Substituting: \( 30 - 40 + 4q_1 - q_1 = 0 \), so \( q_1 = 10/3 \) and \( q_2 = 40/3 \).</p>
\[ \pi_{11} = -2, \quad \pi_{22} = -2, \quad \pi_{12} = -1, \qquad D = 4 - 1 = 3 > 0 \]
<p>\( D > 0 \) and \( \pi_{11} < 0 \): a maximum. Profit there is \( \pi^* = 2100/9 \approx 233.3 \). The cross term \( -q_1 q_2 \) is what links the two decisions: producing more of one product lowers the marginal profit of the other, so each first-order condition contains both quantities and you have to solve them as a system.</p>""",
check=lambda: crit(pi20, (q1, q2)) == [{q1: sp.Rational(10, 3), q2: sp.Rational(40, 3)}]
             and D_at(pi20, (q1, q2), {q1: sp.Rational(10, 3), q2: sp.Rational(40, 3)}) == (3, -2)
             and pi20.subs({q1: sp.Rational(10, 3), q2: sp.Rational(40, 3)}) == sp.Rational(2100, 9)))

V21 = (1 - tau)*yi + (tau - tau**2)*ybar
EX.append(dict(level="Upper Intermediate",
statement=r"""Problem Set 1, Problem 3, as a derivative exercise. An agent with income \( y_i \) gets \( V(\tau, y_i) = (1 - \tau)\,y_i + (\tau - \tau^2)\,\bar y \) from tax rate \( \tau \). Treating \( y_i \) and \( \bar y \) as parameters, show that \( V \) is strictly concave in \( \tau \), find the agent's preferred tax rate \( \tau_i^* \), and show that richer agents prefer lower taxes.""",
solution=r"""<p>Differentiate with respect to \( \tau \) only; \( y_i \) and \( \bar y \) are constants here:</p>
\[ \frac{\partial V}{\partial \tau} = -y_i + (1 - 2\tau)\,\bar y, \qquad \frac{\partial^2 V}{\partial \tau^2} = -2\bar y < 0 \]
<p>The second derivative is negative for any \( \bar y > 0 \), so \( V \) is strictly concave in \( \tau \): preferences are single-peaked, and the first-order condition finds the peak.</p>
\[ -y_i + (1 - 2\tau)\bar y = 0 \quad\Longrightarrow\quad \tau_i^* = \frac12\left(1 - \frac{y_i}{\bar y}\right) \]
<p>valid when \( y_i \leq \bar y \); anyone richer than average wants \( \tau = 0 \). Differentiating the solution with respect to the parameter: \( \partial \tau_i^* / \partial y_i = -1/(2\bar y) < 0 \), so richer agents prefer lower taxes. With uniform income on \( [0, 1] \) the median voter has \( y_m = \bar y = 1/2 \), hence \( \tau^* = 0 \).</p>""",
check=lambda: eq(sp.diff(V21, tau, tau), -2*ybar)
             and eq(sp.solve(sp.diff(V21, tau), tau)[0], (1 - yi/ybar)/2)
             and eq(sp.diff((1 - yi/ybar)/2, yi), -1/(2*ybar))))

V22 = (1 - tau)*yi + (tau - tau**3)*ybar
EX.append(dict(level="Upper Intermediate",
statement=r"""Variation on Problem 3. Suppose the cost of taxation is \( c(\tau) = \tau^3 \) instead of \( \tau^2 \), so \( V(\tau, y_i) = (1 - \tau)\,y_i + (\tau - \tau^3)\,\bar y \). Is \( V \) still concave in \( \tau \) on \( [0, 1] \)? Find \( \tau_i^* \). If \( \bar y = 1/2 \) and the median income is \( y_m = 0.3 \), what tax rate does majority voting choose?""",
solution=r"""\[ \frac{\partial V}{\partial \tau} = -y_i + (1 - 3\tau^2)\,\bar y, \qquad \frac{\partial^2 V}{\partial \tau^2} = -6\tau\,\bar y \leq 0 \text{ on } [0, 1] \]
<p>Concave on the relevant range (strictly for \( \tau > 0 \)), so still single-peaked. First-order condition:</p>
\[ 1 - 3\tau^2 = \frac{y_i}{\bar y} \quad\Longrightarrow\quad \tau_i^* = \sqrt{\frac{1}{3}\left(1 - \frac{y_i}{\bar y}\right)} \quad (y_i \leq \bar y) \]
<p>Median voter: \( y_m / \bar y = 0.3/0.5 = 0.6 \), so \( \tau^* = \sqrt{0.4/3} = \sqrt{2/15} \approx 0.365 \). Two lessons from the change: the median is now below the mean (a more realistic income distribution), so the majority chooses a positive tax; and with a convex cost that starts flat, small taxes are cheap, so the preferred rate is higher than the quadratic case would give.</p>""",
check=lambda: eq(sp.diff(V22, tau, tau), -6*tau*ybar)
             and eq(sp.solve(sp.diff(V22, tau), tau)[0], sp.sqrt((1 - yi/ybar)/3))
             and abs(float(sp.sqrt(sp.Rational(2, 15))) - 0.365) < 0.001))

# --------------------------------------------------------------------------
HEAD = """---
layout: archive
title: "Partial Derivatives Practice"
permalink: /resources/partial-derivatives-practice/
---

<p class="resource-intro">Twenty-two exercises in three levels: first-order partials to warm up, then second-order and cross partials, marginal rates of substitution, level curves and elasticities, then unconstrained optimisation in two variables with the second-order test, ending with the redistribution model from Problem Set 1 treated as a derivative exercise. Every solution is worked in full.</p>

<p class="resource-intro">Work each one on paper first. The theory is in the
<a href="/resources/partial-derivatives/">partial derivatives note</a>; if single-variable derivatives are the problem, start with the
<a href="/resources/derivatives/">derivatives refresher</a>.</p>

<div class="practice practice--long" id="practice">
  <div class="practice-bar">
    <button type="button" class="practice-btn" data-all="open">Show all solutions</button>
    <button type="button" class="practice-btn" data-all="close">Hide all</button>
  </div>
"""

TAIL = """</div>

{% include practice-reveal.html %}
"""

def build():
    failures = [i for i, e in enumerate(EX, 1) if not e["check"]()]
    if failures:
        sys.exit("sympy disagrees with the stated answer of exercise(s): %s" % failures)
    parts = [HEAD, "  {% raw %}\n"]
    level, n = None, 0
    for e in EX:
        if e["level"] != level:
            if level is not None:
                parts.append("  </ol>\n")
            level = e["level"]
            parts.append('  <h2 class="eyebrow practice-level">%s</h2>\n  <ol class="practice-list practice-list--long">\n' % level)
        n += 1
        parts.append(
            '    <li class="practice-item">\n'
            '      <span class="practice-n">%d.</span>\n'
            '      <div class="practice-q">%s</div>\n'
            '      <details class="practice-sol"><summary>Solution</summary>\n'
            '        <div class="practice-a tex2jax_ignore">%s</div>\n'
            '      </details>\n'
            '    </li>\n' % (n, e["statement"], e["solution"]))
    parts.append("  </ol>\n  {% endraw %}\n")
    parts.append(TAIL)
    html = "".join(parts)
    assert "{{" not in html.replace("{% raw %}", "").replace("{% endraw %}", ""), "Liquid clash"
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_pages", "resource-partial-derivatives-practice.html")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print("wrote", out, "with", n, "exercises; all answers verified")

if __name__ == "__main__":
    build()
