## Chapter-11
### Practice questions
1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.\
**Answer:**
```
assert spam>=10,'the spam variable is less than 10'
```

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).\
**Answer:**
```
assert eggs.lower() !=bacon.lower(),'eggs and bacon variable are the same'
```

3. Write an assert statement that always triggers an AssertionError.\
**Answer:**
```
assert False
```

4. What are the two lines that your program must have in order to be able to call logging.debug()?\
**Answer:**
```
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s- %(levelname)s - %(message)s')
```

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?\
**Answer:**
```
import logging
logging.basicConfig(filename='programLog.txt',level=logging.DEBUG,format='%(asctime)s- %(levelname)s- %(messages)s')
```

6. What are the five logging levels?\
**Answer:**\
info,debug,warning,error,critical.

7. What line of code can you add to disable all logging messages in your program?\
**Answer:**\
logging.disable(logging.CRITICAL)

8. Why is using logging messages better than using print() to display the same message?\
**Answer:**\
We need to remove manually all the print statements after completing the program which is time consuming and alse sometimes we may accidentaly delete the no logging print statement.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?\
**Answer:**\
Step In will move the debugger to function call,Step Over will execute the function call without stepping and Step Out executes the rest of the code until it steps out of the function.

10. After you click Continue, when will the debugger stop?\
**Answer:**\
The debugger will stop when it reaches the end of the program or at a breakpoint.

11. What is a breakpoint?\
**Answer:**\
Breakpoint is a setting on a line of code that pauses the debugger when the execution reaches the line.

12. How do you set a breakpoint on a line of code in Mu?\
**Answer:**\
Click the line number to make a red dot appear next to it.


