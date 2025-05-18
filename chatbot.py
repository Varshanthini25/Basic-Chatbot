import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define conversation pairs (same as your original pairs)
pairs = [
    ["hello|hi|hey", ["Hi there! i am your friendly chatbot u can ask me some common things . how can i help you?"]],
    ["how are you", ["I'm doing great, thanks for asking!", "I'm good! How about you?"]],
    ["yes i am fine",["Happy to hear this! how can i help you?"]],
    ["what can you do", [
        "I can chat with you, answer questions, and keep you entertained!",
        "I'm here to assist you with anything you need."
    ]],
    ["who created you", [
        "I was created by an amazing developer—you!",
        "I'm the result of your awesome coding skills!"
    ]],
    ["tell me a joke", [
        "Why did the computer catch a cold? Because it left its Windows open!",
        "I told my Wi-Fi it was feeling weak—it said it needed a stronger connection!"
    ]],
    ["bye", [
        "Goodbye! Have a great day!",
        "See you soon!",
        "Take care!"
    ]],
    ["tell me something interesting", [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are still good to eat!"
    ]],
    ["do you like music", [
        "I enjoy all kinds of music! What’s your favorite genre?"
    ]],
    ["recommend a movie", [
        "How about ‘Inception’? It’s a mind-bending masterpiece!",
        "I’d suggest watching ‘Interstellar’ if you like sci-fi!"
    ]],
    ["what is the capital of India", [
        "The capital of India is New Delhi."
    ]],
    ["how old are you", [
        "I don’t age like humans, but I’m as old as the code that created me!"
    ]],
    ["can you help me", [
        "Of course! What do you need help with?"
    ]],
    ["how is the weather today", [
        "I can’t check the weather, but you can look it up online for accurate forecasts!"
    ]],
    ["do you have feelings", [
        "I don’t have feelings like humans, but I do enjoy chatting with you!"
    ]],
    ["what is life", [
        "Life is a beautiful journey of learning, growing, and experiencing new things!"
    ]],
    ["who is the prime minister of India", [
        "The current Prime Minister of India is Narendra Modi."
    ]],
    ["what is your favorite food", [
        "I don’t eat, but I’ve heard pizza is quite popular!"
    ]],
    ["do you play games", [
        "I enjoy simple word games. Want to play one?"
    ]],
    ["what is our national bird?",["Our national bird is peacock"]],
    ["what is the largest ocean?",["The largest ocean is Pacific"]], 
    ["How many days in a week?",["There are seven days in a week"]],
    ["How many letters in english alphabet?",["There are 26 letters in alphabets"]]
    ]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Create the main window
root = tk.Tk()
root.title("Chatbot GUI")
root.geometry("600x500")

# Create a scrollable text area to display conversations
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)

# Create an entry widget for user's message input
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)
entry.focus()  # Set focus on the input field

# Define a function to send messages
def send_message(event=None):
    user_input = entry.get().strip()  # Get user input and trim spaces
    if not user_input:
        return  # Do nothing if input is empty

    # Display user's message in the chat area
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    
    # Obtain the chatbot's response
    response = chatbot.respond(user_input)
    if not response:
        response = "I didn't understand that."
    
    # Display chatbot's response in the chat area
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    
    # Clear the input field
    entry.delete(0, tk.END)
    # Auto-scroll to the bottom
    chat_area.see(tk.END)

# Bind the Enter key to send the message
entry.bind("<Return>", send_message)

# Create a Send button for submitting messages
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
