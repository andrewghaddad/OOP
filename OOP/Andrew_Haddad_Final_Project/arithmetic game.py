from random import randint
import Myfunctions

num_problems= int(input("How many problems would you like to attempt? "))
width_val= int(input("How wide do you want your digits to be? 5-10: "))
char_val= str(input("What character would you like to use? "))
drill_mode= str(input("Would you like to activate 'drill' mode? yes or no: "))

value1=0
value2=0
operand_value=0
o_value=""
results=[]
add_problems=0
sub_problems=0
mult_problems=0
div_problems=0
correct_add=0
correct_sub=0
correct_mult=0
correct_div=0
extra_attempt_a=0
extra_attempt_s=0
extra_attempt_m=0
extra_attempt_d=0

while (num_problems < 0 ):
    num_problems= int(input("How many problems would you like to attempt? "))

while (width_val < 5 and width_val > 10):
    width_val= int(input("How wide do you want your digits to be? 5-10: "))

while (len(char_val) > 1):
    char_val= str(input("What character would you like to use? "))

print()
print("Here we go!")
print()

if (drill_mode== "no"):
    for i in range(0,num_problems):
        print("What is .....")
        print()
        value1 = randint(0, 9)
        value2 = randint(0, 9)
        operand_value= randint(1, 4)
        if (operand_value == 2):
            operand= Myfunctions.plus(width_val,char_val)
            o_value="+"
            add_problems +=1
        elif (operand_value == 1):
            operand= Myfunctions.minus(width_val,char_val)
            o_value="-"
            sub_problems +=1
        elif (operand_value == 3):
            operand= Myfunctions.mult(width_val,char_val)
            o_value="*"
            mult_problems +=1
        elif (operand_value == 4):
            operand= Myfunctions.div(width_val,char_val)
            o_value="/"
            div_problems +=1


        pattern1= Myfunctions.print_number(value1,width_val,char_val)
        pattern2= Myfunctions.print_number(value2,width_val,char_val)
        print()
        print(pattern1)
        print()
        print(operand)
        print()
        print(pattern2)

        answer= int(input("= "))

        is_correct= Myfunctions.check_answer(value1,value2,answer,o_value)

        if (is_correct== False):
            print("Sorry, that's not correct.")
        else:
            print("Correct!")
            if (o_value== "+"):
                correct_add +=1
            elif (o_value == "-"):
                correct_sub +=1
            elif (o_value == "*"):
                correct_mult +=1
            elif (o_value == "/"):
                correct_div +=1
        
    print("Total addition problems presented: ",add_problems )
    # print("Correct addition problems: ",correct_add," (",(correct_add/add_problems) *100,"%)")
    print("Total subtraction problems presented: ",sub_problems)
    # print("Correct subtraction problems: ",correct_sub," (",(correct_sub/sub_problems) *100,"%)")
    print("Total multipication problems presented: ",mult_problems)
    # print("Correct multipication problems: ",correct_mult," (",(correct_mult/mult_problems) *100,"%)")
    print("Total division problems presented: ",div_problems)
    # print("Correct division problems: ",correct_div," (",(correct_div/div_problems) *100,"%)")
else:
    for i in range(0,num_problems):
        print("What is .....")
        print()
        value1 = randint(0, 9)
        value2 = randint(0, 9)
        operand_value= randint(1, 4)
        if (operand_value == 2):
            operand= Myfunctions.plus(width_val,char_val)
            o_value="+"
        elif (operand_value == 1):
            operand= Myfunctions.minus(width_val,char_val)
            o_value="-"
        elif (operand_value == 3):
            operand= Myfunctions.mult(width_val,char_val)
            o_value="*"
        elif (operand_value == 4):
            operand= Myfunctions.div(width_val,char_val)
            o_value="/"


        pattern1= Myfunctions.print_number(value1,width_val,char_val)
        pattern2= Myfunctions.print_number(value2,width_val,char_val)
        print()
        print(pattern1)
        print()
        print(operand)
        print()
        print(pattern2)

        answer= int(input("= "))

        is_correct= Myfunctions.check_answer(value1,value2,answer,o_value)

        if (is_correct== False):
            if (o_value== "+"):
                extra_attempt_a +=1
            elif (o_value == "-"):
                extra_attempt_s +=1
            elif (o_value == "*"):
                extra_attempt_m +=1
            elif (o_value == "/"):
                extra_attempt_d +=1
            while(is_correct== False):
                if (o_value== "+"):
                    extra_attempt_a +=1
                elif (o_value == "-"):
                    extra_attempt_s +=1
                elif (o_value == "*"):
                    extra_attempt_m +=1
                elif (o_value == "/"):
                    extra_attempt_d +=1

                print("Sorry, that's not correct.")
                answer= int(input("= "))
                is_correct= Myfunctions.check_answer(value1,value2,answer,o_value)
        else:
            print("Correct!")
            if (o_value== "+"):
                correct_add +=1
            elif (o_value == "-"):
                correct_sub +=1
            elif (o_value == "*"):
                correct_mult +=1
            elif (o_value == "/"):
                correct_div +=1

    print("Total addition problems presented: ",add_problems)
    print("# of extra addition attempts needed: ",extra_attempt_a)
    print("Total subtraction problems presented: ",sub_problems)
    print("# of extra substraction attempts needed: ",extra_attempt_s)
    print("Total multipication problems presented: ",mult_problems)
    print("# of extra multipication attempts needed: ",extra_attempt_m)
    print("Total division problems presented: ",div_problems)
    print("# of extra division attempts needed: ",extra_attempt_d)

