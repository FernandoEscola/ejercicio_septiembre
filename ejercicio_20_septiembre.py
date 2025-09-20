import pandas as pd

# datos = {
#     "producto": ["manzanas", "peras","bananas","naranjas"],
#     "precio": [2.5,3.0,1.8,2.2],
#     "cantidad": [100,150,200,80], 
#     "mes": ["enero","enero","febrero","febrero"]}
# df = pd.DataFrame(datos)
# print(df)# muestra data frame
# print("*"*100)
# print(df.iloc[0:2])
# print("*"*100)
# print(df.loc[:,["producto","cantidad"]])
# print("*"*100)
# print(df["precio"]*1.10)
# print("*"*100)
# df["ingresos"] = df["precio"]* df["cantidad"]
# print(df["ingresos"])



import pandas as pd
Datos = {
    'nombre': ['Ana', 'Carlos', 'María', 'Juan', None, 'Laura', 'Pedro', 'Sofía', 'Miguel', 'Elena'],
    'edad': [25, 32, None, 45, 29, 31, None, 28, 35, 27],
    'ciudad': ['Bogotá', 'Medellín', None, 'Cali', 'Villavicencio', None, 'Barranquilla', 'Cali', 'Bogotá', None],
    'departamento': ['Ventas', None, 'IT', 'Ventas', 'RH', 'IT', None, 'Marketing', 'IT', 'Marketing'],
    'fecha_contratacion': pd.to_datetime(['15-01-2020', '20-05-2018', None, '10-11-2015', '05-03-2019', 
                                        '15-07-2021', '01-12-2017', None, '20-08-2016', '28-02-2022']),
    'salario': [30000, 45000, 38000, None, 52000, 41000, 36000, None, 48000, 43000]
}

df = pd.DataFrame(Datos)
print("*"*100)
print(pd.DataFrame(Datos))#imprimir informacion
print("*"*100)
print(df.isnull())#identificar valores nulos 
print("*"*100)
print(df.isnull().sum())#contar valorres nulos
print("*"*100)
df_sin_nulos = df.dropna()#Eliminar filas que contengan almenos un valor nulo 
print(df_sin_nulos)
print("*"*100)
df_sin_columnas_nulas = df.dropna(axis=1)#Eliminar columnas que contengan almenos un valor nulo 
print(df_sin_columnas_nulas)
print("*"*100)
df.dropna(how="all",inplace=True)#Eliminar filas donde todos los valores sean nulos
# df["edad"]=df["edad"].fillna(0)
print(df)
print("*"*100)
df["edad"]=df["edad"].fillna(df["edad"].mean())
print(df)
print("*"*100)
df["edad"]=df["edad"].fillna(df["edad"].median())
print(df)
print("*"*100)
df["salario"]=df["salario"].fillna(df["salario"].mode())
print(df)
print("*"*100)
df["edad"]=df["edad"].interpolate()
print(df)
