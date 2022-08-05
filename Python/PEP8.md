[PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

  | [import](#import) | [괄호](#괄호) | [인덱스](#인덱스) | [수식](#수식) | [Parameter](#Parameter) |




### import

```python
import os
import sys

from subprocess import Popen, PIPE
```
<br>

### 괄호

```python
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

```python
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
```

```python
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

```python
FILES = ('setup.cfg',)

FILES = [
    'setup.cfg',
    'tox.ini',
    ]

initialize(FILES,
           error=True,
           )
```
<br>

### 인덱스

```python
spam(ham[1], {eggs: 2})

foo = (0,)

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```

<br>

### 수식

```python
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

if x == 4: print(x, y); x, y = y, x
```

<br>

### Parameter

```python
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

```python
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```