import pandas as pd 
df = pd.read_csv("ejercicio_7_prueba.csv")
print(df.head())
df.to_excel("ejercicio_7_prueba.xlsx", index=False)
df.to_json("ejercicio_7_prueba.json", orient="records", lines=True)
df.to_html("ejercicio_7_prueba.html", index=False)
df.to_csv("ejercicio_7_prueba_modificado.csv", index=False)
df.to_csv("ejercicio_7_prueba_modificado_puntoycoma.csv", index=False, sep=';')
df.to_csv("ejercicio_7_prueba_modificado_tab.csv", index=False, sep='\t')
df.to_csv("ejercicio_7_prueba_modificado_espacio.csv", index=False, sep=' ')
df.to_csv("ejercicio_7_prueba_modificado_pipe.csv", index=False, sep='|')
print("Archivos creados exitosamente.")



