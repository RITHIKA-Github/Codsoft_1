#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import datetime
# Define predefined rules and responses
rules = {
    r'hello|hi|hey|good morning|good afternoon|good evening': 'Hello! How can I assist you today?',
    r'how are you|how\'s it going|what\'s up': 'I\'m doing well, thank you for asking! How about you?',
    r'(.*) (age|old) are you': 'I am just a computer program, so I don\'t have an age.',
    r'what can you do|what are your capabilities': 'I can assist you with basic tasks like providing information, answering questions, and more. Just ask!',
    r'bye|goodbye|see you later': 'Goodbye! Have a great day!',
    r'what is the time|what time is it': datetime.datetime.now().strftime("%I:%M %p"),
    r'what is the date|what\'s the date today': datetime.datetime.now().strftime("%A, %B %d, %Y"),
    r'what is the weather|how\'s the weather': 'I\'m sorry, I don\'t have access to weather information at the moment,i will try to bring the better version of me',
    r'(.*) (weather|forecast) (today|tomorrow)': 'I\'m sorry, I don\'t have access to weather information at the moment.',
    r'(.*) (where|what) (is|are) (.*)(\?)?': 'I\'m sorry, I don\'t have that information.',
    r'Tell me about yourself': 'I am just a chatbot assistant who makes your work easy by performing tasks. How can I help you?',
}

# Function to respond to user input
def respond(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "Sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the user
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye! Have a great day!")
        break
    else:
        print("ChatBot:", respond(user_input))


# In[ ]:




