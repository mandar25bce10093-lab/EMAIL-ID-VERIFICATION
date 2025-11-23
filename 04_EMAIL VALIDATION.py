'''Conditions for greating an Email ID:
1) The length of the ID should be equal to or more than 6.
2)The first character of the ID shuld be an alphabet.
3)Their should be character such as @ in the ID.
4)The "." should be placed from either at 3 or 4 position from the last.
5)Their should be no space or uppercase or use of any special character other than @ / _ / .  '''

email=input("enter your email: ") 
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email: condition 5")
                else:
                    print("right email")
            else:
                print("wrong email: condition 4")
        else:
            print("wrong email: condition 3")
    else:
        print("wrong email: condition 2")
else:
    print("wrong email: condition 1")              
            
    