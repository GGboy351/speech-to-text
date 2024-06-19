import soundfile as sf  
from pydub import AudioSegment
from pocketsphinx import LiveSpeech
import speech_recognition as sr


#сылку на файл в ogg
data, samplerate = sf.read('path_to_file.ogg')
#новый файл в формате wav
sf.write('new_file.wav', data, samplerate)



# Создаем объект Recognizer
recognizer = sr.Recognizer()

# Загружаем аудиофайл
audio_file = "new_file.wav"
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    
    # Распознаем текст с помощью Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        print("Текст из аудиофайла:")
        print(text)
    except sr.UnknownValueError:
        print("Google Web Speech API не смог распознать речь")
    except sr.RequestError as e:
        print("Не удалось отправить запрос к Google Web Speech API; {0}".format(e))
