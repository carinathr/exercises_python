def funktion_prüfen (x,y) :
    if y ==0:
        print("Nicht möglich durch 0 zu teilen")
    elif x == y:
        print("x und y sind gleich")
    else:
        if x%y == 0:
            print(x, "teilbar durch", y)
        else:
            print(x, "nicht teilbar druch", y)
            
print(funktion_prüfen(3, 3))

    
