def transpose(table: list[list[any]] | tuple[tuple[any]]):
    return [list(row) for row in zip(*table)]


def remove_empty_rows(table: list[list[any]] | tuple[tuple[any]]):
    return [row for row in table if any(cell for cell in row)]


def remove_duplicate_rows(table: list[list[any]] | tuple[tuple[any]]):
    seen_rows = set()
    unique_table = []
    for row in table:
        if tuple(row) not in seen_rows:
            unique_table.append(row)
            seen_rows.add(tuple(row))
    return unique_table


def dot_to_hyphen(cell: str):
    if cell.count(".") == 2:
        return cell.replace(".", "-")

    return cell


def correct_numbers(cell: str):
    if len(cell) > 9 and cell.isdigit():
        return f"{cell[3:6]}-{cell[6:8]}-{cell[8:]}"

    try:
        num = float(cell)
        return f"{round(num, 3):.3f}"
    except ValueError:
        return cell


def name_transformation(cell: str):
    if " " in cell and "." in cell:
        parts = cell.split()
        # print(parts)
        if len(parts) == 3 and parts[1].endswith("."):
            # print(f"{parts[0]} {parts[2]}")
            return f"{parts[0]} {parts[2]}"
    return cell


def main(table: list[list[any]] | tuple[tuple[any]]):
    table = [list(row) for row in table]

    # Step 1: Remove empty rows
    table = remove_empty_rows(table)

    # Step 2: Remove duplicate rows
    table = remove_duplicate_rows(table)

    # Step 3: Remove empty columns after removing duplicates
    table = transpose(table)
    table = remove_empty_rows(table)
    table = remove_duplicate_rows(table)
    table = transpose(table)

    # Step 4: Transform cells
    for row in table:
        # print(f'{row = } before')
        for i, cell in enumerate(row):
            cell = dot_to_hyphen(cell)
            # print(f'{cell = } after dot_to_hyphen')
            cell = name_transformation(cell)
            # print(f'{cell = } after name_transformation')
            cell = correct_numbers(cell)
            # print(f'{cell = } after correct_numbers')
            row[i] = cell

    return table


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
