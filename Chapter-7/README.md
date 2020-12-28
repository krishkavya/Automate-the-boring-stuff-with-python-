## Chapter-7
### Practice questions
1. What is the function that creates Regex objects?\
**Answer:**\
re.compile()

2. Why are raw strings often used when creating Regex objects?\
**Answer:**\
 raw strings are used so that backslashes do not have to be esccaped.

3. What does the search() method return?\
**Answer:**\
Returns match object.

4. How do you get the actual strings that match the pattern from a Match object?\
**Answer:**\
group()

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?\
**Answer:**\
- group 0 covers the entine match.
- group 1 covers first set of parantheses.
- group 2 covers second set of parantheses.

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?\
**Answer:**\
By using these \., \ \

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?\
**Answer:**\
If regex has groups ,a list of tuples of string is returned and if it has no groups then a list of strings is returned .

8. What does the | character signify in regular expressions?\
**Answer:**\
either ,or between two groups.

9. What two things does the ? character signify in regular expressions?\
**Answer:**\
The ? matches zero or one of the preceding group.

10. What is the difference between the + and * characters in regular expressions?\
**Answer:**\
- The + matches one or more of the preceding group.
- The * matches zero or more of the preceding group.

11. What is the difference between {3} and {3,5} in regular expressions?\
**Answer:**\
{3} matches exactly three instances of the preseeding group whereas {3,5} matches between three anf five instances.

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?\
**Answer:**\
- \d - single digit
- \w - word
- \s - space

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?\
**Answer:**\
\D,\W and \S match a single charater that is not a digit ,word,or space respectively.

14. What is the difference between .* and .*??\
**Answer:**\
.* performs greedy match and .*? performs nongreedy match.

15. What is the character class syntax to match all numbers and lowercase letters?\
**Answer:**\
[a-z0-9]

16. How do you make a regular expression case-insensitive?\
**Answer:**\
re.IGNORECASE

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?\
**Answer:**\
. matches any chracter except the newline .If re.DOTALL is passed as the second argument to re.compile() dot will also match newline characters.

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?\
**Answer:**\
 'X drummers, X pipers, five rings, X hens'
 
 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?\
 **Answer:**\
 Add space and comments to the string.
 
 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

- '42'
- '1,234'
- '6,368,745'
but not the following:

- '12,34,567' (which has only two digits between the commas)
- '1234' (which lacks commas)

**Answer:**
```
re.compile(r'^\d{1,3}(,\d{3})*$') 
```

21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

- 'Haruto Watanabe'
- 'Alice Watanabe'
- 'RoboCop Watanabe'
but not the following:

- 'haruto Watanabe' (where the first name is not capitalized)
- 'Mr. Watanabe' (where the preceding word has a nonletter character)
- 'Watanabe' (which has no first name)
- 'Haruto watanabe' (where Watanabe is not capitalized)

**Answer:**\
re.compile(r'[A-Z][a-z]*\sNakamoto')

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

- 'Alice eats apples.'
- 'Bob pets cats.'
- 'Carol throws baseballs.'
- 'Alice throws Apples.'
- 'BOB EATS CATS.'
but not the following:

- 'RoboCop eats apples.'
- 'ALICE THROWS FOOTBALLS.'
- 'Carol eats 7 cats.'

**Answer:**\
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
 

