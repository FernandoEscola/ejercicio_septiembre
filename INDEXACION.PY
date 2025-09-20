import pandas as pd
Empleados=pd.DataFrame({
    "id_empleados":[101,102,103,104,105,106,107],
    "nombre":["Luis Garcia","Ana Martinez","Sofia Lopez","Carlos Roa","Maria Diaz",
              "Pedro Ramirez", "Elena Jimenez"],
    "Edad":[28,30,64,56,26,32,45],
    "departamento": ["Ventas","TI","RH","RH","Finanzas","Ventas","TI"],
    "cargo":["Asistente","Analista","Gerente","Coordinador","Contador","Asesor","Analista"],
    "fecha_contratacion":['15-01-2020', '20-05-2018', '10-11-2015','20-08-2016',
                                        '15-07-2021', '01-12-2017','28-02-2022'],
    "salario" :[30000, 45000, 88000,52000, 41000, 36000, 48000 ]                                 
   })
print(Empleados)
print("*"*100)
print("indexacion por nombres:")
print("registro 2:")
print(Empleados.iloc[1])
print("*"*100)
print("registro 1:")
print(Empleados.loc[0])
print("*"*100)
print("registro 1:")
print(Empleados.loc[:,["nombre","Edad"]])
print("*"*100)
print("Empleados a pensionarse:")
print(Empleados[Empleados["Edad"]>=50])
print("*"*100)
print("imprime 3 registros;")
print(Empleados.loc[0:2])
print("*"*100)
print("imprime rangos:")
print(Empleados.iloc[0:2,0:3])
print("*"*100)
print("nueva colomna de comision:")
Empleados["comision"]=Empleados["salario"]*0.08
Empleados["salario total"]=Empleados["salario"]+Empleados["comision"]
Empleados.loc[Empleados["salario"]<=35000,"salario"]+=2500
print(Empleados)
print(Empleados[["nombre","salario","comision","salario total"]])
print("*"*100)
Empleados["perfil"]=Empleados["departamento"]+"_"+Empleados["cargo"]
print(Empleados)
print("*"*100)
Empleados=Empleados.drop(columns=["perfil"])
print(Empleados)
print("*"*100)
Empleados=Empleados.rename(columns={"id_empleados":"id"})
print(Empleados)
