import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# List all microphone devices and their indices
print("Available microphones:")
print(sr.Microphone.list_microphone_names())

# Adjust device_index to the correct one (if needed)
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjusts based on ambient noise

    print("Say something!")
    audio = recognizer.listen(source)

try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
