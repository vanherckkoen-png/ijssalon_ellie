# huiswerk les 8.1 - deze file aangemaakt

# huiswerk les 8.2 - mijn_functie_1
print("huiswerk les 8.2 - mijn_functie_1")
def mijn_functie_1(a):
    global b
    b = a**2
    return(b)
a=2
mijn_functie_1(a)
print(a," kwadraat is ", b)
a=4
mijn_functie_1(a)
print(a," kwadraat is ", b)
a=10
mijn_functie_1(a)
print(a," kwadraat is ", b)
a=12
mijn_functie_1(a)
print(a," kwadraat is ", b)
print()

# huiswerk les 8.3 - mijn_functie_2
print("huiswerk les 8.3 - mijn_functie_2")
def mijn_functie_2(c,d):
    global output
    output = [c+d, c-d, c*d, c/d]
    print()
    print (c ,",", d, " ===>")
    return(output)
mijn_functie_2(12,3)
print(output)
mijn_functie_2(12,2)
print(output)
mijn_functie_2(10,5)
print(output)
mijn_functie_2(100,20)
print(output)