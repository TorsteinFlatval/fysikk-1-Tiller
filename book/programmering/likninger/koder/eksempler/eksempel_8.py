# Eksempel 8: Teste likningen 2x + 1 = 0 (ingen heltallsløsninger)
for x in range(-10, 11):
    if 2*x + 1 == 0:
        print("x =", x, "er en løsning!")
