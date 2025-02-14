posit_no = []
posit_size = int(input("Input your posit size: "))
es = int(input("Input exponent size (a number between 0 and 4): "))

for i in range(0,posit_size):
    ele = int(input("Input a POSIT number: "))
    posit_no.append(ele)

sign = posit_no[0]
print("Sign of the number is:",sign)
count = 0

for j in range(1,posit_size):
    if posit_no[j] != 0:
        count = count +1
    else:
        count = count

if count>0:
    lz = 0
else:
    lz = 1

print("The lower part of the number is zero:",lz)    

if sign == 1 and lz == 1:
    f_NAR = 1
else:
    f_NAR = 0

print("The number is not a real number:",f_NAR)

if sign == 0 and lz == 1:
    f_NOT = 1
else:
    f_NOT = 0    

print("The number underflows to zero:",f_NOT)

if f_NOT == 0 and f_NAR == 0:
    if sign == 0:

        t = posit_no[1:posit_size]
        print("test:",t)
        i = 0
        if posit_no[1] == 1:
            for i in range(len(t)):
                if t[i] == 1:
                    t[i] = 0
                else:
                    t[i] = 1
        else:
            t = t
        i = 0
        count2 = 0
        for i in range(0,posit_size - 1):
            if t[i] == 0:
                count2 = count2 + 1
            else:
                break
        print("Number of repeating digits:",count2)        
        r = posit_no[count2+2:posit_size]
        print("Number after removing regime bits:",r)
        e = r[0:es]
        print("Exponent bits:",e)
        f = r[es:len(r)]
        print("Fraction bits:",f)
        i = 0
        expo = 0
        if posit_no[1] == 1:
            expo = (count2-1)*(2**es)
        else:
            expo = (-1*count2)*(2**es) 

        fr = ''.join(str(x) for x in f)
        frac = 0
        for i in range(len(fr)):
            digit = int(fr[i])
            frac += digit * 2**(len(fr) - i - 1)
        frac =frac/(2**(len(f)))    
        print("Fractional part is:",frac)

        ex = ''.join(str(x) for x in e)
        exp = 0
        for i in range(len(ex)):
            digit3 = int(ex[i])
            exp += digit3 * 2**(len(ex) - i - 1)
        print("Exponent is:",exp)

        exponent = expo + exp
        print("Final exponent:",exponent)
        print("Integer number:",((2**exponent)*(frac+1)))

    else:
        t = posit_no[1:posit_size]
        print("test:",t)
        i = 0
        if posit_no[1] == 1:
            for i in range(len(t)):
                if t[i] == 1:
                    t[i] = 0
                else:
                    t[i] = 1
        else:
            t = t
        print("test2:",t)
        i = 0
        count2 = 0
        for i in range(0,posit_size - 1):
            if t[i] == 0:
                count2 = count2 + 1
            else:
                break
        print("rc:",count2)        
        r = posit_no[count2+2:posit_size]
        print("Number after removing regime bits:",r)
        e = r[0:es]
        print("Exponent bits:",e)
        f = r[es:len(r)]
        print("Fraction bits:",f)
        
        expo=0
        if posit_no[1]==1 :
            expo=(count2-1)*(2*es)
        else :
            expo=(-count2)*(2*es)
        
        useed=0
        useed=2**(2**(es))
        rg=0
        
        if sign!=t[0]:
            rg=count2-1
        else:
            rg=-count2
        
        print("Regime number:",rg)
        useedfinal=useed**rg 
        print("useed term:",useedfinal)
        
        fr = ''.join(str(x) for x in f)
        frac = 0
        for i in range(len(fr)):
            digit = int(fr[i])
            frac += digit * 2**(len(fr) - i - 1)
        frac=frac/(2**(len(f)))
        print("Fraction part of it:",frac)

        e1=e[0:es]
        i = 0
        for i in range(len(e)):
                if e1[i] == 1:
                    e1[i] = 0
                else:
                        e1[i] = 1
        ex = ''.join(str(x) for x in e1)
        exp = 0
        for i in range(len(ex)):
            digit3 = int(ex[i])
            exp += digit3 * 2**(len(ex) - i - 1)
        print("Exponent from the posit number:",exp)
        exponent=exp
        print("Final exponent:", exponent)

        print("Integer :", (useedfinal*(2**(exponent))*(frac-2)))
else:
    print("-----NaN-----")
