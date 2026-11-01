
# ============================================================
# DECODELABS - ARTIFICIAL INTELLIGENCE PROJECT 1
# Project: Rule-Based AI Chatbot
# Language: Python
# Batch: 2026
#
# Description:
# This is a simple rule-based chatbot that interacts with
# users using predefined instructions and responses.
#
# Main concepts:
# 1. Input and Output
# 2. Conditional Statements (if, elif, else)
# 3. While Loops
# 4. String Methods
# 5. Basic Decision-Making Logic
# ============================================================


# ------------------------------------------------------------
# 1. INTRODUCTION
# ------------------------------------------------------------

# Display a welcome message when the program starts.
print("=" * 50)
print("          WELCOME TO DECODEBOT")
print("       Your Simple AI Virtual Assistant")
print("=" * 50)

print("\nHello! I am DecodeBot.")
print("I am here to have a simple conversation with you.")

# Tell the user how to end the conversation.
print("\nYou can type 'help' to see what I can do.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")


# ------------------------------------------------------------
# 2. CONTINUOUS CHAT LOOP
# ------------------------------------------------------------

# A while loop allows the chatbot to keep running.
# The loop will continue until the user enters an exit command.

while True:

    # Ask the user to enter a message.
    # input() collects the message from the keyboard.
    # strip() removes unnecessary spaces at the beginning
    # and end of the message.
    # lower() converts the message to lowercase.
    # This makes the chatbot less sensitive to capital letters.

    user_input = input("\nYou: ").strip().lower()


    # --------------------------------------------------------
    # 3. CHECK FOR EMPTY INPUT
    # --------------------------------------------------------

    # If the user presses Enter without typing anything,
    # the chatbot asks them to enter a message.

    if user_input == "":
        print("DecodeBot: Please enter a message so we can talk.")


    # --------------------------------------------------------
    # 4. EXIT COMMANDS
    # --------------------------------------------------------

    # Check whether the user wants to end the conversation.
    # break immediately stops the while loop.

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("DecodeBot: Goodbye! It was nice talking to you.")
        print("DecodeBot: Have a wonderful day!")
        break


    # --------------------------------------------------------
    # 5. GREETING RESPONSES
    # --------------------------------------------------------

    # Recognize common greetings and respond appropriately.

    elif user_input in ["hello", "hi", "hey", "good morning",
                        "good afternoon", "good evening"]:

        print("DecodeBot: Hello there!")
        print("DecodeBot: It is nice to meet you.")


    # --------------------------------------------------------
    # 6. RESPOND TO COMMON QUESTIONS
    # --------------------------------------------------------

    # Check whether the user asks how the chatbot is doing.

    elif user_input in ["how are you", "how are you doing",
                        "how is it going"]:

        print("DecodeBot: I am doing great, thank you!")
        print("DecodeBot: How can I help you today?")


    # Recognize questions about the chatbot's name.

    elif user_input in ["what is your name", "who are you",
                        "your name"]:

        print("DecodeBot: My name is DecodeBot.")
        print("DecodeBot: I am a rule-based chatbot created")
        print("as part of DecodeLabs Project 1.")


    # Recognize questions about the chatbot's purpose.

    elif user_input in ["what can you do", "your purpose",
                        "what is your purpose"]:

        print("DecodeBot: I can respond to predefined messages.")
        print("DecodeBot: I can greet you, answer simple questions,")
        print("and have a basic conversation with you.")


    # Respond to questions about artificial intelligence.

    elif user_input in ["what is artificial intelligence",
                        "define ai", "what is ai"]:

        print("DecodeBot: Artificial Intelligence, or AI, is")
        print("the field of creating computer systems that")
        print("perform tasks that normally require human-like")
        print("intelligence.")


    # Respond to questions about Python.

    elif user_input in ["what is python", "define python",
                        "tell me about python"]:

        print("DecodeBot: Python is a popular programming language.")
        print("DecodeBot: It is known for its simple syntax and")
        print("is widely used in AI, web development and data science.")


    # Respond to a thank-you message.

    elif user_input in ["thank you", "thanks", "thank you very much"]:

        print("DecodeBot: You are very welcome!")
        print("DecodeBot: Happy to help.")


    # Respond when the user asks for help.

    elif user_input == "help":

        print("\nDecodeBot: Here are some things you can ask me:")
        print("-----------------------------------------------")
        print("1. Hello")
        print("2. How are you?")
        print("3. What is your name?")
        print("4. What can you do?")
        print("5. What is Artificial Intelligence?")
        print("6. What is Python?")
        print("7. Thank you")
        print("8. Bye")
        print("-----------------------------------------------")


    # --------------------------------------------------------
    # 7. DEFAULT RESPONSE
    # --------------------------------------------------------

    # If none of the conditions above match the user's input,
    # the chatbot displays this response.
    # This prevents the program from stopping unexpectedly.

    else:
        print("DecodeBot: I am sorry, I do not understand that yet.")
        print("DecodeBot: Try asking me something else.")
        print("DecodeBot: You can also type 'help' for suggestions.")


# ------------------------------------------------------------
# 8. PROGRAM TERMINATION
# ------------------------------------------------------------

# This message is displayed after the while loop ends.
# It confirms that the chatbot has successfully stopped.

print("\n" + "=" * 50)
print("       DECODEBOT SESSION ENDED")
print("       Thank you for chatting!")
print("=" * 50)
