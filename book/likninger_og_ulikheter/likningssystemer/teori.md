# Likningssystemer


:::{goals} Læringsmål
* Kunne løse likningssystemer grafisk, algebraisk og med programmering. 
:::

I dette kapittelet skal vi lær eå løse likningsystemer med digitale verktøy. Vi skal begrense oss til likningssystemer der vi har lineære eller kvadratiske potenser for de ukjente. 


Vi kan køse likningssystemer med tre forskjellige strategier:
1. **Grafisk**
2. **Algebraisk** 
3. **Med programmering**

(grafisk-løsning)=
## Grafisk løsning
Når vi løser et ikke-lineært likningssystem grafisk, tegner vi grafene som svarer til likningene og finner skjæringspunktene mellom dem. Hvert skjæringspunkt representerer en løsning på likningssystemet. 

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 1
Et likningssystem er gitt ved 

\begin{align*}
x^2 + y &= 3 \\
x - y &= 3
\end{align*}

::::{solution}
---
dropdown: 0
---
Den første likningen representerer en andregradsfunksjon som vi kan se ved å løse likningen for $y$:

$$
x^2 + y = 3 \liff y = 3 - x^2
$$

Den andre likningen representerer en lineær funksjon som vi kan se ved å løse likningen for $y$:

$$
x - y = 3 \liff y = x - 3
$$

Vi tegner grafene til hver av likningene og leser av skjæringspunktene for å bestemme løsningene: 

:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi ser at grafene skjærer hverandre i punktene $(2, -1)$ og $(-3, -6)$. For å beskrive løsningen, skriver vi:

$$
\mathcal{L} = \{(2, -1), (-3, -6)\}
$$

Vi kan også skrive dette med logiske symboler:

$$
x = 2 \quad \underbrace{\land}_{\text{og samtidig}}  \quad  y = -1  \quad  \overbrace{\lor}^{\text{eller}}  \quad  x = -3 \quad \underbrace{\land}_{\text{og samtidig}}  \quad y = -6
$$

Uten annoteringer, skriver vi altså bare:

$$
x = 2 \and y = -1 \quad \lor \quad x = -3 \and y = -6
$$

Vi tolker dette som at enten så er $x = 2$ og samtidig er $y = -1$. Eller så er $x = -3$ og samtidig er $y = -6$.


::::


:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Et likningssystem er gitt ved

\begin{align*}
x^2 + y &= 1 \\
x + y &= -1
\end{align*}

Grafene til de to likningene er vist i figuren nedenfor.

Bruk figuren til å løse likningssystemet.

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::{answer}
$$
\mathcal{L} = \{(-1, 0), (-3, 2)\}
$$
::::


::::{solution}
Grafene skjærer hverandre i punktene $(-1, 0)$ og $(-3, 2)$. Løsningen av likningssystemet er derfor 

$$
\mathcal{L} = \{(-1, 0), (-3, 2)\}
$$
::::






:::::::::::::::


---

I praksis kan vi bruke graftegner til å tegne grafene og finne skjæringspunktene. La oss se på et eksempel. 


:::::::::::::::{example} Eksempel 2
Et likningssystem er gitt ved 

\begin{align*}
    2x - y &= 3 \\
    x^2 - 2x - y &= 3
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



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
Et likningssystem er gitt ved 

\begin{align*}
    2x - y &= 1 \\
    -x^2 + 3x + y &= 3
\end{align*}

Bruk Geogebra-vinduet nedenfor til å løse likningssystemet grafisk.

:::{ggb}
:::


::::{answer}
$$
\mathcal{L} = \{(1, 1), (4, 7)\}
$$
::::

::::{solution}
Vi skriver inn likningene i algebrafeltet og trykker først på {ggb-icon}`mode_point` for å få opp alternativer og deretter trykker på {ggb-icon}`mode_intersect` (Skjæring mellom to objekt) etterfulgt av å trykke på hver graf for å finne skjæringspunktene. Se figuren nedenfor. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/sol.png
---
class: no-click, adaptive-figure
width: 90%
---
:::

Skjæringspunktene er $(1, 1)$ og $(4, 7)$ som betyr at løsningen av likningsystemet er

$$
\mathcal{L} = \{(1, 1), (4, 7)\}
$$


::::


:::::::::::::::



## Algebraisk løsning 
Når vi løser et ikke-lineært likningssystem algebraisk, bruker vi oftest innsettingsmetoden som leder til en andregradslikning. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 3
Løs likningssystemet 

\begin{align*}
x^2 + y &= 3 \\
x - y &= 3
\end{align*}


::::{solution}
---
dropdown: 0
---
Vi starter med å løse likning 2 for $y$:

$$
x - y = 3 \liff y = x - 3
$$

deretter setter vi inn dette for $y$ i likning 1:

$$
x^2 + (x - 3) = 3 \liff x^2 + x - 6 = 0
$$

Deretter kan vi bruke $abc$-formelen for å løse likningen:

$$
x = \dfrac{-1 \pm \sqrt{1^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1} = \dfrac{-1 \pm \sqrt{25}}{2} = \dfrac{-1 \pm 5}{2}
$$

som gir oss løsningene

$$
x = -3 \or x = 2. 
$$

For hver verdi av $x$ får vi en verdi for $y$. Vi bruker at $y = x - 3$ og setter inn verdiene for $x$. Når $x = -3$, så får vi 

$$
y = -3 - 3 = -6
$$

Når $x = 2$, så får vi 

$$
y = 2 - 3 = -1
$$

Dermed er løsningen av likningssystemet

$$
\mathcal{L} = \{(-3, -6), (2, -1)\}
$$
::::

:::::::::::::::


### CAS
Vi kan bruke CAS til å løse ikke-lineære likningssystemer på samme måte som vi gjorde med lineære likningssystemer. Det skal du se nærmere på i Utforsk 1.


:::::::::::::::{explore} Utforsk 1
I gif-en nedenfor vises det hvordan vi kan bruke CAS til å løse et ikke-lineært likningssystem.

:::{figure} ./cas_likningssystemer.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::


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

Bruk CAS til å løse likningssystemet som er vist i gif-en.

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å løse likningssystemet

\begin{align*}
    x - y &= 1\\
    \\
    -x^2 + 4x + y &= 3
\end{align*}

:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS til å løse likningssystemet

\begin{align*}
    -x^2 + 5x - y &= 6\\
    \\
    x + 2y &= -7
\end{align*}


:::::::::::::


::::::::::::::


:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
Løs likningssystemet nedenfor med CAS.

\begin{align*}
2x - y &= 4 \\
x^2 - 3x - 2y &= -4
\end{align*}

:::{cas-popup}
---
layout: sidebar
---
:::

::::{answer}
$$
\mathcal{L} = \{(4, 4), (3, 2)\}
$$
::::


::::{solution}
Vi løser likning 1 for $y$:

$$
2x - y = 4 \liff y = 2x - 4
$$

Deretter setter vi inn dette for $y$ i likning 2:

$$
x^2 - 3x - 2(2x - 4) = -4 
$$

Så forenkler vi likningen så mye som mulig:

\begin{align*}
x^2 - 3x - 4x + 8 &= -4 \\
\\
x^2 - 7x + 12 &= 0 \\
\\
\end{align*}

Nå kan vi bruke $abc$-formelen for å bestemme verdiene for $x$:

$$
x = \dfrac{-(-7) \pm \sqrt{(-7)^2 - 4 \cdot 1 \cdot 12}}{2 \cdot 1} = \dfrac{7 \pm \sqrt{49 - 48}}{2} = \dfrac{7 \pm 1}{2}
$$

Det gir oss løsningene

$$
x = 4 \or x = 3
$$

For hver verdi av $x$ får vi en verdi for $y$. Vi bruker at $y = 2x - 4$ og setter inn verdiene for $x$. Når $x = 4$, så får vi

$$
y = 2 \cdot 4 - 4 = 8 - 4 = 4
$$

Når $x = 3$, så får vi 

$$
y = 2 \cdot 3 - 4 = 6 - 4 = 2
$$

Dermed er løsningen av likningssystemet

$$
\mathcal{L} = \{(4, 4), (3, 2)\}
$$



::::

:::::::::::::::

(løsning-med-programmering)=
## Løsning med programmering
Når vi løser en ikke-lineært likningssystem med programmering, kan vi bruke systematisk prøve ut punkter $(x, y)$ og sjekke om de oppfyller likningene i systemet. 


:::::::::::::::{explore} Utforsk 2


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


Nedenfor vises et program som løser et likningssystem. 

Bruk CAS til å forutsi utskriften til programmet og kjør det for å sjekke svaret ditt. 
:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet og bruk det til å løse likningssystemet

\begin{align*}
2x + y &= 5 \\
\\
x^2 - 2x + 3y &= 3
\end{align*}


::::{solution}
:::{code-block} python
---
linenos:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if 2*x + y == 5 and x**2 - 2*x + 3*y == 3:
            print((x, y))


:::

som gir utskriften

:::{code-block} console 
(2, 1)
(6, -7)
:::

som betyr at løsningen av likningessystemet er 

$$
\mathcal{L} = \{(2, 1), (6, -7)\}
$$

::::

:::::::::::::


::::::::::::::


:::{interactive-code}
---
predict:
---
for x in range(-10, 11):
    for y in range(-10, 11):
        if x - y == 1 and x**2 - 3*x + y == 2:
            print((x, y))

 
:::



:::::::::::::::