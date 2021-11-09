from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura
class Grupo:
    grado = 12
    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        list=[]
        for x in kwargs.values():
            list.append(x)
        self._asignaturas = list
            #self._asignaturas.append(Asignatura(x))

    '''def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = [alumno]'''

    def agregarAlumno(self, alumno=None, lista=None):
        if (lista is None):
            lista=[]  
            lista.append(alumno)   
            self.listadoAlumnos = lista
        elif(alumno!=None):
            lista.append(alumno)
            self.listadoAlumnos = lista  
        else:
            self.listadoAlumnos = lista   

    def __str__(self) -> str:
        grup = "Grupo de estudiantes: "+ self._grupo 
        return grup          

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre