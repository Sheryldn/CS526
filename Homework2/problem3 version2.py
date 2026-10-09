def ways(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return ways(n-1)+ways(n-2)+ways(n-3)
def show_ways(n,path=""):
    if n==0:
        print(path)
        return
    if n<0:
        return
    for step in (1,2,3):
        if path=="":
            show_ways(n-step,str(step))
        else:
            show_ways(n-step,path+"+"+str(step))
for n in (3,4,7,10):
    print("Step Combinations for an input of",n,"steps:")

    if n==10:
        print("Total Step Combinations: ",ways(n))
    else:
        show_ways(n)
        print("Total Step Combinations: ",ways(n))

    print()