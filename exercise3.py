def steigung_funktion(punkte):
    if punkte[2] - punkte[0] ==0:
        return "Die Steigung ist nicht definiert"
    m = (punkte[3]-punkte[1])/(punkte[2]-punkte[0])
    return m

steigung = steigung_funktion([4,4,8,4])
print(steigung)
    
