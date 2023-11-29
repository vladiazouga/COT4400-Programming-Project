import random
import time

def partition(arr, p, r):
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)

def randomized_select(arr, p, r, i):
    if p == r:
        return arr[p]

    q = randomized_partition(arr, p, r)
    k = q - p + 1

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)

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
    theoretical_running_time = n

    # Run the algorithm multiple times and calculate average running time
    total_empirical_running_time = 0
    ratios = []

    for _ in range(iterations):
        input_array = generate_random_array(n)
        _, empirical_running_time = measure_running_time(randomized_select, input_array, i_value)
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