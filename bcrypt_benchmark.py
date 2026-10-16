#!/usr/bin/env python3
"""Benchmark bcrypt verification time for cost factors 10, 12, and 14."""

import bcrypt
import time
import statistics

password = b"demo123"
repetitions = 5

print("bcrypt verification benchmark")
print(f"Repetitions per cost: {repetitions}")
print()

for cost in (10, 12, 14):
    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt(rounds=cost)
    )

    timings = []

    for _ in range(repetitions):
        start = time.perf_counter()
        valid = bcrypt.checkpw(password, hashed)
        elapsed = time.perf_counter() - start

        assert valid
        timings.append(elapsed * 1000)

    print(f"Cost factor: {cost}")
    print(f"Median time: {statistics.median(timings):.2f} ms")
    print(f"All trials: {[round(t, 2) for t in timings]} ms")
    print()
