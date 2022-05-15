from asyncore import loop
from distutils.command.clean import clean
from turtle import done
def main():
   print("welcome to the calculator made by Ultimate Sow, please type what you want to do")
   x = input("Type here: ")
   if x == "add":
       one_add = float(input("enter first number: " ))
       two_add = float(input("enter second number: "))
       add_ans = one_add + two_add
       print("sum: " + str(add_ans))
   elif x == "subtract":
       one_sub = float(input("enter first number: " ))
       two_sub = float(input("enter second number: "))
       sub_ans = one_sub - two_sub
       print("sum: " + str(sub_ans))
   elif x == "divide":
       one_div = float(input("enter first number: " ))
       two_div = float(input("enter second number: "))
       div_ans = one_div / two_div
       print("sum: " + str(div_ans)) 
   elif x == "multiply":
       one_mul = float(input("enter first number: " ))
       two_mul = float(input("enter second number: "))
       mul_ans = one_mul * two_mul
       print("sum: " + str(mul_ans))
   else:
       input("sorry you did not input a known arithmatic equation ;;")
   again = str(input("would you like to do another problem, yes or no? "))
   if again == "yes":
       main()
   if again == "no":
       input("ok bye")
    
   else:
       input("ERROR: INVALID INPUT")
main()