def get_result_by_key(mapping, key, *values):
    # this function looks up the key in the given mapping and returns the corresponding value from values
    return values[mapping.get(key, -1)]


def main(x):
    # Define mappings for each decision point
    x0_mapping = {"MUPAD": 0, "NIM": 1, "PAN": 2}
    x1_mapping = {1987: 0, 1974: 1, 2003: 2}
    x2_mapping = {"CMAKE": 0, "SAS": 1, "EC": 2}
    x3_mapping = {"RED": 0, "C++": 1}
    x4_mapping = {"INI": 0, "X10": 1, "SCAML": 2}

    x4_values = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    x4_results = [
        get_result_by_key(x4_mapping, x[4], *x4_values[:3]),
        get_result_by_key(x4_mapping, x[4], *x4_values[3:6]),
        get_result_by_key(x4_mapping, x[4], *x4_values[6:9]),
    ]

    x3_result = get_result_by_key(x3_mapping, x[3], 0, x4_results[0])
    x0_result = get_result_by_key(
        x0_mapping,
        x[0],
        x3_result,
        get_result_by_key(x1_mapping, x[1], 4, x4_results[1], x4_results[2]),
        11,
    )

    return get_result_by_key(x2_mapping, x[2], x0_result, 12, 13)
