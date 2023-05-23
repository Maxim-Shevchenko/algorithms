import sys
sys.setrecursionlimit(5000)
#def recursion(x):
   # print("Вызов №:", x)
   # if x == 2700:
   #     return x
   # recursion(x+1)

#recursion(1)

def print_list(x):
    print(x.pop())
    if len(x) == 0:
        return
    print_list(x)
#print_list( [ 11,22,33,44,55,66,77,88,99 ] )



def summ( x ):
    if len(x)==1:
     return x.pop()
    return summ( x[ :len( x )-1 ] )+x.pop()
print( summ( [ 1,1,31,213,312,1,3,2 ] ) )