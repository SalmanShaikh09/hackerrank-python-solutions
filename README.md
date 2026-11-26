#  HackerRank Python Solutions 

Welcome to my **HackerRank Python Solutions** repository!

This repository contains my solutions to Python programming challenges from HackerRank. I'm using these problems to strengthen my Python fundamentals, improve my problem-solving skills, and learn to write clean and readable code.

##  Goals

- Practice Python programming regularly.
- Improve logical thinking and problem-solving.
- Understand Python concepts through practical exercises.
- Track my progress as I learn and solve more challenges.

##  Topics Covered

- Python Lists
- List Comprehensions
- If-Else(Conditional Statements)

*More topics will be added as I progress.*

##  Solutions

| No. | Problem | Solution |
|---|---|---|
| 1 | List Comprehensions | [`list_comprehensions.py`](./list_comprehensions.py) |


## 2. Problem: Python If-Else
    
**Language:** Python 3  
**Topic:** Conditional Statements

### Problem Description
Given an integer `n`, determine whether it is `Weird` or `Not Weird` according to the specified conditions.

### Concepts Used
- `if`, `elif`, and `else`
- Modulo operator (`%`)
- Comparison operators (`<=`, `>`, `!=`)
- Logical conditions

  ### Approach
1. Take an integer as input.
2. Check whether the number is odd or even.
3. Apply the given conditions in the correct order.
4. Print `Weird` or `Not Weird`.

## Solution
[View_Python_solution: Python_If_Else.py](./Python_If_Else.py) |

### What I Learned
- How to use `if`, `elif`, and `else` to make decisions.
- How the modulo operator helps check whether a number is odd or even.
- Why checking conditions in the correct order is important.


## 3. Problem: itertools.product()

### Problem Description
Given two lists, A and B, compute their Cartesian product. The Cartesian product contains all possible ordered pairs formed by taking one element from each list.


### Topics Covered
- Lists
- `input()` and `split()`
- `map()` and `int()`
- `for` loops
- Nested loops
- Tuples
- Cartesian Product
- `itertools.product()`

### Approaches Used

**Approach 1: Nested Loops**
- Use an outer loop to iterate through list A.
- Use an inner loop to iterate through list B.
- Create an ordered pair for each combination.

**Approach 2: Using `itertools.product()`**
- Import `product` from the `itertools` module.
- Generate all possible ordered pairs directly.

### Solution
[View Python Solution: itertools_product.py](itertools_product.py)

### What I Learned
I learned how to generate a Cartesian product using nested loops and how Python's `itertools.product()` function simplifies the same task.


## 4. Problem: Python Lists
 
**Topic:** Lists and List Methods

### Problem Description

Given an empty list, perform different operations such as inserting, removing, appending, sorting, popping, and reversing elements based on the given commands.

Print the list whenever the `print` command is provided.

### Topics Covered

- Lists
- `input()` and `split()`
- `int()` type conversion
- `for` loop
- `if`, `elif` conditional statements
- List methods:
  - `insert()`
  - `append()`
  - `remove()`
  - `sort()`
  - `pop()`
  - `reverse()`
    

### Approach

1. Take the number of commands as input.
2. Initialize an empty list.
3. Use a `for` loop to process each command.
4. Use `split()` to separate the command and its arguments.
5. Apply the corresponding list method using `if` and `elif` conditions.
6. Print the list whenever the `print` command is given.
   

### Solution

View Python solution: [python_List.py](python_List.py)


### What I Learned

- How to create and manipulate Python lists.
- How to use different built-in list methods.
- How to process multiple commands using loops and conditional statements.
- How to perform list operations dynamically based on user input.




## Problem 5: Nested Lists

### Problem Explanation

In this problem, we are given the names and grades of students in a class.

We need to store each student's name and grade in a nested list and find the student(s) who have the **second lowest grade**.

If multiple students have the second lowest grade, we need to:
- Find all students having that grade.
- Arrange their names in alphabetical order.
- Print each name on a separate line.

### Example

**Input:**
```text
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

**Output:**
```text
Berry
Harry
```

### HackerRank Problem

[Nested Lists - HackerRank](https://www.hackerrank.com/challenges/nested-list/problem)

### Topics Covered
- Nested Lists
- List Comprehension
- Sets
- Sorting
- Conditional Statements
- Loops

### Solution

[View Python Solution](Nested_Lists.py)



## Problem 6: Alphabet Rangoli

### Problem Explanation

In this problem, we are given an integer representing the size of the rangoli.

We need to create a symmetrical pattern using lowercase English letters.

The pattern starts with the letter `a` in the center and expands towards the boundary using letters in alphabetical order.

The final pattern should be symmetrical horizontally and vertically, with hyphens (`-`) used to maintain proper spacing.

### Example

**Input:**
```text
5
```

**Output:**
```text
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

### HackerRank Problem

[Alphabet Rangoli - HackerRank](https://www.hackerrank.com/challenges/alphabet-rangoli/problem)

### Topics Covered

**1. Loops**
- Used to generate each row of the rangoli.
- Help repeat the pattern for the required number of rows.

**2. String Manipulation**
- Used to arrange letters in the correct order.
- Helps combine letters and hyphens to create the pattern.

**3. List Operations**
- Useful for storing and arranging the letters before creating each row.

**4. String Formatting**
- Used to maintain equal spacing and alignment in every row.

**5. Pattern Printing**
- Used to create a symmetrical rangoli pattern by combining the generated rows.

### Important Logic

The main logic of this problem is to generate the upper half of the rangoli, including the middle row, and then generate the lower half by reversing the upper half (excluding the middle row).

This avoids writing separate logic for both halves and makes the solution easier to understand.

### Key Learning

Learned how to generate symmetrical patterns using Python loops, string manipulation, and logical thinking.

### Solution

### Solution

[View Python Solution](alphabet_rangoli.py)

  


##  Language and Tools

- **Language:** Python 3
- **Practice Platform:** HackerRank
- **Code Editor:** Visual Studio Code
- **Version Control:** GitHub

##  How to Run

1. Install Python 3 on your computer.
2. Clone or download this repository.
3. Open a terminal in the repository folder.
4. Run the solution you want to test:

   ```bash
   python list_comprehensions.py
   ```

5. Enter the four integer inputs when prompted by the program.

##  My Learning Journey

I'm continuously practicing Python and adding new solutions to this repository as I complete more challenges.

##  Find Me Online

- **GitHub:** [SalmanShaikh09](https://github.com/SalmanShaikh09)
- **HackerRank:** [https://www.hackerrank.com/profile/salmanbca699]

---

 Thank you for visiting my repository!
