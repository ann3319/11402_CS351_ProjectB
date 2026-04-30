print("PROGRAM STARTED")
import csv

# 載入CSV
def load_csv(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# SELECT 查詢
def select_query(data, select_col, where_col=None, where_val=None):
    result = []

    for row in data:
        if where_col:
            if row[where_col] == where_val:
                result.append(row[select_col])
        else:
            result.append(row[select_col])

    return result


print("=== Mini Database ===")

filename = input("Enter CSV file: ")
data = load_csv(filename)

while True:
    command = input("SQL> ")

    if command.upper() == "EXIT":
        break

    try:
        parts = command.split()

        # SELECT Name FROM table
        if len(parts) == 4:
            col = parts[1]
            result = select_query(data, col)

        # SELECT Name FROM table WHERE Dept=CS
        elif len(parts) == 6:
            col = parts[1]
            condition = parts[5]

            where_col = condition.split("=")[0]
            where_val = condition.split("=")[1]

            result = select_query(data, col, where_col, where_val)

        else:
            print("Syntax Error")
            continue

        for item in result:
            print(item)

    except:
        print("Query Error")
