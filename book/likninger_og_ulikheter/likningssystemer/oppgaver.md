# Oppgaver: Ikke-lineære likningssystemer


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 - 2x + y &= 4\\
    \\
    -x + y &= 2
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/a.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\mathcal{L} = \{(-1, 1), (2, 4)\}
$$
::::

::::{solution}
Vi ser fra figuren at grafene til likningene skjærer hverandre i punktene $(-1, 1)$ og $(2, 4)$. Løsningen av likningssystemet er derfor 

$$
\mathcal{L} = \{(-1, 1), (2, 4)\}
$$

::::

:::::::::::::


:::::::::::::{tab-item} b

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 + x - y &= 2\\
    \\
    -2x + y &= 4
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/b.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\mathcal{L} = \{(-2, 0), (3, 10)\}
$$
::::

::::{solution}
Grafene til likningene skjærer hverandre i punktene $(-2, 0)$ og $(3, 10)$. Løsniingen av likningssystemet er derfor

$$
\mathcal{L} = \{(-2, 0), (3, 10)\}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 + 2x - y - 1 &= 0\\
    \\
    3x - y &= -1
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/c.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\mathcal{L} = \{(-1, -2), (2, 7)\}
$$
::::


::::{solution}
Grafene skjærer hverandre i punktene $(-1, -2)$ og $(2, 7)$. Løsningen av likningssystemet er derfor

$$
\mathcal{L} = \{(-1, -2), (2, 7)\}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d

Bruk figuren nedenfor til å løse likningssystemet 

\begin{align*}
    x^2 - 2x + y &= -1\\
    \\
    2x + y &= 3
\end{align*}

:::{figure} ./figurer/oppgaver/oppgave_1/d.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\mathcal{L} = \{(2, -1)\}
$$
::::

::::{solution}
Grafene skjærer hverandre i ett punkt: $(2, -1)$. Løsningen av likningssystemet er derfor

$$
\mathcal{L} = \{(2, -1)\}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Bruk Geogebra til å løse likningssystemene grafisk. 


::::{hints} Hvordan løser jeg likningssystemer grafisk med Geogebra? 
Et likningssystem er gitt ved 

\begin{align*}
    2x - y &= 3 \\
    x^2 - 2y - y &= 3
\end{align*}

Nedenfor ser du en gif som viser hvordan man løser likningen med grafvinduet i Geogebra. Vi trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktet.

:::{figure} ./grafisk_løsning.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

Skjæringspunktene mellom de to grafene er $(4, 5)$ og $(0, -3)$ som betyr at løsningen av likningssystemet er

$$
\mathcal{L} = \{(4, 5), (0, -3)\}
$$

::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{ggb-popup}
---
layout: sidebar
---
:::

\begin{align*}
-x^2 + x + y &= 1 \\
\\
3x + y &= 4
\end{align*}


::::{answer}
$$
\mathcal{L} = \{(-3, 13), (1, 1)\}
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/a.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-3, 13)$ og $(1, 1)$. Da er løsningen av likningssystemet gitt ved 

$$
\mathcal{L} = \{(-3, 13), (1, 1)\}
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
:::{ggb-popup}
---
layout: sidebar
---
:::

\begin{align*}
x^2 - x - y &= 3 \\
\\
x - y &= -5
\end{align*}

::::{answer}
$$
\mathcal{L} = \{(-2, 3), (4, 9)\}
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/b.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-2, 3)$ og $(4, 9)$. Da er løsningen av likningssystemet gitt ved

$$
\mathcal{L} = \{(-2, 3), (4, 9)\}
$$

::::

:::::::::::::



:::::::::::::{tab-item} c
:::{ggb-popup}
---
layout: sidebar
---
:::

\begin{align*}
x^2 + 2x - y &= 0 \\
\\
-2x + y &= 1
\end{align*}


::::{answer}
$$
\mathcal{L} = \{(-1, -1), (1, 3)\}
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/c.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(-1, -1)$ og $(1, 3)$. Da er løsningen av likningssystemet gitt ved

$$
\mathcal{L} = \{(-1, -1), (1, 3)\}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d

:::{ggb-popup}
---
layout: sidebar
---
:::


\begin{align*}
-x^2 + x - y &= -1 \\
\\
2x + y &= 1
\end{align*}


::::{answer}
$$
\mathcal{L} = \{(0, 1), (3, -5)\}
$$
::::


::::{solution}
Vi tegner grafene til likningene i Geogebra og bruker "skjæring mellom to objekt" {ggb-icon}`mode_intersect` for å finne skjæringspunktet mellom dem. Se figuren nedenfor:

:::{figure} ./figurer/oppgaver/oppgave_2/d.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Grafene skjærer hverandre i $(0, 1)$ og $(4, -7)$. Da er løsningen av likningssystemet gitt ved

$$
\mathcal{L} = \{(0, 1), (4, -7)\}
$$
::::

:::::::::::::



::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
---
level: 1
---
Bruk CAS til å løse likningssystemene. 

::::{hints} Hvordan løser jeg likningssystemer med CAS?
Nedenfor ser du en gif som viser hvordan man løser et likningssystem med CAS.

:::{figure} ./cas_likningssystemer.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{cas-popup}
---
layout: sidebar
---
:::

\begin{align*}
-x^2 + 3x + 4y &= 0 \\
\\
-x + 2y &= -2
\end{align*}


::::{answer}
$$
\mathcal{L} = \left\{\left(4, 1\right), \left(1, -\dfrac{1}{2}\right)\right\}
$$
::::

::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/a.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er

$$
\mathcal{L} = \left\{\left(4, 1\right), \left(1, -\dfrac{1}{2}\right)\right\}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::

\begin{align*}
2x^2 - 3x - y &= 2 \\
\\
2x - y &= -5
\end{align*}


::::{answer}
$$
\mathcal{L} = \left\{\left(-1, 3\right), \left(\dfrac{7}{2}, 12\right)\right\}
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/b.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er 

$$
\mathcal{L} = \left\{\left(-1, 3\right), \left(\dfrac{7}{2}, 12\right)\right\}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


\begin{align*}
-x^2 + y &= 2 \\
\\
x + 4y &= 8
\end{align*}


::::{answer}
$$
\mathcal{L} = \left\{\left(0, 2\right), \left(-\dfrac{1}{4}, \dfrac{33}{16}\right)\right\}
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/c.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er

$$
\mathcal{L} = \left\{\left(0, 2\right), \left(-\dfrac{1}{4}, \dfrac{33}{16}\right)\right\}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::


\begin{align*}
2x - y &= 3 \\
\\
x^2 - 3 &= y + 2x
\end{align*}


::::{answer}
$$
x = 0 \and y = -3 \or x = 4 \and y = 5.
$$
::::


::::{solution}
:::{figure} ./figurer/oppgaver/oppgave_4/d.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at løsningen av likningssystemet er 

$$
x = 0 \and y = -3 \or x = 4 \and y = 5.
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---

:::{margin} Tips: Oppgave 4
Det kan være lurt å løse likningene med hensyn på $y$ slik at du kan gjenkjenne likningene som funksjonsuttrykk. 
:::


:::::::::::::::{exercise} Oppgave 4
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 - 2x + y &= -2 \\
x - y &= 0
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/a/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur C. 
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 - 6x - y &= -5\\
x - y &= 5
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/b/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur A. 
::::


:::::::::::::



:::::::::::::{tab-item} c
Avgjør hvilken av figurene nedenfor du kan bruke til å løse likningssystemet 


\begin{align*}
x^2 + 2x + y &= 1 \\
x^2 - 4x - y &= 3
\end{align*}



Løs likningssystemet ved hjelp av riktig figur. 

:::{figure} ./figurer/oppgaver/oppgave_5/c/merged_figure.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
Figur D.
::::


:::::::::::::




::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/a.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::


:::::::::::::{tab-item} b
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/b.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::



:::::::::::::{tab-item} c
Lag et likningssystem du kan bruke figuren nedenfor til å løse

:::{figure} ./figurer/oppgaver/oppgave_6/c.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
Bruk CAS til å forutsi hva som skrives ut av programmene nedenfor.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 == 4*y and x - 2*y == -4:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 + 2*x - y == 3 and 6*x - y == 7:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 + y == 5 and 3*x + y == 7:
            print((x, y))


:::

:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å avgjøre hva som blir skrevet ut av programmet nedenfor.

Skriv inn svaret ditt og sjekk.


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x**2 - 3*y == 16 and x - y == 2:
            print((x, y))


:::

:::::::::::::



::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
Anna har skrevet et program for å løse et likningssystem. Programmet er vist nedenfor.

:::{code-block} python
---
linenos:
---
for x in range(-100, 101):
    for y in range(-100, 101):
        if x**2 + y**2 == 25 and x + y == 5:
            print((x, y))


:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{ggb-popup}
---
layout: sidebar
---
:::

Løs likningssystemet grafisk. 

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

Løs likningssystemet med CAS. 

:::::::::::::


:::::::::::::{tab-item} c
Løs likningssystemet algebraisk. 


:::::::::::::


::::::::::::::
:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 8
---
level: 3
---
:::{cas-popup}
---
layout: sidebar
---
:::


Et likningssystem er gitt ved 

\begin{align*}
-x^2 + y &= k
\\
4x + y &= 5
\end{align*}




::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a


Bestem $k$ slik at likningssystemet har nøyaktig én løsning.


::::{answer}
$$
k = 9
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
For hvilke verdier av $k$ har likningssystemet to løsninger? 


::::{answer}
$$
k > 9
$$
::::


:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
---
level: 3
---

:::{cas-popup}
---
layout: sidebar
---
:::


Et likningssystem er gitt ved 


\begin{align*}
x^2 + kx + y &= 0
\\
x + y &= 2
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $k$ slik at likningssystemet har nøyaktig én løsning.


::::{answer}
$$
k = -1 \or k = 3.
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
For hvilke verdier av $k$ vil likningsystemet ikke ha noen løsning?


::::{answer}
$$
k \in \langle \gets, -1 \rangle \cup \langle 3, \gets \rangle
$$
::::

:::::::::::::

::::::::::::::


:::::::::::::::

