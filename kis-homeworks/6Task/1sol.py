def main(B):
    Theta = {abs(beta) for beta in B if beta > -63}
    K = {7 * beta - abs(beta) for beta in B if (beta <= 24 or beta >= -98)}
    Lambda = {k % 3 + k for k in K if ((k < 98) ^ (k >= -27))}
    return len(Theta.union(Lambda)) - sum(abs(lll) for lll in Lambda)
