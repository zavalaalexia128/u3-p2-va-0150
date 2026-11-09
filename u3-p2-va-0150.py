import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Zavala Medina | NC= 0150
# Datos de servicios de streaming
nfx = ["Netflix", 260, False, 2007]
dis = ["Disney+", 150, False, 2019]
spn = ["Spotify", 602, True, 2008]
ytb = ["YouTube Premium", 100, True, 2014]
hbo = ["Max", 95, False, 2020]

# Creamos una lista de listas
lista_streaming = [nfx, dis, spn, ytb, hbo]

# Crear el DataFrame con pandas (pd) y el argumento columns correcto
df_streaming = pd.DataFrame(
    lista_streaming, columns=["Nombre", "Cantidad", "Es_Musica", "Años"]
)
print(df_streaming)

# Guardar en CSV
df_streaming.to_csv("streaming.csv", index=False)

# Crear grafica de lineas
# Donde x es nombre en el eje horizontal
# Donde Y es Cantidad en el eje vertical
plt.plot(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.title("Grafica Servicios de Streaming 0150")
plt.xlabel("Nombre de las plataformas")
plt.ylabel("Cantidad de usuarios")
plt.show()

# Creamos una grafica de puntos
plt.scatter(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.show()

# Grafica de barras
plt.bar(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.title("Grafica Servicios de Streaming 0150")
plt.xlabel("Nombre de las plataformas")
plt.ylabel("Cantidad de usuarios")
plt.show()

# Ordenar las graficas de barras de manera descendente
# De la mas grande a la pequeña (sin colores)
df_str_ordenar = df_streaming.sort_values("Cantidad", ascending=False)
plt.bar(df_str_ordenar["Nombre"], df_str_ordenar["Cantidad"])
plt.title("Grafica Servicios de Streaming 0150")
plt.xlabel("Nombre de las plataformas")
plt.ylabel("Cantidad de usuarios")
plt.show()

# Ordenar las graficas de barras de manera descendente (con colores)
plt.bar(
    df_str_ordenar["Nombre"],
    df_str_ordenar["Cantidad"],
    color=["b", "g", "c", "m", "y"],
)
plt.title("Grafica Servicios de Streaming 0150")
plt.xlabel("Nombre de las plataformas")
plt.ylabel("Cantidad de usuarios")
plt.show()

print("Programa realizado por Zavala Medina Alexia Paola | NC = 0150")

# Grafica de pastel
plt.plot(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.pie(df_streaming["Cantidad"], labels=df_streaming["Nombre"])
plt.show()