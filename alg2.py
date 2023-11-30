import random  # Import the random module for generating random numbers
import time  # Import the time module for measuring execution time
import math  # Import the math module for mathematical operations

# Function to merge two subarrays of arr[].
def custom_merge(arr, p, q, r):
    n1 = q - p + 1  # Length of the left subarray
    n2 = r - q      # Length of the right subarray

    # Create temporary arrays to hold the left and right subarrays
    left_array = [0] * (n1 + 1)
    right_array = [0] * (n2 + 1)

    # Copy data to temporary arrays left_array[] and right_array[]
    for i in range(n1):
        left_array[i] = arr[p + i]

    for j in range(n2):
        right_array[j] = arr[q + j + 1]

    # Set the last element of each temporary array to infinity
    left_array[n1] = float('inf')
    right_array[n2] = float('inf')

    i = 0
    j = 0

    # Merge the two subarrays back into the original array arr[]
    for k in range(p, r + 1):
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1

# Function to perform merge sort on the array arr[]
def custom_merge_sort(arr, p, r):
    if p < r:
        mid = (p + r) // 2
        custom_merge_sort(arr, p, mid)
        custom_merge_sort(arr, mid + 1, r)
        custom_merge(arr, p, mid, r)

# Function implementing the custom algorithm
def custom_algorithm(arr, i):
    custom_merge_sort(arr, 0, len(arr) - 1)
    return arr[i - 1]

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to measure the execution time of a given algorithm on a given array
def measure_execution_time(algorithm, arr, i):
    start_time = time.time()  # Record the start time
    result = algorithm(arr.copy(), i)  # Execute the algorithm on a copy of the array
    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time

# Experiment parameters
array_sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
iterations = 5
i_value = int(2 * len(array_sizes) / 3)

# Results table header with changed names
print("{:<15} {:<20} {:<20} {:<15} {:<20}".format("Array Size", "Theoretical Time", "Empirical Time (ms)", "Ratio", "Predicted Time"))

# Iterate over array sizes for the experiment
for size in array_sizes:
    theoretical_time = size * math.log(size, 2)  # Theoretical time complexity O(n log(n))

    # Run the algorithm multiple times and calculate average execution time
    total_empirical_time = 0
    ratios = []

    for _ in range(iterations):
        input_array = generate_random_array(size)
        _, empirical_time = measure_execution_time(custom_algorithm, input_array, i_value)
        total_empirical_time += empirical_time

        # Calculate ratio for each iteration
        ratio = empirical_time / theoretical_time
        ratios.append(ratio)

    # Calculate c1 as the maximum ratio
    c1 = max(ratios)

    # Calculate predicted execution time
    predicted_time = c1 * theoretical_time

    average_empirical_time = total_empirical_time / iterations

    # Format the output for better readability
    print("{:<15} {:<20.2f} {:<20.2f} {:<15.8f} {:<20.2f}".format(size, theoretical_time, average_empirical_time, c1, predicted_time))
