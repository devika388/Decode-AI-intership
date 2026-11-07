print("welcome to the chatbot!")
print("How can I assist you today?")
print("type 'exit' or 'bye' to end the conversation.")

while True:
    user= input("You: ").lower()
    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif user == "how are you":
        print("Chatbot: I'm just a program, but I'm doing great! ")
    elif user == "what is your name":
        print("Chatbot: I am a chatbot created to assist you.")
    elif user == "who created you":
        print("Chatbot: I was created by a Devika.")
    elif user == "what can you do":
        print("Chatbot: I can answer your questions and have a conversation with you.")
    elif user == "exit" or user == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot: I'm sorry, I didn't understand that.")
