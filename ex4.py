a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

delta = (b**2) -(4*a*c)

if delta < 0 :

    print('X inexistente dentro do conjunto Real')

elif  delta == 0:

    x1 = (-b+delta**(1/2))/(a*2)
    
    print('x\' e x\'\' valem: ' , x1)

else :
    
    x1 = (-b+delta**(1/2))/(a*2)
    x2 = (-b-delta**(1/2))/(a*2)

    print('x\' = ' , x1, '\nx\'\' = ', x2)