import matplotlib.pyplot as plt

Meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
Ventas = [1500, 1800, 1200, 2000]
gasto_publicitario= [500, 700, 400, 800]


Colores = ["Pink", "Blue", "Purple"]
Texture = ["//", "xx", "oo"]

plt.bar(Meses, Ventas)#color="skyblue", edgecolor="darkblue"
var=plt.bar(Meses,Ventas, color=Colores, linewidth=1)
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




import matplotlib.pyplot as plt

Meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
Ventas = [1500, 1800, 1200, 2000]
gasto_publicitario= [500, 700, 400, 800]

plt.plot( Meses,Ventas, marker='o')
plt.title('Ventas durante los meses', fontsize=16, fontweight='bold', color='darkblue', fontfamily='sans-serif', pad=20)
plt.xlabel(Meses, fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel(Ventas, fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()




