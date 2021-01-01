## Chapter-13
### Practice questions
1. What does the openpyxl.load_workbook() function return?\
**Answer:**\
workbook object.

2. What does the wb.sheetnames workbook attribute contain?\
**ANswer:**\
worksheet object.

3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?\
**Answer:**\
wb['Sheet1']

4. How would you retrieve the Worksheet object for the workbook’s active sheet?\
**Answer:**\
wb.get_active_sheet()

5. How would you retrieve the value in the cell C5?\
**Answer:**\
sheet['C5'].value

6. How would you set the value in the cell C5 to "Hello"?\
**Answer:**\
sheet['C5'] = 'Hello'

7. How would you retrieve the cell’s row and column as integers?\
**Answer:**\
 cell.row and cell.column
 
 8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?\
**Answer:**\
 They hold the highest column and row with values in the sheet.Integers.
 
9. If you needed to get the integer index for column 'M', what function would you need to call?\
**Answer:**\
 openpyxl.cell.column_index_from_string('M')
 
10. If you needed to get the string name for column 14, what function would you need to call?\
**ANswer:**\
openpyxl.cell.get_column_letter(14)

11. How can you retrieve a tuple of all the Cell objects from A1 to F1?\
**Answer:**\
sheet['A1':'F1']

12. How would you save the workbook to the filename example.xlsx?\
**Answer:**\
wb.save('example.xlsx’)

13. How do you set a formula in a cell?\
**Answer:**\
Set the cell’s value attribute to a string of the formula text.

14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?\
**ANswer:**\
 Retrieve the value of cell in which we assigned formula.
 
15. How would you set the height of row 5 to 100?\
**Answer:**\
sheet.row_dimensions[5].height = 100

16. How would you hide column C?\
**Answer:**\
sheet.column_dimensions['C'].hidden = True

17. What is a freeze pane?\
**Answer:**\
Freeze panes are rows and columns that will always appear on the screen.

18. What five functions and methods do you have to call to create a bar chart?\
**ANswer:**\
- openpyxl.chart.Reference() 
- openpyxl.chart.Series()
- openpyxl.chart.BarChart()
- chartObj.append(seriesObj)
- add_chart()




