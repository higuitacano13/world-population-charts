import matplotlib.pyplot as plt

# -------- Generar Gráfica de Barras -------- #
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# -------- Generar Gráfica de Torta -------- #
def generate_pie_char(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 90]

    generate_bar_chart(labels, values)
    generate_pie_char(labels, values)