meses = ["Enero","Febrero","Marzo","Abril"]
ventas = [1500, 1800, 1200, 2000]
gasto_publicitario=[500,700,400,800]

import matplotlib.pyplot as plt
plt.scatter(gasto_publicitario, ventas, color="green")
plt.title("relacion entre gasto e ingresos")
plt.xlabel("gasto_publicitario")
plt.ylabel("ventas")
plt.show()