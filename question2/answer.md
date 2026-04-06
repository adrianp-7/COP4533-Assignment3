# Question 2: Recurrence Equation for HVLCS 

## Definition

Let $A = a_1 a_2 \dots a_m$ and $B = b_1 b_2 \dots b_n$ be two strings over an alphabet where each character c has an associated value $v(c)$.

## Base Cases

$$dp[0][j] = 0 \quad \text{for all } 0 \leq j \leq n$$

$$dp[i][0] = 0 \quad \text{for all } 0 \leq i \leq m$$

When either prefix is empty, no common subsequence exists, so the maximum value is 0.

## Recurrence

For $1 \leq i \leq m$ and $1 \leq j \leq n$:

$$
dp[i][j] = \begin{cases} dp[i-1][j-1] + v(a_i) & \text{if } a_i = b_j \\ \max(dp[i-1][j],\ dp[i][j-1]) & \text{if } a_i \neq b_j \end{cases}
$$

The answer to the HVLCS problem is $dp[m][n]$.

## Correctness

The recurrence considers all possible ways to build an optimal common subsequence of $A[1..i]$ and $B[1..j]$:

**Case 1: $a_i = b_j$ (characters match).**
When the last characters of both prefixes are equal, it is always optimal to include this character in the subsequence.

**Case 2: $a_i \neq b_j$ (characters do not match).**
Since the characters differ, they cannot both appear at the same position in a common subsequence. Any common subsequence of $A[1..i]$ and $B[1..j]$ must either:

- Not use $a_i$, meaning it is a common subsequence of $A[1..i-1]$ and $B[1..j]$, with maximum value $dp[i-1][j]$, or
- Not use $b_j$, meaning it is a common subsequence of $A[1..i]$ and $B[1..j-1]$, with maximum value $dp[i][j-1]$.

Taking the maximum of these two covers all possibilities.

## Optimal Substructure

This recurrence exhibits optimal substructure: the optimal solution to $dp[i][j]$ is built from optimal solutions to smaller subproblems ($dp[i-1][j-1]$, $dp[i-1][j]$, or $dp[i][j-1]$). Any non-optimal choice for a subproblem could be replaced with a better one, improving the overall solution — a contradiction.
