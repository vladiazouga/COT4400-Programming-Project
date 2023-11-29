import random
import time
import math

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = arr[p + i]

    for j in range(n2):
        R[j] = arr[q + j + 1]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def alg2(arr, i):
    merge_sort(arr, 0, len(arr) - 1)
    return arr[i - 1]

def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

def measure_running_time(algorithm, arr, i):
    start_time = time.time()
    result = algorithm(arr.copy(), i)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, running_time

# Experiment parameters
input_sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
iterations = 5
i_value = int(2 * len(input_sizes) / 3)

# Results table header
print("n\tTheoreticalRT\tEmpiricalRT (ms)\tRatio\tPredictedRT")

for n in input_sizes:
    theoretical_running_time = n * math.log(n, 2)  # O(n log(n))

    # Run the algorithm multiple times and calculate average running time
    total_empirical_running_time = 0
    ratios = []

    for _ in range(iterations):
        input_array = generate_random_array(n)
        _, empirical_running_time = measure_running_time(alg2, input_array, i_value)
        total_empirical_running_time += empirical_running_time

        # Calculate ratio for each iteration
        ratio = empirical_running_time / theoretical_running_time
        ratios.append(ratio)

    # Calculate c1 as the maximum ratio
    c1 = max(ratios)

    # Calculate predicted running time
    predicted_running_time = c1 * theoretical_running_time

    average_empirical_running_time = total_empirical_running_time / iterations

    # Format the output for better readability
    print(f"{n}\t{theoretical_running_time:.2f}\t\t{average_empirical_running_time:.2f}\t\t{c1:.8f}\t{predicted_running_time:.2f}")