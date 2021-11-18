# Code:
data_path = "C:/Users/trist/Desktop/Trist'n/School/Syracuse University/Q3 2021/IST652/Week 2/NBAData.txt"

# Loading the data
data = open(data_path, 'r')

# Iterate over the lines of the file and count the number of lines
count = 0
data_list = []

for line in data:
    count += 1

    # Strip the new line at the end of the line
    text_line = line.strip()

    # split the line on whitespace
    items = text_line.split()

    # add to the list of items
    data_list.append(items)

# Creating a team list
team = []
for item in data_list:
    team.append(str(item[0]))

# Creating an attendence list
attendence = []
for item in data_list:
    attendence.append(int(item[1]))

# Creating a ticket list
price = []
for item in data_list:
    price.append(float(item[2]))

# Print statements
for i in range(len(team)):
    print('The attendance at', team[i], 'was', attendence[i], 'and the ticket price was ${:,.2f}'.format(price[i]))
    

# Output:
# The attendance at Atlanta was 13993 and the ticket price was $20.06
# The attendance at Boston was 14916 and the ticket price was $22.54
# The attendance at Charlotte was 23901 and the ticket price was $17.00
# The attendance at Chicago was 18404 and the ticket price was $21.98
# The attendance at Cleveland was 16969 and the ticket price was $19.63
# The attendance at Dallas was 16868 and the ticket price was $17.05
# The attendance at Denver was 12668 and the ticket price was $17.40
# The attendance at Detroit was 21454 and the ticket price was $24.42
# The attendance at Golden_State was 15025 and the ticket price was $17.04
# The attendance at Houston was 15846 and the ticket price was $17.56
# The attendance at Indiana was 12885 and the ticket price was $13.77
# The attendance at LA_Clippers was 11869 and the ticket price was $21.95
# The attendance at LA_Lakers was 17378 and the ticket price was $29.18
# The attendance at Miami was 15008 and the ticket price was $17.60
# The attendance at Milwaukee was 16088 and the ticket price was $14.08
# The attendance at Minnesota was 26160 and the ticket price was $10.92
# The attendance at New_Jersey was 12160 and the ticket price was $13.31
# The attendance at New_York was 17815 and the ticket price was $22.70
# The attendance at Orlando was 15606 and the ticket price was $20.47
# The attendance at Philadelphia was 14017 and the ticket price was $19.04
# The attendance at Phoenix was 14114 and the ticket price was $16.59
# The attendance at Portland was 12884 and the ticket price was $22.19
# The attendance at Sacramento was 17014 and the ticket price was $16.96
# The attendance at San_Antonio was 14722 and the ticket price was $16.79
# The attendance at Seattle was 12244 and the ticket price was $18.11
# The attendance at Utah was 12616 and the ticket price was $18.41
# The attendance at Washington was 11565 and the ticket price was $14.55
