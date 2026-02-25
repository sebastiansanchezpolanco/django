from django.db import models
import oracledb 

# Create your models here.
class Serie:
    def __init__(self):
        self.idSerie=0
        self.nombre=""
        self.imagen=""
        self.anyo=0

class Personaje:
    def __init__(self):
        self.idPersonaje=0
        self.nombre=""
        self.imagen=""
        self.idSerie=0

class ServiceSeries:
    def __init__(self):
        self.connection=oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1")
    def getSeries(self):
        sql="select * from SERIES"
        cursor=self.connection.cursor()
        cursor.execute(sql)
        listaSeries=[]
        for row in cursor:
            serie=Serie()
            serie.idSerie=row[0]
            serie.nombre=row[1]
            serie.imagen=row[2]
            serie.anyo==row[3]
            listaSeries.append(serie)
        cursor.close() 
        return listaSeries
    def getPersonajesSeries(self, idserie):
        sql="select * from PERSONAJES where IDSERIE=:id"
        cursor=self.connection.cursor()
        cursor.execute(sql, (idserie, ))
        listaPersonajes=[]
        for row in cursor:
            personaje=Personaje()
            personaje.idPersonaje=row[0]
            personaje.nombre=row[1]
            personaje.imagen=row[2]
            personaje.idSerie=row[3]
            listaPersonajes.append(personaje)
        cursor.close() 
        return listaPersonajes
    def insertarPersonaje(self, personaje, imagen, idserie):
        sql="select MAX(idpersonaje)+1 as maximo from PERSONAJES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        idnuevopersonaje=int(cursor.fetchone()[0])
        sql="insert into PERSONAJES (:idnuevopersonaje, :personaje, :imagen, :idserie)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (personaje, imagen, idserie))
        self.connection.commit()
        cursor.close()  

