#freecodecamp problem

def arithmetic_formatter(problems=list, display=False):
    #Handling errors
    #if more than 5 problems given, return error 
    if len(problems) > 5:
        print('Error: Too many problems.')
        return 0
    
    for i in problems:
        for c in i:
            #make sure there are only digits
            if c.isalpha():
                print("Error: Numbers must only contain digits.")
                return 0
            #numbers cannot be more than 4 digits 
            if len(c) > 4:
                print("Error: Numbers cannot be more than four digits.")     
                return 0

    if display == True:
        for i in problems:
            print(i, "=", eval(i))

arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "555 + 420"], True)
