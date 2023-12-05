# secret-santa
A Python script for organizing Secret Santa events with constraints. This script accepts the number of players, their names, emails, and optional constraints, and then assigns each participant a Secret Santa recipient while respecting the specified constraints.

## Features

- Random assignment of Secret Santas
- Constraints to prevent specific pairings
- Email notifications to participants with their assignments
- Constraints works like this: Person 1 can not give present to Person 2

## Usage

1. **Run the script and provide the number of players.**
    ```bash
    python secret_santa.py
    ```

2. **Enter the names and emails of participants.**
    - Participants can optionally specify constraints to avoid specific pairings.

3. **Input your email and password for sending notifications.**
    - Participants will receive emails with their Secret Santa assignments.

## Example of using it

Enter the number of players: 5

Enter the name of player 1: Alice
Enter the email of player 1: alice@example.com

Enter the name of player 2: Bob
Enter the email of player 2: bob@example.com

Enter the name of player 3: Charlie
Enter the email of player 3: charlie@example.com

Enter the name of player 4: Dave
Enter the email of player 4: dave@example.com

Enter the name of player 5: Eve
Enter the email of player 5: eve@example.com

Enter your email: your_email@example.com
Enter your email password: your_email_password

Enter the number of constraints: 2

Enter name for constraint 1 (Person 1): Alice
Enter name for constraint 1 (Person 2): Bob

Enter name for constraint 2 (Person 1): Charlie
Enter name for constraint 2 (Person 2): Dave

## Note
If you want that Alice and Bob cant recieve presents form each other you should put two constraints like this: 

Enter name for constraint 1 (Person 1): Alice
Enter name for constraint 1 (Person 2): Bob

Enter name for constraint 2 (Person 1): Bob
Enter name for constraint 2 (Person 2): Alice



