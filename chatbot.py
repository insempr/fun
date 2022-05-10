import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    #
    [
        r"my name is (.)",
        ["Hello %1, How are you"]
    ],
    # Or expression
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello my name is Ethan"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Ethanwhat. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["Thank you for using our intelligence services"]
    ],
    

]

def chat():
    print("Hey there! I am Ethan at your service")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()