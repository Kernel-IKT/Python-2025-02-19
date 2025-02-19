import statistics

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

def do_task(data: list):
    populated = Country()
    for country in data:
        if country.population > populated.population:
            populated = country
    print(f"Legnépesebb ország: {populated.name}")
    
    largest = Country()
    for country in data:
        if country.area > largest.area:
            largest = country
    print(f"Legnagyobb területű ország: {largest.name}")
    
    dense = Country()
    for country in data:
        if country.pop_density > dense.pop_density:
            dense = country
    print(f"Legnagyobb népsűrűségű ország: {dense.name}")
    
    all_density = 0
    for country in data:
        all_density += country.pop_density
    print(f"Átlagos népsűrűség: {all_density / len(data)} fő/km2")
    
    all_area = 0
    for country in data:
        all_area += country.area
    print(f"Összes ország területe: {all_area} km2")
    
    populations = []
    for country in data:
        populations.append(country.population)
    pop_median = statistics.median(populations)
    print(f"Népesség mediánja: {pop_median}")
    
    print("\nNépsűrűség > 150 fő/km2:")
    for country in data:
        if country.pop_density > 150:
            print(country.name)
            
    area_increase = sorted(data, key=lambda x: x.area)
    print("\nOrszágok terület szerint növekvő sorrendben:")
    for c in area_increase:
        print(c.name)
        
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