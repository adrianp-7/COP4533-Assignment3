# COP4533 Assignment 3 — Highest-Value Longest Common Subsequence (HVLCS)

## Student Information

- **Name:** Arnav Bagmar, Adrian Pelaez

## How to Run

### Prerequisites

- Python 3.10+
- `matplotlib` (for Question 1 graphing only): `pip install matplotlib`

### Running the HVLCS Algorithm

```bash
python3 max_val_sequence.py < input_file.txt
```

The program reads from standard input and prints:
1. The maximum value of the HVLCS
2. The subsequence itself

### Running the Benchmark (Question 1)

```bash
python3 question1/benchmark.py
```

This runs `max_val_sequence.py` on all 10 input files in `question1/inputs/` and saves a runtime graph to `question1/runtime_graph.png`.

## Input Format

```
K
c1 v1
c2 v2
...
cK vK
A
B
```

- `K`: number of characters in the alphabet
- `ci vi`: character and its integer value (one per line)
- `A`: first string
- `B`: second string

## Output Format

```
max_value
subsequence
```

## Assumptions

- All character values are positive integers.
- Both strings only contain characters defined in the alphabet.
- Input is well-formed (no extra whitespace or missing lines).

## Written Solutions

- [Question 1: Empirical Comparison](question1/runtime_graph.png) — runtime benchmark and graph
- [Question 2: Recurrence Equation](question2/answer.md) — recurrence, base cases, and correctness proof
- [Question 3: Big-Oh](question3/answer.md) — pseudocode and runtime analysis