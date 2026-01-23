import timeit
import numpy as np

# Number of entities
N = 1_000_000

# --- AoS (Array of Structures) ---
# Each object has "noise" (extra data) that pollutes the cache
class Entity:
    def __init__(self):
        self.health = 100.0
        self.unused_1 = 0.0
        self.unused_2 = 0.0
        self.unused_3 = 0.0

aos_data = [Entity() for _ in range(N)]

# --- SoA (Structure of Arrays) ---
# Just a flat block of memory containing only what we need
soa_data = np.ones(N, dtype=np.float64) * 100.0

def test_aos():
    return sum(e.health for e in aos_data)

def test_soa():
    # NumPy uses C-style contiguous memory (SoA)
    return np.sum(soa_data)

# Timing the results
time_aos = timeit.timeit(test_aos, number=10)
time_soa = timeit.timeit(test_soa, number=10)

print(f"AoS Time: {time_aos:.4f}s")
print(f"SoA Time: {time_soa:.4f}s")
print(f"SoA is {time_aos / time_soa:.1f}x faster!")
