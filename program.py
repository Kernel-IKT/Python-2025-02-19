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
    pass

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