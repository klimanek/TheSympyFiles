"""Odpověď do poradny"""

from sympy import Symbol, diff, solveset, S
from sympy.plotting import plot
from sympy.calculus.util import stationary_points, minimum, maximum

x = Symbol("x")
f = (x + 3) ** 3 - (x + 17) ** 2 - x + 5

# Hledám stacionární body (v oboru reálných čísel) včetně hodnot
sp_x = list(solveset(diff(f, x), domain=S.Reals))  # převádím rovnou na seznam
sp_y = [f.subs(x, spx) for spx in sp_x]  # příslušné hodnoty ve stacionárních bodech

# Graf funkce včetně vykreslení lokálních extrémů
# Pozn.: Více křivek se vykresluje prostým výpisem fcí, popř.
# konstantních hodnot. Protože hodnoty máme výše v seznamu,
# je potřeba je rozbalit, což se udělá jako *list, u nás *sp_y.
f_plot = plot(
    f,
    *sp_y,
    (x, -10, 5),
    size=(12, 8),
    markers=[{"args": [sp_x, sp_y, "ro"]}],
    show=False,
)

f_plot.save("extrema_plot.pdf")
f_plot.show()

print(f"f(x) = {f}")
print(f"df(x) = {diff(f, x)}")
print(f"STBs: {stationary_points(f, x, S.Reals)}")
print(f"Max: {maximum(f, x, S.Reals)}")
print(f"Min: {minimum(f, x, S.Reals)}")
