## Chapter-15
### Practice questions
1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?\
**Answer:**\
File object returned from open().

2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?\
**Answer:**\
'rb' for PdfFoleReader() and 'wb' for PdfFileWriter().

3. How do you acquire a Page object for page 5 from a PdfFileReader object?\
**Answer:**\
getPage(4)

4. What PdfFileReader variable stores the number of pages in the PDF document?\
**Answer:**\
numPages variable

5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?\
**Answer:**\
decrypt('swordfish')

6. What methods do you use to rotate a page?\
**ANswer:**\
rotateClockwise(),otateCounterClockwise().

7. What method returns a Document object for a file named demo.docx?\
**Answer:**\
 docx.Document('demo.docx')
 
8. What is the difference between a Paragraph object and a Run object?\
**Answer:**\
 A paragraph begins on a new line and contains multiple runs. Runs are groups of characters within a paragraph.	
 
9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?\
**Answer:**\
doc.paragraphs.

10. What type of object has bold, underline, italic, strike, and outline variables?\
**Answer:**\
Run Object .

11. What is the difference between setting the bold variable to True, False, or None?\
**Answer:**\
True makes the Run Object bold ,False makes it non bold  and None use the style’s bold setting.

12. How do you create a Document object for a new Word document?\
**Answer:**\
 docx.Document()
 
13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?\ 
**Answer:**\
doc.add_paragraph('Hello there!')

14. What integers represent the levels of headings available in Word documents?\
**ANswer:**\
0,1,2,3 and 4.


