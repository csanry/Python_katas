## Kata name - XXkyu

**Instructions**

- Build a tower by the following given argument:
    - `n_floors`(integer and always greater than 0).

- Tower block is represented as *

- Example of 3 story tower:

```
[  '  *  ',
   ' *** ',
   '*****'  ]
```
---

#### Test cases

```python
print(tower_builder(5))
print(tower_builder(8))
```

#### Output 
```
    *    
   ***   
  *****  
 ******* 
*********
       *       
      ***      
     *****     
    *******    
   *********   
  ***********  
 ************* 
***************
```

---

#### Solution

```python
def tower_builder(n_floors):
    result = []

    for i in range(1, n_floors+1):
        stars = 2 * i - 1
        spaces = n_floors - i
        result.append(f"{' ' * spaces}{'*' * stars}{' ' * spaces}")
    return '\n'.join(result)
```

---


[Codewars link](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)
