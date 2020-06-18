# Healing Paws Website - Reply Message

### Name:

Reply Message

### Description:

This use case enables the staff to reply to the customer's message.

### Actors:

Staff

### Triggers:

The use case is triggered by an unanswered message.

### Preconditions:

There is at least one unanswered message and the staffs must have already logged in.

### Postconditions:

After the use case is complete, the reply message will be sent to the customer, the unanswered messages of the staff should be reduced by one and the replied message of the staff should be added by one.

### Courses of events:

#### Basic course of events:

1. The user logs in the website.
2. The user checks message queue. 
3. The user selects an unanswered message.
4. The user replies message to the customer.
5. The user clicks the 'send' button to send the message.
6. The system saves the message, reduces one unanswered message from the queue and adds one replied message.

#### Alternate course of events(1):

1. The user logs in the website.
2. The user checks message queue.
3. There is no unanswered message.
4. Back to step 2.

#### Alternate course of events(2):

1. The user logs in the website.
2. The user checks message queue.
3. The user selects one replied message.
4. The user chooses to add information.
5. The user adds new message.
6. The user clicks the 'send' button to the message.
7. The system saves the message and adds one replied message.

#### Alternate course of events(3)

1. The user logs in the website.
2. The user checks message queue.
3. The user selects one replied message.
4. The user chooses to delete the message.
5. The user clicks the 'delete' button.
6. The system shows a yes/no dialog to the staff to confirm.
7. The user chooses 'yes'.
8. The system reduces the message from the message queue.
9. The user selects 'no'.
10. Back to step 2.

### Extension Points:

None

### Inclusions:

Log in

