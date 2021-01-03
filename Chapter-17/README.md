## Chapter-17
### Practice questions
1. What is the Unix epoch?\
**Answer:**\
 A reference moment that date and time programs use.
 
2. What function returns the number of seconds since the Unix epoch?\
**Answer:**\
 time.time()
 
3. How can you pause your program for exactly 5 seconds?\
**ANswer:**\
time.sleep(5)

4. What does the round() function return?\
**Answer:**\
Returns the nearest integer to the argument passed.

5. What is the difference between a datetime object and a timedelta object?\
**Answer:**\
- datetime object represents a specific moment in time.
- timedelta object represents a duration of time.

6. Using the datetime module, what day of the week was January 7, 2019?\
**Answer:**\
- Monday
-  datetime.datetime(2019, 1, 7).weekday() which returns 0.This means monday.

7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?\
**Answer:**\
threadObj = threading.Thread(target=spam) threadObj.start()

8. What should you do to avoid concurrency issues with multiple threads?\
**Answer:**\
Run the code in one thread.


