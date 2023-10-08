import pandas as pd

# Read data from two sheets of the same Excel file
file_path = 'file_A.xlsx'
sheet1_name = 'Sheet1'
sheet2_name = 'Sheet 2'

df1 = pd.read_excel(file_path, sheet_name=sheet1_name)
df2 = pd.read_excel(file_path, sheet_name=sheet2_name)


unique_ids = set(df1['id'].unique()).union(df2['id'].unique())
total_unique_ids = len(unique_ids)


unique_ids_sheet1 = set(df1['id'].unique())
unique_ids_sheet2 = set(df2['id'].unique())


count_rows_sheet1 = {id_value: len(df1[df1['id'] == id_value]) for id_value in unique_ids}
count_rows_sheet2 = {id_value: len(df2[df2['id'] == id_value]) for id_value in unique_ids}


for id_value in unique_ids:
    rows1 = df1[df1['id'] == id_value]
    rows2 = df2[df2['id'] == id_value]
    if count_rows_sheet1[id_value] != count_rows_sheet2[id_value]:
        print(f"ID {id_value}: {count_rows_sheet1[id_value]} rows in sheet 1, {count_rows_sheet2[id_value]} rows in sheet 2")
    else:

        if rows1.equals(rows2):
            print(f"ID {id_value}: Rows are identical")
        else:
            print(f"ID {id_value}: Rows are not identical")


for id_value in unique_ids:
    if count_rows_sheet1[id_value] != count_rows_sheet2[id_value]:
        rows1 = df1[df1['id'] == id_value]
        rows2 = df2[df2['id'] == id_value]
        if count_rows_sheet1[id_value] == 4 and count_rows_sheet2[id_value] == 2 and rows1.equals(rows2):
            print(f"ID {id_value}: Rows are identical despite count mismatch")


missing_ids_in_sheet1 = list(unique_ids_sheet2 - unique_ids_sheet1)
missing_ids_in_sheet2 = list(unique_ids_sheet1 - unique_ids_sheet2)

print(f"1. Total unique IDs detected: {total_unique_ids}")
print(f"2. Total Unique IDs in sheet 1: {len(unique_ids_sheet1)}")
print(f"   Total Unique IDs in sheet 2: {len(unique_ids_sheet2)}")
print("3. For each of these unique IDs:")
for id_value in unique_ids:
    print(f"   ID {id_value}: {count_rows_sheet1[id_value]} rows in sheet 1, {count_rows_sheet2[id_value]} rows in sheet 2")
print(f"4. Missing IDs in sheet 1: {missing_ids_in_sheet1}")
print(f"   Missing IDs in sheet 2: {missing_ids_in_sheet2}")
