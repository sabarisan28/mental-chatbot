import random
import re

# Predefined intents and responses (can be expanded)
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello! How are you feeling today?", "Hi there! I'm here to listen."]
    },
    "sadness": {
        "patterns": ["I feel sad", "I am depressed", "I am feeling down", "I am unhappy", "I'm stressed"],
        "responses": [
            "I'm sorry to hear that. Would you like to talk about what's bothering you?",
            "It’s okay to feel sad sometimes. Remember, this too shall pass.",
            "Try to take deep breaths and take it one step at a time."
        ]
    },
    "anxiety": {
        "patterns": ["I feel anxious", "I am nervous", "I am worried", "I'm stressed about"],
        "responses": [
            "Anxiety can be tough. Have you tried any relaxation techniques?",
            "Taking slow, deep breaths might help calm your mind.",
            "Remember, you are not alone, and help is available."
        ]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thank you so much"],
        "responses": ["You're welcome!", "Anytime! I'm here if you want to talk."]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye! Take care of yourself.", "See you later! Remember, I'm here whenever you need."]
    }
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def classify_intent(text):
    text = preprocess(text)
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in text:
                return intent
    return None

def get_response(intent):
    if intent:
        return random.choice(intents[intent]["responses"])
    else:
        return "I'm here to help. Can you please tell me more?"

def chatbot():
    print("Mental Health Support Chatbot\n(Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Take care! Remember, professional help is always available if you need it.")
            break
        intent = classify_intent(user_input)
        response = get_response(intent)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
