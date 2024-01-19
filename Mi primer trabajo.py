def sumar():
    a2=float(input('primer numero '))
    b2=float(input('segundo numero'))
    print('El resultado de la operacion es: ',a2+b2)

def restar():
    a3=float(input('primer numero '))
    b3=float(input('segundo numero '))
    print('El resultado de la operacion es: ',a3-b3)
def multiplicar():
    a4=float(input('primer numero '))
    b4=float(input('segundo numero '))
    print(f"el resultado de la operacion es: {a4*b4} ")
def dividir():
    a5=float(input('primer numero '))
    b5=float(input('segundo numero '))
    print(f"el resultado de la operacion es: {a5/b5}")
def potenciar():
    a6=float(input('numero a potenciar '))
    b6=float(input('numero de potencia '))
    print(f"el resultado de la operacion es: {a6**b6}")
def menu():
    a1=input('que operacion desea realizar? ')
    a1=a1.lower()
    if a1== 'suma':
        sumar()
    if a1== 'resta':
        restar()
    if a1 =='multiplicacion':
        multiplicar()
    if a1 == 'division':
        dividir()
    if a1=='potenciacion':
        potenciar()
    rep=input('Desea realizar otra operacion? ')
    rep=rep.lower()
    while rep=='si':
        menu()
    print('bye byeee')
    
menu()

