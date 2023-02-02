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
                select(Cancion)
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

    def update(cancion):
        try:
            with engie.connect() as connection:
                connection.execute(
                    update(Cancion)
                    .where(Cancion.id == cancion["id"])
                    .values(
                        nombre=cancion["nombre"],
                        duracion = cancion["duracion"],
                        artista = cancion["artista"],
                        album = cancion["album"],
                        calificaion =cancion["calificaion"]
                    )
                )
                connection.commit()
                connection.close()
        except Exception as err:
            return err
        return "ok"

    def delete(cancion):
       
        with engie.connect() as connection:
            try:
                connection.execute(
                    delete(Cancion).where(
                        Cancion.id == cancion["id"]
                    )
                )
                connection.commit()
                connection.close()
            except Exception as err:
                return err
        return "ok"
   





try:
    DATABASE.metadata.create_all(engie)
except:
    pass
