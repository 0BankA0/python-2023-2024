while True:
    
    
    izvele = input("izvelies operaciju(+ , - , *, /): ")

    if izvele in ('+','-','*','/'):
        try:
            num1= float(input('ievadi pirmo skaitli: '))
            num2= float(input('ievadi otro skaitli: '))
        except ValueError:
            print('izvelies operaciju ievadi +, -, *, /')
            continue

        if izvele == '+':
            print(num1 + num2)
            
        elif izvele == '-':
            print(num1 - num2)
            
        elif izvele == '*':
            print(num1 * num2)
            
        elif izvele == '/':
            print(num1 / num2)
            
        turpinat= input('vai velies turpināt?(yes / no): ')
        if turpinat == 'no':
            break