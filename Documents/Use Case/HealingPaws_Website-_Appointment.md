## HealingPaws Website- Appointment

### Name: 

Appointment

### Description:

This use case covers the the functionality for the customer to make a appointment on the HealingPaws System.

### Actors:

Customers

### Triggers:

The use case is triggered by the contact from a user seeking to make a appointment for his or her pet.

### Preconditions:

The customer has already register to the website and got an account. In addition, he or she has already uploaded his or her pet information.

### Postconditions: 

After the use case is completed, the user information of the appointment will be stored in the databases and the user can check the this appointment in the current page.

### Courses of events:

#### Basic course of events:

1. The users open the website via browsers or applications.
2. The users log in their accounts
3. If user has not uploaded the pet information yet, he or she should fill in the information first.
4. If user has already uploaded the pet information, he or she will go through the personal center web page and click the appointment button
5. The user will fill in form of his or her pet information which include pet name, service and the symptom that the pet has 
6. Clicking the submit button and the system remembers the information of the appointment and store it into databases.

#### Alternate course of events:

1. The users open the website via browsers or applications.
2. The users log in successful and jump into 'Personal Center' page of  the website.
3. The users click the appointment button and jump to the "Appointment" web page.
4. The user input their appointment information and the system send it into back-end databases.
5. The system warns the user that the pet has already had an appointment which has existed in the database already and asks user not to submit twice or choosing another pet.
6. The user input another pet which has not had an appointment yet
7. The system remembers the information of users and store it into sessions.
8. The user input the pet name again and the verification is not permitted
9. The system returns to step 5.

### Extension Points:

None