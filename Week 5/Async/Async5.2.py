# Code:
import pandas as pd

state_data = {
    'State':[
        'Alabama', 'Alaska', 'Arizona', 'Arkansas'
    ],
    'PostCode': [
        'AL', 'AK', 'AZ', 'AR'
    ],
    'Area': [
        '52,423', '656,424', '*', '53,182'
    ],
    'Pop':[
        '4,040,587', '550,043', '3,665,228', '2,350,750'
    ]
}

# Creating the df and displaying 
df = pd.DataFrame(state_data, columns=['State', 'PostCode', 'Area', 'Pop'])
print(df)

# Indexing by State
df.set_index('State', inplace=True)
print(df)

# Replace '*' with '0'
df = df.replace('*', 0)
print(df)

# Replace the "," with ""
def item_replace(input_str):
    """
    This function accepts a string as input
    Removes the comma in the string and replaces it with nothing
    """
    input_str = str(input_str)
    return int(input_str.replace(",", ""))

df['Area'] = df['Area'].map(item_replace)
df['Pop'] = df['Pop'].map(item_replace)
print(df)

# Output:
#       State PostCode     Area        Pop
# 0   Alabama       AL   52,423  4,040,587
# 1    Alaska       AK  656,424    550,043
# 2   Arizona       AZ        *  3,665,228
# 3  Arkansas       AR   53,182  2,350,750
#          PostCode     Area        Pop
# State                                
# Alabama        AL   52,423  4,040,587
# Alaska         AK  656,424    550,043
# Arizona        AZ        *  3,665,228
# Arkansas       AR   53,182  2,350,750
#          PostCode     Area        Pop
# State                                
# Alabama        AL   52,423  4,040,587
# Alaska         AK  656,424    550,043
# Arizona        AZ        0  3,665,228
# Arkansas       AR   53,182  2,350,750
#          PostCode    Area      Pop
# State                             
# Alabama        AL   52423  4040587
# Alaska         AK  656424   550043
# Arizona        AZ       0  3665228
# Arkansas       AR   53182  2350750
# (venv) txj@txj-Surface-Laptop:~/workspace/school/syracuse_university/SyracuseUniversity_IST652/Week 5/Async$ python Async5.2.py 
#       State PostCode     Area        Pop
# 0   Alabama       AL   52,423  4,040,587
# 1    Alaska       AK  656,424    550,043
# 2   Arizona       AZ        *  3,665,228
# 3  Arkansas       AR   53,182  2,350,750
#          PostCode     Area        Pop
# State                                
# Alabama        AL   52,423  4,040,587
# Alaska         AK  656,424    550,043
# Arizona        AZ        *  3,665,228
# Arkansas       AR   53,182  2,350,750
#          PostCode     Area        Pop
# State                                
# Alabama        AL   52,423  4,040,587
# Alaska         AK  656,424    550,043
# Arizona        AZ        0  3,665,228
# Arkansas       AR   53,182  2,350,750
#          PostCode    Area      Pop
# State                             
# Alabama        AL   52423  4040587
# Alaska         AK  656424   550043
# Arizona        AZ       0  3665228
# Arkansas       AR   53182  2350750