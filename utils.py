# ------ Importar los módulos ------- #
import csv 
import charts

# ------ Leer el archivo ------- #
def read_csv(path):
    try:
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            header = next(reader)
            data = []

            for row in reader:
                iterable = zip(header, row)
                country_dic = { key : value for key,value in iterable }
                data.append(country_dic)
            return data
    except Exception as error:
        print(error)

# ------ Obtener población ------- #
def get_population(country_dic):
    population_dic = {
        '2022' : int(country_dic['2022 Population']),
        '2020' : int(country_dic['2020 Population']),
        '2015' : int(country_dic['2015 Population']),
        '2010' : int(country_dic['2010 Population']),
        '2000' : int(country_dic['2000 Population']),
        '1990' : int(country_dic['1990 Population']),
        '1980' : int(country_dic['1980 Population']),
        '1997' : int(country_dic['1970 Population']),
    }
    labels = population_dic.keys()
    values = population_dic.values()
    return labels, values

# ------ Obtener población por países ------- #
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

# ------ Ejecutar prueba gráfica de barras de histórico población ------- #
def test_population_chart(data):
    country = input('Ingresa el país => ')
    result = population_by_country(data, country)

    if(len(result) > 0):
        country = result[0]
        keys, values = get_population(country)
        charts.generate_bar_chart(keys, values)

# ------ Ejecutar prueba gráfica de pastel con porcentaje poblacional ------- #
def test_percentages_chart(data):
    print('Selecciona el continente a consultar:\n1- South America \n2- North America \n3- Asia \n4- Europe \n5- Oceania')
    continent = ''
    option_selected = int(input('Selección -> '))

    if option_selected == 1:
        continent = 'South America'
    elif option_selected == 2:
        continent = 'North America'
    elif option_selected == 3:
        continent = 'Asia'
    elif option_selected == 4:
        continent = 'Europe'
    elif option_selected == 5:
        continent = 'Oceania'
    else:
        raise Exception('Seleccionaste una opción no válida')

    data = list(filter(lambda item : item['Continent'] == continent, data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x : x['World Population Percentage'], data))
    charts.generate_pie_char(countries, percentages)

