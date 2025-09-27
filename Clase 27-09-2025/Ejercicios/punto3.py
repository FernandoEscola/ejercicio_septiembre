import matplotlib.pyplot as plt
meses = ["Enero","Febrero","Marzo","Abril"]
ventas = [1500, 1800, 1200, 2000]
gasto_publicitario=[500,700,400,800]
#grafico de dispersion
plt.scatter(gasto_publicitario, ventas, color = "red")
plt.title("relacion entre gasto_publicitario y ventas")
plt.xlabel("gasto_publicitario")
plt.ylabel("ventas")
plt.show()
