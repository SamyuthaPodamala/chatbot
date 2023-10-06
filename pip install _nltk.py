pip install nltk
import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you", ["I'm good, thanks!", "I'm doing well."]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
    # Add more patterns and responses here
]
chatbot = Chat(pairs, reflections)
print("Chatbot: Hello! How can I assist you today? (type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

