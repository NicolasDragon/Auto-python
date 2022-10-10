import datetime
from math import radians, sin , cos , acos
from turtle import pen
lugar1=[]
lugar2=[]
slat=[]
slon=[]
elat=[]
elon=[]
dist=[]	
pago=[]
pago=0
dist=0
a=0
print("Menu Pincipal: \n 1-Registrarse \n 2-Comenzar una carrera \n 3-Salir \n")
i=1
auto="Apagado"
velocidad=0
opc = int(input("Ingrese una opcion: "))
while opc != 3:
    if opc == 1 and a==0:
        nombre=[]
        rut=[]
        modelo=[]
        patente=[]
        cantidad=input("¿Cuantos autos desea ingresar? ")
        for x in range(int(cantidad)):
            nombre.append(input("Nombre: "))
            rut.append(input("Rut: "))
            patente.append(input("Patente: "))
            modelo.append(input("Modelo: "))
            print("")
        print("Nombre: ", nombre)
        print("Rut: ", rut)
        print("Patente: ", patente)
        print("Modelo: ", modelo)
        a=1
    else:
        print("Debe registrarse primero")
    if opc== 2 and a==1:
        print("Menu principal")
        print ("1. Ingresar ubicacion GPS Latitud e ingresar ubicacion gps longitud \n 2. Ver horario \n 3. Encender el vehiculo \n 4. Apagar el vehiculo \n 5. Acelerar \n 6. Girar \n 7. Mostrar todos los datos \n 8. Salir \n")
        opc2 = int(input("Ingrese una opcion: "))
        while opc2 != 9:
            if opc2 == 1:
                for x in range(int(cantidad)):
                    print("Ingrese las coordenadas de dos puntos para calcular la distancia entre ellos")
                    lugar1.append(input("¿En que lugar comienza el recorrido?: "))
                    slat.append(radians(float(input("Latitud del primer lugar: "))))
                    slon.append(radians(float(input("Longitud del primer lugar: "))))
                    lugar2.append(input("¿En donde terminar el recorrido?: "))
                    elat.append(radians(float(input("Latitud del segundo lugar: "))))
                    elon.append(radians(float(input("longitud del segundo lugar:"))))
                    dist = 6371.01 * acos(sin(slat[x])*sin(elat[x]) + cos(slat[x])*cos(elat[x])*cos(slon[x] - elon[x]))
                    r = round(dist, 2)
                    print("La distancia entre: " ,lugar1[x], "y" ,lugar2[x], "es" , r, "Km")
                    precio = int(input("¿Valor del kilometro por hora? en pesos chilenos: "))
                    pago=dist*precio
                    p = round(pago, 2)
                    print("El pago es: ", p, "pesos")
            elif opc2 == 2:
                import datetime
                print(datetime.datetime.now())
            elif opc2 == 3:
                for x in range(int(cantidad)):
                    auto="Encendido"
                    print("El auto esta", auto)
            elif opc2 == 4:
                for x in range(int(cantidad)):
                    auto="Apagado"
                    print("El auto esta apagado")
                if velocidad !=0:
                    print("No se puede apagar el vehiculo")
                else:
                    auto="Apagado"
            elif opc2 == 5 and auto=="Encendido":
                for x in range(int(cantidad)):
                    velocidad=int(input("Ingrese la velocidad: "))
                    print("La velocidad es: ", velocidad)
            elif opc2 == 6:
                for x in range(int(cantidad)):
                    direccion=input("Ingrese la direccion: ")
                    print("La direccion es: ", direccion)
            elif opc2 == 7:
                if dist != 0 and pago !=0:
                    for x in range(int(cantidad)):
                        print("Nombre: ", nombre[x])
                        print("Rut: ", rut[x])
                        print("Patente: ", patente[x])
                        print("Modelo: ", modelo[x])
                        print("La distancia entre: " ,lugar1[x], "y" ,lugar2[x], "es" , r, "Km")
                        print("El pago es: ", p, "pesos")
                        print("El auto esta", auto)
                        print("La velocidad es: ", velocidad)
                        print("La direccion es: ", direccion)
                    print(datetime.datetime.now())
                else :
                    print("Debe ingresar las coordenadas")
            elif opc2 == 8:
                print("Gracias por usar el programa")
                exit()
            else:
                print("Opcion no valida")
            opc2 = int(input("Ingrese una opcion: "))    
    else:
        opc = int(input("Ingrese una opcion: "))
print("Ha salido del programa")
