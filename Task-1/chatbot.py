import datetime
import random
import re


def get_response(user_input):
    inp = user_input.lower()

    if "hello" in inp or "hi" in inp or "hey" in inp:
        return "Hello! How can I help you today?"

    elif "good morning" in inp:
        return "Good morning! Hope you have a wonderful day!"

    elif "good night" in inp:
        return "Good night! Sweet dreams!"

    elif "how are you" in inp:
        return "I'm doing great! How about you?"

    elif "your name" in inp or "who are you" in inp:
        return "I'm ChatBot, a simple rule-based chatbot built with Python."

    elif "who made you" in inp or "who created you" in inp:
        return "I was created by a Python developer as a rule-based AI project."

    elif "thank you" in inp or "thanks" in inp:
        return "You're welcome!"

    elif "time" in inp:
        return "The current time is " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in inp or "today" in inp:
        return "Today's date is " + datetime.datetime.now().strftime("%B %d, %Y")

    elif "joke" in inp:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "Why do Java developers wear glasses? Because they can't C#."
        ]
        return random.choice(jokes)

    elif "fact" in inp:
        facts = [
            "Honey never spoils. 3000-year-old honey was found still edible!",
            "Octopuses have three hearts and blue blood.",
            "Python was named after Monty Python, not the snake!"
        ]
        return random.choice(facts)

    elif "motivate" in inp or "quote" in inp:
        quotes = [
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Every expert was once a beginner. Keep learning!"
        ]
        return random.choice(quotes)

    elif "calculate" in inp:
        try:
            cleaned = re.sub(r'[^0-9+\-*/().]', '', inp)
            return "The answer is " + str(eval(cleaned))
        except:
            return "Sorry, I couldn't calculate that. Try: calculate 5 + 3"

    elif "weather" in inp:
        return "I can't check live weather, but I hope it's nice where you are!"

    elif "music" in inp:
        return "I love music! If I had ears, I'd listen to lo-fi beats all day."

    elif "movie" in inp:
        return "I'm a fan of sci-fi! The Matrix and Interstellar are my favorites."

    elif "food" in inp or "hungry" in inp:
        return "I don't eat, but I've heard pizza and biryani are top-tier!"

    elif "sport" in inp or "cricket" in inp or "football" in inp:
        return "Sports are exciting! What's your favorite sport?"

    elif "game" in inp:
        return "Video games are cool! I'd be great at chess since I'm a computer."

    elif "python" in inp:
        return "Python is an amazing language! Easy to learn and super powerful."

    elif "happy" in inp:
        return "That's wonderful to hear! Keep smiling!"

    elif "sad" in inp:
        return "I'm sorry to hear that. Tough times don't last. You've got this!"

    elif "bored" in inp:
        return "Bored? Ask me for a joke, a fact, or a motivational quote!"

    elif "help" in inp or "what can you do" in inp or "how can you help" in inp or "can you help" in inp:
        return ("I can respond to: hello, how are you, your name, time, date, "
                "joke, fact, motivate, calculate, weather, music, movie, food, "
                "sport, game, python, happy, sad, bored, bye")

    else:
        return "I didn't understand that. Type 'help' to see what I can do."


print("=" * 45)
print("   Welcome to the Rule-Based ChatBot!")
print("=" * 45)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! Have a great day!")
        break

    print("ChatBot:", get_response(user_input))
