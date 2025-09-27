meses = ["Enero","Febrero","Marzo","Abril"]
ventas = [1500, 1800, 1200, 2000]
gasto_publicitario=[500,700,400,800]
Colores=["pink","blue","purple"]
texture=["//","\\","*","||"]#Darle textura a los graficos
import matplotlib.pyplot as plt
#plt.bar(productos, ventas)#color="skyblue", edgecolor="darkblue"
var=plt.bar(meses,ventas, color=Colores, linewidth=1)
for bar, texture in zip (var,texture):
    bar.set_hatch(texture)
for i, bar in enumerate(var):
    altura = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, altura + 0.7,  # ← cambia de +2 a +5
             str(ventas[i]),#Convierte el valor de la barra en texto para mostrarlo como etiqueta
             ha='center', va='bottom',
             fontsize=10, fontweight='bold')
    
plt.title("Ventas por Producto",fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20)#, fontsize=16, fontweight='bold', color='darkblue',fontfamily='sans-serif', pad=20
plt.xlabel("Meses",fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace'
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')#
plt.show()