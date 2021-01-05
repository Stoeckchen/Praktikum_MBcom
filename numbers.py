#def upnum(ux):
#def lownum(lx): 

lx_string = input("Erste Zahl: ")

if not (lx_string.isdigit()):
    print ("Falsche Eingabe, neustarten")
    quit()
else:
    lx_int = int (lx_string)


ux_string = input("Letzte Zahl: ")


if not(ux_string.isdigit()):
    print ("Falsche Eingabe, neustarten")
    quit()
else:
    ux_int = int (ux_string)


gerade = input ("Gerade *g* oder Ungerade *u*?: ")
gerade = gerade.lower ()

if gerade == "g":
    for index in range(lx_int, ux_int + 1):
        if(index % 2 == 0):
            print (index)
    
elif gerade == "u":
    for index in range(lx_int, ux_int + 1):
        if(index % 2 == 1):
            print (index)

else:
    print("Falsche Eingabe, neustarten")
    quit()

 