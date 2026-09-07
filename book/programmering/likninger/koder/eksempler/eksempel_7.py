# Eksempel 7: Løse x^2 - 3x - 10 = 0 ved å teste verdier fra -10 til 10
for x in range(-10, 11):
    if x**2 - 3*x - 10 == 0:
        print("x =", x, "er en løsning!")
