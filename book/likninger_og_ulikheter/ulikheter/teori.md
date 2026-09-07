# Andregradsulikheter

:::{goals} Læringsmål
* Kunne beskrive mengder som består av flere intervaller. 
* Kunne tolke og tegne fortegnslinjer for andregradsfunksjoner.
* Kunne løse andregradsulikheter grafisk og algebraisk. 
:::


Andregradsulikheter er ulikheter der vi lurer på når en andregradsfunksjon er større enn eller mindre enn null. Som når vi jobbet med lineære ulikheter, så hadde vi to strategier vi kunne bruke for å løse ulikhetene: 

1. **Grafisk**
2. **Algebraisk**
    * Ved regning
    * Med CAS

(grafisk-løsning-ulikheter)=
## Grafisk løsning
Å løse en andregradsulikhet grafisk er ganske likt det vi gjorde med lineære ulikheter. Vi tegner grafen til funksjonen og så leser vi av hvor grafen oppfyller ulikheten. 

La oss se på et eksempel: 


:::::::::::::::{example} Eksempel 1
Løs ulikheten

$$
x^2 - 4x + 3 < 0
$$


::::{solution}
---
dropdown: 0
---
Vi tegner grafen til $f(x) = x^2 - 4x + 3$ og ser hvor $y$-koordinaten til grafen er mindre enn null:


:::{figure} ./figurer/eksempler/eksempel_1/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::

Fra grafen til $f$ ser vi at $f(x) < 0$ når 

$$
\mathcal{L} = \langle 1, 3 \rangle
$$



::::

:::::::::::::::


La oss se på et eksempel til der vi trenger en ny måte å beskrive løsningen på:


:::::::::::::::{example} Eksempel 2
Løs ulikheten

$$
x^2 - x - 4 \geq 2
$$

::::{solution}
---
dropdown: 0
---
Vi tegner grafen til $f(x) = x^2 - x - 2$ og ser hvor $y$-koordinaten til grafen er større enn eller lik $y = 2$: 

::::{figure} ./figurer/eksempler/eksempel_2/figur.svg
---
class: no-click, adaptive-figure
width: 80%
---
::::

Fra grafen til $f$ ser vi at $f(x) \geq 2$ når $x \leq -2$ eller når $x \geq 3$. Løsningen er derfor satt sammen av to intervaller. Det ene intervallet er $\langle \gets, -2]$ og det andre er $[3, \to \rangle$. For å sette sammen disse to plasserer vi symbolet $\cup$ mellom dem: 

$$
\mathcal{L} = \langle \gets, -2] \cup [3, \to \rangle
$$

Vi leser det som at $x$ er enten i det første intervallet, eller i det andre. 

::::

:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 1
Grafen til en andregradsfunksjon $f(x) = x^2 - 2x - 8$ er vist i figuren nedenfor. 

Bruk grafen til å løse ulikheten

$$
x^2 - 2x - 10 \geq -2
$$


:::{plot}
width: 70%
function: x**2 - 2*x - 10, f
ymin: -12
ystep: 2
:::



::::{answer}
$$
\mathcal{L} = \langle \gets, -2] \cup [4, \to \rangle
$$
::::


::::{solution}
Vi ser fra grafen at $f(x) \geq -2$ når $x \leq -2$ eller når $x \geq 4$. Løsningen er derfor

$$
\mathcal{L} = \langle \gets, -2] \cup [4, \to \rangle
$$
::::

:::::::::::::::


(algebraisk-løsning-ulikheter)=
## Algebraisk løsning
Å løse en andregradsulikhet algebraisk skiller seg en del fra hvordan vi løste lineære ulikheter. Her får vi ikke isolert $x$ på samme måte som vi kunne gjøre med lineære ulikheter. I stedet må vi bruke en annen strategi. Strategien kan oppsummeres som:

1. Flytt alle ledd over på én side av ulikheten slik at høyre side blir null.
2. Skriv uttrykket på venstre side på nullpunktsform.
3. Tegn en **fortegnslinje** for andregradsfunksjonen på venstre side og les av løsningen som oppfyller ulikheten. 


La oss først se på hvordan vi leser og tegner et fortegnsskjema.

:::::::::::::::{summary} Fortegnslinjer

En **fortegnslinje** er en linje som viser fortegnet til en funksjon på et intervall. Vi bruker **heltrukne** og **stiplede** linjer for å skille mellom fortegnene:

* <span style="display:inline-block; width:100px; border-bottom: 3px solid red; vertical-align:middle;"></span> $=$ Positivt fortegn
* <span style="display:inline-block; width:100px; border-bottom: 3px dashed royalblue; vertical-align:middle;"></span> $=$ Negativt fortegn
* Vi markerer med $0$ ved nullpunktene $x_1$ og $x_2$ til funksjonen. 


:::{figure} ./figurer/teori/fortegnslinjer.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


:::::::::::::::


La oss se på et eksempel: 

:::::::::::::::{example} Eksempel 3
Nedenfor vises fortegnslinja til en andregradsfunksjon $f$ som har nullpunkter $x = -2$ og $x = 3$.

Bruk fortegnslinja til å løse ulikheten 

$$
f(x) < 0
$$


:::{figure} ./figurer/eksempler/eksempel_3/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{solution}
---
dropdown: 0
---
Siden vi skal bestemme når $f(x) < 0$, så må vi se hvor fortegnslinja er **stiplet**. Fra fortegnslinja ser vi at $f(x) < 0$ når $x < -2$ eller når $x > 3$. Løsningen er derfor

$$
\mathcal{L} = \langle \gets, -2 \rangle \cup \langle 3, \to \rangle
$$
::::


:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 2
Nedenfor vises fortegnslinja til en andregradsfunksjon $f$. 

Bruk fortegnslinja til å løse ulikheten $f(x) \geq 0$. 

:::{figure} ./figurer/underveisoppgaver/underveisoppgave_2/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::{answer}
$$
\mathcal{L} = \langle \gets, -1] \cup [2, \to \rangle
$$
::::


::::{solution}
For å løse ulikheten $f(x) \geq 0$ må vi se hvor fortegnslinja er **heltrukket** eller **lik null**. Fra fortegnslinja ser vi at $f(x) \geq 0$ når $x \leq -1$ eller når $x \geq 2$. Løsningen er derfor

$$
\mathcal{L} = \langle \gets, -1] \cup [2, \to \rangle
$$
::::

:::::::::::::::


---


Nå er vi klare for å se hvordan vi kan løse andregradsulikheter algebraisk. La oss se på et eksempel:


:::::::::::::::{example} Eksempel 4
Løs ulikheten 

$$
-x^2 - 2x + 1 > -2
$$


::::{solution}
---
dropdown: 0
---
Vi starter med å samle alle leddene på én side slik at vi får $0$ på høyre side:

$$
-x^2 -2x + 1 > - 2 \liff -x^2 -2x + 1 + 2 > 0 \liff -x^2 -2x + 3 > 0
$$

Deretter må vi bestemme nullpunktene til funksjonen $f(x) = -x^2 - 2x + 3$ som vi kan gjøre med $abc$-formelen: 

$$
x =\frac{-(-2) \pm \sqrt{(-2)^2 - 4\cdot(-1)\cdot3}}{2\cdot(-1)} = \frac{2 \pm \sqrt{4 + 12}}{-2} = \frac{2 \pm 4}{-2}
$$

som gir 

$$
x = \frac{6}{-2} = -3 \or x = \frac{-2}{-2} = 1
$$

Dermed kan vi skrive om ulikheten til 

$$
-1 \cdot(x + 3)(x - 1) > 0
$$

Så tegner vi en fortegnslinje for hver av faktorene i andregradsuttrykket. Får å få fortegnslinja til $f(x)$, ganger vi fortegnet til hver faktor sammen og ser hvilken fortegn vi får. Se figuren nedenfor:

:::{figure} ./figurer/eksempler/eksempel_4/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


Fra fortegnslinja til $f(x)$, kan vi se at $f(x) > 0$ når $-3 < x < 1$. Løsningen er derfor

$$
\mathcal{L} = \langle -3, 1 \rangle
$$


::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
Løs ulikheten 

$$
x^2 + x - 8 < 4
$$


::::{answer}
$$
\mathcal{L} = \langle -4, 3 \rangle
$$
::::

::::{solution}
Vi starter med å samle alle leddene på én side slik at vi får $0$ på høyre side:

$$
x^2 + x - 8 < 4 \liff x^2 + x - 8 - 4 < 0 \liff x^2 + x - 12 < 0
$$

Deretter må vi bestemme nullpunktene til funksjonen $f(x) = x^2 + x - 12$ som vi kan gjøre med $abc$-formelen:

$$
x = \frac{-1 \pm \sqrt{1^2 - 4\cdot1\cdot(-12)}}{2\cdot1} = \frac{-1 \pm \sqrt{1 + 48}}{2} = \frac{-1 \pm 7}{2}
$$

som gir 

$$
x = \frac{6}{2} = 3 \or x = \frac{-8}{2} = -4
$$

Dermed kan vi skrive om ulikheten til

$$
(x + 4)(x - 3) < 0
$$

Nå tegner vi en fortegnslinje for hver av faktorene i andregradsuttrykket. Får å få fortegnslinja til $f(x) = (x + 4)(x - 3)$, ganger vi fortegnet til hver faktor sammen og ser hvilket fortegn vi får. Se figuren nedenfor:


:::{figure} ./figurer/underveisoppgaver/underveisoppgave_3/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::

Fra figuren kan vi se at $f(x) < 0$ når $-4 < x < 3$. Løsningen er derfor

$$
\mathcal{L} = \langle -4, 3 \rangle
$$



::::

:::::::::::::::






### CAS
Vi kan også løse ulikheten algebraisk med CAS. Det skal du se nærmere på Utforsk 1. 


:::::::::::::::{explore} Utforsk 1
I gif-en nedenfor vises det hvordan man løser en andregradsulikhet med CAS.

:::{figure} ./videoer/cas_ulikheter.gif
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

Bruk CAS til å løse ulikheten som løses i gif-en ovenfor. 



:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å løse ulikheten 

$$
x^2 - 4x + 3 < 0
$$


:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bruk CAS til å løse ulikheten

$$
-x^2 + 3x + 2 \geq 0
$$

:::::::::::::


::::::::::::::


:::::::::::::::




