# Programmering av tallfølger

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage programmer som lager tallene i en tallfølge.
* Kunne lage programmer som finner summen av tall i en tallfølge.
:::::

Tallfølger er nært knyttet til de naturlige tallene og egenskaper ved tall. Du har kanskje møtt på figurtall før som trekanttall eller kvadrattall. Dette er eksempler på tallfølger som er representert med figurer. Her skal vi se på hvordan vi kan bruke programmering til å svare på spørsmål knyttet til tallfølger og figurtall. 

## Formler

Når vi skriver et program, så ønsker vi ofte å regne med formler. 


:::::::::::::::{explore} Utforsk 3 
Nedenfor vises et program som bruker en formel for å regne ut og skrive ut noen tall i en tallfølge.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet og forutsi hvilke tall programmet skriver ut.

Skriv inn svaret ditt nedenfor sjekk. 


:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det skriver ut verdiene til tallfølgen 

$$
a_n = n^2 \qfor n \in \set{1, 2, \ldots, 10}
$$

> For å opphøye et tall i Python, bruker vi `**`{l=python}. For eksempel er $2^3$ skrevet som `2 ** 3`{l=python} i Python.


:::::::::::::
::::::::::::::


:::{interactive-code}
---
predict:
---
for n in range(1, 5):
    a = 3 * n + 1
    
    print(a)
:::




:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 4

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
a_n = 2n + 3 \qfor n \in \set{1, 2, 3, 4, 5}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    a = # FYLL INN
    
    print(a)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 6):
    a = 2 * n + 3
    
    print(a)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
b_n = n^2 + 2n + 1 \qfor n \in \set{1, 3, 5, 7, 9}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    b = # FYLL INN
    
    print(b)

:::

::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 10, 2):
    b = n**2 + 2 * n + 1
    
    print(b)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
c_n = 2^n \qfor n \in \set{-2, -1, 0, 1, 2}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    c = # FYLL INN
    
    print(c)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(-2, 3):
    c = 2 ** n
    
    print(c)
:::
::::
:::::::::::::
::::::::::::::



:::::::::::::::


## Summere tall i en tallfølge

I mange tilfeller er vi interessert i å summere tallene i en tallfølge. 


:::{margin} `s = s + n`{l=python}
Når vi skriver `s = s + n`{l=python}, så betyr det at vi legger til verdien til `n`{l=python} til verdien til `s`{l=python} og lagrer resultatet i `s`{l=python}. 
:::

:::::::::::::::{explore} Utforsk 4
Nedenfor vises et program som summerer noen tall. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet nedenfor og forutsi hva som skrives ut. 

Skriv inn svaret ditt nedenfor og sjekk.
:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det summerer alle naturlig tall fra $1$ til og med $100$. 

Hva blir summen? 
:::::::::::::


:::::::::::::{tab-item} 
Endre på programmet slik at det finner summen av de $10$ første kvadrattallene

$$
S = 1^2 + 2^2 + 3^2 + \ldots + 10^2
$$
:::::::::::::

::::::::::::::

:::{interactive-code}
---
predict:
---
s = 0
for n in range(1, 6):
    s = s + n

print(s)
:::

:::::::::::::::


