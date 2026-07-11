print("-----------FACTORIAL USING RECURSION-------")
def function(fact,n,i):
    if n==1:
        print(fact)
        return 
    function(fact*n,n-1,i+1)
function(1,5,0)    