'''
Created on 31 mar. 2019

@author: meyi
'''

def esBisisesto():
    año = int(input("Introduce año: "))
    if año % 4 == 0:
        return True
    else:
        return False

print(esBisisesto())
