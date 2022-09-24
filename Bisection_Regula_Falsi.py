# This program is to help ease the process of finding a root of a polynomial equation.

# Importing Libraries 
# Sympy and Tqdm do not exist within the standard libraries use commands pip install sympy and pip install tqdm
import os
import math
import time
import sympy as smp
from tqdm import tqdm   

# Function to calculate root or range within which root lies
def calc_():
    global eq

    # User input for interval separated by space
    a,b=input("\nEnter interval in which root should be calculated(separated by space): ").split()
    a=int(a);b=int(b)
    ls=[]

    # Substituting values for given range within the function and storing result in a nested list
    for i in range(a,b+1):
        ls.append([i,eq.subs({'x':i})])

    
    for i in range(len(ls)-1):

        # If 0 (ie.root) exists within the function, return an integer value 
        if(ls[i][1]==0):
            return (ls[i][0])
    
        # If a.b<0 (ie.one positive and one negative) exists, return a list of integers 
        elif(ls[i][1]*ls[i+1][1]<0):
            return ([ls[i][0],ls[i+1][0]])

    # If root does not exist within the list
    else:
        return (None)

# Function to print table of substituted values and find the root of the function using Bisection Theoren
def bisection(interval):
    
    global eq

    # Progress bar
    for i in tqdm (range (101), 
               desc="Computing…", 
               ascii=False, ncols=75):
        time.sleep(0.01)
    print("Printing Output...")
    time.sleep(0.35)

    # Lambda function to clear the system terminal
    clear = lambda: os.system('cls')
    clear()

    # Printing Table
    print("\nBisection Theorem:\n")
    print(f"Equation:{eq}")
    print(f"Interval:({interval[0]},{interval[1]})\n")
    print("-------------------------------------------------------------------------")
    print("| Iteration\t| X\t\t| F(X)\t\t| Interval\t\t|")
    print("-------------------------------------------------------------------------")
    
    iteration,sub=1,0

    # Table is calculated to a max of 20 iterations
    while(iteration<21):

        # Bisection Formula - x=(a+b)/2
        sub=(interval[0]+interval[1])/2

        # If f(x)<0 substite the interval which is initally <0 with x
        if(eq.subs({'x':sub})<0):
            if(eq.subs({'x':interval[0]})<0):
                interval[0]=sub
            else:
                interval[1]=sub

        # If f(x)>0 substite the interval which is initally >0 with x
        elif(eq.subs({'x':sub})>0):
            if(eq.subs({'x':interval[0]})>0):
                interval[0]=sub
            else:
                interval[1]=sub

        # Printing Table
        print("| %d\t\t| %.4f  \t| %.4f  \t| (%.4f,%.4f) \t|"%(iteration,sub,eq.subs({'x':sub}),interval[0],interval[1]))
        print("-------------------------------------------------------------------------")
        

        # Incrementing Iteration
        iteration+=1

        # If f(x) is approximately equal to 0 within 4 decimal places
        if(math.isclose(interval[0]-interval[1],0,abs_tol=1e-4)):
            print("Root of the equation: %.4f\n"%sub)
            return

# Function to print table of substituted values and find the root of the function using Bisection Theoren
def regula_falsi(interval):
    
    global eq

    # Progress bar
    for i in tqdm (range (101), 
               desc="Computing…", 
               ascii=False, ncols=75):
        time.sleep(0.01)
    print("Printing Output...")
    time.sleep(0.35)

    # Lambda function to clear the system terminal
    clear = lambda: os.system('cls')
    clear()

    # Printing Table
    print("\nBisection Theorem:\n")
    print(f"Equation:{eq}")
    print(f"Interval:({interval[0]},{interval[1]})\n")

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("| Iteration\t| Interval\t\t| F(A)\t\t|F(B)\t\t| X\t\t| F(X)\t\t| Interval\t\t|")
    print("---------------------------------------------------------------------------------------------------------------------------------")

    iteration,sub=1,0

    # Table is calculated to a max of 10 iterations
    while(iteration<10):
        
        sub=( (interval[0]*eq.subs({'x':interval[1]})) - (interval[1]*eq.subs({'x':interval[0]})) )/( eq.subs({'x':interval[1]}) - eq.subs({'x':interval[0]}) )
        print("| %d\t\t| (%.4f,%.4f) \t| %.4f  \t| %.4f  \t| %.4f  \t| %.4f  \t|"%(iteration,interval[0],interval[1],eq.subs({'x':interval[0]}),eq.subs({'x':interval[1]}),sub,eq.subs({'x':sub})),end="")

        # If f(x)<0 substite the interval which is initally <0 with x
        if(eq.subs({'x':sub})<0):
            if(eq.subs({'x':interval[0]})<0):
                interval[0]=sub
            else:
                interval[1]=sub

        # If f(x)>0 substite the interval which is initally >0 with x
        elif(eq.subs({'x':sub})>0):
            if(eq.subs({'x':interval[0]})>0):
                interval[0]=sub
            else:
                interval[1]=sub

        print(" (%.4f,%.4f) \t|"%(interval[0],interval[1]))

        print("---------------------------------------------------------------------------------------------------------------------------------")
        
        if(math.isclose(eq.subs({'x':sub}),0,abs_tol=1e-4)):
            print("Root of the equation: %.4f\n"%sub)
            return
        
        iteration+=1


# Main Function Declaration
if __name__=='__main__':   

    # Lambda function to clear the system terminal
    clear = lambda: os.system('cls')
    clear()

    # Intializing symbols and input equation
    x=smp.symbols('x',real=True)
    eq=smp.sympify(input("Enter an equation: "))

    # Calculation of interval of function
    interval=calc_()

    # If interval is of type int (ie.interval is root)
    if type(interval)==int:
        print(f"\nRoot of the equation: {interval}")

    # If interval is of type None (ie.root does not exist within the interval)
    if(interval==None):
        # Input interval again
        print("\nRoot does not exist within the interval")
        interval=calc_()

    # If interval is of type list (ie.the root exists between two values)
    else:
        print("Root of the equation exists within the interval")

        # User input to choose
        user=int(input("\nEnter option for calculation of root:\n1)Bisection\n2)Regula-Falsi\n\nEnter 1/2:"))
        if user==1:
            bisection(interval)
        elif user==2:
            regula_falsi(interval)
        else:
            print("Operation not recognized")