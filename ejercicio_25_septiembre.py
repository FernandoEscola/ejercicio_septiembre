import pandas as pd

#Crear DataFrame de ejemplo
Data={
    "ID":[1,2,2,3,4],
    "Nombre":["Ana","Luis","Luis","Carlos","Mary"],
    "Edad":[23,34,34,29,42]
}
df=pd.DataFrame(Data)
print("*"*100)

#Identificar Duplicados
print("El registro 2 es un duplicado")
print(df.duplicated())
print("*"*100)

#Contar Duplicados
print(f"Hay {df.duplicated().sum()} dato duplicado")
print("*"*100)

#Identificar duplicados en columnas específicas
print(f"Resultado booleano en columnas específicas con duplicados:\n{df.duplicated(subset=["ID","Nombre"])}")
print("*"*100)

#Eliminar duplicados directamente
df_Sin_Duplicados=df.drop_duplicates()
print(f"Datos sin duplicados:\n{df_Sin_Duplicados}")
print("*"*100)

#Mantener por defecto la primera aparición 
df_first=df.drop_duplicates(keep="first")
print(f"Mantiene la primera fila repetida:\n{df_first}")
print("*"*100)

#Mantener por defecto la primera aparición 
df_last=df.drop_duplicates(keep="last")
print(f"Mantiene la segunda fila repetida:\n{df_last}")
print("*"*100)

#Detección y eliminación de duplicados en columna específica
df=df.drop_duplicates(subset=["ID"],keep="first")
print(f"Mantiene la primera fila repetida:\n{df}")
print("*"*100)

#CONVERSIÓN DE TIPO DE DATOS
print(f"Imprimir tipos de datos\n{df.dtypes}")
print("*"*100)

#Convertir una columna a número
df["Edad"]=pd.to_numeric(df["Edad"], errors="coerce")
print(f"Columna convertida a número:\n{df}")
print("*"*100)

#Nuevo DataFrame de Fechas
Data = {"Fechas": ["2025-01-01", "2025-02-15", "2025/03/01"]}
df = pd.DataFrame(Data)
print(f"DataFrame de Fechas:\n{df}")
print("*"*100)

# #Convertir la columna a Datatime
# df["Fechas"] = pd.to_datetime(df["Fechas"])
# print(f"DataFrame convertido a formato datatime:\n{df}")
# print("*"*100)

# df["Fechas"]= pd.to_datetime(df["Fechas"],format="%Y-%m-%d")
# print(f"DataFrame en nuevo formato:\n{df}")
# print("*"*100)

#Nuevo DataFrame de Fechas
Data = {"Fechas": ["2025-01-01", "2025-02-15", "2025/03/01"]}
df = pd.DataFrame(Data)
print(f"DataFrame de Fechas:\n{df}")
print("*"*100)

# Estandarizamos las fechas: reemplazamos '/' por '-'
df["Fechas"] = df["Fechas"].str.replace('/', '-')
print(f"Fechas estandarizadas:\n{df}")
print("*"*100)

# Ahora convertimos a datetime
df["Fechas"] = pd.to_datetime(df["Fechas"], errors="coerce")
print(f"DataFrame convertido a formato datatime:\n{df}")
print("*"*100)

# Formateamos para mostrar día primero usando la función format
df["Fechas_formateadas"] = df["Fechas"].apply(lambda x: format(x, "%d-%m-%Y"))
print(f"DataFrame con el día primero:\n{df}")

# Formateamos para mostrar día primero
df["Fechas_formateadas"] = df["Fechas"].dt.strftime("%d-%m-%Y")
print(f"DataFrame con el día de primeras\n{df}")

df["Fechas_formateadas"]=pd.to_datetime(df["Fechas"],errors="coerce")
print(f"DataFrame convertido a formato datatime:\n(df{"Fechas_formateadas"})")
print(f"DataFrame con el dia primero:\n{df}")

Data={
    "ID":[1,2,2,3,4],
    "Nombre":["Ana","Luis","Luis","Carlos","Mary"],
    "Edad":[23,34,34,29,42]
}
df=pd.DataFrame(Data)

df["Nombre"]=df["Nombre"].astype(str)
print(df)
print("*"*100)
df["Edad"]=df["Edad"].astype(int)
print(df)
print("*"*100)
df["Edad"]=df["Edad"].astype(float)
print(df)
print("*"*100)

