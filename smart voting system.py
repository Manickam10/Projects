import speech_recognition as sr
import mysql.connector

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create cursor
c = conn.cursor()

# Create table to store votes if not exists
c.execute('''CREATE TABLE IF NOT EXISTS votes
             (id INT AUTO_INCREMENT PRIMARY KEY, vote VARCHAR(255))''')
conn.commit()

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak your vote...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    return audio

def speech_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def validate_vote(vote_text):
    # Implement your validation logic here
    valid_options = ["option1", "option2", "option3"]  # Example valid options
    
    if vote_text.lower() in valid_options:
        return True
    else:
        return False

def record_vote(vote):
    # Record the vote in the database
    c.execute("INSERT INTO votes (vote) VALUES (%s)", (vote,))
    conn.commit()
    print("Vote recorded:", vote)

def main():
    while True:
        # Capture voice
        audio = capture_voice()
        
        # Convert speech to text
        vote_text = speech_to_text(audio)
        
        if vote_text:
            # Validate the vote
            if validate_vote(vote_text):
                # Record the vote
                record_vote(vote_text)
                print("Thank you for casting your vote!")
                break
            else:
                print("Invalid vote. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection after use
conn.close()
