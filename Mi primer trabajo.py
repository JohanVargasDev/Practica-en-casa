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
def menu():
    a1=input('que operacion desea realizar? ')
    a1=a1.lower()
    if a1== 'suma':
        sumar()
    if a1== 'resta':
        restar()
    if a1 =='multiplicar':
        multiplicar()
    rep=input('Desea realizar otra operacion? ')
    rep=rep.lower()
    while rep=='si':
        menu()
    print('bye byeee')
    
menu()

