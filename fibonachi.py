n = int(input("pleas enter n: "))

fibonachi= [0 , 1] 

for i in range(2 , n):
    f = fibonachi[i-1] + fibonachi[i-2]
    fibonachi.append(f)

print(fibonachi)    


