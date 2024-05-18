def main(B):
    return len(
        {abs(beta) for beta in B if beta > -63}.union(
            Lambda := {
                k % 3 + k
                for k in {
                    7 * beta - abs(beta) for beta in B if (beta <= 24 or beta >= -98)
                }
                if ((k < 98) ^ (k >= -27))
            }
        )
    ) - sum(abs(lll) for lll in Lambda)
