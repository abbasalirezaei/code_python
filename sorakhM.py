x1, x2 = [int(x) for x in input().split()]

fasle=x2-x1
if fasle==0:
    print("Saal Noo Mobarak!")
else:
    if x2>x1:

        for i in range(fasle):
            print("R",end="")    
    else:        
        for i in range(-1*fasle):
            print("L",end="")