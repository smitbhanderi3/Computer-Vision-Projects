# import speech_recognition
# import pyttsx3
# import pyaudio
# import streamlit as st
# )

# sr = speech_recognition.Recognizer()


# with speech_recognition.Microphone() as sourch2:
#     print(" Silence Please ")
    
    
#     sr.adjust_for_ambient_noise(sourch2 , duration=2)
#     print(" Speak Now please.........")
    
#     audio2 = sr.listen(sourch2)
    
#     textt = sr.recognize_google(audio2)
#     textt = textt.lower()
    
    
#     print(" Did you say :"+ textt)


import speech_recognition
import streamlit as st
import pyttsx3
import pyaudio


def SepakNow(command):
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()

# Initialize the speech recognition recognizer
sr = speech_recognition.Recognizer()

# Streamlit UI
st.title("Speech Recognition : ")
st.text("This demo app is using DeepSpeech, an open speech-to-text engine.")

# Capture audio input using Streamlit's microphone widget
with speech_recognition.Microphone() as sourch2:
    st.text(" Silence Please 🔇")
    
    # Adjust for ambient noise
    sr.adjust_for_ambient_noise(sourch2, duration=2)
    
    st.text("Speak Now please.........")
    
    audio = sr.listen(sourch2)
    # global text
    # if audio not in text:
    #     text = sr.recognize_google(audio)
    #     text = text.lower()
    #     st.text("Did you say: " + text)
    #     SepakNow(text)
    # else:
    #     st.title("Please Try Again (Ctrl+R) and Silence Please ")
    
    # # Listen to the audio
    # if sourch2 in audio:
        # Perform speech recognition
    try:    
        text = sr.recognize_google(audio)
        text = text.lower()
            
        st.text("Did you say: " + text)
        SepakNow(text)
    except:
         st.title("Please Try Again (Ctr+R) and Silence Please ")
         

            

        




