import matplotlib.pyplot as plt

productos = ["Manzanas", "Peras", "Naranja"]
ventas = [50,80,40]

Colores=["pink","blue","purple"]
texture=["//","\\","*","||"]#Darle textura a los graficos

#plt.bar(productos, ventas)#color="skyblue", edgecolor="darkblue"
var=plt.bar(productos,ventas, color=Colores, linewidth=1)
for bar, texture in zip (var,texture):
    bar.set_hatch(texture)
for i, bar in enumerate(var):
    altura = bar.get_height() #Obtiene la altura actual, es decir el valor que representa[50,80,40]
    plt.text(bar.get_x() + bar.get_width() / 2, altura + 0.7,  # ← cambia de +2 a +5
             str(ventas[i]),#Convierte el valor de la barra en texto para mostrarlo como etiqueta
             ha='center', va='bottom',
             fontsize=10, fontweight='bold')
    
plt.title("Ventas por Producto",fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)#, fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20
plt.xlabel("Productos",fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace'
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#
plt.show()

# Gráfico de líneas
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', "octubre"]
ventas = [250, 300, 400, 350, 500, 450, 300, 200]

plt.plot(meses, ventas, marker='o', color='darkblue')
plt.title("Evolución de Ventas", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()

# Histograma
edades = [20, 21, 22, 25, 26, 30, 35, 40]

plt.hist(edades, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de Edades", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.xlabel("Rango de Edades", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Frecuencia", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.show()

#Dispersion
ingresos = [100,200,300,400,500]
gasto = [20,40,60,80,100]

plt.scatter(gasto, ingresos, color="blue")
plt.title("relacion entre gasto e ingresos")
plt.xlabel("gasto")
plt.ylabel("ingresos")
plt.show()