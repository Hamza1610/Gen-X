from xyrox_engine.libs.player import Player

import io
from gtts import gTTS
import speech_recognition as sr

player = Player()

class Xyrox():
    """
    _summary_: AI engine for TTS and STT

    """
    @staticmethod 
    def welcome_speech():

        """
        _summary_: Method the make welcoming speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text='Welcome to Xyrox AI, what can I help you with today.', lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)

            # play audio buffer
            player.play(audio_buffer)
            print('Welcoming speech generate!')
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Welcoming Done!')


    @staticmethod 
    def listen_to_speech():

        """
        _summary_: Listen to speech user speech
        """
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please speak something...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            # Listen to the user's voice
            audio = recognizer.listen(source)
            print("Recognition complete. Converting to text...")

        try:
            # Use Google Web Speech API for speech-to-text conversion
            text = recognizer.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            # return "Sorry, could not understand audio."
        except sr.RequestError as e:
            print("Error with the speech recognition service", e)
            # return f"Error with the speech recognition service, {e}"
    @staticmethod 
    def make_speech(text):
        """
        _summary_: Make speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text=text, lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)
            # play audio buffer
            player.play(audio_buffer)
            print('Speech generation done!')

            
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Done!')

    @staticmethod 
    def iscommand(command):
        """
        _summary_: Check local voice commands

        Args:
            command (str): text command
        """
        if command == 'off':
            return True
        else:
            pass
        
    @staticmethod 
    def compute_text(mode, text):
        """
        _summary_: Compute text by Gemini API
        """
        # generate text from GENINI
        gemini_text = Gemini(mode, text)
        return gemini_text
    

    @staticmethod 
    def exit_speech():

        """
        _summary_: Exit speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text='Good bye for now see you later in the day.', lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)

            # play audio buffer
            player.play(audio_buffer)
            print('Exit processing..')
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Exit..')
