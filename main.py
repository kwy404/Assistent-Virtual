import openai
import speech_recognition as sr
import pyttsx3

def new_chat(text):
    openai.api_key = "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"
    # create a completion
    completion = openai.Completion.create(prompt=text, engine= "text-davinci-003", temperature = 0,top_p=1, frequency_penalty=2, presence_penalty=1, best_of=1,max_tokens=1000)
    return completion.choices[0].text

def speech():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        ai_speech("Diga")
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Retorna a frase pronunciada
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        return False
    return frase

def main():
    while True:
        try:
            speech_frase = speech()
            if speech_frase:
                chat_ai = new_chat(speech_frase)
                ai_speech(chat_ai)
        except sr.UnkownValueError:
            return False
        
def ai_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

main()