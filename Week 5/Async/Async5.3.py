# Code:
import pandas as pd

## Creating the data and df
contacts = {
    'person': [
        'Bob', 'Alice', 'Steve'
    ],
    'age': [
        32, 24, 64
    ],
    'weight': [
        128, 86, 95
    ]
}
df = pd.DataFrame(contacts, columns=['person', 'age', 'weight'])

## Changing the index
df.set_index('person', inplace=True)

## Stacking
df_tall = df.stack()
print('Stacked df:')
print(df_tall)

## Resetting the index of the stacked df
df_reset_index = df_tall.reset_index() 
df_reset_index.columns = ['person', 'attribute', 'value']
print('Stacked df with index reset:')
print(df_reset_index)

## Unstacking the df
df_unstacked = df_tall.unstack()
print('Unstacked df:')
print(df_unstacked)

# Output:
# Stacked df:
# person        
# Bob     age        32
#         weight    128
# Alice   age        24
#         weight     86
# Steve   age        64
#         weight     95
# dtype: int64
# Stacked df with index reset:
#   person attribute  value
# 0    Bob       age     32
# 1    Bob    weight    128
# 2  Alice       age     24
# 3  Alice    weight     86
# 4  Steve       age     64
# 5  Steve    weight     95
# Unstacked df:
#         age  weight
# person             
# Bob      32     128
# Alice    24      86