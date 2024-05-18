def decision_processor(x, decisions):
    result = None
    for decision in decisions:
        index, mapping, values = decision
        key = x[index]
        choice = mapping.get(key, None)
        if choice is not None:
            result = values[choice]
    return result


def main(x):
    # Decision mappings and values
    decisions = [
        (
            2,
            {"CMAKE": 0, "SAS": 1, "EC": 2},
            [
                decision_processor(
                    x,
                    [
                        (
                            0,
                            {"MUPAD": 0, "NIM": 1, "PAN": 2},
                            [
                                decision_processor(
                                    x,
                                    [
                                        (
                                            3,
                                            {"RED": 0, "C++": 1},
                                            [
                                                0,
                                                decision_processor(
                                                    x,
                                                    [
                                                        (
                                                            4,
                                                            {
                                                                "INI": 0,
                                                                "X10": 1,
                                                                "SCAML": 2,
                                                            },
                                                            [1, 2, 3],
                                                        )
                                                    ],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                decision_processor(
                                    x,
                                    [
                                        (
                                            1,
                                            {1987: 0, 1974: 1, 2003: 2},
                                            [
                                                4,
                                                decision_processor(
                                                    x,
                                                    [
                                                        (
                                                            4,
                                                            {
                                                                "INI": 0,
                                                                "X10": 1,
                                                                "SCAML": 2,
                                                            },
                                                            [5, 6, 7],
                                                        )
                                                    ],
                                                ),
                                                decision_processor(
                                                    x,
                                                    [
                                                        (
                                                            4,
                                                            {
                                                                "INI": 0,
                                                                "X10": 1,
                                                                "SCAML": 2,
                                                            },
                                                            [8, 9, 10],
                                                        )
                                                    ],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                11,
                            ],
                        )
                    ],
                ),
                12,
                13,
            ],
        )
    ]

    return decision_processor(x, decisions)
