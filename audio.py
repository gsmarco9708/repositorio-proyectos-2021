
import speech_recognition as sr

r = sr.Recognizer()


mic = sr.Microphone()


#sr.Microphone.list_microphone_names()

with mic as source:
    print('AJUSTANDO AMBIENTE')
    r.adjust_for_ambient_noise(source)
    print('GRABANDO AUDIO')
    audio = r.listen(source)
    print('AUDIO GUARDADO')

print("AUDIO A TEXTO:  "+ r.recognize_google(audio, language='es-GT'))
