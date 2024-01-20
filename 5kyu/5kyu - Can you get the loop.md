## Can you get the loop ? - 5kyu

**Instructions**

- You are given a node that is the beginning of a linked list.

- This list always contains a tail and a loop.

- Your objective is to determine the length of the loop.

---


#### Test cases

```python
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(loop_size(node1))
```

#### Output
```
3
```

---

#### Solution

```python
# derivation of Floyd's cycle finding algorithm to traverse sequences at different speeds
def loop_size(node):
    rabbit = node.next.next
    turtle = node.next

    while rabbit != turtle:
        rabbit = rabbit.next.next
        turtle = turtle.next

    rabbit = rabbit.next
    cnt = 1
    while rabbit != turtle:
        rabbit = rabbit.next
        cnt += 1
    return cnt
```

---


[Codewars link](https://www.codewars.com/kata/52a89c2ea8ddc5547a000863)
