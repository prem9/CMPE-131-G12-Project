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

1. User can send a message to another user when pressing the send button
2. User can compose and send an email 
3. User can delete an email
4. User can create a list of multiple objectives which can be marked complete or incomplete with a deadline attached to them.
5. User can reply to a sender's email or chat message
6. User can add attachment files when composing an email
7. User can personalize their profile picture along with their name and biography information
8. User can sign out of their account
9. User can reset their password
10. User can view messages or emails
11. Users should be able to view the emails that they have sent/received from another user
12. System should allow users to change font style of whole web page
13. User can increase and decrease the size of text for the whole web page

## Non-functional Requirements

1. Emails/chats should be sent/received in no more than 20 secs
2. Website can only run on Chrome

## Use Cases

1. User can send a message to another user when pressing the send button
- **Pre-condition:** User is logged in, User is on the send chat page.

- **Trigger:** User clicks on the New/Reply button. 

- **Primary Sequence:**
  
  1. System prompts user to fill in the email of the recipient
  2. User types in recipient's email
  3. User clicks on the chat button
  4. System sends chat message to the recipient and displays the recipient's email on the chat page

- **Primary Postconditions:** Recipient receives a message from the sender 

- **Alternate Sequence:** 
  
  1. User inputs invalid user
  2. System gives pop-up message explaining that the recipient user account does not exist
  3. System redirects user back to the send chat message page
  4. System prompts user to put in new recipient user


2. User can compose an email when clicking on the compose button
- **Pre-condition:** User is logged in, Recipient's email address exist.

- **Trigger:** User clicks on the compose button on the inbox page

- **Primary Sequence:**
  
  1. System prompts user to fill in recipient's name, subject of the email, and body of the email
  2. User fills in the necessary fields
  3. User clicks on the send button
  4. System redirects user back to the inbox page
  5. System notifies user that email has been sent

- **Primary Postconditions:** Recipient receives an email from the sender

- **Alternate Sequence:** 
  
  1. User inputs invalid email address 
  2. System displays pop-up error message - The address "invalid recipient(s) address" in the "To" field was not recognized. 
     Please make sure that all addresses are properly formed.
  3. User inputs valid recipient email address and continue composing email


3. User can create a list of multiple objectives which can be marked complete or incomplete with a deadline attatched to them
- **Pre-condition:** User is logged in.

- **Trigger:** User clicks on the Create List button. 

- **Primary Sequence:**
  
  1. User is allowed to change the title of the list if they choose 
  2. User types in the text box about their task
  3. User clicks on the Add Objective button
  4. System adds the task to the list and displays the updated list to the user
  5. System adds a checkbox and an option to add a deadline for the task after user submits their task
  6. If user decides to add a deadline, user clicks on calendar icon to adjust the date
  7. If user adds a deadline, System updates the deadline for the specific task
  8. User can now choose to add another task 

- **Primary Postconditions:** User is able to see the list with the tasks, if any, and able to mark tasks on it complete or incomplete as well as being allowed to change the deadline at anytime

- **Alternate Sequence:** 
  
  1. User does not input any text into the field for writing the task
  2. User clicks on the Add Objective button
  3. System prompts user that the note is too short

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

5. User can personalize their profile picture along with their name and biography information
- **Pre-condition:** User is logged in, User must have an existing account

- **Trigger:** User presses the Profile button

- **Primary Sequence:**
  
 1. System redirects user to the profile page
 2. Systems displays an option to choose a file and upload it along with fields for name and biography
 3. User clicks on the choose file button
 4. System displays directories on user's computer
 5. User clicks on an image and sends it back to the system
 6. System attaches user's image on the website
 7. User clicks on the upload button
 8. System displays the user's profile picture on the profile page
 9. If user chooses to, user fills in the fields for name and biography sections
 10. User clicks on the save button


- **Primary Postconditions:** System server saves new profile picture and updates the profile page with the user's changes

- **Alternate Sequence:** 
  
  1. User chooses not to upload a profile picture
  2. System displays the default image for the user's profile picture
  3. User chooses not to fill in the fields for name and biography
  4. System leaves the name and biography as "None"
 


6. User can sign out of their account

- **Pre-condition:** User is logged in

- **Trigger:** User clicks the Logout button

- **Primary Sequence:**
  
  1. System redirects the user to the login page
  2. User can decide to either sign in or reset their password
  3. If user chooses to, user can fill in the fields for the email and password to sign in to another account

- **Primary Postconditions:** User is signed out and is unable to access their account without signing in

- **Alternate Sequence:** 
  
  1. User does not click on the sign out button

  2. System does not redirect user to the login page
  
  3. User stays on their current page and stays logged in

7. User can sign in to the email client with their registered account
- **Pre-condition:** User has already registered, User is currently on the sign in page

- **Trigger:** User visits the email website

- **Primary Sequence:**
  
  1. System prompts user to enter the necessary fields for the email and password
  2. User fills in the fields for the email and password
  3. User clicks on the login button

- **Primary Postconditions:** System redirects to the email inbox page associated with the signed-in user

- **Alternate Sequence:** 

  1. User does not fill in the required fields for the email and password
  2. System displays an error message indicating that the provided email or password does not exist
  3. User attempts to type in a random text into the email field
  4. System will display a message to the user to include a valid email with an "@" domain
  
8. User can register for an account on the website 
- **Pre-condition:** User has visited the website, User has a valid email address and password prepared

- **Trigger:** User clicks on a link that redirects them to the registration page of the website 

- **Primary Sequence:**
  
  1. System prompts User to fill in required fields such as email address, username, and password
  2. User fills in the required fields for the email, username, and password
  3. User reenters their password to confirm their password
  4. User clicks on the submit button
  5. System redirects the user to the login page and displays a message that the user's account has been created

- **Primary Postconditions:** System redirects the user to their personal inbox page along with access to other features for logged in users

- **Alternate Sequence:** 

  1. User fills in two different types of passwords for the password and confirm password
  2. System prompts the user that the passwords do not match
  3. System redirects user back to the sign up page
  4. User fills in the correct passwords and does not fill in an email address
  5. System prompts a message to the user that the email field cannot be empty
