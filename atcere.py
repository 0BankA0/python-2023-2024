print(125+24)
print(125-24)
print(125*24)
print(125/24)

inch = float (input('ievadi inčus: '))

m = inch * 0.02545

print(m)

baze = float(input('Ievadi trijstūra bāzes malu: '))
augstums = float(input('Ievadi trijstūra augstumu:'))

laukums = 1/2*baze*augstums

print(laukums)


x = float(input('pirmais skaitlis:'))
y = float(input('otrais skaitlis: '))

if x<y:
    print('3')
elif x>y:
    print('2')
else:
    print('1')
