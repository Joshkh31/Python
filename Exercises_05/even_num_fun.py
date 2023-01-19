def find_even_num(number_list:int, number:int)->bool:
    for iterate_number in number_list:
        if (iterate_number % number) == 0:
            return True
        else:
           pass
    result = find_even_num([1,3,5,6,7,9,24], 2)
    print(result)
    
