## Chapter-4
### Practice Questions
1. What is []?\
**Answer:**\
Empty list value.

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)\
**Answer:**\
```
spam[2]='hello'
```

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].\
3. What does spam[int(int('3' * 2) // 11)] evaluate to?\
**Answer:**\
'd'

4. What does spam[-1] evaluate to?\
**Answer:**\
'd'

5. What does spam[:2] evaluate to?\
**Answer:**\
['a', 'b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].\
6. What does bacon.index('cat') evaluate to?\
**Answer:**\
1

7. What does bacon.append(99) make the list value in bacon look like?\
**Answer:**\
[3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?\
**Answer:**\
[3.14, 11, 'cat', True, 99]

9. What are the operators for list concatenation and list replication?\
**Answer:**\
+ and *

10. What is the difference between the append() and insert() list methods?\
**Answer:**\
append() adds the element at the end of the list and insert() adds the element at a specified index.

11. What are two ways to remove values from a list?\
**Answer:**\
del statement and remove().

12. Name a few ways that list values are similar to string values.\
**Answer:**\
- len() can be used in both.
- for loops can be used in both.

13. What is the difference between lists and tuples?\
**Answer:**\
- lists are enclosed within [] and are mutable(values can be added,removed or changed).
- Tuples are enclosed within () and are immutable.

14. How do you type the tuple value that has just the integer value 42 in it?\
**Answer:**\
(42,)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?\
**Answer:**\
tuple(),listt()

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?\
**Answer:**\
references to the list values.

17. What is the difference between copy.copy() and copy.deepcopy()?\
**Answer:**\
 copy.copy() copies the list values where as copy.deppcopy() copies the inner lists also.


