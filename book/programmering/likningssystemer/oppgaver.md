# Oppgaver: Likningssystemer med programmering


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Finn hvor de to funksjonene har samme verdi:

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll inn koden: $f(x) = x + 1$ og $g(x) = 3x - 5$. Test verdier fra -10 til 10.

:::{interactive-code}
def f(x):
    return x + 1

def g(x):
    return 3*x - 5

for x in range(-10, 11):
    if ??????:
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

::::{answer}
$$\mathcal{L} = \{3\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return x + 1

def g(x):
    return 3*x - 5

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningen er $x = 3$ fordi $f(3) = 4$ og $g(3) = 4$.
::::
:::::::::::::

:::::::::::::{tab-item} b
$f(x) = 2x + 1$ og $g(x) = x + 4$. Test verdier fra -10 til 10.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$\mathcal{L} = \{3\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return 2*x + 1

def g(x):
    return x + 4

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningen er $x = 3$ fordi $f(3) = 7$ og $g(3) = 7$.
::::
:::::::::::::

:::::::::::::{tab-item} c
$f(x) = x^2$ og $g(x) = 4x - 3$. Test verdier fra -10 til 10.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$\mathcal{L} = \{1, 3\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return x**2

def g(x):
    return 4*x - 3

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningene er $x = 1$ og $x = 3$.
::::
:::::::::::::

::::::::::::::

::::::::::::::::


:::::::::::::::{exercise} Oppgave 2
---
level: 2
---
Finn alle løsninger der de to funksjonene har samme verdi:

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$f(x) = x^2 + 1$ og $g(x) = 2x + 3$. Test verdier fra -10 til 10.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
$$\mathcal{L} = \{-1, 2\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return x**2 + 1

def g(x):
    return 2*x + 3

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningene er $x = -1$ og $x = 2$.
::::
:::::::::::::

:::::::::::::{tab-item} b
$f(x) = x^2 + 1$ og $g(x) = 2x + 1$. Test verdier fra -10 til 10.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
$$\mathcal{L} = \{0, 2\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return x**2 + 1

def g(x):
    return 2*x + 1

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningene er $x = 0$ og $x = 2$.
::::
:::::::::::::

:::::::::::::{tab-item} c
$f(x) = x^3 - x$ og $g(x) = 2x$. Test verdier fra -5 til 5.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
$$\mathcal{L} = \{-\sqrt{3}, 0, \sqrt{3}\}$$ eller omtrent $$\{-1.73, 0, 1.73\}$$
::::

::::{solution}
:::{code-block} python
def f(x):
    return x**3 - x

def g(x):
    return 2*x

for x in range(-5, 6):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningen $x = 0$ blir funnet. For desimalløsninger kan vi teste med mindre steg.
::::
:::::::::::::

::::::::::::::

::::::::::::::::


:::::::::::::::{exercise} Oppgave 3
---
level: 2
---
Finn desimalløsninger ved å teste verdier i små steg:

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
La $f(x) = x^2$ og $g(x) = 2x + 1$. Finn hvor de har samme verdi ved å teste desimalverdier i steg på 0.1 fra -2 til 4.

:::{interactive-code}
# Definer funksjonene og finn løsningene med toleransekontroll
:::

::::{answer}
Løsningene er omtrent $x = -0.40$ og $x = 2.40$.
::::

::::{solution}
:::{code-block} python
def f(x):
    return x**2

def g(x):
    return 2*x + 1

x = -2
while x <= 4:
    differanse = f(x) - g(x)
    if -0.15 < differanse < 0.15:
        print(f"x = {x:.2f}: f({x:.2f}) = {f(x):.2f}, g({x:.2f}) = {g(x):.2f}")
    x = x + 0.1
:::

Vi bruker toleransekontroll fordi desimalverdier lagres med små avrundingsfeil.
::::
:::::::::::::

:::::::::::::{tab-item} b
La $f(x) = -x^2 + 5$ og $g(x) = x + 2$. Finn hvor de har samme verdi ved å teste desimalverdier i steg på 0.1 fra -3 til 3.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
Løsningene er omtrent $x \approx -2.30$ og $x \approx 1.30$.
::::

::::{solution}
:::{code-block} python
def f(x):
    return -x**2 + 5

def g(x):
    return x + 2

x = -3
while x <= 3:
    differanse = f(x) - g(x)
    if -0.15 < differanse < 0.15:
        print(f"x = {x:.2f}: f({x:.2f}) = {f(x):.2f}, g({x:.2f}) = {g(x):.2f}")
    x = x + 0.1
:::

Løsningene vises når differansen er nær null.
::::
:::::::::::::

:::::::::::::{tab-item} c
La $f(x) = -0.5x + 1$ og $g(x) = x^2 - 2$. Finn hvor de har samme verdi ved å teste desimalverdier i steg på 0.1 fra -2 til 2.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
Løsningen er omtrent $x = 1.50$.
::::

::::{solution}
:::{code-block} python
def f(x):
    return -0.5*x + 1

def g(x):
    return x**2 - 2

x = -2
while x <= 2:
    differanse = f(x) - g(x)
    if -0.15 < differanse < 0.15:
        print(f"x = {x:.2f}: f({x:.2f}) = {f(x):.2f}, g({x:.2f}) = {g(x):.2f}")
    x = x + 0.1
:::

Løsningen vises når funksjonene har omtrent samme verdi.
::::
:::::::::::::

::::::::::::::

::::::::::::::::


:::::::::::::::{exercise} Oppgave 4
---
level: 3
---
Løs likningssystemer med tre ukjente (x, y, z):

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Finn alle heltallsløsninger i intervallet [-10, 10] for systemet:

$$\begin{align}
x + y + z &= 6 \\
x - y + z &= 2 \\
x + y - z &= 4
\end{align}$$

:::{interactive-code}
# Bruk tre nøstede for-løkker
:::

::::{answer}
$$\mathcal{L} = \{(3, 1, 2)\}$$
::::

::::{solution}
Med tre ukjente bruker vi tre nøstede `for`{l=python}-løkker:

:::{code-block} python
for x in range(-10, 11):
    for y in range(-10, 11):
        for z in range(-10, 11):
            if x + y + z == 6 and x - y + z == 2 and x + y - z == 4:
                print((x, y, z))
:::

Løsningen er $(3, 1, 2)$.
::::
:::::::::::::

:::::::::::::{tab-item} b
Finn alle heltallsløsninger i intervallet [-5, 5] for systemet:

$$\begin{align}
x + y + z &= 0 \\
2x - y + z &= 3 \\
x + 2y - z &= -1
\end{align}$$

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$\mathcal{L} = \{(1, -1, 0)\}$$
::::

::::{solution}
:::{code-block} python
for x in range(-5, 6):
    for y in range(-5, 6):
        for z in range(-5, 6):
            if x + y + z == 0 and 2*x - y + z == 3 and x + 2*y - z == -1:
                print((x, y, z))
:::

Løsningen er $(1, -1, 0)$.
::::
:::::::::::::

:::::::::::::{tab-item} c
Finn alle heltallsløsninger i intervallet [-10, 10] for systemet:

$$\begin{align}
x^2 + y + z &= 6 \\
x - y^2 + z &= 2 \\
x + y - z &= 1
\end{align}$$

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$\mathcal{L} = \{(2, 1, 0), (1, 0, 0)\}$$
::::

::::{solution}
:::{code-block} python
for x in range(-10, 11):
    for y in range(-10, 11):
        for z in range(-10, 11):
            if x**2 + y + z == 6 and x - y**2 + z == 2 and x + y - z == 1:
                print((x, y, z))
:::

Løsningene er $(2, 1, 0)$ og $(1, 0, 0)$.
::::
:::::::::::::

::::::::::::::

::::::::::::::::
