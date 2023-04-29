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
3. User can delete an email
4. User can create multiple lists of objectives which can be marked complete or incomplete with a deadline attatched to them.
5. User can reply to a sender's email or send the email to someone else
6. User can share lists to other people
7. edit user profile
8. User can sign out of their account
9. Ability to send images/Urls
10. User can view messages or emails
11. Users should be able to sort their emails based on different criteria such as date, sender, and subject
12. System should allow users to format their emails using various font styles, bold text, sizes, and colors when composing an email

## Non-functional Requirements

1. Emails/chats should be sent/received in no more than 20 secs
2. Website can only run on Chrome

## Use Cases

1. User can send a message to one or more users when pressing the send button
- **Pre-condition:** User is logged in, User is in chat box with one or more users.

- **Trigger:** User clicks textbox below chat. 

- **Primary Sequence:**
  
  1. System prompts user to fills in recipient box
  2. User types in recipient users
  3. System prompts user to draft message
  4. User clicks "send" button

- **Primary Postconditions:** Recipient(s) receive a message from the sender

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

- **Primary Postconditions:** Recipient(s) receive an email from the sender

- **Alternate Sequence:** 
  
  1. User inputs invalid email address 
  2. System displays pop-up error message - The address "invalid recipient(s) address" in the "To" field was not recognized. 
Please make sure that all addresses are properly formed.
  3. User inputs valid recipient email address and continue composing email


3. User can create multiple lists of objectives which can be marked complete or incomplete with a deadline attatched to them
- **Pre-condition:** User is logged in.

- **Trigger:** User clicks on "create a list" button. 

- **Primary Sequence:**
  
  1. Systen prompts user to create a title for the list
  2. User writes a title for the list
  3. System prompts user to create a task
  4. User finishes writing task out
  5. System prompts user if they want to attatch a deadline to the task
  6. User attatches a date and time to the task
  7. System prompts a check box to mark the task to be completed or incompleted
  8. User marks task as completed or incompleted
  9. System prompts user if they want to create another task
  10. User chooses to create another task or finishes list

- **Primary Postconditions:** User is able to see the list and able to mark tasks on it complete or incomplete

- **Alternate Sequence:** 
  
  1. Systen prompts user to create a title for the list
  2. User writes a title for the list
  3. System prompts user to create a task
  4. User finishes writing task out
  5. System prompts user if they want to attatch a deadline to the task
  6. User attatches an invalid date or time to the task
  7. System prompts user "invalid deadline" and asks user to input a different date or time

4. User can delete an email
- **Pre-condition:** User is logged in. User has received an email from another user and is viewing it

- **Trigger:** User clicks on the "delete" button

- **Primary Sequence:**
  
  1. System prompts user to confirm whether they want to delete the email or not
  2. User clicks "yes" on the prompt
  3. System removes email from User's view

- **Primary Postconditions:**  User can not see the email sent to them or they sent

- **Alternate Sequence:** 
  
  1. System prompts user to confirm whether they want to delete the email or not
  2. User clicks "no" on the prompt
  3. System closes the prompt and goes back to the email.

5. edit user profile (profile picture,username,password)
- **Pre-condition:** User must have an existing account

- **Trigger:** User presses 'edit profile' button

- **Primary Sequence:**
  
 1. User chooses to edit their profile picture
 2. System prompts user to allow access to photos to upload new profile picture
 3. User gives system permission and chooses a picture from camera roll
 4. System prompts user to confirm their choice
 5. System changes profile picture
 6. User chooses to edit username/password
 7. system prompts user to enter new changes
 8. system prompts user to confirm their choices
 9. system saves changes


- **Primary Postconditions:** System server saves new profile picture and it is viewable by other users

- **Alternate Sequence:** 
  
  1. User doesn't allow access to photos
  2. System can't change profile picture
 


6. User can sign out of their account
- **Pre-condition:** user must be signed into their account

- **Trigger:** User clicks 'sign-out' button

- **Primary Sequence:**
  
  1. System prompts are you sure with a yes or no option
  2. User clicks 'yes'
  3. System redirects user to log-in page

- **Primary Postconditions:** User is signed-out and is unable to access their account without signing in

- **Alternate Sequence:** 
  
  1. System prompts are you sure with a 'yes' or 'no' option

  2. User clicks 'no'
  
  3. System redirects to main page for signed-in user

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
  
  1. System prompts User to fill in required fields such as email address and password
  2. User fills in the required fields
  3. User is offered the option to check a box to opt for two-factor authentication
  4. If user opts for PIN authentication, system will request the user to enter a PIN number 
  5. User accepts the terms and conditions
  6. User clicks on the "register" button
  7. System validates the information and creates the account for the user and stores the information of the user in its database

- **Primary Postconditions:** System displays a message to the user indicating that they have successfully registered

- **Alternate Sequence:** 

  1. System will display an error message if the email already exists in its database or missing fields on the
     registration page
  2. System will prompt the user to correct the information provided
  3. System will request the user to attempt the PIN authentication again if the user has failed to verify
