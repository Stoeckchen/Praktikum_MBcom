def print_pyramid(height):
    pass

height = int (input("Höhe: "))

    
for index in range(height):
    print (index, end =" ")

    for _index in range(index):
        print( _index, end = " ") 
    print ("\r")