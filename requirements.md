## Functional Requirements

1. User can send a message to one or more users when pressing the send button
2. User can compose an email when clicking on the compose button
3. User can delete an email by checking the box of the email that the user wants to delete
4. User can create an objective which can be marked as completed or uncompleted
5. User can create multiple lists with different titles
6. User can set deadlines for these objectives
7. User messages are stored and saved
8. User account has two factor authentication when logging in
9. Confirmation email sent when user creates account
10. User can view messages/emails
11. Account creation/database
12. Sign-in

## Non-functional Requirements

1. Profile picture for all users
2. Username(not email address) for all users

## Use Cases

1. User can send a message to one or more users when pressing the send button
- **Pre-condition:** User is logged in, User is in chat box with one or more users.

- **Trigger:** User clicks textbox below chat. 

- **Primary Sequence:**
  
  1. System prompts user to fills in recipient box
  2. User types in recipient users
  3. System prompts user to draft message
  4. User clicks "send" button
  5. System sends message to recipient users

- **Primary Postconditions:** Recipient(s) must have received message from user

- **Alternate Sequence:** 
  
  1. User inputs invalid user
  2. System gives pop-up message explaining that the recipient user account does not exist
  3. System prompts user to put in new recipient user


2. User can compose an email when clicking on the compose button
- **Pre-condition:** User is logged in, Recipient addresses exist.

- **Trigger:** User clicks draft email / compose email

- **Primary Sequence:**
  
  1. System prompts user to fill in recipient(s) email address
  2. User types in recipient(s) email address
  3. System prompts user to fill in subject header
  4. User types in subject header
  5. System prompts user to draft the email body
  6. User types in email body
  7. User clicks "send" button
  8. System sends email to recipient(s)

- **Primary Postconditions:** Recipient(s) receive an email from the sender

- **Alternate Sequence:** 
  
  1. User inputs invalid email address 
  2. System displays pop-up error message - The address "invalid recipient(s) address" in the "To" field was not recognized. 
Please make sure that all addresses are properly formed.
  3. User inputs valid recipient email address and continue composing email


3. User can create an objective which can be marked as completed or uncompleted
- **Pre-condition:** User is logged in.

- **Trigger:** User clicks on "create a task" button. 

- **Primary Sequence:**
  
  1. System prompts user to write a task or sentence of the task
  2. User finishes writing task out
  3. System prompts user to mark the task complete or incomplete
  4. User marks the task complete or incomplete

- **Primary Postconditions:** User is able to see the task they created marked incomplete or complete

- **Alternate Sequence:** 
  
  1. User inputs invalid date
  2. System prompts date has already past the present
  3. System prompts user to enter a valid date


4. User can set a deadline for the created task
- **Pre-condition:** User is logged in. User has created a task

- **Trigger:** User clicks the set a deadline symbol button on the task

- **Primary Sequence:**
  
  1. System prompts user to set a date
  2. User selects a date for the deadline
  3. System prompts user to input specified time on the specified date
  4. User inputs time for the deadline

- **Primary Postconditions:** Date and time is displayed on the specified task to the user

- **Alternate Sequence:** 
  
  1. User inputs invalid date which has passed
  2. System gives pop-up message prompting the user that the date provided has already passed
  3. System prompts user to put in new date

- **Alternate Sequence:**
  
  1. User inputs invalid time outside of time constraints
  2. System gives pop-up message prompting user that inputted time is invalid
  3. System prompts user to input in new time


5. User messages are stored and saved
- **Pre-condition:** User is logged in, User is ready to send a message to recipient(s)

- **Trigger:** User sends a message

- **Primary Sequence:**
  
  1. System sees that User has sent a message to a recipient(s)
  2. System saves message on server's library 
  3. System saves information related to the message like a recipient and sender

- **Primary Postconditions:** Information around the message is saved on the system.

- **Alternate Sequence:** 
  
  1. System saves message
  2. System's server's library is full
  3. System delete's user's oldest message


6. System sends a confirmation email when user attempts to create an account
- **Pre-condition:** User has already inputted all information needed to create an account

- **Trigger:** User clicks button "send confirmation email"

- **Primary Sequence:**
  
  1. System sends an email to User
  2. User opens email and clicks on confirmation link
  3. System creates user account on the server

- **Primary Postconditions:** System's server contains user's information on logging into the website

- **Alternate Sequence:** 
  
  1. User fails to open confirmation link in email after 24 hrs
  2. System does not create the account on the server
  3. System deletes given information user has given to create the account

