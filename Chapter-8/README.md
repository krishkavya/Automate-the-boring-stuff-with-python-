## Chapter-8
### Practice questions 
1. Does PyInputPlus come with the Python Standard Library?\
**ANswer:**\
No,PyInputPlus is a third party module.

2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?\
**Answer:**\
To make the code shorter.It is easier to type pyip.inputStr() instead of pyinputplus.inputStr().

3. What is the difference between inputInt() and inputFloat()?\
**Answer:**\
When you want the user to type in a decimal use float(input()) , if you want the user to type in an integer use int(input()).

4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?\
**Answer:**\
pyip.inputint(min=0,max=99)

5. What is passed to the allowRegexes and blockRegexes keyword arguments?\
**Answer:**\
A lists of strings that are either allowed or denied.

6. What does inputStr(limit=3) do if blank input is entered three times?\
**Answer:**\
The function raises "RetryLimitException".

7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?\
**Answer:**\
```
'hello'
```


