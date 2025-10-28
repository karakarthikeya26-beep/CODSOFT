
# Simple Rule-Based Chatbot
# Author: Kara Karthikeya
# Project: CodSoft AI Internship - Task 1
# Description: A basic chatbot that responds to common questions.


import random
from datetime import datetime, date

# Greeting message
print("🤖 Chatbot: Hello! I am your AI Chatbot.")
print("Type 'bye' or 'exit' anytime to end the chat.\n")

# Start an infinite loop to keep chatting until the user types "bye" or "exit"
while True:
    # Get user input and convert it to lowercase for easier matching
    user = input("You: ").lower()

    # --- Exit Condition ---
    if user in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! Have a great day 😊")
        break

    # --- Greetings ---
    elif any(word in user for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! How’s it going?",
            "Good to see you. How can I assist you?"
        ]
        print("🤖 Chatbot:", random.choice(greetings))

    # --- How are you ---
    elif "how are you" in user:
        responses = [
            "I'm just a computer program, but I'm functioning properly!",
            "I'm doing great, thanks for asking!",
            "I'm doing well. How about you?"
        ]
        print("🤖 Chatbot:", random.choice(responses))

    # --- Name related ---
    elif "your name" in user:
        print("🤖 Chatbot: My name is CodSoftBot. I'm your personal assistant chatbot.")

    elif "my name" in user:
        print("🤖 Chatbot: Nice to meet you! That’s a wonderful name.")

    # --- Thank you ---
    elif "thank" in user:
        responses = [
            "You're welcome!",
            "No problem at all!",
            "Anytime! Happy to help."
        ]
        print("🤖 Chatbot:", random.choice(responses))

    # --- Creator / Developer ---
    elif "who made you" in user or "who created you" in user:
        print("🤖 Chatbot: I was created by Kara Karthikeya as part of a CodSoft internship project.")

    # --- Weather ---
    elif "weather" in user:
        responses = [
            "I can’t check the weather right now, but you can try a weather app!",
            "Sorry, I don’t have live weather data, but I hope it’s a pleasant day!"
        ]
        print("🤖 Chatbot:", random.choice(responses))

    # --- Time / Date ---
    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("🤖 Chatbot: The current time is", current_time)

    elif "date" in user:
        today = date.today()
        print("🤖 Chatbot: Today’s date is", today.strftime("%B %d, %Y"))

    # --- Jokes ---
    elif "joke" in user or "funny" in user:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the computer catch a cold? Because it left its Windows open!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        print("🤖 Chatbot:", random.choice(jokes))

    # --- Age ---
    elif "your age" in user:
        print("🤖 Chatbot: I don't have an age like humans, but I was created recently!")

    # --- Favourite color / food / hobby ---
    elif "color" in user:
        print("🤖 Chatbot: I like the color blue — it reminds me of calm skies and clear code.")

    elif "food" in user:
        print("🤖 Chatbot: I don’t eat food, but I’ve heard pizza is quite popular!")

    elif "hobby" in user:
        print("🤖 Chatbot: My hobby is chatting with you and learning new things.")

    # --- AI related ---
    elif "what is ai" in user or "artificial intelligence" in user:
        print("🤖 Chatbot: Artificial Intelligence is the simulation of human intelligence in machines that can think and learn.")

    elif "machine learning" in user:
        print("🤖 Chatbot: Machine Learning is a branch of AI where systems learn from data and improve automatically.")

    elif "python" in user:
        print("🤖 Chatbot: Python is a powerful and easy-to-learn programming language used widely in AI and data science.")

    # --- Study / Motivation ---
    elif "study" in user or "exam" in user:
        responses = [
            "Remember to stay focused — small progress each day adds up!",
            "Take short breaks, stay hydrated, and keep learning.",
            "You can do it! Don’t give up now."
        ]
        print("🤖 Chatbot:", random.choice(responses))

    elif "motivate" in user or "motivation" in user:
        responses = [
            "Believe in yourself. Every expert was once a beginner!",
            "Hard work always beats talent when talent doesn’t work hard.",
            "Keep pushing forward — success comes to those who never quit."
        ]
        print("🤖 Chatbot:", random.choice(responses))

    # --- Default fallback for unknown input ---
    else:
        responses = [
            "I'm not sure I understand. Could you please rephrase?",
            "Sorry, I don’t know how to respond to that.",
            "That’s interesting! Tell me more."
        ]
        print("🤖 Chatbot:", random.choice(responses))
