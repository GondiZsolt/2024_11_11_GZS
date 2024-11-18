"""
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában.
A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""
folytat = True

szinek = ["piros", "kék", "sárga", "zöld",]

print(szinek)
megadott_szin = input("Adj meg egy színt: ")
# while folytat:
#     if megadott_szin in szinek:
#         print(f"A megadott szín, {megadott_szin} szerepel a listában")
#         print(szinek)
#     else:
#         print(f"A megadott szín, {megadott_szin} nem szerepel a listában")
#         szinek.append(megadott_szin)
#         print(szinek)

szinek.remove(megadott_szin)
print(szinek)