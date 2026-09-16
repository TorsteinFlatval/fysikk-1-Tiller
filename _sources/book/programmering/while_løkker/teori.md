# `while`{l=python}-løkker

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage programmer som bruker `while`{l=python}-løkker
* Forstå når det er passende å bruke `while`{l=python}-løkker i stedet for `for`{l=python}-løkker
:::::

## `while`{l=python}-løkker

:::{margin}
Tidligere lærte vi om `for`{l=python}-løkker. En `while`{l=python}-løkke fungerer annerledes og er nyttig når vi ikke vet på forhånd hvor mange ganger løkken skal kjøres.
:::

En `while`{l=python}-løkke lar oss gjenta en kodeblokk så lenge en bestemt betingelse er sann. Dette er nyttig når vi ikke vet på forhånd hvor mange ganger koden skal gjentas, eller når vi ønsker å stoppe løkken basert på en spesifikk betingelse.

:::::::::::::::{summary} `while`{l=python}-løkker
En `while`{l=python}-løkke som skal gjenta en kodeblokk så lenge en betingelse er sann kan skrives slik:

:::{code-block} python
---
linenos:
---
while betingelse:
    # Kode som skal gjentas står her
:::

Løkken stopper når betingelsen blir usann. Det er **viktig** at koden inni løkken endrer noe som gjør at betingelsen til slutt blir usann, ellers blir det en uendelig løkke!
:::::::::::::::

Nedenfor i Utforsk 1 kan du utforske nærmere hvordan en `while`{l=python}-løkke fungerer.

:::{margin} Initieliseringsvariabel
I Utforsk 1 vil du se at vi må sette en variabel før `while`{l=python}-løkken starter. Denne kalles ofte for en *initieliseringsvariabel*. Inni løkken øker vi verdien av variabelen slik at betingelsen etter hvert blir usann.
:::

:::::::::::::::{example} Eksempel 1: En enkel `while`{l=python}-løkke
La oss se på et lite eksempel:

:::{code-block} python
---
linenos:
---
n = 1
while n < 4:
    print(n)
    n = n + 1
:::

Dette programmet skriver ut:
```text
1
2
3
```

Løkken starter med `n = 1`{l=python} og fortsetter så lenge `n < 4`{l=python} er sant. For hver runde øker vi `n`{l=python} med `1`{l=python}, og når `n`{l=python} blir `4`{l=python}, stopper løkken fordi betingelsen ikke lenger er sann.
:::::::::::::::

:::::::::::::::{explore} Utforsk 1
Nedenfor vises noen programmer som bruker `while`{l=python}-løkker til å skrive ut noen tall.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!

:::{interactive-code}
---
predict:
---
n = 1
while n <= 5:
    print(n)
    n = n + 1
:::
:::::::::::::

:::::::::::::{tab-item} b
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!

:::{interactive-code}
---
predict:
---
n = 2
while n <= 10:
    print(n)
    n = n + 2
:::
:::::::::::::

:::::::::::::{tab-item} c
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!

:::{interactive-code}
---
predict:
---
n = 10
while n > 0:
    print(n)
    n = n - 1
:::
:::::::::::::

::::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen!

:::{quiz}
Q: Hvilke tall skrives ut av programmet nedenfor?  <pre><code class="python">n = 1\nwhile n < 4:\n    print(n)\n    n = n + 1</code></pre>
+ 1, 2, 3
- 1, 2, 3, 4
- 1, 4
- 2, 3


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 0\nwhile n <= 5:\n    print(n)\n    n = n + 1</code></pre>
+ 0, 1, 2, 3, 4, 5
- 0, 1, 2, 3, 4, 5, 6
- 0, 5
- 1, 2, 3, 4, 5


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1</code></pre>
+ 5, 4, 3, 2, 1
- 5, 4, 3, 2, 1, 0
- 5, 1
- 4, 3, 2, 1


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 2\nwhile n < 10:\n    print(n)\n    n = n + 2</code></pre>
+ 2, 4, 6, 8
- 2, 4, 6, 8, 10
- 2, 10
- 2, 4, 6

:::
:::::::::::::::

---

### Sammenligning av `for`{l=python}- og `while`{l=python}-løkker

Både `for`{l=python}- og `while`{l=python}-løkker kan gjenta kode flere ganger, men de brukes i ulike situasjoner:

- **`for`{l=python}-løkker** brukes når vi vet på forhånd hvor mange ganger koden skal gjentas
- **`while`{l=python}-løkker** brukes når vi ikke vet på forhånd hvor mange ganger koden skal gjentas, eller når vi ønsker å stoppe basert på en betingelse

:::::::::::::::{exercise} Underveisoppgave 2
:::{quiz}
Q: Hvilket program skriver ut den samme tallfølgen? <pre><code class="python">for n in range(1, 6):\n    print(n)</code></pre>
+ <pre><code class="python">n = 1\nwhile n < 6:\n    print(n)\n    n = n + 1</code></pre>
- <pre><code class="python">n = 1\nwhile n <= 6:\n    print(n)\n    n = n + 1</code></pre>
- <pre><code class="python">n = 1\nwhile n < 5:\n    print(n)\n    n = n + 1</code></pre>
- <pre><code class="python">n = 0\nwhile n < 6:\n    print(n)\n    n = n + 1</code></pre>

Q: Hvilket program vil kjøre uendelig (eller til det er stoppet)?
+ <pre><code class="python">n = 1\nwhile n > 0:\n    print(n)\n    n = n + 1</code></pre>
- <pre><code class="python">n = 1\nwhile n < 10:\n    print(n)\n    n = n + 1</code></pre>
- <pre><code class="python">n = 10\nwhile n > 0:\n    print(n)\n    n = n - 1</code></pre>
- <pre><code class="python">n = 1\nwhile n <= 5:\n    print(n)\n    n = n + 1</code></pre>

Q: Hvilket av disse programmene kan brukes til å finne hvor mange ganger du må legge til 2 til 1 før du kommer over 100?
+ <pre><code class="python">n = 1\ncount = 0\nwhile n <= 100:\n    n = n + 2\n    count = count + 1\nprint(count)</code></pre>
- <pre><code class="python">for n in range(1, 100, 2):\n    count = 0\n    count = count + 1</code></pre>
- <pre><code class="python">n = 1\nwhile n < 100:\n    print(n)</code></pre>
- <pre><code class="python">for n in range(1, 100, 2):\n    print(n)</code></pre>

:::
:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 3
Nedenfor finner du interaktive kodevinduer du kan skrive kode i og kjøre direkte.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut partallene fra og med $2$ til og med $20$.

:::{interactive-code}
# Skriv ditt program her



:::

:::::{answer}
Utskriften blir:

:::{code-block} console
2
4
6
8
10
12
14
16
18
20
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
n = 2
while n <= 20:
    print(n)
    n = n + 2
:::
:::::

:::::::::::::

:::::::::::::{tab-item} b
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut oddetallene fra og med $1$ til og med $19$.

:::{interactive-code}
# Skriv ditt program her



:::

:::::{answer}
Utskriften blir:

:::{code-block} console
1
3
5
7
9
11
13
15
17
19
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
n = 1
while n <= 19:
    print(n)
    n = n + 2
:::
:::::

:::::::::::::

:::::::::::::{tab-item} c
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut tallfølgen fra $10$ ned til $1$.

:::{interactive-code}
# Skriv ditt program her



:::

:::::{answer}
Utskriften blir:

:::{code-block} console
10
9
8
7
6
5
4
3
2
1
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
n = 10
while n >= 1:
    print(n)
    n = n - 1
:::
:::::

:::::::::::::

::::::::::::::
:::::::::::::::
