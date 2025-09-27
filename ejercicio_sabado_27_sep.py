import matplotlib.pyplot as plt

productos =  ["manzanas", "peras","bananas","naranjas"]
ventas = [100,150,200,80]
plt.bar(productos, ventas)
plt.title("ventas por producto")
plt.xlabel("productos")
plt.ylabel("ventas")
plt.show()
