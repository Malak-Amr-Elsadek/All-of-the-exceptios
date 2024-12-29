try:
    num1,num2 =eval(input("Enter two nubers seperated by a comma:"))
    result=num1/num2
    print("Result is:",result)

except SyntaxError:
    print("Use a comma between the numbers")
except NameError:
    print("Numbers only")
except ZeroDivisionError:
    print("Don't divide by 0")

finally:
    print("Code will run no matter what!!!")