# Python-2025-02-19
Dolgozat
---

Python projekt a 2025.02.19-ei dolgozatra

### Feladatok

> Importáld és olvasd be az adatokat egy megfelelő adatszerkezetbe (pl. lista vagy tömb)

```py
class Country:
    def __init__(self, name = "", capital = "", area = 0, population = 0, pop_density = 0.0):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population
        self.pop_density = pop_density

def import_cdata(filename:str) -> list:
    countries = []
    
    with open(f"./{filename}", 'r', encoding='utf-8') as source:
        next(source)
        for line in source:
            data = line.strip().split(';')
            country = Country(data[0], data[1], int(data[2]), int(data[3]), float(data[4].replace(',', '.')))
            countries.append(country)
            
    return countries
```

```py
print("Európa")
data = import_cdata('forras_europa.txt')
do_task(data)
input("\n\nNyomjon Enter-t a következő kontinenshez lépéshez...")
print("\n\n\n\nÁzsia")
data = import_cdata('forras_azsia.txt')
do_task(data)
input("\n\nNyomjon Enter-t a következő kontinenshez lépéshez...")
print("\n\n\n\nAfrika")
data = import_cdata('forras_afrika.txt')
do_task(data)
```

> Határozd meg, melyik ország rendelkezik a legnagyobb népességgel

```py
populated = Country()
for country in data:
    if country.population > populated.population:
        populated = country
print(f"Legnépesebb ország: {populated.name}")
```

> Határozd meg, melyik ország a legnagyobb területű

```py
largest = Country()
for country in data:
    if country.area > largest.area:
        largest = country
print(f"Legnagyobb területű ország: {largest.name}")
```

> Határozd meg, melyik országban a legnagyobb a népsűrűség

```py
dense = Country()
for country in data:
    if country.pop_density > dense.pop_density:
        dense = country
print(f"Legnagyobb népsűrűségű ország: {dense.name}")
```

> Számítsd ki az országok átlagos népsűrűségét

```py
all_density = 0
for country in data:
    all_density += country.pop_density
print(f"Átlagos népsűrűség: {all_density / len(data)} fő/km2")
```

> Számítsd ki az összes ország együttes területét

```py
all_area = 0
for country in data:
    all_area += country.area
print(f"Összes ország területe: {all_area} km2")
```

> Határozd meg az országok népességének mediánját

```py
import statistics
```

```py
populations = []
for country in data:
    populations.append(country.population)
pop_median = statistics.median(populations)
print(f"Népesség mediánja: {pop_median}")
```

> Listázd ki azokat az országokat, ahol a népsűrűség nagyobb, mint 150 fő/km²

```py
print("\nNépsűrűség > 150 fő/km2:")
for country in data:
    if country.pop_density > 150:
        print(country.name)
```

> Rendezd az országokat területük szerint növekvő sorrendben

```py
area_increase = sorted(data, key=lambda x: x.area)
print("\nOrszágok terület szerint növekvő sorrendben:")
for c in area_increase:
    print(c.name)
```

> Csoportosítsd az országokat alacsony (100 alatt), közepes (100–300) és magas (300 felett) népsűrűség kategóriákba.

```py
alacsony = []
kozepes = []
magas = []
for country in data:
    if country.pop_density < 100:
        alacsony.append(country.name)
    elif country.pop_density < 300:
        kozepes.append(country.name)
    else:
        magas.append(country.name)
alacsony.sort()
kozepes.sort()
magas.sort()
print("\n\nAlacsony népsűrűség (<100):")
for c in alacsony:
    print(c)
print("\nKözepes népsűrűség (>100, <300):")
for c in kozepes:
    print(c)
print("\nMagas népsűrűség (>300):")
for c in magas:
    print(c)
```
