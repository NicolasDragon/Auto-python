import pygame
class Vehiculo:
    def acelerar(self,cuanto=0)-> None:
        self.velocidad += 10 + cuanto
    def frenar(self,cuanto=0)-> None:
        self.velocidad -= 10 + cuanto
    def avanzar(self):
        self.lat += (self.velocidad/100)+5
        pass
    def retroceder(self):
        self.lat -= (self.velocidad/100)+5
        pass
    def __init__(self,velocidad=0,lat=0.0,lon=300.0,modelo="",ppu="",color="") -> None:
        self.velocidad = velocidad
        self.lat = lat
        self.lon = lon
        self.modelo = modelo
        self.ppu = ppu
        self.color= color
    def __str__(self)->str:
        return (f'El vehiculo {self.modelo} patente {self.ppu} color {self.color} va a {self.velocidad} km/h')
class Carretera: 
    ejex = 0.0
    ejey = 0.0
carretera = Carretera()
objeto = Vehiculo()
pygame.init()
ventana = pygame.display.set_mode((1024,900))
autito = pygame.image.load('./car.png').convert_alpha()
fondo = pygame.image.load('./fondo.png').convert_alpha()
enemigo = pygame.image.load('./enemigo.png').convert_alpha()
while(True):
    for event in pygame.event.get():
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_d):
            objeto.acelerar()
            objeto.avanzar()
            print(objeto)    
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_a):
            objeto.frenar()
            objeto.retroceder() 
            print(objeto)
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_s):
            objeto.lon +=10
            pass   
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_w):
            objeto.lon -= 10
            pass
    carretera.ejex -= objeto.velocidad/100
    if(carretera.ejex<-500):
        carretera.ejex = 0
    ventana.blit(fondo,(carretera.ejex,carretera.ejey))
    ventana.blit(autito,(objeto.lat,objeto.lon))
    pygame.display.update()