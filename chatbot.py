def simple_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        # Rule-based logic 
        if "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks for asking!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that yet.")

simple_chatbot()

