import pandas as pd
url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)

nuevos_nombres = {
    'sepal_length': 'longitud_sepalo',
    'sepal_width': 'ancho_sepalo',
    'petal_length': 'longitud_petalo',
    'petal_width': 'ancho_petalo',
    'species': 'especie'
}


df.rename(columns=nuevos_nombres, inplace=True)

df.columns = df.columns.str.upper()
print("\nEncabezados cambiados exitosamente a español\n")
print(df)
print("\nSe conectó exitosamente\n")