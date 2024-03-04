import cmath

'''
z = input()
z = complex(z)
po = cmath.polar(z)
print(po[0])
print(po[1])
'''

print(*cmath.polar(complex(input())), sep='\n')
