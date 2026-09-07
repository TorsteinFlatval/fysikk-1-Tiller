# `if`{l=python}-`else`{l=python}-setninger

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke `if`{l=python}-setninger for å gjøre programmer som reagerer på ulike betingelser.
* Forstå hvordan sammenligningsoperatorer fungerer.
* Kunne kombinere flere betingelser i en `if`{l=python}-setning.
:::::

I programmering er det ofte nyttig å gjøre ulike ting avhengig av om noe er sant eller usant. For eksempel kanskje vi ønsker at et program skal skrive ut noe dersom et tall er større enn et annet tall, eller dersom en liste er tom. Dette er hvor `if`{l=python}-setninger er veldig nyttige. En `if`{l=python}-setning lar oss skrive kode som bare kjører dersom en bestemt betingelse er oppfylt.

## Sammenligningsoperatorer

For å kunne bruke `if`{l=python}-setninger må vi først forstå sammenligningsoperatorer. Disse brukes til å sammenligne to verdier og returnerer enten `True`{l=python} eller `False`{l=python}.

:::::::::::::::{summary} Sammenligningsoperatorer
Nedenfor ser du de viktigste sammenligningsoperatorene:

| Operator | Betydning | Eksempel | Resultat |
|----------|-----------|----------|---------|
| `==`{l=python} | Er lik | `5 == 5` | `True`{l=python} |
| `!=`{l=python} | Er ikke lik | `5 != 3` | `True`{l=python} |
| `<`{l=python} | Mindre enn | `3 < 5` | `True`{l=python} |
| `>`{l=python} | Større enn | `5 < 3` | `False`{l=python} |
| `<=`{l=python} | Mindre enn eller lik | `5 <= 5` | `True`{l=python} |
| `>=`{l=python} | Større enn eller lik | `5 >= 3` | `True`{l=python} |

:::::::::::::::

## Enkle `if`{l=python}-setninger

En enkel `if`{l=python}-setning har følgende struktur:

:::::::::::::::{summary} Syntaks for `if`{l=python}-setninger
:::{code-block} python
---
linenos:
---
if <betingelse>:
    # Kode som kjører dersom betingelsen er True
:::

Legg merke til at koden som skal kjøres dersom betingelsen er sann må være **innrykket** (indentert).
:::::::::::::::

:::::::::::::::{explore} Utforsk 1
La oss utforske hvordan `if`{l=python}-setninger fungerer.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
x = 10
if x > 5:
    print("x er større enn 5")
:::
:::::::::::::

:::::::::::::{tab-item} b
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
x = 3
if x > 5:
    print("x er større enn 5")
:::
:::::::::::::

:::::::::::::{tab-item} c
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
navn = "Anne"
if navn == "Anne":
    print("Hallo Anne!")
:::
:::::::::::::

::::::::::::::

:::::::::::::::

## `if`{l=python}-`else`{l=python}-setninger

Ofte ønsker vi å gjøre en ting dersom en betingelse er sann, og en annen ting dersom den er usann. For det bruker vi `else`{l=python}:

:::::::::::::::{summary} Syntaks for `if`{l=python}-`else`{l=python}
:::{code-block} python
---
linenos:
---
if <betingelse>:
    # Kode som kjører dersom betingelsen er True
else:
    # Kode som kjører dersom betingelsen er False
:::

::::::::::::::
:::::::::::::::{explore} Utforsk 2
La oss utforske `if`{l=python}-`else`{l=python}-setninger.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
x = 8
if x > 10:
    print("x er større enn 10")
else:
    print("x er ikke større enn 10")
:::
:::::::::::::
:::::::::::::{tab-item} b
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
alder = 15
if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")
:::
:::::::::::::

:::::::::::::{tab-item} c
Les programmet og prøv å forutsi hva som blir skrevet ut.

:::{interactive-code}
---
predict:
---
tall = 7
if tall % 2 == 0:
    print("Tallet er partall")
else:
    print("Tallet er oddetall")
:::
:::::::::::::

::::::::::::::

:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 1
Skriv kode som løser oppgavene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som sjekker om et tall `x` er negativt. Dersom det er negativt, skal programmet skrive ut "Tallet er negativt". Ellers skal det skrive ut "Tallet er ikke negativt".

:::{interactive-code}
x = -5
# FYLL INN DIN KODE HER
:::

:::::{answer}
Utskriften blir:

:::{code-block} console
Tallet er negativt
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
x = -5
if x < 0:
    print("Tallet er negativt")
else:
    print("Tallet er ikke negativt")
:::
:::::

:::::::::::::

:::::::::::::{tab-item} b
Lag et program som sjekker om et tall `x` er større enn eller lik 0. Dersom det er det, skal programmet skrive ut "Tallet er ikke-negativt". Ellers skal det skrive ut "Tallet er negativt".

:::{interactive-code}
x = 10
# FYLL INN DIN KODE HER
:::

:::::{answer}
Utskriften blir:

:::{code-block} console
Tallet er ikke-negativt
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
x = 10
if x >= 0:
    print("Tallet er ikke-negativt")
else:
    print("Tallet er negativt")
:::
:::::

:::::::::::::

:::::::::::::{tab-item} c
Lag et program som sjekker om en variabel `navn` er lik "Bob". Dersom den er det, skal programmet skrive ut "Hallo Bob!". Ellers skal det skrive ut "Du er ikke Bob".

:::{interactive-code}
navn = "Alice"
# FYLL INN DIN KODE HER
:::

:::::{answer}
Utskriften blir:

:::{code-block} console
Du er ikke Bob
:::
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
navn = "Alice"
if navn == "Bob":
    print("Hallo Bob!")
else:
    print("Du er ikke Bob")
:::
:::::

:::::::::::::

::::::::::::::
:::::::::::::::
