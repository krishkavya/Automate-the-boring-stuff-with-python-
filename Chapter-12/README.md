## Chapter-12
### Practice questions
1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.\
**Answer:**\
The webbrowser module has open() function that lauches a web browser to a specific URL.requests module downloads files and from the web.Bs4 module parses HTML .selenium module can launch and control a browser.

2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?\
**Answer:**\
Response object , that has a text attribute that contains the downloaded content as a string . 

3. What requests method checks that the download worked?\
**Answer:**\
raise_for_status() method raise exceptions if the download had problems.

4. How can you get the HTTP status code of a requests response?\
**Answer:**\
status_code attribute of the Response object has the HTTP status code.

5. How do you save a requests response to a file?\
**Answer:**\
```
saveFile = open('filename.html', 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
```

6. What is the keyboard shortcut for opening a browser’s developer tools?\
**Answer:**\
<kbd>Ctrl<kbd> + <kbd>Shift<kbd> + <kbd>C<kbd>

7. How can you view (in the developer tools) the HTML of a specific element on a web page?\
**Answer:**\
 Right-click the element in the page and select Inspect Element from the menu.
 
8. What is the CSS selector string that would find the element with an id attribute of main?\
**Answer:**\
'#main'
 
9. What is the CSS selector string that would find the elements with a CSS class of highlight?\
**Answer:**\ 
'.highlight'

10. What is the CSS selector string that would find all the <div> elements inside another <div> element?\
**Answer:**\
'div div'

11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
**Answer:**\
'button[value="favourite"]'

12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?\
**Answer:**\
spam.getText()

13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?\
**Answer:**\
linkElem.attrs

14. Running import selenium doesn’t work. How do you properly import the selenium module?\
**Answer:**\
selenium module is imported with selenium import webdriver.

15. What’s the difference between the find_element_* and find_elements_* methods?\
**Answer:**\
- find_element_* : returns first matching element
- find_elements_* : returns a list of matching elements

16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?\
**Answer:**\
click() and send_keys()

17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?\
**Answer:**\
calling the submit() method

18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?\
**Answer:**\
forward(),back(),refresh() 

