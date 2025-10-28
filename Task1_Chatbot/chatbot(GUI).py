
# GUI Rule-Based Chatbot using Tkinter
# Author: Kara Karthikeya
# Project: CodSoft AI Internship - Task 1 (GUI Version)


import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime, date

# ------------------ Chatbot Logic ------------------ #
def get_response(user):
    user = user.lower()

    # Exit / goodbye
    if user in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day 😊"

    # Greetings
    elif any(word in user for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! How’s it going?",
            "Good to see you. How can I assist you?"
        ])

    # How are you
    elif "how are you" in user:
        return random.choice([
            "I'm doing great, thanks for asking!",
            "I'm just a chatbot, but I'm feeling fantastic!",
            "I'm working perfectly. How about you?"
        ])

    # Name
    elif "your name" in user:
        return "My name is CodSoftBot — your friendly AI chatbot."

    elif "my name" in user:
        return "Nice to meet you! That’s a wonderful name."

    # Thank you
    elif "thank" in user:
        return random.choice(["You're welcome!", "No problem at all!", "Anytime!"])

    # Creator
    elif "who made you" in user or "who created you" in user:
        return "I was created by Kara Karthikeya as part of a CodSoft AI Internship project."

    # Date and Time
    elif "time" in user:
        return "The current time is " + datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + date.today().strftime("%B %d, %Y")

    # AI / Python related
    elif "what is ai" in user or "artificial intelligence" in user:
        return "Artificial Intelligence is the simulation of human intelligence in machines that can think and learn."

    elif "machine learning" in user:
        return "Machine Learning is a branch of AI where systems learn from data automatically."

    elif "python" in user:
        return "Python is a powerful, easy-to-learn language used widely in AI and data science."

    # Jokes
    elif "joke" in user or "funny" in user:
        return random.choice([
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the computer catch a cold? Because it left its Windows open!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ])

    # Study or Motivation
    elif "study" in user or "exam" in user:
        return random.choice([
            "Stay focused — small progress every day adds up to big results!",
            "Take breaks, stay calm, and keep learning. You got this!",
            "You can do it! Keep going!"
        ])

    elif "motivate" in user or "motivation" in user:
        return random.choice([
            "Believe in yourself — every expert was once a beginner!",
            "Hard work always beats talent when talent doesn’t work hard.",
            "Success comes to those who never give up."
        ])

    # Default / Unknown
    else:
        return random.choice([
            "I'm not sure I understand. Could you please rephrase?",
            "Sorry, I don’t know how to respond to that.",
            "That’s interesting! Tell me more."
        ])

# ------------------ GUI Setup ------------------ #

# Main window
window = tk.Tk()
window.title("CodSoft AI Chatbot")
window.geometry("600x500")
window.resizable(False, False)
window.config(bg="#f0f0f0")

# Chat display area (scrollable)
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20, font=("Arial", 11))
chat_area.place(x=20, y=20)
chat_area.insert(tk.END, "🤖 Chatbot: Hello! I am your AI Chatbot.\nType 'bye' or 'exit' anytime to end the chat.\n\n")
chat_area.config(state=tk.DISABLED)

# User input box
user_input = tk.Entry(window, width=55, font=("Arial", 11))
user_input.place(x=20, y=430)

# Function to send message
def send_message():
    user_text = user_input.get().strip()
    if user_text == "":
        return

    # Display user's message
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_text + "\n")

    # Get chatbot response
    response = get_response(user_text)
    chat_area.insert(tk.END, "🤖 Chatbot: " + response + "\n\n")
    chat_area.config(state=tk.DISABLED)

    # Auto-scroll to bottom
    chat_area.yview(tk.END)

    # Clear input field
    user_input.delete(0, tk.END)

    # Exit program if user says bye
    if user_text.lower() in ["bye", "exit", "quit"]:
        window.after(1000, window.destroy)

# Send button
send_button = tk.Button(window, text="Send", command=send_message, width=10, bg="#0078D7", fg="white", font=("Arial", 11, "bold"))
send_button.place(x=480, y=425)

# Bind Enter key to send message
window.bind("<Return>", lambda event: send_message())

# Run the GUI loop
window.mainloop()
