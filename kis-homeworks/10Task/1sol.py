# def transform_cell(cell):
#     cell = str(cell)
#     # Date transformation
#     if "." in cell and cell.count(".") == 2:
#         cell = cell.replace(".", "-")
#     # Rounding numbers
#     try:
#         num = float(cell)
#         cell = f"{round(num, 3):.3f}"
#     except ValueError:
#         pass
#     # Name transformation
#     if " " in cell:
#         parts = cell.split()
#
#         cell = f"{parts[0]} {parts[2]}"
#     # Phone number transformation
#     if len(cell) >= 9 and ".000" in cell:
#         cell = cell[0:-4]
#         cell = "0" * (10 - len(cell)) + cell
#         cell = f"{cell[3:6]}-{cell[6:8]}-{cell[8:]}"
#     return cell
#
#
# def uniquyfy_table(table):
#     seen_columns = set()
#     unique_table = []
#     for row in table:
#         new_row = []
#         for col in row:
#             if col not in seen_columns:
#                 new_row.append(col)
#                 seen_columns.add(col)
#         unique_table.append(new_row)
#     return unique_table
#
#
# def main(table):
#     # Step 1: Remove duplicate columns
#     table = [[cell for cell in row if bool(cell)] for row in table if any(row)]
#     unique_table = uniquyfy_table(table)
#
#     filtered_table = unique_table
#
#     # Step 4: Transform cell contents
#     transformed_table = [
#         [transform_cell(cell) for cell in row] for row in filtered_table
#     ]
#
#     return transformed_table
#
#
# # Example input table
# input_table = [
#     ["03.10.99", "0.7", "Роман Л. Содский", None, "5152218272", None, "5152218272"],
#     [None, None, None, None, None, None, None],
#     ["27.11.01", "0.2", "Демид А. Лосий", None, "7073952123", None, "7073952123"],
#     ["11.02.02", "0.4", "Иван О. Рацич", None, "5164452044", None, "5164452044"],
#     ["06.04.00", "0.2", "Илья Д. Дучасяк", None, "2143133531", None, "2143133531"],
# ]
#
# # Transforming the table
# output_table = main(input_table)
#
# # Printing the output table
# for row in output_table:
#     print(row)
def transform_cell(cell):
    if cell is None:
        return ""
    cell = str(cell)

    # Date transformation
    if "." in cell and cell.count(".") == 2:
        cell = cell.replace(".", "-")

    # Rounding numbers
    try:
        num = float(cell)
        cell = f"{round(num, 3):.3f}"
    except ValueError:
        pass

    # Name transformation
    if " " in cell and "." in cell:
        parts = cell.split()
        if len(parts) == 3 and parts[1].endswith("."):
            cell = f"{parts[0]} {parts[2]}"

    # Phone number transformation
    if cell.isdigit() and len(cell) >= 7:
        cell = cell.zfill(10)  # Pad to ensure it's at least 10 digits
        cell = f"{cell[-10:-7]}-{cell[-7:-5]}-{cell[-5:-3]}-{cell[-3:]}"

    return cell


def uniquify_table(table):
    seen_columns = set()
    unique_table = []
    for row in table:
        new_row = []
        for col in row:
            if col not in seen_columns:
                new_row.append(col)
                seen_columns.add(col)
        unique_table.append(new_row)
    return unique_table


def main(table):
    # Step 1: Remove empty rows
    table = [row for row in table if any(cell for cell in row)]

    # Step 2: Remove duplicate columns
    unique_table = uniquify_table(table)

    # Step 3: Remove empty columns after removing duplicates
    transpose_table = list(
        zip(*unique_table)
    )  # Transpose the table for easy column operations
    non_empty_columns = [
        col
        for col in transpose_table
        if any(cell is not None and cell != "" for cell in col)
    ]
    filtered_table = list(zip(*non_empty_columns))  # Transpose back to original layout

    # Step 4: Transform cell contents
    transformed_table = [
        [transform_cell(cell) for cell in row] for row in filtered_table
    ]

    return transformed_table


# Example input table
input_table = [
    ["03.10.99", "0.7", "Роман Г. Содский", "221827272", "221827272"],
    ["27.11.01", "0.2", "Демид Л. Лосий", "395212345", "395212345"],
    ["11.02.02", "0.4", "Иван Н. Рацич", "445202012", "445202012"],
    ["06.04.00", "0.2", "Илья И. Дучасяк", "313353131", "313353131"],
]

# Transforming the table
output_table = main(input_table)

# Printing the output table
for row in output_table:
    print(row)
