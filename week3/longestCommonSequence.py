def lcs_length(x, y):
    m, n = len(x), len(y)

    # Create a matrix to store length of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the matrix
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[m][n]


# Example usage
seq1 = "ABCDEF"
seq2 = "AEBDF"

length = lcs_length(seq1, seq2)

print(f"Longest common subsequence length btw '{seq1}' and '{seq2}': {length}")