"""
Author: Tami Green, PhD
Date: October 2024
Script Name: compound_function_efficiency.py
License: MIT License

Description:
This script demonstrates a performance comparison between traditional nested loop approaches (O(n^2))
and optimized compound functions using set-based lookups (O(n)). It generates a graph showing the 
difference in efficiency as dataset sizes grow, proving the effectiveness of compound functions for
scalable software performance.

MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import random
import matplotlib.pyplot as plt
import os  # Import os to get the current directory

# Generate random user IDs
def generate_user_ids(n):
    return random.sample(range(1, 10**6), n)

# Traditional O(n^2) approach (nested loops)
def find_matches_nested_loops(listA, listB):
    matches = []
    for userA in listA:
        for userB in listB:
            if userA == userB:
                matches.append(userA)
    return matches

# Optimized O(n) approach using set
def find_matches_using_set(listA, listB):
    setB = set(listB)
    matches = [userA for userA in listA if userA in setB]
    return matches

# Measure the runtime of both approaches
def measure_performance(list_sizes):
    nested_times = []
    optimized_times = []
    
    for size in list_sizes:
        listA = generate_user_ids(size)
        listB = generate_user_ids(size)
        
        # Measure nested loop time
        start_time = time.time()
        find_matches_nested_loops(listA, listB)
        nested_times.append(time.time() - start_time)
        
        # Measure optimized set time
        start_time = time.time()
        find_matches_using_set(listA, listB)
        optimized_times.append(time.time() - start_time)
    
    return nested_times, optimized_times

# Plot the comparison graph and save
def plot_performance_graph(list_sizes, nested_times, optimized_times):
    plt.figure(figsize=(10, 6))
    plt.plot(list_sizes, nested_times, label="Nested Loops (O(n^2))", color='red', marker='o')
    plt.plot(list_sizes, optimized_times, label="Set-based Lookup (O(n))", color='blue', marker='o')
    
    plt.title("Performance Comparison: Nested Loops vs Set-based Lookup")
    plt.xlabel("Size of List (n)")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid(True)
    
    # Get the current working directory
    current_directory = os.getcwd()
    # Define the file path where the graph will be saved
    graph_path = os.path.join(current_directory, "performance_comparison.png")
    
    # Save the graph in the current directory
    plt.savefig(graph_path)
    print(f"Graph saved as 'performance_comparison.png' in {current_directory}")
    plt.show()

# Example usage
if __name__ == "__main__":
    list_sizes = [100, 500, 1000, 5000, 10000, 20000, 50000]  # Sizes of the lists to test
    nested_times, optimized_times = measure_performance(list_sizes)  # Measure performance of both approaches
    plot_performance_graph(list_sizes, nested_times, optimized_times)  # Plot and save the performance graph
