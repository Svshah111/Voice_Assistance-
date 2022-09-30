from unittest import result
import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser
import os
import smtplib
import datetime as date
import time
import pyautogui
import psutil
import screen_brightness_control as sbc
from requests import get
import requests
from requests.api import request
from bs4 import BeautifulSoup
import cv2
import random
import instaloader
import pyjokes
import keyboard
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty ('rate')
engine.setProperty('rate', 125)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
      

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        takecommand = query.replace('friday', '')

    except :
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M")   
    now = datetime.datetime.now()
    day = (now.strftime("%A"))
    if hour>=0 and hour<12:
        speak(f"Good Morning sir ")
        speak(f"time is:{strTime}")
        speak(f"today is:{day}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon sir ")
        speak(f"time is:{strTime}")
        speak(f"today is:{day}")  

    else:
        speak(f"Good night sir ") 
        speak(f"time is:{strTime}")
        speak(f"today is:{day}") 

    speak("I am friday Sir. Please tell me how may I help you")       


#### volume function ++++++++++++++++
def volume():
    pyautogui.press('volumeup')
    
def unlimit():
    pyautogui.press('volumeup')
    
def volume_decrease():
    pyautogui.press('volumedown')
def volume_mute():
    pyautogui.press('volumemute')
####  end volume function ++++++++++++++++
def stop_music():
    pyautogui.press('playpause')
def start_music():
    pyautogui.press('playpause')
def next_music():
    pyautogui.press('nexttrack')
def back_music():
    pyautogui.press('prevtrack')   
    
##################### end music function

### writing function start #######
def end():
    pyautogui.press('end')
def big_letter():
    pyautogui.press('capslock')
def backspace ():
    pyautogui.press('backspace')
    
## End writing function start #######
###############page up amd down###############
def page_up():
    pyautogui.press('pageup')
def page_down():
    pyautogui.press('pagedown')
###############page up amd down###############
################bettrey################
def charge():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percentage = battery.percent
    speak(f"sir our system have {percentage} percent battery")
    if percentage>=99:
        speak("sir our system have enough power so continue our work")
    elif percentage>=75:
        speak("sir our system doesn't need charging")
    elif percentage>50:
        speak("sir our system  need charging but you have no time so don't  problem")
    elif percentage<=30:
        speak("sir our system need charging ")
    elif percentage<=15:
        speak("sir our system have very low power please connect to charging otherwise i am going to shutdown ver soon ")
def select():
    pyautogui.press('ctrl' 'a ')
   

################# function is working  cut all file and folder#########
def cut():
    pyautogui.press('ctrl')
    pyautogui.press('x')

######################function is working paste all file and folder####
def pest():
    pyautogui.press('ctrl')
    pyautogui.press('v')

def copy():
    pyautogui.press('ctrl')
    pyautogui.press('c')

def virtual_window():
    pyautogui.hotkey('winleft','ctrl','D')

def minimize():
    pyautogui.hotkey('winleft','M')

    


def hello():
    speak("sir i am here")
    speak("hello sir how are you ")
    
def love():
    speak("but sir alexa so advance please develop me sir")
    speak("alexa said me you are not advance so please sir develop me please...")
#def friends():
    #speak("my best friends is Alexa ,seri,google assistance,AlphaGo,and AlphaZero")

def ip():
    ipAdd = requests.get("https://api.ipify.org").text
    speak(f"sir your ip address:{ipAdd}", ipAdd)
    
################## off function cannot work ###########
def off():
    pyautogui.hotkey('fn','f6')

 ################## off function cannot work ###########   

 ################## screen brightness ###########  
def screen1():
    sbc.fade_brightness(0)
def screen2():
    sbc.fade_brightness(50) 
def screen3():
    sbc.fade_brightness(75)
def screen4():
    sbc.fade_brightness(100)
 ##################end  screen brightness ###########  

 #####################switch window#############
def window_switch():
 # Holds down the alt key
    pyautogui.keyDown("alt")
    # Presses the tab key once
    pyautogui.press("tab")
    time.sleep(6)
# Lets go of the alt key
    pyautogui.keyUp("alt")
##################### end switch window#############
#####################close window tab#############
def close_window_tab():
 # Holds down the alt key
    pyautogui.keyDown("alt")
    # Presses the tab key once
    pyautogui.press("f4")
    time.sleep(6)
# Lets go of the alt key
    pyautogui.keyUp("alt")
##################### close window #############
##################### window  off #############
def log_out():
    pyautogui.hotkey('winleft','L')
    os.system("shutdown - l")  
def shutdown():
    speak('shutdown out in 5 second')
    time.sleep(5)
    os.system("shutdown /s /t 1") 
##################### window  off #############
##################### clean window   #############

def clean():
    os.system('cls')
def next_page():
    pyautogui.press('right')
def back_page():
    pyautogui.press('left')
    
    
# def goolge():
#     import wikipedia as googleScrap
#     query = query.replace("friday","")
#     query = query.replace("google search","")
#     query = query.replace("google","")
    
#     try:
#         pywhatkit.search(query)
#         result = googleScrap.summary(query,3)
#     except:
#         speak('hello world')
    
     
def Friday_AI():
    wishMe()
    while True:

        query = takecommand().lower()

        # Logic for executing tasks based on query
        if'search' in query:
           pywhatkit.search(query)
           result = googleScrap.summary(query,5)
           speak(result)
                  
        elif 'friday song on youtube' in query:
            pywhatkit.playonyt(query)
                    
        elif 'open control pannel' in query:
            os.system("start control")
               

        elif 'open youtube' in query:
            speak("sir what are you search on youtube")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open google' in query:
            speak("sir, are you serch on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif 'open firefox' in query:
            firefox = webbrowser.Mozilla("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
          
        elif 'open crome 'in query:
            GoogleChrome =  webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome")
####################### name of day######  ++++++++++++++++++++++  
        elif 'day today' in query:
            now = datetime.datetime.now()
            day = (now.strftime("%A"))
            speak(f"today is:{day}")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")   
            speak(f"Sir, the time is {strTime}")
            
        elif 'date' in query:
            today = date.today
            speak(f"sir the date is:{today}")
####################### end name of day######  ++++++++++++++++++++++  
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")  
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")    

        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
            ###########end hide function==================
        elif "fever" in query or " feel like fever" in query or "body temperature increased" in query:
            speak("sir please tell me your body temperature ")
            condition = takecommand().lower()
            if "99" in condition:
                speak("sir please wait  let me check ")
                speak("sir,normal temperature of body")
            elif "100" in condition or "hundred degree" in condition:
                speak("sir please wait  let me check best medicine for you")
                speak("sir please take niko ")
                speak(" paracetamol 500mg ")
                speak("for adult take three times age 17 to 60 ")
                speak("for child take half of one tablet childe age is 8 to 9 years old")
                
            elif "104" in condition or "one hundred four degree" in condition:
                speak("sir i think you fever is hard please consult  from doctor i am not develop more ")
#######################  wheater ==================
        elif 'temperature' in query:
            search = "temperature in kathmandu"
            url = f"https://www.google.com/search?q={search}" 
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current a{search} is {temp}")

####################### end wheater fnction==========


###################### how to cock any thing function===
############ open camera @#####################
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while(cap.isOpened()):
                while True:
                    ret, img = cap.read()
                    cv2.imshow('img', img)
                    if cv2.waitKey(30) & 0xff == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows() 
############ end  open camera @#####################

##################increase and decrease volume_____________________
        elif "volume hundred" in query or "volume 100 percent" in query or "volume hundred percent" in query or "hundred" in query:
            unlimit()
        elif "increase volume" in query:
            volume()
        elif 'decrease volume ' in query:
            volume_decrease()
        elif "stop speaking" in query or "mute" in query:
            volume_mute()
################## end increase and decrease volume_______________

################writning function###############++++++++++++

        elif 'caps lock' in query:
            big_letter()
        elif 'end' in query:
            end()
        elif 'backspace' in query:
            backspace()
############### writning function###############++++++++++++
############### start page up and down ###############++++++++++++
        elif 'up' in query : 
            page_up()
        elif 'down' in query :
            page_down()
        elif' next page ' in query:
            next_page()
        elif 'back page' in query:
             back_page()
        elif 'change Desktop' in query:
            virtual_window()
       
        elif 'clean display' in query:
            minimize()
            
############### end page up and downn###############++++++++++++
        elif 'power we have' in query or 'how much power you have' in query or 'battery percent' in query:
            charge()
            
################ music function ++++++++++++++__________________
            
        elif 'stop ' in query:
            stop_music()
        elif 'start ' in query:
            start_music()
        elif 'change music' in query:
            next_music()
        elif 'music back' in query:
            back_music()
        
        elif "play song" in query:
            music_dir = "C:\\Users\\Sanjiv Shah\\OneDrive\\Desktop\\Minor_project\\Sanjiv"
            songs = os.listdir(music_dir)
            re = random.choices(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'play bhojpuri audio' in query:
            music_dir = "F:\\music\\bhojpuri"
            songs = os.listdir(music_dir)
            re = random.choices(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        elif 'play  video' in query:
            music_dir = "F:\Videos"
            songs = os.listdir(music_dir)
            re = random.choices(songs)
            for song in songs:
                if song.endswith(''):
                    os.startfile(os.path.join(music_dir, song))
                    
                    
   ################  end music function ++++++++++++++__________________                 
                    
        
      ##########-------------------find location ----------------
      
                
        elif "whate is my IP address" in query:
            ip()
        
        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not seure ,but i thing we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir ,due to network")
                pass
     
     
     
     ####################------------check my instagram account--------------
        elif "instagram profile" in query or "check my instagram profile" in query:
            speak("sir please wait enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user{name}")
            time.sleep(5)
            speak("sir would you like to downlord profile picture of this account.")
            condition = takecommand.lower()
            if "yes" in condition:
                mod = instaloader.instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("i am done sir ,profile  picture is saved in our main folder.now i am ready")
            else:
                pass
    #################-----------end instagram----------------------
     #################-----------screnn shot function ----------------------
     
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir please tall me the name of this sceenshot ")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking th name of this screenshot")
            time.sleep(3)
            imgscreenshot = pyautogui.screenshot()
            imgscreenshot.save(r"C:\\Users\sahsa\\Desktop\\AI project\\{name}.png")#name in middle bricket{name}
            speak("sir i am done the screenshot is saved in our main folder  ") 
            
    
            
################## screen control function ###########  
        elif "low brightness" in query or  "brightness 0%" in query or "brightness zero percent" in query:
            screen1()
        elif "half brightness" in query or "brightness 50%" in query or "brightness fifty percent" in query:
            screen2()
        elif "brightness  75 percent" in query or "brightness 75%" in query or "brightness seventyfive" in query:
            screen3()
        elif "full brightness" in query:
            screen4()
##################  screen control function ###########           
# to close any application

        elif "close cmd" in query:
            speak("oky boos, closing cmd")
            os.system("taskkill /f /im cmd.exe")
        
        elif 'open calculator' in query:
            os.system("start calc")
        elif 'close calculator' in query:
            os.system("taskkil /f /im calc.exe")
           
##
#####################switch window function #############

        elif 'switch window' in query:
            window_switch()
        elif 'clean it' in query:
            clean()
        
# to close any application

        elif 'select' in query:
            select()
        elif 'copy' in query:
            copy()
        elif 'cut' in query:
            cut()
        elif 'paste' in query:
            pest()
            
#  talk to  vision 


        elif "friday" in query:
            hello()
        elif "friday" in query:
            speak("Hello Sir")
            
            
        elif "i am good " in query:
            speak(" sir i am always ready with you ")
        
        elif 'tell me about god' in query:
            speak("god is our belive.god make every thing bucase my god name is boss because he develop me , so he my god")
            
        elif 'god stay on earth' in query:
            speak("yes, god is stable on earth. sanjiv sir always say me father and mother is my god ")
            
        elif "where god live" in query:
            speak("god live in your home")
            
        elif 'what' in query:
            speak("yes god in your home you know your father and mother is your god") 
            
        elif 'who developed you' in query:
            speak("sir  sanjiv  develop me")

        elif "really" in query:
            speak('yes sir he develop me')
        elif 'really sanjiv develop you' in query:
            speak('yes it real he genius very help full ')
        elif 'virsion ' in query or 'tell me your version' in query:
            speak("sir my virsion is 0.1")
        elif 'you are bloody bastard' in query or ' you usually' in query or " you are useless" in query:
            speak("sir please donot say sir i alwaye with you boss")  
            
        elif 'introduction yourself' in query:
            speak('i am friday.i am a female assistance. my version is 0.10  developed by python programming and i am under developing .doesnot advance more than Alexa & seri' )
# jokes tell me from vision 
        elif 'joks' in query:
            joke = pyjokes.get_joke()
            speak(joke)        
            
#########################systme close system ++++++++++++++
        
        elif 'shutdown' in query:
            shutdown()
        
        elif 'restart' in query:
            os.system("shutdown /r")
            
        elif 'log out' in query:
            log_out()
            
            
            
 ##################### end sustem colsing system+++++++++++   
        
        
            
        elif "screen off " in query:
            off()

        elif "ok" in query in "ok friday" in query:
            speak('well come sir its my pleasure')    

        elif "sleep now" in query:
            speak('thanks you , have you good day boss')
            break   
        
            
        #speak("sir, do you have any other work")
if __name__ == "__main__":
    Friday_AI()