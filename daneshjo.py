tedad = int(input("tedad daneshjoyan ra vared konid: "))
nomarat = []

for i in range(tedad):
    nomre = float(input("nomre ra vared konid: ")) 
    nomarat.append(nomre)
    
a = sum(nomarat) / tedad

b = min(nomarat)
c = max(nomarat)

print(a , "miangin"  , b , "min" ,   c,"max")
