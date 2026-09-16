# Oppgaver: `while`{l=python}-løkker


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Ta quizen!

:::{quiz}
Q: Hvilke tall skrives ut av programmet nedenfor?  <pre><code class="python">n = 1\nwhile n < 5:\n    print(n)\n    n = n + 1</code></pre>
+ 1, 2, 3, 4
- 1, 2, 3, 4, 5
- 1, 5
- 2, 3, 4


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 3\nwhile n <= 7:\n    print(n)\n    n = n + 1</code></pre>
+ 3, 4, 5, 6, 7
- 3, 4, 5, 6
- 3, 7
- 4, 5, 6, 7


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 10\nwhile n > 5:\n    print(n)\n    n = n - 1</code></pre>
+ 10, 9, 8, 7, 6
- 10, 9, 8, 7, 6, 5
- 10, 5
- 9, 8, 7, 6, 5


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 0\nwhile n < 8:\n    print(n)\n    n = n + 2</code></pre>
+ 0, 2, 4, 6
- 0, 2, 4, 6, 8
- 0, 8
- 2, 4, 6, 8


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">n = 1\nwhile n <= 10:\n    print(n)\n    n = n + 3</code></pre>
+ 1, 4, 7, 10
- 1, 4, 7, 10, 13
- 1, 3, 10
- 1, 10, 3

:::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Nedenfor vises noen programkoder som skriver ut noen tall. Les programmene og prøv å forutsi hvilke tall de skriver ut.

Skriv inn gjetningen din og sjekk svaret ditt for hvert av programmene.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{interactive-code}
---
predict:
---
n = 0
while n < 4:
    print(n)
    n = n + 1
:::
:::::::::::::

:::::::::::::{tab-item} b
:::{interactive-code}
---
predict:
---
n = 5
while n > 0:
    print(n)
    n = n - 1
:::
:::::::::::::

:::::::::::::{tab-item} c
:::{interactive-code}
---
predict:
---
n = 1
while n <= 10:
    print(n)
    n = n + 2
:::
:::::::::::::

:::::::::::::{tab-item} d
:::{interactive-code}
---
predict:
---
n = 20
while n > 0:
    print(n)
    n = n - 5
:::
:::::::::::::

::::::::::::::

:::::::::::::::


:::::::::::::::{exercise} Oppgave 3
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut alle tallene fra 1 til 8.

:::{interactive-code}
n = ????
while n <= ????: # FYLL INN
    print(n)
    n = n + 1

:::


::::{answer}
Utskrift:

```text
1
2
3
4
5
6
7
8
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 1
while n <= 8:
    print(n)
    n = n + 1
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
2, 4, 6, 8.
$$

:::{interactive-code}
n = ????
while n <= ????: # FYLL INN
    print(n)
    n = n + ????


:::


::::{answer}
Utskrift:

```text
2
4
6
8
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 2
while n <= 8:
    print(n)
    n = n + 2
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
1, 5, 9, 13.
$$


:::{interactive-code}
n = ????
while n <= ????: # FYLL INN
    print(n)
    n = n + ????


:::


::::{answer}
Utskrift:

```text
1
5
9
13
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 1
while n <= 13:
    print(n)
    n = n + 4
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
20, 16, 12, 8, 4.
$$

:::{interactive-code}
n = ????
while n >= ????: # FYLL INN
    print(n)
    n = n - ????


:::


::::{answer}
Utskrift:

```text
20
16
12
8
4
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 20
while n >= 4:
    print(n)
    n = n - 4
:::
::::

:::::::::::::

::::::::::::::

:::::::::::::::


:::::::::::::::{exercise} Oppgave 4
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som bruker en `while`{l=python}-løkke og skriver ut tallfølgen

$$
10, 6, 2
$$

:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
Utskrift:

```text
10
6
2
```
:::::

:::::{solution}
:::{code-block} python
n = 10
while n >= 2:
    print(n)
    n = n - 4
:::
:::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som bruker en `while`{l=python}-løkke og skriver ut tallfølgen

$$
100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0
$$

:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
Utskrift:

```text
100
90
80
70
60
50
40
30
20
10
0
```
:::::

:::::{solution}
:::{code-block} python
n = 100
while n >= 0:
    print(n)
    n = n - 10
:::
:::::

:::::::::::::


:::::::::::::{tab-item} c
Lag et program som bruker en `while`{l=python}-løkke og skriver ut tallfølgen

$$
5, 3, 1, -1, -3, -5
$$

:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
Utskrift:

```text
5
3
1
-1
-3
-5
```
:::::

:::::{solution}
:::{code-block} python
n = 5
while n >= -5:
    print(n)
    n = n - 2
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som bruker en `while`{l=python}-løkke og skriver ut tallfølgen

$$
-2, -5, -8, -11, -14
$$

:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
Utskrift:

```text
-2
-5
-8
-11
-14
```
:::::

:::::{solution}
:::{code-block} python
n = -2
while n >= -14:
    print(n)
    n = n - 3
:::
:::::

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
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut alle partallene til og med 20. 


:::{interactive-code}
# Skriv ditt program her




:::


::::{answer}
Utskrift:

```text
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
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 2
while n <= 20:
    print(n)
    n = n + 2
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut alle oddetallene til og med 21. 


:::{interactive-code}
# Skriv ditt program her




:::


::::{answer}
Utskrift:

```text
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
21
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
n = 1
while n <= 21:
    print(n)
    n = n + 2
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut de 15 første partallene.


:::{interactive-code}
# Skriv ditt program her




:::



:::::{answer}
Utskrift:

```text
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
22
24
26
28
30
```
:::::

:::::{solution}
:::{code-block} python
n = 1
count = 0
while count < 15:
    partall = 2 * n
    print(partall)
    n = n + 1
    count = count + 1
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som bruker en `while`{l=python}-løkke til å skrive ut de 15 første oddetallene.


:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
Utskrift:

```text
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
21
23
25
27
29
```
:::::

:::::{solution}
:::{code-block} python
n = 1
count = 0
while count < 15:
    oddetall = 2 * n - 1
    print(oddetall)
    n = n + 1
    count = count + 1
:::
:::::

:::::::::::::

::::::::::::::

:::::::::::::::
