# Oppgaver: Programmering av tallfølger


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Ta quizen! 

:::{quiz}
Q: Hvilke tall skrives ut av programmet nedenfor?  <pre><code class="python">for n in range(-2, 3):\n    print(n)</code></pre>
+ $-2, -1, 0, 1, 2$
- $-2, 3$
- $-2, -1, 0, 1, 2, 3$
- $-2, 1, 3$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(4):\n    print(n)</code></pre>
+ $0, 1, 2, 3$
- $0, 1, 2, 3, 4$
- $4$
- $1, 2, 3, 4$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(-2, 2, 1):\n    print(n)</code></pre>
+ $-2, -1, 0, 1$
- $-2, 2, 1$
- $-2, -1, 0, 1, 2$
- $-1, 0, 1, 2$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(1, 6, 2):\n    print(n)</code></pre>
+ $1, 3, 5$
- $1, 6, 2$
- $1, 2, 6$
- $1, 3, 5, 6$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(1, 10, 3):\n    print(n)</code></pre>
+ $1, 4, 7$
- $1, 4, 7, 10$
- $1, 3, 10$
- $1, 10, 3$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(0, 101, 10):\n    print(n)</code></pre>
+ $0, 10, 20, \ldots, 90, 100$
- $0, 10, 20, \ldots, 90$
- $0, 101, 10$
- $0, 10, 100$
:::
::::::::::::::


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
for n in range(3):
    print(n)
:::
:::::::::::::

:::::::::::::{tab-item} b
:::{interactive-code}
---
predict:
---
for n in range(-4, 1):
    print(n)
:::
:::::::::::::

:::::::::::::{tab-item} c
:::{interactive-code}
---
predict:
---
for n in range(-10, 11, 4):
    print(n)
:::
:::::::::::::

:::::::::::::{tab-item} d
:::{interactive-code}
---
predict:
---
for n in range(10, 1, -2):
    print(n)
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
Fyll ut programmet nedenfor slik at det skriver ut alle tallfølgen

$$
1, 2, 3, 4, 5, 6, 7, 8.
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


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
for n in range(1, 9):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
2, 4, 6, 8.
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


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
for n in range(2, 10, 2):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
1, 5, 9, 13. 
$$


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


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
for n in range(1, 14, 4):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
-5, -3, -1, 1, 3, 5. 
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


:::


::::{answer}
Utskrift:

```text
-5
-3
-1
1
3
5
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
for n in range(-5, 6, 2):
    print(n)
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
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
10, 6, 2
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


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
for n in range(10, 1, -4):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


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
for n in range(100, -1, -10):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
5, 3, 1, -1, -3, -5
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


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
for n in range(5, -6, -2):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
-2, -5, -8, -11, -14
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


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
for n in range(-2, -15, -3):
    print(n)
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
Fyll ut programmet nedenfor slik at det skriver ut alle partallene til og med $20$. 


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    print(n)


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
for n in range(2, 21, 2):
    print(n)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut alle oddetallene til og med $21$. 


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    print(n)


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
for n in range(1, 22, 2):
    print(n)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag et program som skriver ut de $20$ **første** partallene.


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
32
34
36
38
40
```
:::::

:::::{solution}
:::{code-block} python
for n in range(1, 21):
    partall = 2 * n
    print(partall)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som skriver ut de $20$ **første** oddetallene.


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
31
33
35
37
39
```
:::::

:::::{solution}
:::{code-block} python
for n in range(1, 21):
    oddetall = 2 * n - 1
    print(oddetall)
:::
:::::

:::::::::::::

::::::::::::::


:::::::::::::::