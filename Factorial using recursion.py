print("-----------FACTORIAL USING RECURSION-------")
def function(fact,n,i):
    if n==1:
        print(fact)
        return 
    function(fact*n,n-1,i+1)
function(1,5,0)    
print("-----------FACTORIAL USING FOR LOOPS------")
n=10
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(factorial)
    
    
