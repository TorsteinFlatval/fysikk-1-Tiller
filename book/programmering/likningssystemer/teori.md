# Likningssystemer med programmering

:::::{admonition} Læringsmål
---
class: tip
---
* Forstå hvordan nøstede `for`{l=python}-løkker fungerer
* Kunne bruke programmering til å løse likningssystemer med to ukjente
* Kunne bruke `and`{l=python} for å sjekke flere betingelser samtidig
* Kunne systematisk finne alle heltallsløsninger i et likningssystem
:::::

Et likningssystem har ofte to ukjente, $x$ og $y$. I programmering kan vi løse slike systemer ved å teste alle mulige par $(x, y)$ i et område og sjekke hvilke som oppfyller begge likningene samtidig.

## Nøstede `for`{l=python}-løkker

For å teste alle par $(x, y)$ bruker vi to `for`{l=python}-løkker: en for $x$ og en for $y$. Den ene løkken nøstes (plasseres) inne i den andre.

:::::::::::::::{summary} Nøstede `for`{l=python}-løkker
For å teste alle par $(x, y)$ bruker vi to `for`{l=python}-løkker:

:::{code-block} python
---
linenos:
---
for x in range(start, slutt):
    for y in range(start, slutt):
        # Kode som kjøres for hver kombinasjon av x og y
:::

Den ytre løkken itererer over $x$, og for hver $x$ itererer den indre løkken over alle $y$-verdier.
:::::::::::::::

:::::::::::::::{explore} Utforsk 1
La oss utforske hvordan nøstede `for`{l=python}-løkker fungerer.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva tror du programmet skriver ut?

:::{interactive-code}
---
predict:
---
for x in range(1, 3):
    for y in range(1, 3):
        print((x, y))
:::
:::::::::::::

:::::::::::::{tab-item} b
Hva tror du programmet skriver ut?

:::{interactive-code}
---
predict:
---
for x in range(1, 4):
    for y in range(1, 3):
        print((x, y))
:::
:::::::::::::

:::::::::::::{tab-item} c
Hva tror du programmet skriver ut?

:::{interactive-code}
---
predict:
---
for x in range(0, 2):
    for y in range(0, 3):
        print((x, y))
:::
:::::::::::::

::::::::::::::

:::::::::::::::

---

## Sjekke flere betingelser samtidig

For å løse et likningssystem må begge likningene være oppfylt samtidig. Vi bruker `and`{l=python} for å sjekke flere betingelser i samme `if`{l=python}-setning.

:::::::::::::::{summary} `and`{l=python} - flere betingelser
Vi bruker `and`{l=python} når både betingelse 1 OG betingelse 2 må være sann:

:::{code-block} python
---
linenos:
---
if <betingelse_1> and <betingelse_2>:
    # Kode som kjøres hvis BEGGE betingelsene er sanne
:::

Hvis bare en av betingelsene er usann, kjøres koden ikke.
:::::::::::::::

:::::::::::::::{explore} Utforsk 2
La oss utforske hvordan `and`{l=python} fungerer når vi sjekker to betingelser.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva tror du programmet skriver ut når vi tester $(x, y) = (3, 2)$ mot systemet $x + y = 5$ og $x - y = 1$?

:::{interactive-code}
---
predict:
---
x = 3
y = 2
if x + y == 5 and x - y == 1:
    print("(", x, ",", y, ") er en løsning!")
:::
:::::::::::::

:::::::::::::{tab-item} b
Hva tror du programmet skriver ut når vi tester $(x, y) = (2, 2)$ mot systemet $x + y = 5$ og $x - y = 1$?

:::{interactive-code}
---
predict:
---
x = 2
y = 2
if x + y == 5 and x - y == 1:
    print("(", x, ",", y, ") er en løsning!")
:::
:::::::::::::

:::::::::::::{tab-item} c
Hva tror du programmet skriver ut når vi tester $(x, y) = (4, 2)$ mot systemet $x + y = 5$ og $x - y = 1$?

:::{interactive-code}
---
predict:
---
x = 4
y = 2
if x + y == 5 and x - y == 1:
    print("(", x, ",", y, ") er en løsning!")
:::
:::::::::::::

::::::::::::::

:::::::::::::::

---

## Løse likningssystemer

Nå kombinerer vi nøstede `for`{l=python}-løkker og `and`{l=python} for å finne alle løsninger på et likningssystem.

:::::::::::::::{summary} Slik løser vi likningssystemer
For å finne løsninger på et likningssystem tester vi alle par $(x, y)$ i et område:

:::{code-block} python
---
linenos:
---
for x in range(start, slutt):
    for y in range(start, slutt):
        if <likning_1> and <likning_2>:
            print((x, y))
:::

Alle par som gjør begge likningene sanne blir skrevet ut.
:::::::::::::::

:::::::::::::::{example} Eksempel 1
La oss løse likningssystemet

$$\begin{align}
x + y &= 5 \\
x - y &= 1
\end{align}$$

ved å teste alle heltallsverdier fra -10 til 10.

:::{interactive-code}
for x in range(-10, 11):
    for y in range(-10, 11):
        if x + y == 5 and x - y == 1:
            print((x, y))
:::

::::{solution}
---
dropdown: 0
---

Vi tester alle par $(x, y)$. For hver kombinasjon sjekker vi om både $x + y = 5$ og $x - y = 1$ er sanne.

Bare paret $(3, 2)$ oppfyller begge likningene:
- $3 + 2 = 5$ ✓
- $3 - 2 = 1$ ✓

Utskriften blir:

:::{code-block} console
(3, 2)
:::

Løsningen er:

$$\mathcal{L} = \{(3, 2)\}$$

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 2
La oss løse likningssystemet

$$\begin{align}
x^2 + y &= 7 \\
x - y &= -1
\end{align}$$

ved å teste alle heltallsverdier fra -10 til 10.

:::{interactive-code}
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 + y == 7 and x - y == -1:
            print((x, y))
:::

::::{solution}
---
dropdown: 0
---

Fra likning 2: $y = x + 1$

Setter vi dette inn i likning 1: $x^2 + (x + 1) = 7$, som gir $x^2 + x - 6 = 0$.

Løsningen er $(2, 3)$:
- $2^2 + 3 = 4 + 3 = 7$ ✓
- $2 - 3 = -1$ ✓

Utskriften blir:

:::{code-block} console
(2, 3)
:::

Løsningen er:

$$\mathcal{L} = \{(2, 3)\}$$

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 3
Noen ganger ønsker vi å finne når to funksjoner har samme verdi, altså når $f(x) = g(x)$.

La $f(x) = x^2$ og $g(x) = 2x$. Finn alle heltallsløsninger der $f(x) = g(x)$ ved å teste verdier fra -5 til 5.

:::{interactive-code}
def f(x):
    return x**2

def g(x):
    return 2*x

for x in range(-5, 6):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

::::{solution}
---
dropdown: 0
---

Vi definerer de to funksjonene og tester hver $x$-verdi. Når $f(x) = g(x)$ oppfyller at:

- For $x = 0$: $f(0) = 0^2 = 0$ og $g(0) = 2 \cdot 0 = 0$ ✓
- For $x = 2$: $f(2) = 2^2 = 4$ og $g(2) = 2 \cdot 2 = 4$ ✓

Utskriften blir:

:::{code-block} console
x = 0: f(0) = g(0) = 0
x = 2: f(2) = g(2) = 4
:::

Løsningene er $x = 0$ og $x = 2$.

$$\mathcal{L} = \{0, 2\}$$

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Definer funksjonene $f(x) = x$ og $g(x) = 2x - 1$, og finn hvor de har samme verdi ved å teste verdier fra -10 til 10.

:::{interactive-code}
# Definer funksjonene og finn løsningen
:::

::::{answer}
$$\mathcal{L} = \{1\}$$
::::

::::{solution}
Vi definerer de to funksjonene og tester hvor $f(x) = g(x)$:

:::{code-block} python
def f(x):
    return x

def g(x):
    return 2*x - 1

for x in range(-10, 11):
    if f(x) == g(x):
        print(f"x = {x}: f({x}) = g({x}) = {f(x)}")
:::

Løsningen er $x = 1$ fordi:
- $f(1) = 1$
- $g(1) = 2(1) - 1 = 1$

Utskriften blir:

:::{code-block} console
x = 1: f(1) = g(1) = 1
:::

$$\mathcal{L} = \{1\}$$

::::

:::::::::::::::

---



---

:::::::::::::::{example} Eksempel 4
La oss løse $f(x) = g(x)$ der $f(x) = x^2$ og $g(x) = 2x$ ved å teste desimalverdier i steg på 0.1 fra -1 til 3.

:::{interactive-code}
def f(x):
    return x**2

def g(x):
    return 2*x

x = -1
while x <= 3:
    differanse = f(x) - g(x)
    if -0.1 < differanse < 0.1:
        print(f"x = {x:.2f}: f({x:.2f}) = {f(x):.2f}, g({x:.2f}) = {g(x):.2f}")
    x = x + 0.1
:::

::::{solution}
---
dropdown: 0
---

Ved å sjekke om differansen mellom $f(x)$ og $g(x)$ ligger nær 0, finner vi de punktene der funksjonene har omtrent samme verdi:

:::{code-block} console
x = 0.00: f(0.00) = 0.00, g(0.00) = 0.00
x = 2.00: f(2.00) = 4.00, g(2.00) = 4.00
:::

Løsningene er $x = 0$ og $x = 2$.

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
Definer funksjonene $f(x) = x^2 - 1$ og $g(x) = 0.5x + 1$. Finn hvor de har samme verdi ved å teste desimalverdier i steg på 0.1 fra -3 til 3.

:::{interactive-code}
# Definer funksjonene og finn løsningene
:::

::::{answer}
Løsningene er omtrent $x \approx -1.20$ og $x \approx 1.70$.
::::

::::{solution}
Vi definerer funksjonene og tester desimalverdier med toleransekontroll:

:::{code-block} python
def f(x):
    return x**2 - 1

def g(x):
    return 0.5*x + 1

x = -3
while x <= 3:
    differanse = f(x) - g(x)
    if -0.1 < differanse < 0.1:
        print(f"x = {x:.2f}: f({x:.2f}) = {f(x):.2f}, g({x:.2f}) = {g(x):.2f}")
    x = x + 0.1
:::

Utskriften viser punktene der funksjonene er omtrent like:

:::{code-block} console
x = -1.20: f(-1.20) = 0.44, g(-1.20) = 0.40
x = 1.70: f(1.70) = 1.89, g(1.70) = 1.85
:::

Løsningene er $x \approx -1.20$ og $x \approx 1.70$.

:::{code-block} console
x = -1.20: f(-1.20) = 0.44, g(-1.20) = 0.40
x = 1.70: f(1.70) = 1.89, g(1.70) = 1.85
:::

Løsningspunktene er omtrent $(−1.20, 0.40)$ og $(1.70, 1.85)$.

:::::::::::::::

---