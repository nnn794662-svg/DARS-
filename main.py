ism = "Diyor"

print(ism.upper())

print(ism.lower())
name = 'ali'
print(name.title())
print(name.capitalize())

matn = "salom jigar ganday yaxshimisan"
print(matn.title())
print(matn.capitalize())

ismlar = ['behruz', 'Nodirbek', 'farrux', 'asilbek']
ismlar.sort()
print(ismlar)

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek']
print(sorted(ismlar))

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek']
print(sorted(ismlar, reverse=True))

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek', 'ulugbek', 'murod', 'begzod']
del ismlar[6]
print(ismlar)

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek', 'ulugbek', 'murod', 'begzod']
ismlar.append("Ali")
ismlar.append("Guli")
print(ismlar)

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek', 'ulugbek', 'murod', 'begzod']
ismlar.insert(1, 'Otabek')
print(ismlar)

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek', 'ulugbek', 'murod', 'begzod']
print(ismlar.pop(4))
print(ismlar)

ismlar = ['behruz', 'nodirbek', 'farrux', 'asilbek', 'ulugbek', 'murod', 'begzod']
ismlar.remove('farrux')
print(ismlar)