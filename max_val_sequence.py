def max_value_subsequence():
    """
    1. Create a DP table where dp[i][j] stores the max value of a common subsequence of A[0:i] and B[0:j]
    2. Fill the table by considering three cases:
        If A[i-1] == B[j-1], we can include this character
        If A[i-1] != B[j-1], we take the maximum of excluding from A or B
    3. Reconstruct the subsequence by backtracking through the DP table
    """

    # Read number of characters in alphabet
    K = int(input())

    # Build a dictionary mapping characters to their values
    char_values = {}
    for _ in range(K):
        parts = input().split()
        char = parts[0]
        value = int(parts[1])
        char_values[char] = value

    # Read the two strings
    A = input().strip()
    B = input().strip()

    m, n = len(A), len(B)

    # Initialize DP table: dp[i][j] = max value of common subsequence of A[0:i] and B[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # Characters match: include this character in the subsequence
                char = A[i - 1]
                dp[i][j] = dp[i - 1][j - 1] + char_values[char]
            else:
                # Characters don't match: take maximum of two options
                # Case 1: exclude A[i-1] -> look at dp[i-1][j]
                # Case 2: exclude B[j-1] -> look at dp[i][j-1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The max value is at dp[m][n]
    max_value = dp[m][n]

    # Reconstruct the optimal subsequence by backtracking
    subsequence = []
    i, j = m, n

if __name__ == "__main__":
    max_value_subsequence()
