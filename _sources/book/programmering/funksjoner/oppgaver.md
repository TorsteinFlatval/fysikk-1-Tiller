# Oppgaver: Funksjoner i Python


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Ta quizen!

:::{quiz}
Q: Hva blir skrevet ut?
   <pre><code class="python">def sum_to(a, b):\n    return a + b\n\nprint(sum_to(2, 4))</code></pre>
+ 6
- 24
- 2
- 4


Q: Hva returnerer funksjonen?
   <pre><code class="python">def f(x):\n    return x * 10</code></pre>
+ Verdien `x * 10`
- Alltid 10
- Alltid 0
- Ingenting


Q: Hva er riktig funksjonskall?
+ `areal_rektangel(5, 2)`
- `areal_rektangel = (5, 2)`
- `areal_rektangel[5, 2]`
- `areal_rektangel{5, 2}`
:::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Fyll inn koden slik at funksjonen returnerer dobbelt av tallet.

:::{interactive-code}
def dobbel(x):
    # FYLL INN
    return ????

print(dobbel(8))
:::

::::{answer}
Utskrift:

```text
16
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
def dobbel(x):
    return 2 * x

print(dobbel(8))
:::
::::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 3
---
level: 2
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Definer en funksjon `f(x)` som beregner $f(x) = x^2 + 2$. Bruk deretter en `for`{l=python}-løkke til å beregne og printe funksjonsværdien for hver $x$-verdi fra $-10$ til og med $10$.

:::{interactive-code}
# Skriv koden din her
:::

:::::{answer}
Utskrift:

```text
102
83
66
51
38
27
18
11
6
3
2
3
6
11
18
27
38
51
66
83
102
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
def f(x):
    return x**2 + 2

for x in range(-10, 11):
    print(f(x))
:::
:::::
:::::::::::::

:::::::::::::{tab-item} b
Definer en funksjon `g(x)` som beregner $g(x) = x^3 - 2x + 1$. Bruk en `while`{l=python}-løkke og en `if`{l=python}-setning til å beregne og printe de positive funksjonsværdiene for hver heltall fra $-10$ til og med $10$.

:::{interactive-code}
# Skriv koden din her
:::

:::::{answer}
Utskrift:

```text
2
1
5
22
57
116
205
330
497
712
981
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
def g(x):
    return x**3 - 2*x + 1

x = -10
while x <= 10:
    verdi = g(x)
    if verdi > 0:
        print(verdi)
    x += 1
:::
:::::
:::::::::::::

::::::::::::::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 4
---
level: 2
---
Lag en funksjon `minste`{l=python} som tar to tall og returnerer det minste.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
Utskrift:

```text
3
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
def minste(a, b):
    if a < b:
        return a
    return b

print(minste(7, 3))
:::
::::
:::::::::::::::
