x = "Hallo, Berlin"
x_list = list(x)
for i in x_list:
    print(i.isalpha())
    
text_list = "Hallo, Berlin"
buchstaben_zählen = []

for buchstaben in text_list:
    print(buchstaben.isalpha)
    if buchstaben.isalpha() == 1:
        buchstaben_zählen.append(buchstaben.isalpha())
        
print(sum(buchstaben_zählen))