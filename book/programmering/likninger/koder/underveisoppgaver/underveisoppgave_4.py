# Underveisoppgave 4: Løse x^2 + x - 12 = 0 ved å teste verdier fra -10 til 10
for x in range(-10, 11):
    if x**2 + x - 12 == 0:
        print("x =", x, "er en løsning!")
