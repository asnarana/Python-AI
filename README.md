#  Voice Assistant in Python
This is a simple voice-activated assistant written in Python. It can recognize spoken commands, speak responses, search Wikipedia, compute answers using WolframAlpha, open websites, and take notes.

# Features
- Voice Activation: Responds to the activation word friend.
- Speech Recognition: Uses your microphone to listen for commands.
- Text-to-Speech: Speaks responses using your system’s voice.
- Wikipedia Search: Answers questions using Wikipedia.
- WolframAlpha Integration: Computes answers to factual queries.
- Web Navigation: Opens websites in Google Chrome.
- Note Taking: Records spoken notes to timestamped text files.
- Custom Commands: Say “friend say hello” or “friend say [something]” for custom speech.

 # Requirements 
 - Python 3.x
- speech_recognition
- pyttsx3
- wikipedia
- wolframalpha
- keyboard

Install dependencies with: 
pip install SpeechRecognition pyttsx3 wikipedia wolframalpha keyboard

# Setup 
1. WolframAlpha App ID:
Get your App ID from WolframAlpha and set it in the code:   appId = 'YOUR_APP_ID'

2. Google Chrome path :
 Make sure the chrome_path variable matches your system’s Chrome installation.

# Usage 
Run the script :
python solution.py (or your .py file name)

Say the activation word friend followed by a command, for example:
- friend say hello
 - friend go to google.com
- friend wikipedia Python programming
- friend compute 2 plus 2
- friend log (then dictate your note)
- friend exit (to quit)

# Notes
- The assistant uses your system’s default microphone and speakers.
- Notes are saved as note_YYYY-MM-DD-HH-MM-SS.txt in the current directory.
- Make sure your microphone is enabled and working.
