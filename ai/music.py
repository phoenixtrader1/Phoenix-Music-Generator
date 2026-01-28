import random
import base64

def generate_music(prompt):
    """
    Simulate AI music generation. Returns a Base64 "dummy" music clip.
    Replace with real AI music API integration.
    """
    dummy_data = f"MusicTrack:{prompt}:{random.randint(1000,9999)}"
    encoded = base64.b64encode(dummy_data.encode()).decode()
    return f"data:audio/wav;base64,{encoded}"
