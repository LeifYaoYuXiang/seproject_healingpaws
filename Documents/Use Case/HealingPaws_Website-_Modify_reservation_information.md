## HealingPaws Website- Modify reservation information

### Name: 

Modify reservation information

### Description:

This use case covers the ability for Medical staff to modify their pet reservation information after logging in

### Actors:

Medical staff

### Triggers:

This use case is triggered by the contact of a Medical staff trying to modify the reservation information for his or her pet

### Preconditions:

The customer has registered an account on the website. In addition, The hospital needs to show the results of the pet's treatment in real time, such as during or after surgery or discharge.

### Postconditions: 

After the use case is completed, the user information for the new appointment will be stored in the database, the original information will be overwritten, and the hospital will receive the new data.

### Courses of events:

#### Basic course of events:

1. The edical staff open the website via browsers or applications.
2. The edical staff log in their accounts
3. He or she will go through the personal center web page and click the appointment button.
4.  Paramedics use hospital records to modify the appointment information.
5. Clicking the submit button and the system remembers the information of the appointment and store it into databases.

#### Alternate course of events:

1. The edical staff open the website via browsers or applications.
2. The edical staff log in successful and jump into 'Personal Center' page of  the website.
3. Edical staff can find their existing reservation information in the personal center.
4. The edical staff input their appointment information and the system send it into back-end databases.
5. The system warns the user that the pet has already had an appointment which has existed in the database already and asks user not to submit twice or choosing another pet or change the appointment.
6. The edical staff modifies the reservation information.
7. The system remembers the information of users and store it into sessions.
8. The edical staff input the pet name again and the verification is not permitted
9. The system returns to step 5.

### Extension Points:

None