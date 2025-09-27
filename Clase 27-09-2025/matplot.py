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