import random
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# List of words for the game
words = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "kiwi", "blueberry", "peach"]

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Say the word:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize the speech
            word = recognizer.recognize_google(audio).lower()
            return word
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return ""

# Main function for the game
def speak_it():
    print("Welcome to SpeakIt!")
    print("Try to speak out the word displayed on the screen correctly.")

    score = 0

    while True:
        # Select a random word from the list
        word_to_speak = random.choice(words)
        print("Word to speak:", word_to_speak)

        # Recognize speech
        user_word = recognize_speech()

        if user_word == word_to_speak:
            print("Correct! You earned 1 point.")
            score += 1
        else:
            print("Incorrect! The correct word was:", word_to_speak)

        print("Your score:", score)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing SpeakIt! Your final score is:", score)
            break

if __name__ == "__main__":
    speak_it()
