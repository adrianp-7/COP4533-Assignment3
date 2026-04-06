# Question 3: Big-Oh

## Pseudocode

```
HVLCS(A, B, v):
    m = length(A)
    n = length(B)

    // Initialize (m+1) x (n+1) table with zeros
    for i = 0 to m:
        dp[i][0] = 0
    for j = 0 to n:
        dp[0][j] = 0

    // Fill the table
    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + v(A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

## Runtime Analysis

**Initialization:** Zeroing the first row takes $O(n)$ and the first column takes $O(m)$, giving $O(m + n)$ total.

**Table filling:** The nested loop iterates over all pairs $(i, j)$ where $1 \leq i \leq m$ and $1 \leq j \leq n$. Each cell performs $O(1)$ work (one comparison, one addition or max, and one assignment). Total: $O(m \cdot n)$.

**Return:** $O(1)$.

**Overall runtime:** $O(m \cdot n)$, where $m = |A|$ and $n = |B|$.

**Space complexity:** $O(m \cdot n)$ for the DP table.
