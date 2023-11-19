import time
import random
import tkinter as tk
from tkinter import ttk
def counting_algorithm(arr):
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    result = []
    for i in range(len(counts)):
        result.extend([i] * counts[i])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def linear_search_unordered(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, None)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(algorithm, *args, **kwargs):
    start_time = time.time()
    algorithm(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

# Generate random data for testing
data_sizes = [5000]
random_data = {size: random.sample(range(size * 10), size) for size in data_sizes}

# Compare and print the time taken by each algorithm for each data size
for size in data_sizes:
    print(f"\nData Size: {size}")
    data = random_data[size]

    counting_algorithm_time = measure_time(counting_algorithm, data.copy())
    print(f"Counting Algorithm Time: {counting_algorithm_time:.6f} seconds")

    insertion_sort_time = measure_time(insertion_sort, data.copy())
    print(f"Insertion Sort Time: {insertion_sort_time:.6f} seconds")

    selection_sort_time = measure_time(selection_sort, data.copy())
    print(f"Selection Sort Time: {selection_sort_time:.6f} seconds")

    linear_search_unordered_time = measure_time(linear_search_unordered, data.copy(), target=random.choice(data))
    print(f"Linear Search (Unordered) Time: {linear_search_unordered_time:.6f} seconds")

    hash_table = HashTable()
    for num in data:
        hash_table.insert(num, num)
    hash_table_search_time = measure_time(hash_table.search, key=random.choice(data))
    print(f"Hash Table Search Time: {hash_table_search_time:.6f} seconds")

    sorted_data = sorted(data.copy())
    binary_search_time = measure_time(binary_search, sorted_data, target=random.choice(data))
    print(f"Binary Search Time: {binary_search_time:.6f} seconds")

    # Compare the times and print the name of the fastest algorithm
    fastest_algorithm = min(
        ("Counting Algorithm", counting_algorithm_time),
        ("Insertion Sort", insertion_sort_time),
        ("Selection Sort", selection_sort_time),
        ("Linear Search (Unordered)", linear_search_unordered_time),
        ("Hash Table Search", hash_table_search_time),
        ("Binary Search", binary_search_time),
        key=lambda x: x[1]
    )
    print(f"The fastest algorithm is {fastest_algorithm[0]} with a time of {fastest_algorithm[1]:.6f} seconds.\n")


import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PyQt5 import QtWidgets
class AlgorithmComparisonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Algorithm Performance Comparison')
        self.setGeometry(100, 100, 600, 400)

        self.algorithm1_label = QLabel('Algorithm 1:')
        self.algorithm1_entry = QLineEdit(self)

        self.algorithm2_label = QLabel('Algorithm 2:')
        self.algorithm2_entry = QLineEdit(self)

        self.run_button = QPushButton('Run Comparison', self)
        self.run_button.clicked.connect(self.run_comparison)

        self.results_label = QLabel('Results:')
        self.results_text = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.algorithm1_label)
        layout.addWidget(self.algorithm1_entry)
        layout.addWidget(self.algorithm2_label)
        layout.addWidget(self.algorithm2_entry)
        layout.addWidget(self.run_button)
        layout.addWidget(self.results_label)
        layout.addWidget(self.results_text)

        self.setLayout(layout)

        self.show()

    def run_comparison(self):
        algorithm1_name = self.algorithm1_entry.text().strip()
        algorithm2_name = self.algorithm2_entry.text().strip()

        if not algorithm1_name or not algorithm2_name:
            self.show_error('Error', 'Please enter names for both algorithms.')
            return

        algorithm1 = globals().get(algorithm1_name)
        algorithm2 = globals().get(algorithm2_name)

        if not algorithm1 or not algorithm2:
            self.show_error('Error', 'One or both of the specified algorithms are not defined.')
            return

        self.results_text.clear()
        for size in [5000]:
            result = f"\nData Size: {size}\n"
            data = random.sample(range(size * 10), size)

            algorithm1_time = measure_time(algorithm1, data.copy())
            result += f"{algorithm1_name} Time: {algorithm1_time:.6f} seconds\n"

            algorithm2_time = measure_time(algorithm2, data.copy())
            result += f"{algorithm2_name} Time: {algorithm2_time:.6f} seconds\n"

            if(algorithm1_time<algorithm2_time):
                result += f"{algorithm1_name}\n"
            else:
                result += f"{algorithm2_name}\n"

            self.results_text.append(result)
        

    def show_error(self, title, message):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowTitle(title)
        error_dialog.showMessage(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlgorithmComparisonApp()
    sys.exit(app.exec_())
