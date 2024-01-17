import utils

if __name__ == '__main__':
    csv_path = './world_population_delimiter.csv'
    data = utils.read_csv(csv_path)

    print('***' * 25)
    print('Bienvenido a la sección de ejercicios de gráficación de datos con Matplotlib')
    print('Selecciona el ejercicio a ejecutar:\n1- Gráfica de valores poblacionales en el pasar de los años. \n2- Gráfica porcentaje poblacional por continente')
    option_selected = int(input('Selección -> '))

    if option_selected == 1:
        utils.test_population_chart(data)
    elif option_selected == 2:
        utils.test_percentages_chart(data)
    else:
        raise Exception('Seleccionaste una opción no válida')

        
