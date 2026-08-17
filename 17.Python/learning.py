from decimal import Decimal

#------- First Code ----------#
# print("Hello this is my first code")

# print("hello this is my second code")

#-------- Variable and dataTypes ----------#
# name = "alis"
# print(name) 

# age = 22
# print(age)

# height = 6.5
# print(height)

# is_true = False
# print(is_true)

#----------- How Variables Work Internally ----------#
# x = 20
# print(x)

# y = x
# print(y)

# # Both point to same object!       
# print(id(x)) #4388237888
# print(id(y)) #4388237888

# a = 100
# b = 100
# print(a is b) #true

# a = 1000
# b = 1000
# print(b is a) #true

#----------- Numerical Data Types ------------#
#----------------------------------------------- 
# INTEGER (Int) 
#------------------------------------------------
# x = 10              #10
# big_num = 123432456785312
# print(big_num)  #123432456785312

# negative = -22      #-22

# binaryNum = 0b1001  
# print(binaryNum)    #10

# octal = 0o26
# print(octal)        #22

#---------------------------------------------
# Integer operations 
#----------------------------------------------
# print(10 // 3)    #3   (floor division)
# print(20 % 3)     #2   (module)
# print(2 ** 5)     #32  (exponentiation)

#----------------------------------------------
# Useful methods 
#-----------------------------------------------
# print(bin(10))      #0b1010
# print(hex(255))     #0xff
# print(oct(22))      #0o26
# print(int(64))      #64

#-------------------------------------------------------
# FLOATS (float) - 64-bit IEEE 754 double precision
#------------------------------------------------------- 
pi = 3.14159
print(pi)

# ⚠️ Floating point precision issues
print(0.1 + 0.2)          #0.30000000000000004
print(0.1 + 0.2 == 0.3)   # false

# Solution: Use decimal for precision like (from decimal import Decimal)
# print(Decimal('0.1') + Decimal('0.2'))                        #0.3
# print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))      #true 

#------------------------------------------------------------
# COMPLEX NUMBERS (complex)
#------------------------------------------------------------
# z = 3 + 4j
# print(z.real)            # 3.0
# print(z.imag)            # 4.0
# print(abs(z))            # 5.0 (magnitude)
# print(z.conjugate())     # (3-4j)



#------- Sequence Data Types -------#

