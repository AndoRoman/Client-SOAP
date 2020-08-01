from zeep import client
import zeep

settings = zeep.Settings(strict=False, xml_huge_tree=True)
cliente = zeep.client('http://localhost:7000/ws/EstudianteWebServices?wsdl', settings=settings)

with zeep.client.Settings(raw_response=True):
    ListEstudiantes = cliente.EstudianteWebServicesService.getListaEstudiante()


print("[INFO] LISTA DE ESTUDIANTES\n\n " + str(ListEstudiantes))

print()