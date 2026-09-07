# Eksempel 9: Lagre løsninger i en liste
løsninger = []

for x in range(-10, 11):
    if x**2 - 5*x + 6 == 0:
        løsninger.append(x)

print("Løsningene er:", løsninger)
