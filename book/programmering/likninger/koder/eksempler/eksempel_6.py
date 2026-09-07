# Eksempel 6: Løse x^2 = 16 ved å teste verdier fra -10 til 10
for x in range(-10, 11):
    if x**2 == 16:
        print("x =", x, "er en løsning!")
