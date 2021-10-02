import subprocess
import webbrowser
import os
def you():
    global a
    a=input('you: ')   

you()    
    
b="bot: "


def bot():
     
    if "hello" in a:
        print(b+'hi :)')
        you()
        bot()
    elif "bye" in a:
        print(b+'bye bye!')
        you()
        bot()
    elif "angry" in a:
        print(b+'sorry if I have done any mistake :(')
        you()
        bot()
    elif "name" in a:
        print(b+'chagan')
        you()
        bot()
    elif "nice" in a:
        print(b+'me also!')
        you()
        bot() 
    elif "bye" in a:
        print(b+'bye bye!')
        you()
        bot()
    elif "open chrome" in a:
        print('ok')
        global chrome
        chrome=subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\ronit.exe')
        you()
        bot()
    elif "open music file" in a:
        subprocess.Popen('')
        you()
        bot()      
    elif "open youtube" in a:
        print('ok')
        webbrowser.open('https://www.youtube.com/')
        you()
        bot()  
    elif "open pycharm" in a:
        print('ok')
        global p
        p = subprocess.Popen('C:\\Program Files\\JetBrains\PyCharm Community Edition 2021.2\\bin\\pycharm.exe')
        you()
        bot()  
    elif "close"in a:
        global c    
    elif "sweta"in a:
        print(b+"your sister")
        you()
        bot()   
    elif "sakshi"in a:
        print(b+"your sister")  
        you()
        bot()   
    elif "shadhya devi"in a:
        print(b+"your mother")
        you()
        bot()   
    elif "vimlesh mishra"in a:
        print(b+"your father")   
        you()
        bot()   
    elif "are you"in a:
        print(b+"I am fine! what about you??")   
        you()
        bot()      
    elif "fine" or "am fine" in a:
        print(b+"ok :)")
        you()
        bot()  
    else:
        print(b+'sorry! could not understand :(')
        you()
        bot()    


bot()