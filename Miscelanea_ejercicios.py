import math
import calendar

print()
menu = """Bienvenido a mi miscelanea de ejercicios, menu de operaciones:

        1.  Operadores
        2.  Condicionales
        3.  Ciclos
        99. Salir

        """
opcion = 0
opcion2 = 0
opcion3 = 0
opcion4 = 0

while opcion != 99:
    print(menu)
    opcion = int(input("Ingrese el valor de la tarea deseada. Digite 99 para salir: "))
    
    
    if opcion == 1:
        submenu = """
                Lista de operadores: 

                1--> Area de triangulo
                2--> Suma
                3--> Numero al cuadrado
                4--> Conversion dolares a euros
                5--> Area y perimetro de cuadrado
                6--> Area y volumen de un cilindro
                7--> Area y longitud de un circulo
                8--> Promedio de 3 numeros  
                9--> Volver
                """
        
        while opcion2 != 9:
            print(submenu)
            opcion2 = int(input("Ingrese operacion a realizar: "))
        
            if opcion2 == 1:
                base, altura = map(float,input("Ingrese el valor de la base y la altura ").split())
                triangulo = base * altura / 2
                print(f"El valor del area del triangulo es: {triangulo}")
                
                
            elif opcion2 == 2:
                num1, num2 = map(int,input("Digita los numeros a sumar: ").split())
                print("Tu suma es: ", num1 + num2)
                
            elif opcion2 == 3:
                num1 = int(input("Ingrese numero a elevar: "))
                cuadrado = pow(num1,2)
                print(f"El numero {num1} elevado al cuadrado es: {cuadrado}")
                

            elif opcion2 == 4:
                euro = float(input("Valor en euros: "))
                dolar = euro * 1.105
                print(f"{euro} euros es equivalente a: {round(dolar,2)} dolares ")
                

            elif opcion2 == 5:
                lado_cuadrado = int(input("Ingresa el valor del lado del cuadrado: ")) 
                area_c = lado_cuadrado *lado_cuadrado
                perimetro = lado_cuadrado * 4
                print(f"El area del cuadrado registrado es: {area_c}cm y su perimetro es: {perimetro}cm")
                

            elif opcion2 == 6:
                altura_cil, radio_cil = map(float, input("Ingrese la altura y el radio del cilindro: ").split())
                volumen = math.pi * radio_cil * radio_cil * altura_cil
                area_cil = 2.0 *math.pi * radio_cil * (radio_cil + altura_cil)
                print(f"El volumen del cilindro es: {volumen} y el area es: {area_cil} ")
                

            elif opcion2 == 7:
                radio_circulo = float(input("Ingrese el radio del circulo: "))
                lon_circulo = 2 * math.pi * radio_circulo
                area_circulo = math.pi * pow(radio_circulo,2)
                print(f"La longitud de la circunferencia es: {round(lon_circulo,2) } y su area es: {round(area_circulo,2)}")


            elif opcion2 == 8:
                prom1, prom2, prom3 = map(float,input("Ingrese 3 numeros para validar promedio: ").split())
                promedio = (prom1 + prom2 + prom3)//3
                print(f"El promedio del número es: {round(promedio,2)}")

            elif opcion2 == 9:
                opcion2 = 9

            else:
                print("Ingrese una opcion entre 1 y 8")

    elif opcion == 2:
        submenu = """
                Lista de condicionales: 

                1--> Numero positivo o negativo
                2--> Numero mayor o menor
                3--> ¿Cua es el numero mayor y menor de un conjunto de 3 numeros?
                4--> Dados dos números A y B, sumarlos si A es menor que B o sino restarlos
                5--> Dados dos números A y B encontrar el cociente entre A y B
                6--> Sumar 2 numeros si al menos uno de ellos es negativo, en caso contrario multiplicarlos.
                7--> Año bisiesto 
                8--> Volver  
                """

        while opcion3 != 8:
            print(submenu)
            opcion3 = int(input("Ingrese operacion deseada: "))

            if opcion3 == 1:
                num1 = int(input("Ingrese su numero: "))
                if num1 < 0:
                    print("Tu número es negativo")
                else:
                    print("Tu número es positivo")


            elif opcion3 == 2:
                num1, num2 = map(int,input("Ingrese 2 numeros: ").split())
                if num1 > num2:
                    print(f"{num1} es el mayor y {num2} es el menor")
                else:
                    print(f"{num2} es el mayor y {num1} es el menor") 


            elif opcion3 == 3:
                num1, num2, num3 = map(int,input("Ingrese 3 numeros: ").split())
                if num1 > num2 and num2 > num3:
                    print(f"{num1} es el mayor y {num3} es el menor")

                elif num2 > num1 and num2 > num3 and num3 > num1:
                    print(f"{num2} es el mayor y {num1} es el menor")

                elif num3 > num2 and num3 > num1 and num1 > num2:
                    print(f"{num3} es el mayor y {num2} es el menor")


            elif opcion3 == 4:
                num1, num2 = map(int,input("Ingrese 2 numeros, si el primero es mayor, sumara, sino, restara: ").split())
                if num1 > num2:
                    print("Suma!")
                    print("El resultado es " ,num1 + num2)
                else:
                    print("Resta!")
                    print("La resta de los números es: ", num1 - num2)

            elif opcion3 == 5:
                num1 , num2 = map(float,input("Ingrese el dividendo y el divisor: ").split())
                if num1 == 0 or num2 == 0:
                    print("No es posible dividir en ceros!! :(")
                else:
                    print("El cociente de la operacion es: ", (num1/num2))


            elif opcion3 == 6:
                num1 , num2 = map(float,input("Ingrese 2 numeros negativos o positivos: ").split())
                if num1 < 0 or num2 < 0:
                    print("Hay al menos un numero negativo!! Se sumará")
                    print("El resultado es: ",num1 + num2 )

                else:
                    print("No hay numeros negativos! Se multiplicará")
                    print("El resultado es: ", num1 * num2)

            elif opcion3 == 7:
                año = int(input("Ingrese un año cualquiera: "))

                bisiesto = calendar.isleap(año)

                if bisiesto == True:
                    print(f"{año} es un año bisiesto")
                else:
                    print("No es un año bisiesto")


            elif opcion3 == 8:
                opcion3 = 8

            else:
                print("Ingrese un valor entre 1 a 8")


    elif opcion == 3:

        submenu = """
                Lista de ciclos: 
                
                1--> Multiplos de 3 existentes entre 1 y 100
                2--> Números impares entre 0 a 100
                3--> Números pares entre 1 y 100
                4--> Cuadrados de los numeros del 1 al 30
                5--> Suma los cuadrados de los cien primeros números naturales
                6--> Números naturales en secuencia ascendente.
                7--> Suma de números ingresados mientras no sea cero
                8--> Volver  
                """

        while opcion4 != 8:
            print(submenu)
            opcion4 = int(input("Ingrese operacion deseada: "))

            if opcion4==1:
                print("Lista de multiplos de 3 hasta 100") 
                for i in range(3,100,3):
                    print(i)


            elif opcion4==2:
                print("Numeros impares del 0 al 100")
                for i in range(1,100,2):
                    print(i)

            elif opcion4==3:
                print("Numeros pares del 1 al 100") 
                for i in range(1,51):
                    print(i*2)

            elif opcion4==4:
                print("Cuadrados de los números del 1 al 30")
                for i in range(1,31):
                    print(i * i)

            elif opcion4==5:
                print("Suma de los cuadrados del 1 al 100")
                suma = 0
                for i in range(1,101):
                    cuadrado= i * i
                    suma+= cuadrado
                print(suma)


            elif opcion4==6:
                print("Numeros comprendidos")
                num1, num2 = map(int,input("Ingrese un numero de inicio y un numero final dentro del rango").split())

                for i in range(num1,num2+1):
                    print(i)

            elif opcion4==7:
                numero = 1
                sumar = 0
                while numero !=0:
                    numero = int(input("Ingrese cualquier cantidad de numeros. Digite 0 para terminar la suma: "))
                    sumar+=numero

                print(f"La suma total de tus números digitados fue: {sumar}")

            elif opcion4 == 8:
                opcion4 = 8

            else:
                print("Digite un valor entre 1 y 8")        

print()
print("Gracias por usar la miscelanea de ejercicios, vuelva pronto :) ")




