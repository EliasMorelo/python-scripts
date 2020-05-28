#Codigo para registar paciente a un hospital, validando su información y luego mostrando los pacientes

pacientes = []

n = int(input("Ingrese la cantidad de pacientes a ingresar: "))
    
for i in range(0, n):
    paciente = []
    print ("Ingresando datos del paciente "+str(i+1))

    nombre = (input("Ingrese el nombre del paciente: "))
    paciente.append(nombre)
    edad = int(input("Ingrese la edad del paciente: "))
    if(edad<=0): 
        print("ERROR: el número que indicaste no es valido")
        continue;
    else: 
        paciente.append(edad)
        enfermedad = (input("Ingrese la enfermedad del paciente: "))
        paciente.append(enfermedad)
        estadoDeSalud = int(input("Ingrese el estado de salud\n"+
        "Digite 1 si es critico\n"+
        "Digite 2 si es regular\n"+
        "Digite 3 si es estable\n"+
        ":        "))
        if((estadoDeSalud > 0) and (estadoDeSalud < 4)):
            paciente.append(estadoDeSalud)
            pacientes.append(paciente)
        else:
            print("ERROR: el número que indicaste no es valido")
            continue;

print("----------------Mostrando pacientes-----------------")
for paciente in pacientes:
    print()
    print ("Nombre del paciente: "+ str(paciente[0]))
    print ("Edad del paciente: "+ str(paciente[1]))
    print ("Enfermedad del paciente: "+ str(paciente[2]))
    if(paciente[3] == 1):
        estado = "Critico"
    elif(paciente[3]== 2):
        estado = "Regular"
    else:
        estado = "Estable"
    print ("Estado de salud del paciente: " + estado)
    print()
    print("----------------------------------------------------")

