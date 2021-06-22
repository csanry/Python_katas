# supermarket queue - 6kyu

"""
There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!

Input
customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

Output
The function should return an integer, the total time required.
"""

def queue_time(customers, n):
    import heapq
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

print(queue_time([2, 2, 3, 3, 4, 4], 2))
print(queue_time([2, 8, 16, 5, 8, 7, 17], 3))