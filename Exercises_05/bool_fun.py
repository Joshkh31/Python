def divisible(numerator: int, denominator: int)->bool:
 return numerator % denominator == 0
print(divisible(30,4))
# here the ans would be false bcoz 30/4 != 0

""""""
# For result to be true we can change the value of denominator to 3/6/2/10/5 which will prove the statement numerator%denominator == 0

def divisible(numerator: int, denominator: int)->bool:
 return numerator % denominator == 0
print(divisible(30,10))

""""""

def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number == number:
        return True
    else:
        pass
result = find_num([1,2,3,4,5,6,7,8],9)
print(result)
# Here the result is none becoz iterate_num i.e number_list is not equal to number(i.e 9) 

""""""
#To make the result true we will add 9 to number_list and then check the result

def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number == number:
        return True
    else:
        pass
result = find_num([1,2,3,4,5,6,7,8,9], 9)
print(result)

#To get 'false' result
def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number != number:
        return False
    else:
        pass
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

""""""
# OR
def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number == number:
        return True
    else:
         return False
result = find_num([1,2,3,4,5,6,7,8],9)
print(result)