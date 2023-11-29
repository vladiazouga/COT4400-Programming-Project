import random
import time

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

def alg1(arr, i):
    insertion_sort(arr)
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
    theoretical_running_time = n ** 2

    # Run the algorithm multiple times and calculate average running time
    total_empirical_running_time = 0
    ratios = []

    for _ in range(iterations):
        input_array = generate_random_array(n)
        _, empirical_running_time = measure_running_time(alg1, input_array, i_value)
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