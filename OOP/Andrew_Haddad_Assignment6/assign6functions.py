def listlen(sample_list):
    if sample_list== []:
        value=0
        return value

    length= 0 
    for i in sample_list:
        length += 1
    return length
        

def listmax(sample_list):
    if sample_list== []:
        return none

    max_list_val=0
    for i in sample_list:
        if sample_list[i] > max_list_val:
            max_list_val= sample_list[i]
    return  max_list_val

# def listcopy(sample_list):
#     sample_list_copy=[]
#     if sample_list== []:
#         return sample_list
    
#     copied_value=0
#     sample_list_length= len(sample_list)
#     for i in range(sample_list_length +1):
#         copied_value= sample_list[i]
#         sample_list_copy[i]= copied_value

#     return sample_list_copy
def listcopy(sample_list):
    copy = []
    if listlen(sample_list) == 0:
        return copy
    
    for i in range(listlen(sample_list)):
        copy = copy + [sample_list[i]]
    return copy

def listappend(sample_list, value):
    sample_list = sample_list + [value]
    return sample_list

def listinsert(sample_list, location, value):
    sample_list = sample_list[:location] + [value] + sample_list[location:]
    return sample_list

def listremove(sample_list, value):
        i = 0
        length = listlen(sample_list)

        while i != length:
            if sample_list[i] == value:
                sample_list = sample_list[:i] + sample_list[i+1:]
                length -= 1
            i +=1
        return sample_list

def listreverse(sample_list):
        return sample_list[::-1]

sample= [1,2,3,4,5]

x= listreverse(sample)

print("x= ",x)
