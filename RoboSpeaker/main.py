import pyttsx3

 # Initialize the pyttsx3 engine
engine = pyttsx3.init()
 # Set properties (optional)
engine.setProperty('rate', 100)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
while True:
    
    # Get user input
    x = input("Enter the text: ")
    if x=='q':
        engine.say("Goodbye")
        engine.runAndWait() # Process the "Goodbye" message

        break

    
    

    
    # Speak the entered text

    engine.say(x)

    # Block while processing the commands
    engine.runAndWait()
