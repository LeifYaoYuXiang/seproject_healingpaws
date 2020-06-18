## HealingPaws Website- Register

### Name: 

Register

### Description:

This use case covers the the functionality to register one new account on the HealingPaws System.

### Actors:

Customers

### Triggers:

The use case is triggered by the contact from a user seeking to register their own new accounts.

### Preconditions:

The account that the user want to register cannot exist in the system.

### Postconditions: 

After the use case is completed, the user information will be stored in the databases and the user will log into their own accounts. 

### Courses of events:

#### Basic course of events:

1. The users open the website via browsers or applications.
2. The users jump into 'Register' page of  the website.
3. The system ask users to input their account id and password.
4. The user input their id and password and the system send it into back-end databases.
5. The system remembers the information of users and store it into both databases and sessions.

#### Alternate course of events:

1. The users open the website via browsers or applications.
2. The users jump into 'Register' page of  the website.
3. The system ask users to input their account id and password.
4. The user input their id and password and the system send it into back-end databases.
5. The system warns the user that the id has existed in the database already and asks user to input it again.
6. The user input it again and the verification is permitted
7. The system remembers the information of users and store it into sessions.
8. The user input them again and the verification is not permitted
9. The system returns to step 5.

### Extension Points:

None