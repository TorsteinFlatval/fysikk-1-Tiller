# Likninger med programmering

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke programmering til å løse likninger
* Kunne systematisk teste ulike verdier i en likning
* Kunne kombinere `for`{l=python}-løkker og `if`{l=python}-setninger for å finne heltallsløsninger
* Kunne bruke `while`{l=python}-løkker til å teste desimalverdier
:::::

I programmering kan vi løse likninger ved å teste mange verdier systematisk. I stedet for å løse algebraisk, lar vi datamaskinen teste alle mulige verdier i et område og finne hvilke som oppfyller likningen. 

**Viktig:** Denne metoden fungerer best når vi leter etter **heltallsløsninger**. Hvis løsningene ikke er heltall, vil programmet ikke finne dem når vi bare tester hele tall.

---

## Sammenligne verdier i en likning

For å løse likninger må vi kunne sjekke om en verdi oppfyller likningen. Vi bruker `==` (likhetstegn) til å sammenligne verdier.

:::::::::::::::{summary} Sammenligne verdier
Vi bruker `==` for å sjekke om to verdier er like:

:::{code-block} python
---
linenos:
---
if <venstre_side> == <høyre_side>:
    print("Betingelsen er oppfylt!")
:::

Merk: `==` brukes for å sammenligne (spørre "er de like?"), mens `=` brukes for å tilordne en verdi.
:::::::::::::::

:::::::::::::::{explore} Utforsk 1
La oss utforske hvordan vi tester om en verdi oppfyller en likning.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hva tror du programmet skriver ut når vi tester $2x + 3 = 11$ med $x = 4$?

:::{interactive-code}
---
predict:
---
x = 4
if 2*x + 3 == 11:
    print("x =", x, "er en løsning!")
:::
:::::::::::::

:::::::::::::{tab-item} b
Hva tror du programmet skriver ut når vi tester $2x + 3 = 11$ med $x = 3$?

:::{interactive-code}
---
predict:
---
x = 3
if 2*x + 3 == 11:
    print("x =", x, "er en løsning!")
:::
:::::::::::::

:::::::::::::{tab-item} c
Hva tror du programmet skriver ut når vi tester $3x - 2 = 13$ med $x = 5$?

:::{interactive-code}
---
predict:
---
x = 5
if 3*x - 2 == 13:
    print("x =", x, "er en løsning!")
:::
:::::::::::::

::::::::::::::

:::::::::::::::

---

## Løse likninger ved å teste verdier

Vi kombinerer `for`{l=python}-løkker og `if`{l=python}-setninger. For hver verdi i løkken sjekker vi om den oppfyller likningen. Hvis ja, skriver vi ut løsningen!

:::::::::::::::{summary} Slik løser vi likninger
For å finne løsninger på en likning tester vi alle heltallsverdier i et område:

:::{code-block} python
---
linenos:
---
for x in range(start, slutt):
    if <likning>:
        print("x =", x, "er en løsning!")
:::

Alle heltallsverdier av `x` som gjør likningen sann blir skrevet ut.
:::::::::::::::

:::::::::::::::{example} Eksempel 1
La oss løse likningen $2x + 3 = 11$ ved å teste alle verdier fra 0 til 10.

:::{interactive-code}
for x in range(11):
    if 2*x + 3 == 11:
        print("x =", x, "er en løsning!")
:::

::::{solution}
---
dropdown: 0
---

For-løkken tester alle verdier fra 0 til 10. For hver `x` sjekker vi om $2x + 3 = 11$.

Kun når $x = 4$ er likningen oppfylt: $2 \cdot 4 + 3 = 11$ ✓

Utskriften blir:

:::{code-block} console
x = 4 er en løsning!
:::

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 2
La oss løse likningen $x^2 - 5 = 20$ ved å teste verdier fra -10 til 10.

:::{interactive-code}
for x in range(-10, 11):
    if x**2 - 5 == 20:
        print("x =", x, "er en løsning!")
:::

::::{solution}
---
dropdown: 0
---

Vi løser $x^2 - 5 = 20$, som betyr $x^2 = 25$.

Programmet finner begge løsningene $x = 5$ og $x = -5$:

:::{code-block} console
x = 5 er en løsning!
x = -5 er en løsning!
:::

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Hva skriver programmet ut når det løser likningen $3x + 1 = 10$?

:::{interactive-code}
for x in range(10):
    if 3*x + 1 == 10:
        print("x =", x, "er en løsning!")
:::

::::{answer}
:::{code-block} console
x = 3 er en løsning!
:::
::::

::::{solution}
Vi løser $3x + 1 = 10$, som betyr $3x = 9$, så $x = 3$.

Utskriften blir:

:::{code-block} console
x = 3 er en løsning!
:::
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
Endre programmet til å løse likningen $x^2 = 9$ og test verdier fra -5 til 5.

:::{interactive-code}
for x in range(11):
    if 2*x + 3 == 11:
        print("x =", x, "er en løsning!")
:::

::::{answer}
:::{code-block} console
x = 3 er en løsning!
x = -3 er en løsning!
:::
::::

::::{solution}
Vi endrer likningen og søkeområdet:

:::{code-block} python
for x in range(-5, 6):
    if x**2 == 9:
        print("x =", x, "er en løsning!")
:::

Likningen $x^2 = 9$ har løsningene $x = 3$ og $x = -3$:

:::{code-block} console
x = 3 er en løsning!
x = -3 er en løsning!
:::
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 3
Løs likningen $x^2 + x = 6$ ved å teste verdier fra -5 til 5.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
:::{code-block} console
x = 2 er en løsning!
x = -3 er en løsning!
:::
::::

::::{solution}
Vi løser $x^2 + x = 6$:

:::{code-block} python
for x in range(-5, 6):
    if x**2 + x == 6:
        print("x =", x, "er en løsning!")
:::

Løsningene er $x = 2$ og $x = -3$:

:::{code-block} console
x = 2 er en løsning!
x = -3 er en løsning!
:::
::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 3
La oss løse likningen $x^2 - 3x - 10 = 0$ ved å teste verdier fra -10 til 10.

:::{interactive-code}
for x in range(-10, 11):
    if x**2 - 3*x - 10 == 0:
        print("x =", x, "er en løsning!")
:::

::::{solution}
---
dropdown: 0
---

For-løkken tester alle verdiene fra -10 til 10. Likningen har to løsninger: $x = -2$ og $x = 5$.

La oss sjekk:
- For $x = -2$: $(-2)^2 - 3(-2) - 10 = 4 + 6 - 10 = 0$ ✓
- For $x = 5$: $5^2 - 3(5) - 10 = 25 - 15 - 10 = 0$ ✓

Utskriften blir:

:::{code-block} console
x = -2 er en løsning!
x = 5 er en løsning!
:::

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 4
Definer funksjonen $f(x) = x^2 + x - 12$ og finn alle nullpunkt ved å teste verdier fra -10 til 10.

:::{interactive-code}
# Definer funksjonen og finn nullpunktene
:::

::::{answer}
:::{code-block} console
x = -4 er en løsning!
x = 3 er en løsning!
:::
::::

::::{solution}
Vi definerer funksjonen og søker etter nullpunkt (der $f(x) = 0$):

:::{code-block} python
def f(x):
    return x**2 + x - 12

for x in range(-10, 11):
    if f(x) == 0:
        print("x =", x, "er en løsning!")
:::

Utskriften blir:

:::{code-block} console
x = -4 er en løsning!
x = 3 er en løsning!
:::

Vi kan sjekke:
- For $x = -4$: $f(-4) = (-4)^2 + (-4) - 12 = 16 - 4 - 12 = 0$ ✓
- For $x = 3$: $f(3) = 3^2 + 3 - 12 = 9 + 3 - 12 = 0$ ✓

::::

:::::::::::::::

---

## Teste desimalverdier med while-løkke

Noen likninger har løsninger som ikke er heltall. Vi kan bruke en `while`{l=python}-løkke til å teste desimalverdier ved å øke verdien i små steg. Men det er en utfordring!

:::::::::::::::{explore} Utforsk 3
La oss prøve å løse likningen $2x - 1 = 0$ ved å teste desimalverdier i steg på 0.01. Hva skriver programmet ut?

:::{interactive-code}
x = 0
while x <= 1:
    if 2*x - 1 == 0:
        print("x = ",x, " er en løsning!")
    x = x + 0.01
print("Ferdig!")
:::

::::{solution}
---
dropdown: 0
---

Programmet skriver kun "Ferdig!" - det finner ingen løsninger! Men likningen $2x - 1 = 0$ har jo løsningen $x = 0.5$.

**Hvorfor fungerer det ikke?**

Problemet ligger i hvordan datamaskinen lagrer desimaltall. Når vi legger til 0.01 mange ganger (`x = x + 0.01`), oppstår små avrundingsfeil som gjør at `x` blir verdier som `0.5000000000000001` eller `0.4999999999999999` i stedet for nøyaktig `0.5`. Derfor blir sjekken `2*x - 1 == 0` alltid usann.

**Løsningen:** I stedet for å sjekke om resultatet er nøyaktig 0, sjekker vi om det er **nær** 0:

:::{code-block} python
x = 0
while x <= 1:
    løsning = 2*x - 1
    if -0.01 < løsning < 0.01:
        print(f"x = {x:.2f} er en løsning!")
    x = x + 0.01
:::

Nå sjekker vi om `løsning` ligger mellom -0.01 og 0.01, noe som fanger opp løsninger selv med små avrundingsfeil.

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 4
La oss løse likningen $2x - 1 = 0$ ved å teste desimalverdier i steg på 0.01, og sjekke om resultatet er nær 0.

:::{interactive-code}
x = 0
while x <= 1:
    løsning = 2*x - 1
    if -0.01 < løsning < 0.01:
        print(f"x = {x:.2f} er en løsning!")
    x = x + 0.01
:::

::::{solution}
---
dropdown: 0
---

Ved å sjekke om `løsning` ligger nær 0 (mellom -0.01 og 0.01), kan vi finne løsningen selv med små avrundingsfeil:

:::{code-block} console
x = 0.50 er en løsning!
:::

::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 5
Løs likningen $x^2 - 2 = 0$ ved å teste desimalverdier i steg på 0.01 fra 1 til 2.

Hint: Løsningen er $x = \sqrt{2} \approx 1.41$.

:::{interactive-code}
# Skriv koden din her
:::

::::{answer}
:::{code-block} console
x = 1.41 er en løsning!
:::
::::

::::{solution}
Vi bruker en `while`{l=python}-løkke som tester desimalverdier i steg på 0.01:

:::{code-block} python
x = 1
while x <= 2:
    løsning = x**2 - 2
    if -0.01 < løsning < 0.01:
        print(f"x = {x:.2f} er en løsning!")
    x = x + 0.01
:::

Løsningen $x = \sqrt{2} \approx 1.41$ blir funnet:

:::{code-block} console
x = 1.41 er en løsning!
:::

::::

::::::::::::::::
