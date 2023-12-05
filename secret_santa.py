import random
import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient_email

            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {str(e)}")

def isValid(pairs, constraints):
    for pair in pairs:
        if pair in constraints:
            return False
    return True

def secret_santa(names, constraints=None):
    original_names = names.copy()  # Keep the original order of names

    # Ensure the constraint is not violated
    while 1:
        random.shuffle(names)
        pairs = list(zip(names, names[1:] + [names[0]]))

        if(isValid(pairs, constraints)):
            break

    results = []
    for (giver, receiver) in pairs:
        results.append({'giver': giver, 'receiver': receiver})

    results = sorted(results, key=lambda x: original_names.index(x['giver']))

    return results


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))

    names = []
    emails = {}

    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        email = input(f"Enter the email of player {name}: ")

        names.append(name)
        emails[name] = email

    sender_email = input("Enter your email: ")
    sender_password = input("Enter your email password: ")

    # Take constraints as input from CLI
    num_constraints = int(input("Enter the number of constraints: "))
    constraints = []

    for i in range(num_constraints):
        name1 = input(f"Enter name for constraint {i + 1} (Person 1): ")
        name2 = input(f"Enter name for constraint {i + 1} (Person 2): ")
        constraints.append((name1, name2))

    assignments = secret_santa(names,constraints)

    for assignment in assignments:
        message = f"Dear {assignment['giver']},\n\nYou are the Secret Santa for {assignment['receiver']}!"
        subject = "Secret Santa Assignment"
        send_email(sender_email, sender_password, emails[assignment['giver']], subject, message)


