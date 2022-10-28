def isodd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def mid(str):
    length = len(str)
    if (isodd(length)):
        mid_index = int((length / 2))
        mid_char = str[mid_index]
        return mid_char
    else:
        return ""
        
        
print(mid(""))
    
    
    
    
    
    
    
