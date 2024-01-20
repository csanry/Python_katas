## Write out expression! - 7kyu

**Instructions**

- Create a function to write out a math expression for you.

- Operators to use are:

```
"+"   -->  "Plus"
"-"   -->  "Minus"
"*"   -->  "Times"
"/"   -->  "Divided By"
"**"  -->  "To The Power Of"
"="   -->  "Equals"
"!="  -->  "Does Not Equal"
```

- The input will always be given as a string, in the following format: `number space operator space number`; for example: `"1 + 3"` or `"2 - 10"`.

- The numbers used will be 1 to 10

- Invalid operators will also be tested, to which you should return `"That's not an operator!"`

---

#### Test cases

```python
print(expression_out('1 + 3'))
print(expression_out('2 - 10'))
print(expression_out('6 ** 9'))
print(expression_out('5 = 5'))
print(expression_out('7 * 4'))
print(expression_out('2 / 2'))
print(expression_out('8 != 5'))
```

#### Output
```
One Plus Three
Two Minus Ten
Six To The Power Of Nine
Five Equals Five
Seven Times Four
Two Divided By Two
Eight Does Not Equal Five
```

---

#### Solution

```python
def expression_out(exp):
    ops = {'+': 'Plus ', '-': 'Minus ', '*': 'Times ',
           '/': 'Divided By ', '**': 'To The Power Of ',
           '=': 'Equals ', '!=': 'Does Not Equal '}
    num = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
           '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
           '9': 'Nine', '10': 'Ten'}
    left, mid, right = exp.split()
    return f"{num.get(left)} {ops.get(mid)}{num.get(right)}" if mid in ops else 'That\'s not an operator!'
```

---

[Codewars link](https://www.codewars.com/kata/57e2afb6e108c01da000026e)
