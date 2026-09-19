"""Builds the derivative practice pages in _pages/ from the exercise lists below.

Solutions are computed with sympy rather than transcribed, so they can be trusted.
Run it after editing a sheet:  pip install sympy && python tools/gen_practice.py
Any page it writes is generated output; edit the lists here, not the HTML.
"""
import sys, os
import sympy as sp

import re
def L(e):
    s = e if isinstance(e, str) else sp.latex(e)
    s = s.replace(r"\log", r"\ln")
    s = re.sub(r"\\ln\{\\left\((.*?) \\right\)\}", r"\\ln(\1)", s)
    return s

def shorter(*cands):
    return min(cands, key=lambda e: len(sp.latex(e)))

def signed_frac(num, den_tex):
    """Renders num/den, pulling a leading minus out in front of the fraction."""
    nl = sign = ""
    nl = sp.latex(num)
    if nl.lstrip().startswith("-"):
        alt = sp.latex(-num)
        if not alt.lstrip().startswith("-"):
            sign, nl = "- ", alt
    return sign + r"\frac{%s}{%s}" % (nl, den_tex)

def den_tex(den, q, var):
    """Prefers the original denominator raised to a power, e.g. (x^2+1)^2,
    over sympy's fully factored or expanded version. Substituting x = t^2
    lets cancel() see through square roots."""
    if q != 1 and q.atoms(sp.Add):          # only worth it when q is a sum
        t = sp.Dummy("t", positive=True)
        for k in (2, 1, 3):
            ratio = sp.cancel(den.subs(var, t**2) / q.subs(var, t**2)**k)
            if not ratio.atoms(sp.Add) and sp.denom(ratio) == 1:
                ratio = sp.powsimp(ratio.subs(t, sp.sqrt(var)))
                pre = "" if ratio == 1 else sp.latex(ratio) + " "
                return pre + sp.latex(q**k)
    return sp.latex(sp.factor(den))

def deriv(expr, var, order=1):
    """Textbook form: sums stay term by term, quotients become one fraction
    with a tidy numerator over a recognisable denominator."""
    d = sp.diff(expr, var, order)
    if isinstance(expr, sp.Add):            # written as a sum -> keep the answer term by term
        parts = []
        for t in sp.expand(d).as_ordered_terms():
            n, dd = sp.fraction(sp.together(t))
            parts.append(sp.latex(t) if dd == 1 else signed_frac(n, sp.latex(sp.factor(dd))))
        out = parts[0]
        for p in parts[1:]:
            out += (" - " + p.lstrip()[1:].lstrip()) if p.lstrip().startswith("-") else (" + " + p)
        return out
    q = sp.fraction(sp.together(expr))[1]
    num, den = sp.fraction(sp.cancel(sp.together(sp.simplify(d))))
    if den == 1 or q == 1:                  # not written as a fraction
        return sp.latex(shorter(sp.expand(d), sp.factor(d), sp.radsimp(sp.together(sp.simplify(d)))))
    return signed_frac(shorter(sp.expand(num), sp.factor(num)), den_tex(den, q, var))

# label, function name, variable, question latex (rhs), expression, order, style
SHEET_A = [
    ("g", "x", r"10", "10"),
    ("T", "y", r"-8", "-8"),
    ("f", "x", r"5x + 7", "5*x+7"),
    ("Q", "t", r"1 - 12t", "1-12*t"),
    ("f", "z", r"z^2 + 3", "z**2+3"),
    ("R", "w", r"w^2 - 8w + 20", "w**2-8*w+20"),
    ("V", "t", r"6t - t^2", "6*t-t**2"),
    ("Q", "t", r"2t^2 - 8t + 10", "2*t**2-8*t+10"),
    ("g", "z", r"1 + 10z - 7z^2", "1+10*z-7*z**2"),
    ("f", "x", r"5x - x^3", "5*x-x**3"),
    ("Y", "t", r"2t^3 + 9t + 5", "2*t**3+9*t+5"),
    ("Z", "x", r"2x^3 - x^2 - x", "2*x**3-x**2-x"),
    ("f", "t", r"2t - 3", "2*t-3"),
    ("g", "x", r"\frac{x+2}{1-x}", "(x+2)/(1-x)"),
    ("Q", "t", r"\frac{t^2}{t+2}", "t**2/(t+2)"),
    ("f", "w", r"\sqrt{w+8}", "sqrt(w+8)"),
    ("V", "t", r"\sqrt{14+3t}", "sqrt(14+3*t)"),
    ("G", "x", r"\sqrt{2-5x}", "sqrt(2-5*x)"),
    ("Q", "t", r"\sqrt{1+4t}", "sqrt(1+4*t)"),
    ("f", "x", r"\sqrt{x^2+1}", "sqrt(x**2+1)"),
    ("W", "t", r"\frac{1}{\sqrt{t}}", "1/sqrt(t)"),
    ("g", "x", r"4\sqrt{1-x}", "4*sqrt(1-x)"),
    ("f", "x", r"x + \sqrt{x}", "x+sqrt(x)"),
    ("f", "x", r"x + \frac{1}{x}", "x+1/x"),
]

SHEET_B = [
    ("f", r"3x^2 + 2x + 1", "3*x**2+2*x+1"),
    ("g", r"\frac{5x^2+3x}{x}", "(5*x**2+3*x)/x"),
    ("h", r"\ln(x^2)", "log(x**2)"),
    ("k", r"\frac{x^2-1}{x+1}", "(x**2-1)/(x+1)"),
    ("m", r"\frac{1}{x^3}", "1/x**3"),
    ("n", r"\sqrt{x} + x^2", "sqrt(x)+x**2"),
    ("p", r"x^3 \cdot x^2", "x**3*x**2"),
    ("q", r"\frac{x^2+2}{x^3-1}", "(x**2+2)/(x**3-1)"),
    ("r", r"\frac{1}{x^2+1}", "1/(x**2+1)"),
    ("s", r"x^5 - 3x^2 + \frac{1}{x}", "x**5-3*x**2+1/x"),
    ("f", r"x^2 \ln(x)", "x**2*log(x)"),
    ("g", r"\frac{\ln(x)}{x}", "log(x)/x"),
    ("h", r"x e^x", "x*exp(x)"),
    ("k", r"\frac{e^x}{x^2}", "exp(x)/x**2"),
    ("m", r"x^2 + \frac{1}{\sqrt{x}}", "x**2+1/sqrt(x)"),
    ("n", r"\frac{x^2+1}{x^2-1}", "(x**2+1)/(x**2-1)"),
    ("p", r"\ln(x^3)", "log(x**3)"),
    ("q", r"x^2 - 3x + 4 + \ln(x)", "x**2-3*x+4+log(x)"),
    ("r", r"\frac{x^3+1}{x^2+1}", "(x**3+1)/(x**2+1)"),
    ("s", r"e^x - x^2 + \frac{1}{x}", "exp(x)-x**2+1/x"),
    ("f", r"\frac{x^2-4x+3}{x}", "(x**2-4*x+3)/x"),
    ("g", r"\frac{\ln(x)}{x^2}", "log(x)/x**2"),
    ("h", r"x^3 \ln(x)", "x**3*log(x)"),
    ("k", r"x^3 + \frac{1}{x^3}", "x**3+1/x**3"),
    ("m", r"\frac{2x+3}{x^2}", "(2*x+3)/x**2"),
    ("n", r"\frac{x}{x^2+1}", "x/(x**2+1)"),
    ("p", r"x\sqrt{x}", "x*sqrt(x)"),
    ("q", r"x^4 - \frac{1}{x}", "x**4-1/x"),
    ("r", r"x^2 + \ln(x^2)", "x**2+log(x**2)"),
    ("s", r"\frac{1+x^2}{x^3}", "(1+x**2)/x**3"),
    ("f", r"x + \ln(x)", "x+log(x)"),
    ("g", r"\frac{x^2-1}{x^2+1}", "(x**2-1)/(x**2+1)"),
    ("h", r"\frac{1}{x^2}", "1/x**2"),
    ("k", r"x^2 + \frac{1}{x^2}", "x**2+1/x**2"),
    ("m", r"\frac{x}{\sqrt{x}}", "x/sqrt(x)"),
    ("n", r"\frac{x^3+2x}{x+1}", "(x**3+2*x)/(x+1)"),
    ("p", r"x^2 e^x", "x**2*exp(x)"),
    ("q", r"\frac{1}{x^3+1}", "1/(x**3+1)"),
    ("r", r"\frac{x^2-2x+1}{x}", "(x**2-2*x+1)/x"),
    ("s", r"x^4 - 2x + \frac{1}{x}", "x**4-2*x+1/x"),
    ("f", r"\ln(x^2+1)", "log(x**2+1)"),
    ("g", r"\frac{1}{x} + \ln(x)", "1/x+log(x)"),
    ("h", r"\frac{x^3-1}{x^2-1}", "(x**3-1)/(x**2-1)"),
    ("k", r"x^2 + x e^x", "x**2+x*exp(x)"),
    ("m", r"\sqrt{x} + \ln(x)", "sqrt(x)+log(x)"),
    ("n", r"x e^x + 1", "x*exp(x)+1"),
    ("p", r"\frac{x^2+2x+1}{x+1}", "(x**2+2*x+1)/(x+1)"),
    ("q", r"\frac{e^x}{x}", "exp(x)/x"),
    ("r", r"x^2 + \frac{1}{x^2+1}", "x**2+1/(x**2+1)"),
    ("s", r"\frac{x+1}{x-1}", "(x+1)/(x-1)"),
    ("f", r"x^2 + x^3 + x^4", "x**2+x**3+x**4"),
    ("g", r"\frac{x^2}{\sqrt{x}}", "x**2/sqrt(x)"),
    ("h", r"x - \frac{1}{x} + \ln(x)", "x-1/x+log(x)"),
    ("k", r"\frac{x^3+2}{x}", "(x**3+2)/x"),
    ("m", r"\frac{x}{e^x}", "x/exp(x)"),
    ("n", r"\ln(x) + x^2", "log(x)+x**2"),
    ("p", r"x^3 - x^2 + \frac{1}{x}", "x**3-x**2+1/x"),
    ("q", r"x^2 + \frac{2}{x} + 1", "x**2+2/x+1"),
    ("r", r"x^5 + x + \frac{1}{x^3}", "x**5+x+1/x**3"),
    ("s", r"\ln(x^4)", "log(x**4)"),
    ("f", r"\frac{x^4-1}{x^2+1}", "(x**4-1)/(x**2+1)"),
    ("g", r"x^2 + x^2 \ln(x)", "x**2+x**2*log(x)"),
    ("h", r"x \ln(x^2)", "x*log(x**2)"),
    ("k", r"\frac{1}{x^3+2}", "1/(x**3+2)"),
    ("m", r"x^3 + e^x", "x**3+exp(x)"),
    ("n", r"\frac{x^2-x+1}{x^3}", "(x**2-x+1)/x**3"),
    ("p", r"\frac{1}{\sqrt{x}+1}", "1/(sqrt(x)+1)"),
    ("q", r"x^2 + \frac{1}{x+1}", "x**2+1/(x+1)"),
    ("r", r"x \ln(x) + x", "x*log(x)+x"),
    ("s", r"\frac{1}{x^2-1}", "1/(x**2-1)"),
    ("f", r"\frac{x^2+x+1}{\sqrt{x}}", "(x**2+x+1)/sqrt(x)"),
    ("g", r"x e^x + x^2", "x*exp(x)+x**2"),
    ("h", r"x^2 + \frac{1}{x^3}", "x**2+1/x**3"),
    ("k", r"x^2 - \frac{1}{\sqrt{x}}", "x**2-1/sqrt(x)"),
    ("m", r"x^2 + \ln(x^3)", "x**2+log(x**3)"),
    ("n", r"x^3 + x + \ln(x)", "x**3+x+log(x)"),
    ("p", r"x^2 \cdot x^3", "x**2*x**3"),
    ("q", r"x^5 + \frac{1}{x^2}", "x**5+1/x**2"),
    ("r", r"\frac{x^3+1}{\sqrt{x}}", "(x**3+1)/sqrt(x)"),
    ("s", r"x + \frac{1}{x^3}", "x+1/x**3"),
    ("f", r"x^3 - \ln(x)", "x**3-log(x)"),
    ("g", r"\frac{e^x+1}{x}", "(exp(x)+1)/x"),
    ("h", r"x^2 + e^x", "x**2+exp(x)"),
    ("k", r"\frac{x^4+x^2+1}{x}", "(x**4+x**2+1)/x"),
    ("m", r"x + x \ln(x)", "x+x*log(x)"),
    ("n", r"x^2 - 1 + \frac{1}{x^2}", "x**2-1+1/x**2"),
    ("p", r"\frac{x^2+1}{\sqrt{x^3}}", "(x**2+1)/sqrt(x**3)"),
    ("q", r"\frac{x^2-1}{x^3+1}", "(x**2-1)/(x**3+1)"),
    ("r", r"x^2 \cdot \ln(x^2)", "x**2*log(x**2)"),
    ("s", r"\frac{e^x-1}{x^2}", "(exp(x)-1)/x**2"),
    ("f", r"x^2 + x^3 + \ln(x)", "x**2+x**3+log(x)"),
    ("g", r"x^4 - \frac{1}{x^2}", "x**4-1/x**2"),
    ("h", r"x \cdot \frac{1}{x^2+1}", "x/(x**2+1)"),
    ("k", r"x^3 + \frac{1}{x} + e^x", "x**3+1/x+exp(x)"),
    ("m", r"\frac{\ln(x)}{\sqrt{x}}", "log(x)/sqrt(x)"),
    ("n", r"\frac{x^2+\ln(x)}{x}", "(x**2+log(x))/x"),
    ("p", r"\frac{1}{x^2+\ln(x)}", "1/(x**2+log(x))"),
    ("q", r"x^4 + x^2 + 1", "x**4+x**2+1"),
    ("r", r"\frac{1}{\sqrt{x^2+1}}", "1/sqrt(x**2+1)"),
    ("s", r"x^2 + \frac{1}{x^4}", "x**2+1/x**4"),
]

SHEET_C = [
    (r"(x^2+3)^5", "(x**2+3)**5", 1),
    (r"\ln(4x^2+1)", "log(4*x**2+1)", 1),
    (r"\frac{e^x}{x^2+1}", "exp(x)/(x**2+1)", 1),
    (r"\sqrt{x} \cdot \ln(x)", "sqrt(x)*log(x)", 1),
    (r"x^{1/4} \cdot e^{x^2}", "x**Rational(1,4)*exp(x**2)", 1),
    (r"\frac{x^3+2x}{\sqrt{x}}", "(x**3+2*x)/sqrt(x)", 1),
    (r"\frac{\ln(x)}{x^2}", "log(x)/x**2", 1),
    (r"\frac{(2x+1)^3}{x^2+1}", "(2*x+1)**3/(x**2+1)", 1),
    (r"e^{\ln(x^2+1)}", "exp(log(x**2+1))", 1),
    (r"x \cdot \ln(x^2+1)", "x*log(x**2+1)", 1),
    (r"x^2 \cdot \ln(x)", "x**2*log(x)", 2),
    (r"e^{2x} \cdot x", "exp(2*x)*x", 2),
    (r"\frac{1}{x} \cdot \ln(x)", "log(x)/x", 2),
    (r"(x^2+1)^3", "(x**2+1)**3", 2),
    (r"\sqrt{x^3+2}", "sqrt(x**3+2)", 2),
    (r"x \cdot e^{-x}", "x*exp(-x)", 2),
    (r"\ln(x^2+3x+2)", "log(x**2+3*x+2)", 2),
    (r"\frac{e^x}{x}", "exp(x)/x", 2),
    (r"x^3 \cdot \ln(x)", "x**3*log(x)", 2),
    (r"\frac{\ln(x)}{x+1}", "log(x)/(x+1)", 2),
]

# his PDF answer keys, for cross-checking (sheet C only; sheet A checked separately)
C_KEY = {
    1: "10*x*(x**2+3)**4", 2: "8*x/(4*x**2+1)", 3: "exp(x)*(x**2+1-2*x)/(x**2+1)**2",
    4: "log(x)/(2*sqrt(x))+1/sqrt(x)", 5: "x**Rational(-3,4)*exp(x**2)+2*x**Rational(5,4)*exp(x**2)",
    6: "((3*x**2+2)*sqrt(x)-(x**3+2*x)*Rational(1,2)*x**Rational(-1,2))/x",
    7: "(1-2*log(x))/x**3",
    8: "(6*(2*x+1)**2*(x**2+1)-2*x*(2*x+1)**3)/(x**2+1)**2",
    9: "2*x", 10: "log(x**2+1)+2*x**2/(x**2+1)",
    11: "2*log(x)+3", 12: "4*exp(2*x)+4*x*exp(2*x)", 13: "(2-log(x))/x**3",
    14: "6*(x**2+1)**2+12*x**2*(x**2+1)", 15: "3*x/(x**3+2)**Rational(1,2)-9*x**2/(4*(x**3+2)**Rational(3,2))",
    16: "exp(-x)*(x-2)", 17: "-2*(3*x+2)/(x**2+3*x+2)**2", 18: "exp(x)*(x-2)/x**2",
    19: "6*x*log(x)+7*x**2-3*x**2/x**2", 20: "((x+1)-2*log(x))/(x+1)**3",
}

def build(sheet, kind):
    rows = []
    if kind == "A":
        for i, (name, v, q, e) in enumerate(sheet, 1):
            var = sp.Symbol(v, positive=True)
            expr = sp.sympify(e, locals={v: var})
            ans = deriv(expr, var)
            rows.append((i, f"{name}({v}) = {q}", f"{name}'({v}) = {L(ans)}"))
    elif kind == "B":
        x = sp.Symbol("x", positive=True)
        for i, (name, q, e) in enumerate(sheet, 1):
            expr = sp.sympify(e, locals={"x": x})
            ans = deriv(expr, x)
            rows.append((i, f"{name}(x) = {q}", f"{name}'(x) = {L(ans)}"))
    else:
        x = sp.Symbol("x", positive=True)
        for i, (q, e, order) in enumerate(sheet, 1):
            expr = sp.sympify(e, locals={"x": x, "Rational": sp.Rational})
            ans = deriv(expr, x, order)
            prime = "'" * order
            rows.append((i, f"f(x) = {q}", f"f{prime}(x) = {L(ans)}"))
            key = C_KEY.get(i)
            if key:
                mine = sp.simplify(sp.diff(expr, x, order))
                his = sp.sympify(key, locals={"x": x, "Rational": sp.Rational})
                same = sp.simplify(mine - his) == 0
                if not same:
                    print(f"  [C{i}] PDF key differs: pdf={sp.simplify(his)}   correct={sp.simplify(mine)}")
    return rows

OVERRIDE = {("C", 15): r"f''(x) = \frac{3x\left(x^{3} + 8\right)}{4\left(x^{3} + 2\right)^{\frac{3}{2}}}"}

PAGES = {
    "A": dict(
        fname="resource-derivatives-warmup.html",
        title="Derivatives Practice: Starter",
        permalink="/resources/derivatives-warmup/",
        intro="Twenty-four exercises straight from the definition or from the basic rules. Constants, polynomials, "
              "two quotients and a run of square roots. Start here if the rules are still new.",
    ),
    "B": dict(
        fname="resource-derivatives-100.html",
        title="Derivatives Practice: Intermediate",
        permalink="/resources/derivatives-100/",
        intro="One hundred functions to differentiate, built out of powers, roots, logs, exponentials, "
              "products and quotients. Almost none of them need the chain rule, so this is the sheet "
              "for drilling the product and quotient rules until they are automatic.",
    ),
    "C": dict(
        fname="resource-derivatives-second.html",
        title="Derivatives Practice: Upper Intermediate",
        permalink="/resources/derivatives-second/",
        intro="Harder than the other two sheets: chain rule throughout, and the second half asks for "
              "the second derivative. Compute the first derivative for 1 to 10 and the second "
              "derivative for 11 to 20, without a calculator.",
    ),
}

HEAD = """---
layout: archive
title: "%(title)s"
permalink: %(permalink)s
---

<p class="resource-intro">%(intro)s</p>

<p class="resource-intro">Work each one out on paper first, then open the solution to check it. The theory is in the
<a href="/resources/derivatives/">derivatives refresher</a>; the other sheets are on the
<a href="/resources/">resources page</a>.</p>

<div class="practice" id="practice">
  <div class="practice-bar">
    <button type="button" class="practice-btn" data-all="open">Show all solutions</button>
    <button type="button" class="practice-btn" data-all="close">Hide all</button>
  </div>
"""

TAIL = """</div>

<script>
(function () {
  var root = document.getElementById('practice');
  if (!root) { return; }
  function typeset(el) {
    el.querySelectorAll('.tex2jax_ignore').forEach(function (n) { n.classList.remove('tex2jax_ignore'); });
    if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise([el]); }
  }
  root.querySelectorAll('details.practice-sol').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open && !d.dataset.done) { d.dataset.done = '1'; typeset(d); }
    });
  });
  root.querySelectorAll('.practice-btn').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.dataset.all === 'open';
      root.querySelectorAll('details.practice-sol').forEach(function (d) { d.dataset.done = '1'; d.open = open; });
      if (open) { typeset(root); }
    });
  });
})();
</script>
"""

def write_page(key, rows, outdir):
    meta = PAGES[key]
    parts = [HEAD % meta, "  {% raw %}\n", '  <ol class="practice-list">\n']
    for i, q, a in rows:
        a = OVERRIDE.get((key, i), a)
        parts.append(
            '    <li class="practice-item">\n'
            '      <span class="practice-n">%d.</span>\n'
            '      <div class="practice-q">\\( %s \\)</div>\n'
            '      <details class="practice-sol"><summary>Solution</summary>\n'
            '        <div class="practice-a tex2jax_ignore">\\( %s \\)</div>\n'
            '      </details>\n'
            '    </li>\n' % (i, q, a))
    parts.append('  </ol>\n  {% endraw %}\n')
    parts.append(TAIL)
    html = "".join(parts)
    assert "{{" not in html.replace("{% raw %}", "").replace("{% endraw %}", ""), "Liquid clash"
    path = os.path.join(outdir, meta["fname"])
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print("wrote", path, len(rows), "exercises")

if __name__ == "__main__":
    print("== checking sheet C against the PDF answer key ==")
    A = build(SHEET_A, "A"); B = build(SHEET_B, "B"); C = build(SHEET_C, "C")
    pages_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_pages")
    for name, rows in (("A", A), ("B", B), ("C", C)):
        print(f"\n== sheet {name}: {len(rows)} rows ==")
        for i, q, a in rows:
            print(f"{i:>3}. {q}    ->    {a}")
        write_page(name, rows, pages_dir)
