# Part 1

# a.)
def horizontal_line(width_val,char_val):
    line=""
    for i in range(0,width_val):
        line += char_val        
    return line

def vertical_line(shift_val,height_val,char_val):
    line=""
    line= (((' '* shift_val) + char_val + "\r\n") * int(height_val))  
    return line

def two_vertical_line(width_val,height_val,char_val):
    line=""
    line= (((char_val+(" " * width_val) + char_val) + "\r\n") * height_val)
    return line

# b.)
def number_1(width_val, char_val):
    pattern = vertical_line(width_val-1,5,char_val)
    return pattern

def number_0(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= two_vertical_line ((width_val)-2, 3, char_val)
    pattern3= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3
    return result

def number_2(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= vertical_line (width_val-1, 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= vertical_line (width_val- (width_val), 1, char_val)
    pattern5= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4+pattern5
    return result

def number_3(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= vertical_line (width_val-1, 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= vertical_line (width_val-1, 1, char_val)
    pattern5= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4+pattern5
    return result

def number_4(width_val, char_val):
    pattern1= two_vertical_line (width_val-2, 2, char_val)
    pattern2= horizontal_line(width_val,char_val)
    pattern3= vertical_line (width_val-1, 2, char_val)
    result= pattern1+pattern2+"\n"+pattern3
    return result

def number_5(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= vertical_line (width_val- (width_val), 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= vertical_line (width_val-1, 1, char_val)
    pattern5= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4+pattern5
    return result

def number_6(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= vertical_line (width_val- (width_val), 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= two_vertical_line (width_val-2, 1, char_val)
    pattern5= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4+pattern5
    return result

def number_7(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= vertical_line (width_val- 1, 4, char_val)
    result= pattern1+"\n"+pattern2
    return result


def number_8(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= two_vertical_line (width_val-2, 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= two_vertical_line (width_val-2, 1, char_val)
    pattern5= horizontal_line(width_val,char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4+pattern5
    return result

def number_9(width_val, char_val):
    pattern1= horizontal_line(width_val,char_val)
    pattern2= two_vertical_line (width_val-2, 1, char_val)
    pattern3= horizontal_line(width_val,char_val)
    pattern4= vertical_line (width_val-1, 2, char_val)
    result= pattern1+"\n"+pattern2+pattern3+"\n"+pattern4
    return result

# c.)
def print_number(integer_val, width_val,char_val):
    if integer_val== 0:
        pattern= number_0(width_val, char_val)
        return pattern
    elif integer_val== 1:
        pattern= number_1(width_val, char_val)
        return pattern
    elif integer_val== 2:
        pattern= number_2(width_val, char_val)
        return pattern
    elif integer_val== 3:
        pattern= number_3(width_val, char_val)
        return pattern
    elif integer_val== 4:
        pattern= number_4(width_val, char_val)
        return pattern
    elif integer_val== 5:
        pattern= number_5(width_val, char_val)
        return pattern
    elif integer_val== 6:
        pattern= number_6(width_val, char_val)
        return pattern
    elif integer_val== 7:
        pattern= number_7(width_val, char_val)
        return pattern
    elif integer_val== 8:
        pattern= number_8(width_val, char_val)
        return pattern
    elif integer_val== 9:
        pattern= number_9(width_val, char_val)
        return pattern

# d.)
def plus(width_val,char_val):

    middle= (width_val/2) +1
    middle= int(middle)
    

    if (width_val % 2 ==0):
        pattern1= vertical_line((middle-2),2,char_val*2)
        pattern2= horizontal_line(width_val,char_val)
        pattern3= vertical_line((middle-2),2,char_val*2)
        result= pattern1+pattern2+"\n"+pattern3
        return result
    else:
        pattern1= vertical_line(middle-1,2,char_val)
        pattern2= horizontal_line(width_val,char_val)
        pattern3= vertical_line(middle-1,2,char_val)
        result= pattern1+pattern2+"\n"+pattern3
        return result

def minus(width_val,char_val):
    pattern= horizontal_line(width_val,char_val)
    return pattern 

# h.)
def mult(width_val,char_val):
    for i in range(width_val):
        for j in range(width_val):
            if (i == j) or ((width_val - j -1) == i):
                print(char_val, end = '')
            else:
                print(' ', end = '')
        print('')

# i.)

def div(width_val,char_val):
    middle= (width_val/2) +1
    middle= int(middle)
    

    if (width_val % 2 ==0):
        pattern1= vertical_line((middle-2),1,char_val*2)
        pattern2= horizontal_line(width_val,char_val)
        pattern3= vertical_line((middle-2),1,char_val*2)
        result= pattern1+"\n"+"\n"+pattern2+"\n"+"\n"+pattern3
        return result
    else:
        pattern1= vertical_line(middle-1,1,char_val)
        pattern2= horizontal_line(width_val,char_val)
        pattern3= vertical_line(middle-1,1,char_val)
        result= pattern1+"\n"+"\n"+pattern2+"\n"+"\n"+pattern3
        return result


# e.)
def check_answer(integer_val1, integer_val2, answer_val,operand_val):
    ans=0
    result= True
    if (operand_val == "+"):
        ans= integer_val1+integer_val2
    elif (operand_val == "-"):
        ans= integer_val1-integer_val2
    elif (operand_val == "*"):
        ans= integer_val1*integer_val2
    elif (operand_val == "/"):
        ans= integer_val1/integer_val2
        ans= int(ans)

    if (answer_val== ans):
        return result
    else:
        result= False
        return result