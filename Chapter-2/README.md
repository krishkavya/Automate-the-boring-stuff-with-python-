## Chapter-2
### Practice Questions
1. What are the two values of the Boolean data type? How do you write them?
**Answer:**
True and False

2. What are the three Boolean operators?
**Answer:**
 And, or and not are referred to as boolean operators.
 
 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

**Answer:**
|Expression|Evaluates to |
|----|----|
|True and True|True|
|True and False|False|
|False and True|False|
|False and False|False|
|True or True|True|
|True or False|True|
|False or True|True|
|False or False|False|
|not True|False|
|not False |True|

4. What do the following expressions evaluate to?
```
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
**Answer:**
- False
- False
- True
- False 
- False 
- True

5. What are the six comparison operators?
**Answer:**
|==|Equal to|
|!=|Not equal to|
|<|Less than|
|>|Greater than|
|<=|Less than or equal to|
|>=|Greater than or equal to|

6. What is the difference between the equal to operator and the assignment operator?
**Answer:**
==(equal to)is used to compare two values while =(assignment operator) is used to store a value in a variable.

7. Explain what a condition is and where you would use one.
**Answer:**
A condition is an expression used in a flow of control statement that evaluates either to 'True' or to 'False'.

8. Identify the three blocks in this code:
```
spam = 0
if spam == 10:          #first block
    print('eggs')
    if spam > 5:        #second block
        print('bacon')
    else:               #third block
        print('ham')
    print('spam')
print('spam')
```
9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```
spam=int(input("Number:"))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings")
```
 
10. What keys can you press if your program is stuck in an infinite loop?

**Answer:**
<kbd>Ctrl<kbd> + <kbd>C<kbd>

11. What is the difference between break and continue?
**Answer:**
Break statements exist in Python to exit or “break” a for or while conditional loop.The continue statement is used to skip code within a loop for certain iterations of the loop.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

**Answer:**
- The range(10) call ranges from 0 up to 10.
- The range(0, 10) does the same as above and explicitly tells the loop to start at 0.
- The range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

using for:
```
for i in range(1,11):
    print(i)
```
using while:
```
i=1
while i<11:
    print(i)
    i=i+1
```

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```
spam.bacon()
```

