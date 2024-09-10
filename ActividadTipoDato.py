#Actividad 1
lista=[4,5,6,7,8,9]
operacion=[]
for i in lista:
    operacion.append(i**2)

print(f"\nLista original: {lista}\nlista con los numeros elevados al cuadrado: {operacion} \n\n//////////////////////////////////\n")

#Actividad 2
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

mensaje=f"Hola, mi nombre es {nombre} y tengo {edad} años"

print(mensaje,"\n\n/////////////////////////////////\n")

#Actividad 3
if edad>=18:
    msj="Usted es mayor de edad"
else:
    msj="Usted es menor de edad"

print(msj,"\n\n////////////////////////////////////\n")

#Actividad 4
saldo=50.0
while saldo>10:
    retiro=15.0
    saldo-=retiro
    print(F"Se ha retirado {retiro} saldo actual {saldo}")
print("\n//////////////////////////////////\n")

#Actividad 5 
persona={
    "nombre":"Valery",
    "edad": 17,
    "Ciudad": "Sevilla"
}
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")



