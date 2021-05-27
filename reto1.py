
print('“Bienvenido al sistema de ubicación para zonas públicas WIFI')

usuario = 51707
contraseña = 70715
numero_1 = 707
numero_2 = (5*1-7+1+1)+(7%5-1-1)+(7**1/7-1)

ingreso_usuario = int(input('Ingrese su usuario: '))

if ingreso_usuario != usuario: 
    print('Error')
else: 
    ingrese_contraeña = int(input('Ingrese su contraseña: '))

    if ingrese_contraeña != contraseña:
        print('Error')
    else: 
        print(numero_1, '+', numero_2, '=')
        captcha = int(input('Respuesta:  '))

        if captcha == numero_1 + numero_2:
            print('Sesión iniciada')
        
        else:
            print('Error')






