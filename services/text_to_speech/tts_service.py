from gtts import gTTS

def generate_voice(text):

    audio_file = "response.mp3"

    tts = gTTS(text=text, lang="en")

    tts.save(audio_file)

    return audio_file