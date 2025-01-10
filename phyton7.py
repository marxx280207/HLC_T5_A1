def sumar(num1,num2):
    return num1+num2

def sumardatos():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    resultado = sumar(num1,num2)
    print(f"La suma de {num1} y {num2} es {resultado}.")

sumardatos()

