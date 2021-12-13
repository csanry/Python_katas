## Supermarket Queue - 6kyu

**Instructions**

- There is a queue for the self-checkout tills at the supermarket. 

- Write a function to calculate the total time required for all the customers to check out.

**Input**

`customers`: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.

`n`: a positive integer, the number of checkout tills.

**Output**

Integer representing the total time required.

---

#### Test cases

```python
print(queue_time([2, 2, 3, 3, 4, 4], 2))
print(queue_time([2, 8, 16, 5, 8, 7, 17], 3))
```

#### Output 

```
9
32
```

---

#### Solution

```python
import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)
```

---

[Codewars link](https://www.codewars.com/kata/57b06f90e298a7b53d000a86)
