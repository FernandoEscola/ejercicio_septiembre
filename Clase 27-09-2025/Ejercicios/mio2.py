meses = ["Enero","Febrero","Marzo","Abril"]
ventas = [1500, 1800, 1200, 2000]
gasto_publicitario=[500,700,400,800]

import matplotlib.pyplot as plt
plt.plot(meses, ventas, marker='o', color='green')
plt.title("Evolución de Ventas durante los meses", fontsize=16, fontweight='bold', color='darkblue', fontfamily='monospace')
plt.ylabel("Ventas", fontsize=12, fontweight='bold', color='darkgreen', fontfamily='monospace')
plt.grid(True)
plt.show()