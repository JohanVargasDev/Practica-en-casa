def sumar():
    a2=int(input('primer numero '))
    b2=int(input('segundo numero'))
    print('El resultado de la operacion es: ',a2+b2)

def restar():
    a3=int(input('primer numero '))
    b3=int(input('segundo numero '))
    print('El resultado de la operacion es: ',a3-b3)
def menu():
    a1=input('que operacion desea realizar? ')
    a1=a1.lower()
    if a1== 'suma':
        sumar()
    if a1== 'resta':
        restar()
    rep=input('Desea realizar otra operacion? ')
    rep=rep.lower()
    while rep=='si':
        menu()
    print('bye byeee')
    
menu()

