import numpy as np
import matplotlib.pyplot as plt

x = 2
approx_error_precent = 0
h_val = [0.2,0.15,0.10,0.01,0.001,0.0001]

def my_func(x):
    return (7 * np.exp(0.5*x))
    # return (3*(x**2))
    
def derv_func(x, h):
    return (my_func(x+h) - my_func(x))/h
    
def approx_error_percent_func(curr, prev):
    return abs((curr - prev))*100
    
def main():
    curr = derv_func(2,0.3)
    for i in h_val:
        prev = curr
        curr = derv_func(2,i)
        approx_error_precent = approx_error_percent_func(curr, prev)
        if(approx_error_precent <= 0.5):
            break

    print(f"Differential is: {curr}\nApproximate error is: {approx_error_precent: .7f}%")      

main()

