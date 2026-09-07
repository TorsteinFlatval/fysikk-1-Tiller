# Underveisoppgave 5: Lagre løsninger på x^2 - x - 6 = 0 i en liste
løsninger = []

for x in range(-10, 11):
    if x**2 - x - 6 == 0:
        løsninger.append(x)

print("Løsningene er:", løsninger)
