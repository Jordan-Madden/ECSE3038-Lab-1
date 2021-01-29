'''
    Author: Jordan Madden
    Usage: python lab1.py
'''

def hello():
    print("ECSE3038 - Engineering IoT Systems")

def validatePassword(password):
    alnum, nums = 0, 0
    
    if len(password) >= 8:
        for val in password:
            if val.isalnum():
                try:
                    if isinstance(int(val), int):
                        nums += 1
                except:
                    pass
            else:
                print("[ERROR] The password can only have alphanumeric values") 
                continue
        if nums >= 2:
            return True
        else:
            print("[ERROR] The password must have more than 2 numbers.")
    else:
        print("[ERROR] Password must have at least 8 letters")
    
    return False

def sumUpToN(num):
    val = 0
    for i in range(1, num+1):
        val += i

    return val 

if __name__ == "__main__":
    # Part 1
    hello()
    print("\n")

    # Part 2
    password = "GreetingsFe11owKids"
    print(validatePassword(password))
    print("\n")
                
    # Part 3
    sum = sumUpToN(14)
    print(sum)
