# Oppgaver

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Finn løsningene på følgende likninger ved å teste verdier:

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen $3x + 2 = 14$ ved å teste verdier fra 0 til 10.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$
\mathcal{L} = \{4\}
$$
::::

::::{solution}
Vi bruker en for-løkke som tester verdier fra 0 til 10:

:::{code-block} python
for x in range(11):
    if 3*x + 2 == 14:
        print("x =", x, "er en løsning!")
:::

Løsningen er $x = 4$ fordi $3 \cdot 4 + 2 = 12 + 2 = 14$.

$$
\mathcal{L} = \{4\}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Løs likningen $x^2 - 4 = 0$ ved å teste verdier fra -5 til 5.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$
\mathcal{L} = \{-2, 2\}
$$
::::

::::{solution}
Vi bruker en for-løkke som tester verdier fra -5 til 5:

:::{code-block} python
for x in range(-5, 6):
    if x**2 - 4 == 0:
        print("x =", x, "er en løsning!")
:::

Løsningene er $x = -2$ og $x = 2$.

$$
\mathcal{L} = \{-2, 2\}
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
Løs likningen $x^2 + 3x - 4 = 0$ ved å teste verdier fra -10 til 10.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$
\mathcal{L} = \{-4, 1\}
$$
::::

::::{solution}
Vi bruker en for-løkke som tester verdier fra -10 til 10:

:::{code-block} python
for x in range(-10, 11):
    if x**2 + 3*x - 4 == 0:
        print("x =", x, "er en løsning!")
:::

Løsningene er $x = -4$ og $x = 1$.

$$
\mathcal{L} = \{-4, 1\}
$$
::::

:::::::::::::

::::::::::::::

::::::::::::::


:::::::::::::::{exercise} Oppgave 2
Definer funksjonen $f(x) = x^2 + 2x + 4$ og finn alle nullpunkt ved å teste verdier fra -10 til 10.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
Likningen har ingen heltallsløsninger.
::::

::::{solution}
Vi definerer funksjonen og ser etter nullpunkt (der $f(x) = 0$):

:::{code-block} python
def f(x):
    return x**2 + 2*x + 4

for x in range(-10, 11):
    if f(x) == 0:
        print("x =", x, "er en løsning!")

print("Ingen nullpunkt funnet blant heltallene.")
:::

Diskriminanten er: $\Delta = 2^2 - 4(1)(4) = 4 - 16 = -12 < 0$

Siden diskriminanten er negativ, har funksjonen ingen reelle nullpunkt.

::::

::::::::::::::


:::::::::::::::{exercise} Oppgave 3
Finn løsningene på likningen $2x^2 - 8 = 0$ ved å teste desimalverdier i steg på 0.01 fra -3 til 3.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
$$
\mathcal{L} = \{-2, 2\}
$$
::::

::::{solution}
Vi bruker en `while`{l=python}-løkke som tester desimalverdier:

:::{code-block} python
x = -3
while x <= 3:
    løsning = 2*x**2 - 8
    if -0.01 < løsning < 0.01:
        print(f"x = {x:.2f} er en løsning!")
    x = x + 0.01
:::

Løsningene er $x = -2$ og $x = 2$.

$$
\mathcal{L} = \{-2, 2\}
$$

::::

:::::::::::::::
