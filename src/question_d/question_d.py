#write functions here, don't add input('') statements here!
def create_multiplication_table():
    table = []
    for row in range(1, 6):
        table_row = []
        for col in range (1,11):
            table_row.append(row * col)
        table.append(table_row)
    return table

def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:<4}", end="")
        print()