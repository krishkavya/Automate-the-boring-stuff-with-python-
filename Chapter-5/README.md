## Chapter-5
### Practice questions
1. What does the code for an empty dictionary look like?\
**Answer:**\
{}

2. What does a dictionary value with a key 'foo' and a value 42 look like?\
**Answer:**\
{'foo':42}

3. What is the main difference between a dictionary and a list?\
**Answer:**\
- items in a list are ordered.
- items in a dictionary are unordered.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?\
**Answer:**\
Keyerror

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?\
**Answer:**\
No difference.It checks if the value exist as a key in the dictionary.

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?\
**Answer:**\
- 'cat' in spam checks if 'cat' is a key in the dictionary.
- 'cat' in spam.values() checks if 'cat' is a value for any of the keys.

7. What is a shortcut for the following code?
```
if 'color' not in spam:
    spam['color'] = 'black'
```
**Answer:**
```
spam.setdefault('color','black')
```

8. What module and function can be used to “pretty print” dictionary values?\
**Answer:**\
pprint.pprint()

