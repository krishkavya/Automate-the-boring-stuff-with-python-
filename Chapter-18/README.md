## Chapter-18
### Practice questions
1. What is the protocol for sending email? For checking and receiving email?\
**Answer:**\
SMTP and IMAP.

2. What four smtplib functions/methods must you call to log in to an SMTP server?\
**Answer:**\
smtplib.SMTP(), smtpObj.ehlo(), smptObj.starttls(),smtpObj.login().

3. What two imapclient functions/methods must you call to log in to an IMAP server?\
**Answer:**\
imapclient.IMAPClient()

4. What kind of argument do you pass to imapObj.search()?\
**Answer:**\


5. What do you do if your code gets an error message that says got more than 10000 bytes?\
**Answer:**\
Assign the variable imaplib._MAXLINE a large integer value.

6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?\
**Answer:**\
pyzmail module

7. When using the Gmail API, what are the credentials.json and token.json files?\
**Answer:**\
credentials.json and token.json files tell the EZGmail module which Google account to use when accessing Gmail.

8. In the Gmail API, what’s the difference between “thread” and “message” objects?\
**Answer:**\
A single mail is called a message and a back-forth conversation consisting of many emails is a thread.

9. Using ezgmail.search(), how can you find emails that have file attachments?\
**Answer:**\
 Add 'has:attachment'in the string you pass to search().
 
10. What three pieces of information do you need from Twilio before you can send text messages?\
**Answer:**\
Twilio account SID number, the authentication token number, and your Twilio phone number.
