#!/usr/bin/env python3

vzorec = input("Co chcete pocitat?(objem, obsah, obvod): ")

if vzorec == "objem":  
    
    vzorec1 = input("krychle, kvadr nebo koule? ")
    
    if vzorec1 == "krychle":
        A = float(input("zadejte stranu A: "))
        vysledek = print (A*A*A)
   
    if vzorec1 == "kvadr":
        A = float (input("zadejte stranu A: "))
        B = float (input("zadejte stranu B: ")) 
        C = float (input("zadejte stranu C: "))
        vysledek = print (A*B*C)
   
    if vzorec1 == "koule":
        R = float (input("zadejte polomer R: "))
        vysledek = print (4/3*3.14*R*R*R)

if vzorec == "obsah":

    vzorec2 = input("krychle, kvadr, koule, ctverec, obdelnik nebo kruh? ")
    
    if vzorec2 == "krychle":
        A = float (input("zadejte stranu A: "))
        vysledek = print(6*A*A)
    
    if vzorec2 == "kvadr":
        A = float (input("zadejte stranu A: "))
        B = float (input("zadejte stranu B: "))
        C = float (input("zadejte stranu C: "))
        vysledek = print (2*A*B+2*A*C+2*C*B)
        
    if vzorec2 == "koule":
        R = float (input("zadejte polomer R: "))
        vysledek = print (4*3.14*R*R)
   
    if vzorec2 == "ctverec":
        A = float (input("zadejte stranu A: "))
        vysledek = print (A*A)
    
    if vzorec2 == "obdelnik":
        A = float (input("zadejte stranu A: "))
        B = float (input("zadejte stranu B: "))
        vysledek = print (A*B)
    
    if vzorec2 == "kruh":
        R = float (input("zadejte polomer R: "))
        vysledek = print (3.14*R*R)

if vzorec == "obvod":
    
    vzorec3 = input("ctverec, obdelnik nebo kruh? ")
    
    if vzorec3 == "ctverec":
        A = float (input("zadejte stranu A: "))
        vysledek = print (4*A)
   
    if vzorec3 == "obdelnik":
        A = float (input("zadejte stranu A: "))
        B = float (input("zadejte stranu B: "))
        vysledek = print (2*A+2*B)
    
    if vzorec3 == "kruh":
        R = float (input("zadejte polomer R: "))
        vysledek = print (2*3.14*R)