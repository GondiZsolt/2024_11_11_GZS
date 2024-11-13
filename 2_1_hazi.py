"""2.1/2.2 Feladat
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja.
Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja.
A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!
"""
folytat = True
szavak = []

while True:
    szo = input('Adj meg "A" betűvel kezdődő szavakat. Ha végeztél nyomj egy ENTER gombot.')

    if szo.startswith("a") or szo.startswith("A"):
        print("tárolva")
        szavak.append(szo)
    elif szo == (""):
        break
    else:
        print('A megadott szó nem kezdődik "A" betűvel')

print(f"A szavaid:{szavak}")