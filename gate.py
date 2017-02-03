#!/usr/bin/env python

#Title: gate
#
#Author: Ian Britz
#Date Created : 1/25/2017
#Last Modified: 2/03/2017
#
#Purpose: list of logic gates


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
    
    Dependencies: NAND
    
    """""""""""""""""

    if a == '1' and b == '1':
        return '0'
    else:
        return '1'

print NOT('1')
