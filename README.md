# QuickSelect Comparison – Lomuto vs. Hoare Partition

**Author:** Laura Estremera
**Course:** CSC 380 – Design and Analysis of Algorithms
**Instructor:** Dr. Devon Simmonds
**Date:** October 2024

---

## About
This program implements the **Quickselect algorithm** in Python to find the *k*-th smallest element in a list—specifically, the **median**. It compares two partitioning methods used within Quickselect:

* **Lomuto Partition**
* **Hoare Partition**

Performance is measured across both schemes using:

* (a) The total **number of swaps**
* (b) The **runtime** in seconds

The comparison is conducted over four randomized lists:

1. Small (20 elements)
2. Medium (1,000 elements)
3. Large (10,000 elements)
4. Very Large (100,000 elements)

---

## Features

* Implements both **Lomuto and Hoare partition schemes**
* Accurately tracks and compares **swap counts**
* Uses `time.perf_counter()` for **precise runtime measurement**
* Tests on **lists of increasing size**, using **random integers**
* Finds the **median (middle index)** in each case

---

## Assumptions

* Input lists are randomly generated with integers
* `k` is always set to the median index (`len(arr) // 2`)
* All lists are tested independently using both partitioning strategies
* List sizes and k-values are **hardcoded** for testing purposes

---

## Output Metrics

For each list size, the program prints:

* **Partition Method**
* **Median Value Found**
* **Number of Swaps**
* **Elapsed Runtime (in seconds)**

---

## Example Output (Truncated)

```
Testing on Medium List:
Lomuto: Median = 516, Swaps = 998, Time = 0.002731 seconds
Hoare: Median = 516, Swaps = 872, Time = 0.002089 seconds
```

---

## Tech Stack

* **Python 3.x**
* Standard libraries: `random`, `time`

---

## File List

| File             | Description                                         |
| ---------------- | --------------------------------------------------- |
| `QuickSelect.py` | Full implementation and performance comparison code |

---
