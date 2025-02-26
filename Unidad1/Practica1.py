
#Simulacion
## Unidad 2
### Practica 1.Generacion de numeros aleatorios por el metodo de centros al cuadrado
##Profesor: 
##Alumno:Daniel Ximena Rivera Gutierrez Macias

##Semilla Inicial
semilla=2005
n=4
resultados=[]
iteraciones = 100
resultados=[]

for _ in range(iteraciones): 
    #Elevar la semilla al cuadrado
    cuadrado=str(semilla**2).zfill(2 * n) #Agregar los espacios necesarios
    #Extraer los digitos centrales
    inicio=(len(cuadrado)-n)//2
    semilla=int(cuadrado[inicio:inicio + n])
    resultados.append(semilla)

    #Imprimir los resultados 
    for i, numero in enumerate(resultados, 1):
        print (f"Numero Aleatorio{i}:{numero}")
