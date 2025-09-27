import matplotlib.pyplot as plt
edades = [22,25,30,30,32,35,40,42,50,55,60,60,65,70,75]

plt.hist(edades, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de Edades", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.xlabel("Rango de Edades", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Frecuencia", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.show()

plt.hist(edades, bins=80, color='white', edgecolor='black')
plt.title("Distribución de Edades grueso", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.xlabel("Rango de Edades", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Frecuencia", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.show()

plt.hist(edades, bins=100, color='black', edgecolor='black')
plt.title("Distribución de Edades hiper grueso", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.xlabel("Rango de Edades", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.ylabel("Frecuencia", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.show()