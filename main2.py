from suds.client import Client
url = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'
client = Client(url)
#Printeando
print (client.service.getListaEstudiante())