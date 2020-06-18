## HealingPaws Website- Log In
### Name: 
Log In
### Description:
This use case covers the the functionality to log into the HealingPaws System by users' ids and passwords.
### Actors:
Customers & Staff
### Triggers:
The use case is triggered by the contact from a user seeking to log into their own account.
### Preconditions:
The account of the user must already exist in the system
### Postconditions: 
After the use case is completed, the user information will be stored in the sessions and the user will be able to check/change their personal information. 
### Courses of events:
#### Basic course of events:
1. The users open the website via browsers or applications.
2. The users jump into 'Login' page of  the website
3. The system ask users to input their account id and password
4. The user input their id and password and the system send it into back-end databases to verify the input information 
5. The system remembers the information of users and store it into sessions.
#### Alternate course of events:
1. The users open the website via browsers or applications.
2. The users jump into 'Login' page of  the website.
3. The system ask users to input their account id and password.
4. The user input their id and password and the system send it into back-end databases to verify the input information. 
5. The system warns the user that the password or accountant is not correct and asks user to input it again.
6. The user input them again and the verification is permitted
7. The system remembers the information of users and store it into sessions.
8. The user input them again and the verification is not permitted
9. The system returns to step 5.

### Extension Points:
None