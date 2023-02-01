__version__ = '1.0'
__author__ = 'Julian Camilo Builes Serrano'

from sqlalchemy import (
    Column,
    String,
    Float,
    ForeignKey,
    insert,
    update,
    delete,
    select
)

from components.db_conection import DATABASE, engie

# from db_conection import DATABASE,engie


class Cancion(DATABASE):
    """Clase que contiene la estructura de el tecnico
    y tambien permite realizar el mapeo de clase a entidad
    relacion por medio de sqlalchemy

    Args:
        DATABASE (DATABASE): estructura que permite heradar los 
        atributos para generar el mapeo a la bd
    """
    __tablename__ = "cancion"
    id = Column(String(20), primary_key=True)
    nombre = Column(String(30), nullable=False)
    duracion = Column(String(10), nullable=False)
    artista = Column(String(50),nullable=False)
    album = Column(String(50),nullable=False)
    calificaion = Column(Float,nullable=False)
    def get_all():       
        query = """select id,nombre,duracion,artista,album,calificaion from cancion;"""
        with engie.connect() as connection:
            result = connection.execute(
                query
            )
            
            connection.close()
        return result.all()

    def instert(cancion):
        with engie.connect() as connection:
            if 1:
                connection.execute(
                    insert(Cancion).values(
                        id=cancion["id"],
                        nombre=cancion["nombre"],
                        duracion = cancion["duracion"],
                        artista = cancion["artista"],
                        album = cancion["album"],
                        calificaion =cancion["calificaion"]
                    )
                )
                connection.commit()
                connection.close()
            # except Exception as err:
            #     return err
        return "ok"

    def update(tecnico):
        try:
            with engie.connect() as connection:
                connection.execute(
                    update(Tecnico)
                    .where(Tecnico.id == tecnico["id"])
                    .values(
                        nombre=tecnico["nombre"],
                        sueldo=tecnico["sueldo"],
                        sucursal_id=tecnico["sucursal_id"],
                    )
                )
                for elemento in tecnico["elementos"]:
                    elemento_id =  elemento["id"]
                    cantidad = elemento["cantidad"]
                    connection.execute(
                        update(ElementoXTecnico)
                        .where(
                            ElementoXTecnico.elemento_id == elemento_id
                            and ElementoXTecnico.tecnico_id == tecnico["id"]
                        )
                        .values(cantidad=cantidad)
                    )
                connection.close()
        except Exception as err:
            return err
        return "ok"

    def delete(tecnico):

        with engie.connect() as connection:
            connection.execute(
                delete(ElementoXTecnico).where(
                    ElementoXTecnico.tecnico_id == tecnico["id"]
                )
            )
            connection.execute(delete(Tecnico).where(Tecnico.id == tecnico["id"]))
            connection.close()
    def get_elementos(tecnico):
        id =  tecnico["id"]
        query = """
            select t.id,et.cantidad,e.id, e.nombre, e.descripcion from test.tecnico t 
            inner join test.elementoxtecnico et on t.id = et.tecnico_id
            inner join test.elemento e on et.elemento_id =  e.id
            where t.id = '{}';""".format(str(id))
        with engie.connect() as connection:
            result = connection.execute(query)
            print(result)
            connection.close()

        return result.all()






try:
    DATABASE.metadata.create_all(engie)
except:
    pass
