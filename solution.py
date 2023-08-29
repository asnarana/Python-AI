
#importing dependencies 
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import keyboard


#local speech engine initialisation 
engine = pyttsx3.init()
voices = engine.getProperty('voices')  #acessing voices property 
engine.setProperty('voice', voices[0].id) # 0 = male, 1 = female

activationWord = 'friend' #single world to let ai know we are talking 
#configure browswer
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path)) #set the path 


# Wolfram alpha client  
appId = 'UYH7W9-EKW6X45PPA'
wolframClient = wolframalpha.Client(appId)
 
#allows text to speech library to be useful and retrieve speech 
def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
     
     
# navigating to website 
# understanding what is coming through from microphone and parsing it using the Google API to convert it to text
def parseCommand():
    listener = sr.Recognizer() # getting access to microphone 
    print('Listening for command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2 #time of gap between user's speech before listening ends 
        input_speech = listener.listen(source)

    try: 
        print('Recognizing speech.. ')
        query = listener.recognize_google(input_speech,language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
            print('I did not catch that')
            speak('I did not catch that')
            print(exception)
            return 'None'

    return query

#defining search method  for wikepedia 
def search_wik(query = ''):
    searchResults = wikipedia.search(query) #searching for query
    if not searchResults:
        print('No wikepedia search.')
        return 'No result recieved'
    #otherwise, try this 
    try :
         wikiPage = wikipedia.page(searchResults[0]) # getting wik page for object specified in terminal
    except wikipedia.DisambiguationError as error: # catching invalid object specified 
         wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

# helper method to parse whether result from wolframalpha is list or dictionary 
def listorDict(var):
     if isinstance(var,list):
          return var[0]['plaintext'] # returns first element of list 
     else :
          return var['plaintext'] # returns dict 

# defining search method for wolframalpha 

def search_wolframAlpha(query=''):
    response = wolframClient.query(query)
  
    # @success: Wolfram Alpha was able to resolve the query
    # @numpods: Number of results returned
    # pod: List of results. This can also contain subpods

    # Query not resolved
    if response['@success'] == 'false':
        speak('I could not compute')
    # Query resolved
    else: 
        result = ''
        # Question
        pod0 = response['pod'][0]
        # May contain answer (Has highest confidence value) 
        # if it's primary or has the title of result or definition, then it's the official result
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            # Get the result
            result = listorDict(pod1['subpod'])
            # Remove bracketed section
            return result.split('(')[0]
        else:
            # Get the interpretation from pod0
            question = listorDict(pod0['subpod'])
            # Remove bracketed section
            question = question.split('(')[0]
            # Could search wiki instead here? 
            return question
     

     
#Main loop 
if __name__ == '__main__':
     speak('All systems nominal.', 120 )
     
     while True: # listening for commands until user ends app
          # Parse as list 
          query = parseCommand().lower().split()

          if query[0] == activationWord:
               query.pop(0) #remove activation word from query 
               if query[0] == 'say':
                    if 'hello' in query:
                         speak('Greetings, all.')
                    else:
                         query.pop(0) #removing say
                         speech = ' '.join(query)
                         speak(speech)
                         
            # Navigation
          if query[0] == 'go' and query[1] == 'to' :
                speak('Opening....')
                query = ' '.join(query[2:]) # specifies the destination after the phrase 'go to'
                webbrowser.get('chrome').open_new(query) # will launch the web browser

          #Wikepedia 
          if query[0] == 'wikipedia':
               query = ' '.join(query[1:]) #skipping the wikepedia command word 
               speak('Querying the universal databank.')
               result = search_wik(query)
               speak(result)

          # Wolfram alpha 
          if query[0] == 'compute' or query[0] == 'computer':
               query = ' '.join(query[1:]) 
               speak('Computing')
               try: 
                    result = search_wolframAlpha(query)
                    speak(result)
               except: 
                    speak('Unable to compute')

           #note taking 
          if query[0] == 'log':
               speak ('Ready to record your note ')
               newNote = parseCommand().lower()
               
               now = datetime.now().strftime('%Y-%m-$d-%H-%M-%S')
               with open('note_%s.txt' % now, 'w' ) as newFile:
                    newFile.write(newNote)
               speak('Note Written')

          if query[0] == 'exit':
               speak('Goodbye')

               




               




                        
                              
                         
                         
                        
              

                    
                    

         

               

               
          
        
          
 