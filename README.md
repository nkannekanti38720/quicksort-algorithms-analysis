# Quicksort Algorithms Analysis
Welcome to the "quicksort-algorithms-analysis" repository! In this project, I have implemented and analyzed the performance of both deterministic and randomized versions of the Quicksort algorithm.

Project Overview
In this project, I explored the Quicksort algorithm, focusing on:

Implementing the deterministic version of Quicksort, where the pivot is selected as the last element.

Implementing a randomized version of Quicksort, where the pivot is selected randomly, reducing the likelihood of encountering the worst-case time complexity.

Conducting an empirical analysis to compare the running time of both versions on different input sizes and distributions (random, sorted, reverse-sorted).

Providing insights into the time complexity and space complexity of both versions in various scenarios.

Features
Deterministic Quicksort: The classic version where the pivot is always the last element of the array.

Randomized Quicksort: An enhanced version where the pivot is chosen randomly to mitigate the chances of encountering the worst-case scenario.

Empirical Results: Detailed performance comparisons between the two algorithms, tested with different input sizes and distributions.

Getting Started
To get started with the project:

Clone this repository to your local machine:

bash
git clone https:[//github.com/your-username/quicksort-algorithms-analysis.git](https://github.com/nkannekanti38720/quicksort-algorithms-analysis)
Navigate to the project directory:

bash
cd quicksort-algorithms-analysis
Install Python if you haven’t already (Python 3.6+ recommended).

Run the code by executing the Python scripts directly:

bash
python empirical_analysis.py
This will execute the empirical analysis and output the performance results for both the deterministic and randomized versions of Quicksort.

File Structure
empirical_analysis.py: The main script for testing the performance of the Quicksort algorithms.

quicksort.py: Contains the implementation of both the deterministic and randomized Quicksort algorithms.

README.md: This file.

Results and Analysis
In my analysis, I tested both algorithms on various input sizes (ranging from 10 to 10,000 elements) and distributions (random, sorted, reverse sorted). The results will show the differences in performance between the two versions and help understand the impact of randomization on Quicksort’s performance.

Time Complexity:
Best and Average Case: 
O(nlogn)

Worst Case: 
𝑂(𝑛2)
 (for deterministic version when the pivot selection is poor)

Randomized Version: Avoids the worst-case scenario, maintaining O(nlogn) performance on average
