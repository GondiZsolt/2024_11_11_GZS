
nyelvek = ['Python', 'C', 'C++', 'Java', 'Python']

# sorbarendezi a listát
nyelvek.sort()
print(nyelvek)

# fordított sorrendbe rendezi a listát
nyelvek.reverse() 
print(nyelvek)

nyelvek2 = sorted(nyelvek) # válozóhoz mentve megtartja az eredeti listát is cig nig



# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))
print(nyelvek.index('C++'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))
print(nyelvek.count('Py'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)
print('C+++' in nyelvek)