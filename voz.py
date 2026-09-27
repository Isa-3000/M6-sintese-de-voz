import pyttsx3 # A text-to-speech conversion library in Python
engine = pyttsx3.init()  # object creation

frase = input('Escreva algo:')

def texto_para_fala(frase) -> None:
     # engine connects us to hardware in this case
    pt = pyttsx3.init()
     # Engine created
    pt.say(frase)
    # Runs for small duration of time otherwise we may not be able to hear
    pt.runAndWait()

voz = input('Escolha sua voz (1 ou 2):')
# VOICE
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male
if voz == '1':
    engine.setProperty("voice", voices[1].id)  # changing index, changes voices. 1 for female
elif voz == '2':
    engine.setProperty("voice", voices[0].id)  # changing index, changes voices. 1 for female

texto_para_fala(frase)