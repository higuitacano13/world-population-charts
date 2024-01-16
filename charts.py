import matplotlib.pyplot as plt
import numpy as np

# -------- Generar Gráfica de Barras -------- #
def generate_bar_chart(labels, values):
    # --- Seleccionar paleta de colores --- #
    colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))

    # --- Crear la gráfica --- #
    fig, ax = plt.subplots()
    ax.bar(labels, values, color = colors)

    # --- Asignar valores a los Labels y al Titulo --- #
    ax.set_xlabel('Año')
    ax.set_ylabel('Población (en miles)')
    plt.title('Población por Año')

    # --- Mostrar gráfica --- #
    plt.show()

# -------- Generar Gráfica de Torta -------- #
def generate_pie_char(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.title('Porcentaje poblacional')
    plt.show()
