folytat = True
nevek = []
while folytat:
    nev = input("ADJÁL NEVEKT")
    if nev == "":
        break
    nevek.append(nev)

print(nevek)