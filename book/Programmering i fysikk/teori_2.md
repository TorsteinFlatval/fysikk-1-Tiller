## Bevegelse med varierende akselerasjon


I mange virkelige situasjoner er akselerasjonen ikke konstant, men avhenger av farten selv. For eksempel et 100-metersløp. Da er kselerasjonen er stor ved starten, men blir mindre og mindre etter hvert som farten nærmer seg toppfarten.


### Akselerasjonen som en funksjon


For å beskrive dette kan vi skrive akselerasjonen som en funksjon av farten, `a(v)`{l=python}. Vi definerer en funksjon med `def`{l=python}, akkurat som når vi lager en funksjon i matematikk:


:::{code-block} python
---
linenos:
---
def a(v): # akselerasjonen er en funksjon av farten
    aks = -0.5*v + 6  # beregner akselerasjonen
    return aks        # returnerer akselerasjonen
:::


Legg merke til at akselerasjonen er stor når farten er lav, og går mot null når farten nærmer seg en toppfart. Vi kan teste funksjonen for ulike verdier av `v`{l=python}.

Akselerasjonen når `v = 0`{l=python}. Blir `a(0)`{l=python} $= -0.5\cdot0+6=6$. <br>
Akselerasjonen når `v = 10`{l=python}. Blir `a(10)`{l=python} $= -0.5\cdot10+6=1$. <br>
Akselerasjonen når `v = 12`{l=python}. Blir `a(12)`{l=python} $= -0.5\cdot12+6=0$. <br>




:::{code-block} python
---
linenos:
---
print(a(0))   # akselerasjon ved v = 0 m/s
print(a(10))  # akselerasjon ved v = 10 m/s
print(a(12))  # akselerasjon ved v = 12 m/s

:::

Dette vil gi følgende utskrift:
```text
6.0
1.0
0.0
```
:::::::::::::::


:::{explore} Utforsk 1
Regn selv ut `a(2.5)`{l=python} ved å sette `v = 2.5`{l=python} inn i formelen `aks = -0.5*v + 6`{l=python}. Test deretter i koden om du fikk rett, og prøv deg fram med ulike verdier for `v`{l=python} for å finne ved hvilken fart akselerasjonen blir `2`{l=python}.

:::{interactive-code}
---
predict:
---
def a(v):
    aks = -0.5*v + 6
    return aks

print(a(2.5))
:::
:::


###  ` while s < s_slutt`{l=python}


I dette programmet er vi ikke interessert i å stoppe etter en gitt tid, men når løperen har tilbakelagt `100`{l=python} meter. Da bruker vi betingelsen `s < s_slutt`{l=python} i stedet for `t < t_slutt`{l=python}. Inni løkka bruker vi funksjonen `a(v)`{l=python} til å regne ut akselerasjonen som passer til farten akkurat da:


:::{code-block} python
---
linenos:
---
while s < s_slutt:     # etter 100 m er løpet over
  v = v + a(v)*dt      # beregner ny fart
  s = s + v*dt         # beregner ny posisjon
  t = t + dt           # øker tiden med dt
  s_verdier.append(s)  # legger s inn i posisjonslisten
  v_verdier.append(v)  # legger v inn i fartslisten
:::


Prøv å kjøre hele programmet under. Det tegner opp en v-s-graf som viser hvordan farten øker raskt i starten, og deretter flater ut mot en toppfart etter hvert som løperen nærmer seg 100 meter.


:::{interactive-code}
import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 100
dt = 0.01
s_verdier = [s]
v_verdier = [v]

def a(v):
  aks = -0.5*v + 6
  return aks

while s < s_slutt:
  v = v + a(v)*dt
  s = s + v*dt
  t = t + dt
  s_verdier.append(s)
  v_verdier.append(v)

plt.plot(s_verdier, v_verdier)
plt.title("Fart som funksjon av posisjon")
plt.xlabel("$s$ (m)")
plt.ylabel("$v$ (m/s)")
plt.grid()
plt.show()
:::


::::::{exercise} Underveisoppgave 1
En fallskjermhopper hopper ut ifra et fly og akselererer mot bakken $a=g=9.81 m/s^2$
Positiv regning er nedover.

:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} a

Definer en funksjon `a(v)`{l=python} hvor akselerasjonen avtar med $v^2$

:::{interactive-code}
def a(v):
    aks =
    return aks

:::



:::{solution}
:::{code-block} python
---
linenos:
---
def a(v):
    aks = 9.81 - v**2
    return aks
:::
:::

::::

::::{tab-item} b

Bruk funksjonen du fant i forrige oppgave og tegn posisjonsgrafen de første 1500 meterene.

:::{interactive-code}
import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 100
dt = 0.01
s_verdier = [s]
t_verdier = [t]

def a(v):


while s < s_slutt:
  v = v + a(v)*dt
  s = s + v*dt
  t = t + dt
  s_verdier.append(s)
  t_verdier.append(v)

plt.plot(s_verdier, t_verdier)
plt.title("Posisjon som funksjon av tid")
plt.xlabel("$t$ (s)")
plt.ylabel("$s$ (m)")
plt.grid()
plt.show()

# FYLL INN DIN KODE HER
:::



:::{solution}
:::{code-block} python
---
linenos:
---
Bruk funksjonen du fant i forrige oppgave og tegn posisjonsgrafen de første 1500 meterene.

:::{interactive-code}
import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 1500
dt = 0.01
s_verdier = [s]
v_verdier = [v]

def a(v):
    aks = 9.81 - v**2
    return aks


while s < s_slutt:
  v = v + a(v)*dt
  s = s + v*dt
  t = t + dt
  s_verdier.append(s)
  v_verdier.append(v)

plt.plot(s_verdier, v_verdier)
plt.title("Fart som funksjon av posisjon")
plt.xlabel("$s$ (m)")
plt.ylabel("$v$ (m/s)")
plt.grid()
plt.show()
:::
:::

::::

::::{tab-item} c
Tegn akselerasjonsgrafen for de første 1 500 meterene.

:::{interactive-code}
import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 1500
dt = 0.01
s_verdier = [s]
v_verdier = [v]

def a(v):
    aks = 9.81 - v**2
    return aks


while s < s_slutt:
  v = v + a(v)*dt
  s = s + v*dt
  t = t + dt
  s_verdier.append(s)
  v_verdier.append(v)

plt.plot(s_verdier, v_verdier)
plt.title("Fart som funksjon av posisjon")
plt.xlabel("$s$ (m)")
plt.ylabel("$v$ (m/s)")
plt.grid()
plt.show()
:::



:::{solution}
:::{code-block} python
---
linenos:
---
simport matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 1500
dt = 0.01
s_verdier = [s]
v_verdier = [v]

def a(v):
    aks = 9.81 - v**2
    return aks


while s < s_slutt:
  v = v + a(v)*dt
  s = s + v*dt
  t = t + dt
  s_verdier.append(s)
  v_verdier.append(v)

plt.plot(s_verdier, v_verdier)
plt.title("Fart som funksjon av posisjon")
plt.xlabel("$s$ (m)")
plt.ylabel("$v$ (m/s)")
plt.grid()
plt.show()
:::
:::

::::

:::::
::::::

## Vi lager en akselerasjonsfunksjon for luftmotstand


Vi ønsker å finne akselerasjonen til en gjenstand som faller med luftmotstand. Vi velger positiv retning nedover.


### Krefter som virker på fallene gjenstander med luftmostand

Når gjenstanden faller, og positiv retning er nedover, virker tyngdekraften nedover og luftmotstanden oppover. Tyngdekraften $G = mg$ og luftmotstanden $L = kv^2$.


:::Konstanten $k$ bestemmer hvor stor luftmotstanden er ved en gitt fart. Den avhenger blant annet av gjenstandens form, tverrsnittsareal og luftas tetthet. I fysikk 1 er den bare oppgitt som et tall.

Siden nedover er positiv retning, får tyngdekraften positivt fortegn og luftmotstanden negativt fortegn. Newtons andre lov gir da

$$
\sum F = ma
$$

$$
G-L = ma.
$$

$$
mg-kv^2 = ma.
$$

Vi deler på massen og får uttrykket som brukes i funksjonen:

$$
a = \frac{mg-kv^2}{m}.
$$


```{image} acfb4b2e-620b-4045-a042-c594f486c836.png
:alt: Illustrasjon av krefter på en fallende gjenstand
:width: 600px
:align: center
```

For en gjenstand som slippes fra ro, er luftmotstanden null i starten. Da er akselerasjonen lik $g$. Etter hvert som farten øker, øker luftmotstanden og akselerasjonen blir mindre.

Når luftmotstanden er like stor som tyngdekraften, får vi

$$
mg-kv^2=0
\quad\Rightarrow\quad
a=0.
$$

Da faller gjenstanden med konstant fart, kalt terminalfart. Null akselerasjon betyr ikke at gjenstanden står stille, men at farten ikke endrer seg.


#### Definere funksjonen

:::{code-block} python
---
linenos:
---
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a
:::

| Parameter | Betydning | Enhet |
|---|---|---|
| `m`{l=python} | Gjenstandens masse | kg |
| `g`{l=python} | Tyngdeakselerasjonen | m/s² |
| `k`{l=python} | Konstanten i luftmotstandsmodellen | kg/m |
| `v`{l=python} | Gjenstandens fart nedover | m/s |


Funksjonen beregner bare akselerasjonen. Den oppdaterer ikke farten eller posisjonen, og den skriver ikke ut svaret med mindre vi bruker `print()`{l=python}.

:::::::::::::::{example} Eksempel 1

En gjenstand har massen $2,0$ kg og farten $10,0$ m/s nedover. Vi setter tyngdeakselerasjonen til $9,81$ m/s² og luftmotstandskonstanten til $0,10$ kg/m.

:::{code-block} python
---
linenos:
---
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

a = aks(2.0, 9.81, 0.10, 10.0)
print("Akselerasjonen er", round(a, 2), "m/s²")
:::

Programmet skriver ut:

```text
Akselerasjonen er 4.81 m/s²
```

Beregningen er

$$
a = \frac{2,0\cdot 9,81-0,10\cdot 10,0^2}{2,0}
  = 4,81\ \text{m/s}^2.
$$

Akselerasjonen er positiv, altså rettet nedover. Gjenstanden øker derfor farten nedover i dette øyeblikket.

:::::::::::::::

:::







