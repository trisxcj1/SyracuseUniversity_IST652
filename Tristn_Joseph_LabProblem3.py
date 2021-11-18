# Code:
# Problem 1
# Write a Python function to multiply all the numbers in a list.

def multiply_list(input_list):
    """
    """

    result = 1

    for number in input_list:
        result = result * number

    return(result)

sample_list = [8, 2, 3, -1, 7]
print('Sample list:', sample_list, ', Output:', multiply_list(sample_list))

trial_list_1 = [1]
trial_list_2 = [11, 12, 13, 14, 15]
trial_list_3 = [9, 20000, 5, 17, 891]
trial_list_4 = [4, -1, 0, 1]
print('Sample list:', trial_list_1, ', Output:', multiply_list(trial_list_1))
print('Sample list:', trial_list_2, ', Output:', multiply_list(trial_list_2))
print('Sample list:', trial_list_3, ', Output:', multiply_list(trial_list_3))
print('Sample list:', trial_list_4, ', Output:', multiply_list(trial_list_4))

# Problem 2
# Write a Python function that accepts a string and calculate the number of upper
# case letters and lower case letters.
def calculate_number_of_upper_and_lower_case_letters(input_string):
    """
    """
    case_count = {'upper_case': 0, 'lower_case': 0}
    for letter in input_string:
        
        if letter.isupper():
            case_count['upper_case'] += 1
            
        else:
            case_count['lower_case'] += 1

    print("The number of upper case letters in '", input_string, "' is:", case_count['upper_case'])
    print("The number of lower case letters in '", input_string, "' is:", case_count['lower_case'])

print('Letter calculations:')
calculate_number_of_upper_and_lower_case_letters('The quick Brown Fox')
calculate_number_of_upper_and_lower_case_letters('i ReAlLy LoVe ThIs CoUrSe')
calculate_number_of_upper_and_lower_case_letters('alrighty there bud.')
calculate_number_of_upper_and_lower_case_letters('DATA@SYRACUSE')

# Output:
# Sample list: [8, 2, 3, -1, 7] , Output: -336
# Sample list: [1] , Output: 1
# Sample list: [11, 12, 13, 14, 15] , Output: 360360
# Sample list: [9, 20000, 5, 17, 891] , Output: 13632300000
# Sample list: [4, -1, 0, 1] , Output: 0
# Letter calculations:
# The number of upper case letters in ' The quick Brown Fox ' is: 3
# The number of lower case letters in ' The quick Brown Fox ' is: 16
# The number of upper case letters in ' i ReAlLy LoVe ThIs CoUrSe ' is: 10
# The number of lower case letters in ' i ReAlLy LoVe ThIs CoUrSe ' is: 15
# The number of upper case letters in ' alrighty there bud. ' is: 0
# The number of lower case letters in ' alrighty there bud. ' is: 19
# The number of upper case letters in ' DATA@SYRACUSE ' is: 12
# The number of lower case letters in ' DATA@SYRACUSE ' is: 1
