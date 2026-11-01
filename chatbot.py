
print("================================")
print("       CHATBOT       ")
print("================================")

print("Hello! I am your AI chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: I am DecodeBot, your virtual assistant.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a wonderful day.")
        break
    elif user_input == "whats the weather like":
        print("Bot: I am not sure about the weather right now. You can check a weather app for the latest updates.")
        break
    

    else:
        print("Bot: Sorry, I don't understand that yet.")
