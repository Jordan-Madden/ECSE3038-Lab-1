'''
    Author: Jordan Madden
    Usage: python lab1.py
'''

def hello():
    print("ECSE3038 - Engineering IoT Systems")

def validatePassword(password):
    alnum, nums = 0, 0

    if len(password) >= 8 and password.isalnum():
        for val in password:
            try:
                if isinstance(int(val), int):
                    nums += 1
            except:
                pass
        
        if nums >= 2:
            return True
    
    return False

def sumUpToN(num):
    val = 0

    if num > 1:
        for i in range(1, num+1):
            val += i

    return val 

if __name__ == "__main__":
    # Part 1
    hello()
    print("\n")

    # Part 2
    password = "GreetingsFe1owKids"
    print(validatePassword(password))
    print("\n")
                
    # Part 3
    sum = sumUpToN(14)
    print(sum)
