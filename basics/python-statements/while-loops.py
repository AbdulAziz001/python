print("************* while demo  ***********************")
x = 0
while x < 5:
    print(f" value of x is {x}")
    x += 1
else:
    print(" x is not less than 5 ")

print("************* pass demo  ***********************")
x = [1, 2, 3]
for value in x:
    pass
print(" outside the loop ")

print("************* continue demo  ***********************")
x = [1, 2, 3]
for value in x:
    if value == 2:
        continue
    print(f" value of x is {value} ")

print("************* break demo  ***********************")
x = [1, 2, 3]
for value in x:
    if value == 2:
        break
    print(f" value of x is {value} ")

"""
************* while demo  ***********************
 value of x is 0
 value of x is 1
 value of x is 2
 value of x is 3
 value of x is 4
 x is not less than 5 
************* pass demo  ***********************
 outside the loop 
************* continue demo  ***********************
 value of x is 1 
 value of x is 3 
************* break demo  ***********************
 value of x is 1 

"""