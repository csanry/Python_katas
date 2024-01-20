## Refactored Greeting - 7kyu

**Instructions**

- Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet method.

- The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.

- Here is how the final refactored code would be used:

```python
joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
```

---

#### Test cases

```python
jack = Person('Jack')
jill = Person('Jill')

print(jack.greet('Jill'))
print(jill.greet('Jack'))
```

#### Output
```
Hello Jill, my name is Jack
Hello Jack, my name is Jill
```

---

#### Solution

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.name}'
```

---

[Codewars link](https://www.codewars.com/kata/5121303128ef4b495f000001)
