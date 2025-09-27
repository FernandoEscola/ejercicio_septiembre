import matplotlib.pyplot as plt

Productos = ['Manzanas', 'Bananas', 'Cerezas']
Ventas = [150, 200, 100]

Colores = ["Pink", "Blue", "Purple"]
Texture = ["//", "xx", "oo"]

plt.bar(Productos, Ventas)#color="skyblue", edgecolor="darkblue"
var=plt.bar(Productos,Ventas, color=Colores, linewidth=1)
for bar, texture in zip (var,Texture):
    bar.set_hatch(texture)

for i, bar in enumerate(var):
    altura = bar.get_height() #Obtiene la altura actual, es decir el valor que representa[50,80,40]
    plt.text(bar.get_x() + bar.get_width() / 2, altura + 0.7,  # ← cambia de +2 a +5
             str(Ventas[i]),#Convierte el valor de la barra en texto para mostrarlo como etiqueta
             ha='center', va='bottom',
             fontsize=10, fontweight='bold')


plt.title("Ventas por Producto",fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)#, fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20
plt.xlabel("Productos",fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace'
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#
plt.show()

meses= ["Enero", "Febrero", "Marzo"]
Ventas = [150, 200, 100]

#Gráfico de líneas
plt.plot(meses, Ventas, color='orange', marker='o', linestyle='--', linewidth=2, markersize=8)
plt.title("Evolución De Ventas", fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)
plt.xlabel("meses", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()

edades= [18, 25, 30, 35, 40, 45, 50, 55, 60, 70]
plt.hist(edades, bins=5, color='lightblue', edgecolor='black')
plt.title("Distribución de Edades", fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)
plt.xlabel("Rango De Edades", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Frecuencia", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()


ingresos = [5000, 7000, 6000, 8000]
gasto= [20, 40, 60, 80, 100]

#Grafico de dispersión
plt.scatter(ingresos, gasto, color='green', marker='o') #marker='x' cambia la forma del marcador
plt.title("Ingresos vs Gasto", fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)
plt.xlabel("Gasto Publicitario", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Ingresos", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()


