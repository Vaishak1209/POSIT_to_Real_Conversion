integer = float(input("Input your integer number: "))
posit_size = int(input("Input your posit bit size: "))
es = int(input("Input your exponent size (between 0 and 4): "))

if(integer>0):

    useed = 2**(2**(es))
    count = 0
    count5 = 0
    out1 = integer-useed
    while (out1>=useed):
        out1 = out1-useed
        count5 = count5+1
    out = count5 + 1   
    if(integer>useed):
        while (out>=useed):
            temp = out-useed
            count6 = 0
            while(temp>=useed):
                temp = temp-useed
                count6 = count6  +1
            out = count6 + 1
            count = count + 1
    else:
        count = -1
    r = count + 1
    print("No. of divisions (useed):",r)
    term1 = useed**r
    count7 = 0
    out4 = integer-term1
    while (out4>=term1):
        out4 = out4-term1
        count7 = count7+1
    rem = count7 + 1  
    count1 = 0
    count8 = 0
    out2 = rem - 2
    while (out2>=2):
        out2 = out2 - 2
        count8 = count8 + 1
    out3 = count8 + 1
    if(rem>2):
        while (out3>=2):
            out3 = out3/2
            count1 = count1+1
    else:
        count1 = -1
    e = count1 + 1
    print("No. of divisions (2):",e)

    term2 = (2**e)*term1

    frac = (integer/term2) 
    if frac == 0:
        print("Fraction:",frac)
    else:
        frac = frac - 1
        print("Fraction:",frac)

    posit_no = []
    if (integer>0):
        posit_no.append(0)
    elif (integer<0):
        posit_no.append(1)
    else:
        i = 0
        for i in range(0,posit_size):
            posit_no.append(0)

    if (r>0):
        i = 0
        for i in range(0,r+1):
            posit_no.append(1)
        posit_no.append(0)    
    elif(r<0):
        i = 0
        for i in range(0,r):
            posit_no.append(0)
        posit_no.append(1)
    else:
        posit_no.append(1)
        posit_no.append(0) 

    srg = posit_no

    expo = []
    def DecimalToBinary(num):
        
        
        if num >= 1:
            DecimalToBinary(num // 2)
        expo.append(num % 2)
    
    # Driver Code
    if __name__ == '__main__':
        
        # decimal value
        dec_val = e
        
        # Calling function
        DecimalToBinary(dec_val)   

    i = 0
    count2 = 0
    for i in range(0,len(expo)):
        if expo[i] == 0:
            count2 = count2 + 1
        else:
            break
    exponent = expo[count2:len(expo)]

    i = 0 
    for i in range(0,es-len(exponent)):
        posit_no.append(0)

    posit_no = posit_no + exponent


    fraclen = posit_size - len(srg) - len(exponent)

    bits = 2**fraclen
    decim = frac*bits
    decim = round(decim)
    fraction = []
    def DecimalToBinary(num):
        
        
        if num >= 1:
            DecimalToBinary(num // 2)
        fraction.append(num % 2)
    
    # Driver Code
    if __name__ == '__main__':
        
        # decimal value
        dec_val = decim
        
        # Calling function
        DecimalToBinary(dec_val)

    i = 0
    count3 = 0
    for i in range(0,len(fraction)):
        if fraction[i] == 0:
            count3 = count3 + 1
        else:
            break
    fract = fraction[count3:len(fraction)]    
    finalfrac = []  
    if (len(fract) == fraclen):
        finalfrac = fract
        posit_no = posit_no + finalfrac
    elif (len(fract)<fraclen):
        i = 0
        for i in range(0,fraclen-len(fract)):
            finalfrac.append(0)
        posit_no = posit_no + finalfrac + fract
    else:
        finalfrac = fract[0:fraclen]
        posit_no = posit_no + finalfrac    

    print("POSIT number is:",posit_no)

else:
        