def number_of_bottles():
    a="bottles of milk on the wall,"
    a1="bottle of milk on the wall,"
    b="bottles of milk."
    b1="bottle of milk."
    c="Take one down and pass it around,"
    d="bottles of milk on the wall."
    e="bottle of milk on the wall."
    f=" no more bottles of milk on the wall."
    g="No more bottles of milk on the wall, no more bottles of milk."
    h="Go to the store and by some more, 99 bottles of milk on the wall."
    for i in range(99,2,-1):
        print(i,a,i,b)
        print(c,i-1,d)
    print(2,a,2,b)
    print(c,1,e) 
    print(1,a1,1,b1)   
    print(c,f)
    print(g)
    print(h)

number_of_bottles()