from zeep.client import Client
import zeep

settings = zeep.Settings(strict=False, xml_huge_tree=True)
wsdl = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'
cliente = Client(wsdl)

ListEstudiantes = cliente.service.getListaEstudiante()

def consultar(matricula):
    Estudiante = cliente.service.getEstudiante(matricula)
    return Estudiante

def CrearEstudiante(matricula, nombre, carrera):
    factory = cliente.type_factory('http://soap.eict.pucmm.edu/')
    nuevoEstudiante = factory.estudiante(carrera=carrera, matricula=carrera, nombre=nombre)
    creado = cliente.service.crearEstudiante(nuevoEstudiante)
    return creado

def EliminarEstudiante(matricula):

    return cliente.service.eliminarEstudiante(matricula)

print("[INFO] LISTA DE ESTUDIANTES: ")
for est in ListEstudiantes:
    print('[Nombre]: ' + est.nombre + ' [Matricula]: ' + str(est.matricula))


print('[INFO] Ingrese matricula del Estudiante que desea consultar:  {DEFAULT= 20011136} \n')
id = input()
print('[INFO] ESTUDIANTE CONSULTADO: \n' + str(consultar(matricula=id)))

print('[INFO] Ingrese Información del Nuevo Estudiante que desea CREAR: ')
print('[CARRERA]: ')
carrera = input()
print('[matricula]: ')
matricula = input()
print('[nombre]: ')
nombre = input()

print('[INFO] ESTUDIANTE CREADO: ' + str(CrearEstudiante(matricula=matricula,nombre=nombre,carrera=carrera)))

print('[INFO] Matricular del Estudiante que desea ELIMINAR: ')
id = input()
if(EliminarEstudiante(matricula=id)):
    print('[INFO] ESTUDIANTE Eliminado!')

print('~(^_^)~ --[HAPPY CODING!!]-- ~(^_^)~ ')



