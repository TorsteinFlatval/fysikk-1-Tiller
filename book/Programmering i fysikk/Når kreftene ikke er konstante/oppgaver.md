# Oppgaver: Når kreftene ikke er konstante


Du skal hoppe i fallskjerm fra 4 000 m og vil simulere hvordan du vil akselerere og etter hvert nå terminalfart.  

:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Gå gjennom koden og forklar hva hver del gjør.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Forklar hva del 1 gjør.

:::{code-block} python
---
linenos:
---
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s
:::
:::::::::::::

:::::::::::::{tab-item} b
Forklar hva del 2 gjør.

:::{code-block} python
---
linenos:
---
# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]
:::
:::::::::::::

:::::::::::::{tab-item} c
Forklar hva del 3 gjør.

:::{code-block} python
---
linenos:
---
# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a
:::
:::::::::::::

:::::::::::::{tab-item} d
Forklar hva del 4 gjør.

:::{code-block} python
---
linenos:
---
# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)
:::
:::::::::::::

:::::::::::::{tab-item} e
Forklar hva del 5 gjør.

:::{code-block} python
---
linenos:
---
# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::

:::::::::::::{tab-item} f
Kjør hele koden og tolk resultatet.

:::{interactive-code}
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s

# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]

# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)

# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::

::::::::::::::
:::::::::::::::

:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Vi ønsker nå å endre koden slik at vi kan finne terminalfarten.

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Lag en liste for fartsverdiene og en liste for akselerasjonsverdiene i del 2. Oppdater listene for hver iterasjon i del 4.

Tegn deretter fart–tid-grafen og akselerasjon–tid-grafen i del 5.

:::{interactive-code}
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s

# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]

# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)

# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::

:::::::::::::{tab-item} b
Hva har massen `m`{l=python} å si for endringen av fart?

* Endre `m`{l=python} og se hva terminalfarten blir for ulike masser.
* Hva skjer med terminalfarten når `m`{l=python} øker?
* Er akselerasjonen i starten lik?

:::{interactive-code}
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s

# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]

# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)

# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::

:::::::::::::{tab-item} c
Som programmet er nå, kjører det i $20$ s.

Endre betingelsen i `while`{l=python}-løkka i del 4 slik at den kjører helt til fallskjermhopperen har beveget seg $10\,000$ m.

:::{interactive-code}
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s

# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]

# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)

# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::

::::::::::::::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 3
---
level: 1
---
Når man hopper i fallskjerm, vil man helst løse ut fallskjermen på et tidspunkt. Dette vil gi et mye større luftmotstandstall på `k = 20`{l=python}. En vanlig utløsningshøyde er $1000$ m.

Endre programmet slik at det viser posisjonsgrafen, fartsgrafen og akselerasjonsgrafen når personen løser ut en fallskjerm $1000$ m over bakken.

:::{interactive-code}
import matplotlib.pyplot as plt

# Del 1
# Definerer konstanter
m = 83       # masse i kg
g = 9.81     # tyngdeakselerasjonen på jorda i m/s^2
k = 0.32     # luftmotstandstallet
dt = 0.01    # steglengde for hver beregning i s
t_slutt = 20 # når beregningene skal stoppe, i s

# Del 2
# Startverdier
t = 0
s = 0
v = 0
a = g

# Lager lister med startverdiene
t_verdier = [t]
s_verdier = [s]

# Del 3
# Funksjon for å beregne akselerasjon
def aks(m, g, k, v):
    a = (m*g - k*v**2)/m
    return a

# Del 4
while t < t_slutt:
    t = t + dt
    s = s + v*dt
    v = v + a*dt
    a = aks(m, g, k, v)

    t_verdier.append(t)
    s_verdier.append(s)

# Del 5
plt.plot(t_verdier, s_verdier)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Posisjon-tid-graf')
plt.grid()
plt.show()
:::
:::::::::::::::