print("PROGRAM STARTED")
import csv
import re

# 載入 CSV(有錯誤處理)
def load_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
        return None

# SELECT 查詢(支援多欄位、支援 *、欄位錯誤會說明是哪個欄位)
def select_query(data, select_cols, where_col=None, where_val=None):
    if where_col is not None and data and where_col not in data[0]:
        raise KeyError(where_col)

    result = []
    for row in data:
        if where_col is not None and row[where_col] != where_val:
            continue
        if select_cols == ["*"]:
            result.append(list(row.values()))
        else:
            values = []
            for col in select_cols:
                if col not in row:
                    raise KeyError(col)
                values.append(row[col])
            result.append(values)
    return result

# 解析一行 SQL(用正規表達式)
# 支援: SELECT col1, col2 FROM table [WHERE col=val]
SQL_PATTERN = re.compile(
    r'^SELECT\s+(?P<cols>.+?)\s+FROM\s+(?P<table>\S+)'
    r'(?:\s+WHERE\s+(?P<wcol>\S+?)\s*=\s*(?P<wval>\S+))?$',
    re.IGNORECASE
)

print("=== Mini Database ===")
filename = input("Enter CSV file: ")
data = load_csv(filename)

while True:
    command = input("SQL> ").strip()
    if command.upper() == "EXIT":
        break
    if data is None:
        print("No data loaded. Please restart with a valid CSV file.")
        continue
    if not command:
        continue
    match = SQL_PATTERN.match(command)
    if not match:
        print("Syntax Error")
        continue
    try:
        cols_part = match.group("cols")
        select_cols = ["*"] if cols_part.strip() == "*" else [c.strip() for c in cols_part.split(",")]
        where_col = match.group("wcol")
        where_val = match.group("wval")
        result = select_query(data, select_cols, where_col, where_val)
        if not result:
            print("(no rows)")
        for row in result:
            print(", ".join(row))
    except KeyError as e:
        print(f"Query Error: unknown column '{e.args[0]}'")
    except Exception:
        print("Query Error")
