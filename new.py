def simple_intrest(p, n, r):
    
    """
    This function takes following inputs
    p = Principal in INR
    n = Number of years
    r = Rate of Intrest in %p.a.
    Output = Intrest and amount
    """
    I = (p*n*r)/100
    A = p + I
    return I, A
    I = (p*n*r) / 100
    A = p + I 
    return I,A    

# Take input from the user 
p = float(input("please enter principle in INR : ")) 
n = float(input("please enter number of years : ")) 
r = float(input("please enter rate of interest in %p.a : ")) 

# call the function  
I,A = simple_intrest(p, n, r)

# print the results 
print (f"simple Interest : {I:.2f} INR")  
print (f"Amount : {A:.2f} INR")