code_grid = [['D', 'A', 'V', 'I', 'O'],
             ['N', 'B', 'C', 'E', 'F'],
             ['G', 'H', 'K', 'L', 'M'],
             ['P', 'Q', 'R', 'S', 'T'],
             ['U', 'W', 'X', 'Y', 'Z']]


coded_message = "HU UJND RXBQ RKJI XFXA XBJF ZKHL V"


coded_message = coded_message.upper()


coded_message = coded_message.replace(" ", "")


decoded_message = []


for i in range(0, len(coded_message), 2):
    
    first_letter = coded_message[i]
    first_row = None
    first_col = None
    for row in range(len(code_grid)):
        if first_letter in code_grid[row]:
            first_row = row
            first_col = code_grid[row].index(first_letter)
            break
    second_letter = coded_message[i+1]
    second_row = None
    second_col = None
    for row in range(len(code_grid)):
        if second_letter in code_grid[row]:
            second_row = row
            second_col = code_grid[row].index(second_letter)
            break
    
    
    if first_row == second_row:
        first_col = (first_col - 1) % 5
        second_col = (second_col - 1) % 5
    
    elif first_col == second_col:
        first_row = (first_row - 1) % 5
        second_row = (second_row - 1) % 5
    
    else:
        first_col, second_col = second_col, first_col
    decoded_message.append(code_grid[first_row][first_col])
    decoded_message.append(code_grid[second_row][second_col])


print("".join(decoded_message))
