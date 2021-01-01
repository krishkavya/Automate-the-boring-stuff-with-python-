## Chapter-14
### practice questions
1. What three files do you need for EZSheets to access Google Sheets?\
**Answer:**\
credential file,token file for google sheets,token file for gogle drive.

2. What two types of objects does EZSheets have?\
**Answer:**\
ezsheets.Spreadsheet and ezsheets.Sheet

3. How can you create an Excel file from a Google Sheet spreadsheet?\
**Answer:**\
downloadAsExcel() 

4. How can you create a Google Sheet spreadsheet from an Excel file?\
**Answer:**\
ezsheets.upload() function and pass the filename of the Excel file.

5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?\
**Answer:**\
ss.title = 'Students'

6. How can you find the column letters for column 999?\
**Answer:**\
ezsheets.getColumnLetterOf(999)

7. How can you find out how many rows and columns a sheet has?\
**Answer:**\
sheet.rowCount and sheet.columnCount

8. How do you delete a spreadsheet? Is this deletion permanent?\
**Answer:**\
ss.delete()
The delete() method will move your spreadsheet to the Trash folder on your Google Drive.This is only permanent if you pass the permanent=True keyword argument.

9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?\
**Answer:**\
 createSpreadsheet() and createSheet()
 
10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
**Answer:**\
Attempting to exceed this quota will raise the googleapiclient.errors.HttpError “Quota exceeded for quota group” exception.



