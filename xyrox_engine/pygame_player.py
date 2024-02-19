import pygame

class Player:

    def __init__(self):
        pygame.mixer.init()

    def play(self, audio_buffer):
        """: play audio_buffer

        Args:
            audio_buffer (buffer): audio type
        """
        # Load the audio from the buffer
        pygame.mixer.music.load(audio_buffer)
        # Play the audio
        pygame.mixer.music.play()
        # Optional: Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    
    def stop(self):
        """"_summary: stop buffer play
        """
        pygame.mixer.music.stop()
    