#!/usr/bin/env python

#Title: gate
#
#Author: Ian Britz
#Date Created : 1/25/2017
#Last Modified: 2/03/2017
#
#Purpose: list of logic gates

def MUX(s, a, b):
    """""""""""""""""

    Input: 0, 1
    
    Output: Selection between a and b

    s a b | out
    -----------
    0 0 0 |  0
    0 0 1 |  0
    0 1 0 |  1
    0 1 1 |  1
    1 0 0 |  0
    1 0 1 |  1
    1 1 0 |  0
    1 1 1 |  1
    
    Dependencies: NOT, AND, OR
    
    """""""""""""""""

    return OR ( AND(a, NOT(s)), AND(b, s) )

def XOR(a, b):
    """""""""""""""""

    Input: 0, 1
    
    Output: Logical Exclusive OR 

    a b | out
    ---------
    0 0 |  0
    0 1 |  1
    1 0 |  1
    1 1 |  0
    
    Dependencies: NAND, AND, OR
    
    """""""""""""""""

    return AND ( NAND(a, b), OR(a,b) )
    
    
def OR(a, b):
    """""""""""""""""

    Input: 0, 1
    
    Output: Logical OR

    a b | out
    ---------
    0 0 |  0
    0 1 |  1
    1 0 |  1
    1 1 |  1
    
    Dependencies: NAND
    
    """""""""""""""""

    return NAND( NAND(a, '1'), NAND(b, '1') )

    
def AND(a, b):
    """""""""""""""""

    Input: 0, 1
    
    Output: Logical AND

    a b | out
    ---------
    0 0 |  0
    0 1 |  0
    1 0 |  0
    1 1 |  1
    
    Dependencies: NAND, NOT
    
    """""""""""""""""

    return NOT( NAND(a, b) )

def NOT(a):
    """""""""""""""""

    Input: 0, 1
    
    Output: Logical NOT

     a | out
    --------
     0 |  1
     1 |  0
    
    Dependencies: NAND
    
    """""""""""""""""

    return NAND(a, a)

def NAND(a, b):
    """""""""""""""""

    Input: 0, 1
    
    Output: Logical NAND

    a b | out
    ---------
    0 0 |  1
    0 1 |  1
    1 0 |  1
    1 1 |  0
    
    Dependencies: None
    
    """""""""""""""""

    if a == '1' and b == '1':
        
        return '0'
    else:
        return '1'


#Test case
for i in xrange(0, 8):
    b = list(format(i, '03b'))
    print MUX(b[0], b[1], b[2])
    
