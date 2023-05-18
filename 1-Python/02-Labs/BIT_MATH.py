import os

def clear_bit(num, bit_pos):
    num = (num&(~(1<<bit_pos)))
    return num 



def toggle_bit(num, bit_pos):
    num=(num^(1<<bit_pos))
    return num 



def set_bit(num, bit_pos):
    num =(num|(1<<bit_pos))
    return num



def get_bit(num, bit_pos):
    
    return ((num>>bit_pos)&0x01)



print(dir(dir))

num = 1  
num = clear_bit(num, 0)  
print("Clear :",num)

num = 3  
num = toggle_bit(num, 2)  
print("Toggle :",num)

num = 10  
num = set_bit(num, 3) 
print("Set :",num)

num = 8  
bit = get_bit(num, 3) 
print("get :",num)



