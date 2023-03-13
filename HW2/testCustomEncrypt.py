from customEncrypt import customEncrypt

def testCustomEncrypt():

    invalid_u = True    
    invalid_p = True
    invalid_n = True
    invalid_d = True

    userID = input("Please enter your userID: ")
    userID_list = list(userID)
    while(invalid_u):
        for char in userID_list:
            if char == ' ' or char == '!':
                userID = input("Please enter a valid userID: ")
                userID_list = list(userID)
                break
            else:
                invalid_u = False
    

    password = input("Please enter your password: ")
    password_list = list(password)
    while(invalid_p):
        for char in password_list:
            if char == ' ' or char == '!':
                password = input("Please enter a valid password: ")
                password_list = list(password)
                break
            else:
                invalid_p = False
        
    
    try:
        N = int(input("Please enter a value of n: "))
        if N < 1:
            while(invalid_n):
                try:
                    N = int(input("Please enter a valid value of n: "))
                    if N < 1:
                        N = int(input("Please enter a valid value of n: "))
                    else:
                        invalid_n = False
                except:
                    continue
        else:
                invalid_n = False
    except:
        while(invalid_n):
            try:
                N = int(input("Please enter a valid value of n: "))
                if N < 1:
                    N = int(input("Please enter a valid value of n: "))
                else:
                    invalid_n = False
            except:
                continue

    try:
        D = int(input("Please enter a value of d: "))
        if D == 0 or D < -1 or D > 1:
            while(invalid_d):
                try:
                    D = int(input("Please enter a valid value of d: "))
                    if D == 0 or D < -1 or D > 1:
                        D= int(input("Please enter a valid value of d: "))
                    else:
                        invalid_d = False
                except:
                    continue
        else:
            invalid_d = False
    except:
        while(invalid_d):
            try:
                D = int(input("Please enter a valid value of d: "))
                if D == 0 or D < -1 or D > 1:
                    D= int(input("Please enter a valid value of d: "))
                else:
                    invalid_d = False
            except:
                continue

    userID_encrypt = customEncrypt(userID, N, D)
    password_encrypt = customEncrypt(password, N, D)
    
    print("Encrypted userID: " + userID_encrypt)
    print("Encrypted password: " + password_encrypt)
    
    if D == 1:
        print("Original userID: " + customEncrypt(userID_encrypt, N, D-2))
        print("Original password: " + customEncrypt(password_encrypt, N, D-2))
    else:
        print("Original userID: " + customEncrypt(userID_encrypt, N, D+2))
        print("Original password: " + customEncrypt(password_encrypt, N, D+2))