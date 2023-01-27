# Functions.py

#######################
#Exponential function
def exp(x):
    """
    """
    k = 0
    err = 1.
    tol = 1e-16   #About 16 digits of precision
    s = 1.
    fact_k = 1
    while err > tol:
        k += 1
        fact_k *= k
        t = (x ** k) / fact_k #Calculate term 
        s += t   #Sum increment        
        err = abs(t/s)  #Update error
    return s



##########################################
####Convert Decimal to mantissa and exponent
def decimal_2_mne(num):
    """
    """
    ########Convert decimal to base 2
    #Find if num is greater or less than 1
    n = 0
    while True:
        if num >1:
            num /= 2
            e = n+1
            n += 1
            #print(remainder,'if')
        else:
            num *= 2
            e = n-1
            n +=1
            #print(remainder,'else')
        if num>=0.5 and num <1:
            break
    #print("Mantissa #:", num, "Exponent #:", e)
    return num, e

#################################
####Convert mantissa and exponent to binary
def me_2_bin(m,e):
    import numpy as np
    """
    """
    ####### Converts mantissa to binary
    rem = m
    sb = np.zeros(53)
    i = 0
    for k in range(-1,-53,-1):
        if rem >= 2**k:
            #print("remainder:", rem, "2^k:", 2**k, "k:",k)
            sb[i] = 1
            rem -= 2**k
            i +=1
        else:
            sb[i]= 0   
            i +=1
    ########
    #Convert exponent to binary
    rem = e
    se = np.zeros(10)
    i = 0
    for k in range(9,0,-1):
        if rem >= 2**k:
            se[i] = 1
            rem -= 2**k
            i +=1
        else:
            se[i] = 0
            i +=1
    #print("Exponent:", se, "Mantissa:", sb)
    return sb,se
    
############################################
if __name__ == '__main__':
    print(f'exp(0): {exp(0)}') #A form of Verification, know e(0) by the series function
    print(f'exp(1): {exp(1)}') #A form of Validation, need to look to find e(1)
    # m,e = decimal_2_mne(173)
    # print("Mantissa:",m,"Exponent:",e)
    # sb, se = me_2_bin(m,e)
    # print("Exponent:", se, "Mantissa:", sb)