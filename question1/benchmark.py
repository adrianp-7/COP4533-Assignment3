"""Benchmark max_val_sequence.py on all input files and graph the results."""

import os
import re
import subprocess
import time

import matplotlib.pyplot as plt


def run_benchmark(input_file: str, script_path: str, num_trials: int = 5) -> float:
    """Run max_val_sequence.py on an input file and return average runtime."""
    times = []
    for _ in range(num_trials):
        start = time.perf_counter()
        with open(input_file) as f:
            subprocess.run(
                ["python3", script_path],
                stdin=f,
                stdout=subprocess.DEVNULL,
                check=True,
            )
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    return sum(times) / len(times)


def extract_length(filename: str) -> int:
    """Extract string length from filename like input_01_len25.txt."""
    match = re.search(r"len(\d+)", filename)
    return int(match.group(1)) if match else 0


def main() -> None:
    inputs_dir = os.path.join(os.path.dirname(__file__), "inputs")
    script_path = os.path.join(os.path.dirname(__file__), "..", "max_val_sequence.py")

    input_files = sorted(
        [f for f in os.listdir(inputs_dir) if f.startswith("input_")],
        key=extract_length,
    )

    lengths: list[int] = []
    runtimes: list[float] = []

    print(f"{'File':<30} {'Length':>8} {'Avg Runtime (s)':>16}")
    print("-" * 58)

    for filename in input_files:
        filepath = os.path.join(inputs_dir, filename)
        length = extract_length(filename)
        avg_time = run_benchmark(filepath, script_path)

        lengths.append(length)
        runtimes.append(avg_time)
        print(f"{filename:<30} {length:>8} {avg_time:>16.6f}")

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, runtimes, 'bo-', linewidth=2, markersize=8)
    plt.xlabel("String Length (n = |A| = |B|)", fontsize=12)
    plt.ylabel("Average Runtime (seconds)", fontsize=12)
    plt.title("Runtime of Max-Value Common Subsequence (DP) — O(n²)", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), "runtime_graph.png")
    plt.savefig(output_path, dpi=150)
    print(f"\nGraph saved to {output_path}")


if __name__ == "__main__":
    main()
