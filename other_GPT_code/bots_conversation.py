import random
import time

# List of possible names for the chatbots
names = ["John", "Mary", "Peter", "Lucy", "Mike", "Sarah", "David", "Emily"]

# Generate random names for the chatbots
bot1_name = random.choice(names)
bot2_name = random.choice(names)
while bot2_name == bot1_name:
    bot2_name = random.choice(names)

# Open a file for outputting the conversation
file_name = f"{bot1_name}_and_{bot2_name}_conversation.txt"
with open(file_name, "w") as f:
    # Print the names of the chatbots
    f.write(f"{bot1_name}: Hi, I'm {bot1_name}!\n")
    f.write(f"{bot2_name}: Hi, I'm {bot2_name}!\n")
    f.write("\n")

    # Start the conversation
    for i in range(20):
        # Generate a random delay between 10 and 30 seconds
        delay = random.randint(10, 30)
        time.sleep(delay)

        # Generate a random message for each chatbot
        bot1_message = f"{bot1_name}: {generate_message()}\n"
        bot2_message = f"{bot2_name}: {generate_message()}\n"

        # Output the messages to the console and to the file
        print(bot1_message.strip())
        print(bot2_message.strip())
        f.write(bot1_message)
        f.write(bot2_message)

# Function to generate a random message
def generate_message():
    # List of possible message types
    message_types = ["greeting", "question", "statement"]

    # List of possible messages for each message type
    greetings = ["Hello!", "Hi there!", "Good morning!", "Good afternoon!"]
    questions = ["How are you?", "What are you up to?", "How's the weather?", "Have you seen any good movies lately?"]
    statements = ["I went for a run this morning.", "I'm really enjoying this book I'm reading.", "I need to go grocery shopping later.", "I'm thinking of taking a vacation next month."]

    # Generate a random message type and message
    message_type = random.choice(message_types)
    if message_type == "greeting":
        message = random.choice(greetings)
    elif message_type == "question":
        message = random.choice(questions)
    else:
        message = random.choice(statements)

    return message