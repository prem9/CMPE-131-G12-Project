## Functional Requirements Assigned Tasks:
Alvin: 1-3
Prem: 4-6
Julie: 7-9
Justin 10-12

## Use Cases Assigned Tasks:
Alvin: 1-2
Prem: 3-4
Julie: 5-6
Justin: 7-8

## Functional Requirements

1. User can send a message to one or more users when pressing the send button
2. User can compose an email when clicking on the compose button
3. User can delete an email by checking the box of the email that the user wants to delete
4. User can create an objective which can be marked as completed or uncompleted
5. User can create multiple lists with different titles
6. User can set deadlines for these objectives
7. edit user profile
8. User account has two factor authentication when logging in
9.  Ability to send images/Urls
10. User can view messages or emails
11. Users should be able to sort their emails based on different criteria such as date, sender, and subject
12. System should allow users to format their emails using various font styles, bold text, sizes, and colors when composing an email

## Non-functional Requirements

1. Emails/chats should be sent/received in no more than 20 secs
2. Platform design is in english only

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


5. edit user profile
- **Pre-condition:** User must have an existing account

- **Trigger:** User presses 'edit pofile' button

- **Primary Sequence:**
  
 1. User chooses to edit their pfp
 2. System prompts user to allow access to photos to upload new pfp
 3. User gives system permission and chooses a picture from camera roll
 4. System prompts user to confirm their choice
 5. System changes pfp 


- **Primary Postconditions:** System server saves new pfp as is viewable by other users

- **Alternate Sequence:** 
  
  1. User doesn't allow access to photos
  2. System can't change pfp
 


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

7. User can sign in to the email client with their registered account
- **Pre-condition:** User has already registered, User has entered their email/password in the designated fields,   
User is currently on the sign in portal

- **Trigger:** User clicks on the "Sign In" button

- **Primary Sequence:**
  
  1. System validates the provided information stored in its database
  2. After validation, system authenticates the user and grants access to their account
  3. System displays a message to the user that confirms they have successfully signed into their account

- **Primary Postconditions:** System redirects to the email client page associated with the signed-in user

- **Alternate Sequence:** 

  1. System does not redirect the user to their email client page
  2. System displays an error message indicating that the provided email or password information is invalid
  3. System will again request the user to fill in the required information to sign in
  
8. User can register for an account on the website 
- **Pre-condition:** User has visited the website, User has a valid email address and password prepared

- **Trigger:** User clicks on a link that redirects them to the registration page of the website 

- **Primary Sequence:**
  
  1. User is navigated to the website's registration page
  2. User fills in the required fields such as email address and password
  3. User is offered the option to check a box to opt for two-factor authentication
  4. If user opts for two-factor authentication, system will request the user to enter a PIN number 
  5. System will display a CAPTCHA to the user to verify their identity
  6. User accepts the terms and conditions
  7. User clicks on the "register" button
  8. System validates the information and creates the account for the user and stores the information of the user in 
     its database

- **Primary Postconditions:** System displays a message to the user indicating that they have successfully registered

- **Alternate Sequence:** 

  1. System will display an error message if the email already exists in its database or missing fields on the   
     registration page
  2. System will prompt the user to correct the information provided
  3. System will request the user to attempt the CAPTCHA again if the user has failed to verify
