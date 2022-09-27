import datetime
from math import radians, sin , cos , acos
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
        nombre=input("Ingrese su nombre y apellido: ")
        rut=input("Ingrese su rut: ")
        modelo=input("Ingrese el modelo de su auto: ")
        patente=input("Ingrese la patente de su auto: ")
        a=1
    else:
        print("Debe registrarse primero")
    if opc== 2 and a==1:
        print("Menu principal")
        print ("1. Ingresar ubicacion GPS Latitud e ingresar ubicacion gps longitud \n 2. Ver horario \n 3. Encender el vehiculo \n 4. Apagar el vehiculo \n 5. Acelerar \n 6. Girar \n 7. Mostrar todos los datos \n 8. Salir \n")
        opc2 = int(input("Ingrese una opcion: "))
        while opc2 != 9:
            if opc2 == 1:
                print("Ingrese las coordenadas de dos puntos para calcular la distancia entre ellos")
                slat = radians(float(input("Latitud del primer punto: ")))
                elat = radians(float(input("Latitud del segundo punto: ")))
                slon = radians(float(input("Longitud del primer punto: ")))
                elon = radians(float(input("longitud del segundo punto:")))
                dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
                print("La distancia entre los dos puntos es: ", dist, "Km")
                precio = int(input("valor del kilometro por hora? en pesos chilenos: "))
                pago=dist*precio
                print("El pago es: ", pago, "pesos")
            elif opc2 == 2:
                import datetime
                print(datetime.datetime.now())
            elif opc2 == 3:
                auto="Encendido"
                print("El auto esta encendido")
            elif opc2 == 4:
                if velocidad !=0:
                    print("No se puede apagar el vehiculo")
                else:
                    auto="Apagado"    
                print("Auto apagado")
            elif opc2 == 5 and auto=="Encendido":
                n = int(input("Cantidad de veces que desea acelerar: "))
                while n > 0:
                    velocidad += 10
                    print("Usted está viajando a", velocidad ,"Km/h")
                    n -= 1
            elif opc2 == 6:
                f = int(input("Ingrese el angulo de giro: "))
                if f > 0 and f < 360:
                    print("El auto gira a", f, "grados")
                else:
                    print("El angulo de giro debe estar entre 0 y 360")
            elif opc2 == 7:
                if dist != 0 and pago !=0:
                    print("Nombre: ", nombre, "\n Rut: ", rut, "\n Modelo: ", modelo, "\n Patente: ", patente, "\n Distancia Recorrida: ", dist, "\n Velocidad: ", velocidad, "\n Pago: ", pago , "\n El vehiculo ha girado : ", f, "grados")
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

