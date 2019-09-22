# -*- coding: utf-8 -*-

def recursion():
    '''
        Recursão - quando uma função chama a si própria
    '''
    # Fatorial
    # 0! = 1
    # 3! = 3 * 2 * 1
    # 4! = 4 * 3 * 2 * 1


# Implementação recursiva
def fat(n):
    '''
        fat(3) = 3 * fat(2) = 3 * 2 = 6
        fat(2) = 2 * fat(1) = 2 * 1 = 2
        fat(1) = 1 * fat(0) = 1 * 1 = 1
        fat(0) = 1
    '''
    if n == 0:
        return 1
    return n * fat(n - 1)

# print(fat(5))
