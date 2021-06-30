# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portions of the string after the colon character, and then use the float function to convert the extracted string into a floating point number with two decimals.

given_str = 'X-DSPAM-Confidence:0.8475'

colon_char_index = given_str.find(":")
string_colon_char = float(given_str[colon_char_index + 1:len(given_str)])
print('{:.2f}'.format(string_colon_char))

# Output:
# 0.85
