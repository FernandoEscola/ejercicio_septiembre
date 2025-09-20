from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///mi_base_datos.db')
metadata = MetaData()

# Definir y crear la tabla
mi_tabla = Table('mi_tabla', metadata,
    Column('id', Integer, primary_key=True),
    Column('Nombre', String(50)),
    Column('Edad', Integer), 
    Column('Ciudad', String(50))
)

metadata.create_all(engine)

#Consultar tabla
from sqlalchemy import select
with engine.connect() as Conexion:
    Consultar=select(mi_tabla)
    Resultado=Conexion.execute(Consultar)
    for Fila in Resultado:
        print(Fila)

#Actualizar tabla
from sqlalchemy import update
with engine.connect() as Conexion:
    Actulizar=update(mi_tabla).where(mi_tabla.c.id==4).values(Nombre="Karina",Edad=38,Ciudad="Granada")
    Resultado=Conexion.execute(Actulizar)
    Conexion.commit()
    
# #Eliminar Registro
# from sqlalchemy import delete
# with engine.connect() as Conexion:
#     Eliminar=delete(mi_tabla).where(mi_tabla.c.id==4)
#     Resultado=Conexion.execute(Eliminar)
#     Conexion.commit()
    
#Insertar registros
from sqlalchemy import insert
with engine.connect() as Conexion:
    Insertar=insert(mi_tabla).values(Nombre="Héctor", Edad=42, Ciudad="Bogotá")
    Insertar=insert(mi_tabla).values(Nombre="Maria", Edad=32, Ciudad="Bogotá")
    Insertar=insert(mi_tabla).values(Nombre="Claudia", Edad=51, Ciudad="Bogotá")
    Resultado=Conexion.execute(Insertar)
    Conexion.commit()
