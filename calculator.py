calculadora

def sumar():
    num1 = int(input("ingrese un número: \n"))
    num2 = int(input("ingrese un número: \n"))
    resultado = num1 + num2
    print(f"{resultado})
    
def restar():
    
def Multiplicar():
    
def dividir():
    
def potencia():
    
def raiz():
    
def Salir():
    
    




print("1) sumar")
print("2) restar")
print("3) Multiplicar")
print("4) dividir")
print("5) potencia")
print("6) raiz")
print("7) Salir")

opcion =int(input("Escoga una opcion"))

match opcion:
    case 1:
        print("suma")
    
    case 2:
        print("resta")
    
    case 3:
        print("Multiplicar")
    
    case 4:
        print("dividir")
    
    case 5:
        print("potencia")
    
    case 6:
        print("raiz")
    case 7:
        print("salir")
        
    case _:
        print("Eror")
