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


if __name__ == "__main__":
    max_value_subsequence()
