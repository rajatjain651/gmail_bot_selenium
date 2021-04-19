path ="C:\\Users\\ADMIN\\Desktop\\gmail\\chromedriver.exe"
# add the phone number on line 78
#add the recovery email on line 194



from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import sounddevice as sd
import soundfile as sf
import pyaudio
import wave
import pyttsx3
import time
import speech_recognition as sr
import re



def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

dob = '1-1-2000'
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
arr = int(dob.split('-')[1])
month_dob =  months[arr-1]
from time import gmtime, strftime
x2 =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
x4 = x2.replace('-','')
x4 = x4.replace(' ','')
x4 = x4.replace(':','')
username  = "John.Smith" +x4


n = random.randint(99,9999999)
#username  = "John.Smith" + str(n)
password = 'john@smith123'+ str(n)

driver = webdriver.Chrome(path)

driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()
print(username,password)
time.sleep(9)



element = driver.find_element_by_id("firstName")
element.send_keys("John")
element = driver.find_element_by_id("lastName")
element.send_keys("Smith")


element = driver.find_element_by_id("username")
element.send_keys(username)
element = driver.find_element_by_name("Passwd")
element.send_keys(password)
element = driver.find_element_by_name("ConfirmPasswd")
element.send_keys(password)

element = driver.find_element_by_id("accountDetailsNext")
element.click()
SpeakText('the username and password are printed in the command line interface note it down to use it later.')
time.sleep(9)


element = driver.find_element_by_id("phoneNumberId")
element.send_keys('')
elem = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
action = ActionChains(driver)
action.move_to_element(elem).click().perform()


def func():
    otp = False
    SpeakText("""Just answer in only yes or no. please  speak only after I  say   one   two   three   start""")
    while otp == False:
        time.sleep(1)
        SpeakText("""Did you recieved the otp on your mobile phone? the audio recording will start in
                  one   two   three   start """)
        samplerate = 44100  # Hertz
        duration12 = 5  # seconds
        filename12 = 'otp12345.wav'
        mydata12 = sd.rec(int(samplerate * duration12), samplerate=samplerate,
                        channels=2, blocking=True)
        sf.write(filename12, mydata12, samplerate)
        r = sr.Recognizer()
        with sr.AudioFile(filename12) as source:
            # listen for the data (load audio to memory)
            audio_data12 = r.record(source)
            # recognize (convert from speech to text)
            text1 = r.recognize_google(audio_data12)
            #print(text1)
        if text1[:3].lower() == 'yes':
            otp = True
            break


    confirm = False
    
    while confirm != True:
        samplerate = 44100  # Hertz
        duration = 15 # seconds
        filename = 'output12345.wav'

        #print("* recording")
        SpeakText('the audio recording will be starting in few seconds. ')
        time.sleep(1)
        SpeakText("""You will have 15 seconds to enter the otp that you have recieved on your mobile phone.
        the audio recording will start in    one    two   three   start """)


        mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                        channels=2, blocking=True)

        #print("* done recording")
        SpeakText('the recording is finished thanks')

        sf.write(filename, mydata, samplerate)

        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            #print(text)
        
        c = re.findall('\d',text)
        sentotp = ''
        if len(c)<6:
            SpeakText("""Please check the otp because the number of digits are not equal to 6 you will have to speak again.""")
            digits = False
        else:
            digits = True
            for i in range(6):
                sentotp += c[i]
        if digits==False:
            continue
        
        SpeakText("""I will repeat the otp for the confirmation please hear me carefully !! """)
        time.sleep(1)
        SpeakText(text)
        time.sleep(1)
        SpeakText("""was this the correct otp. please reply in yes or no only? 
        the audio recording will start in  one  two  three   start""")      
        
        samplerate = 44100  # Hertz
        duration12 = 5 # seconds
        filename12 = 'otp12345.wav'
        mydata12 = sd.rec(int(samplerate * duration12), samplerate=samplerate,
                        channels=2, blocking=True)
        sf.write(filename12, mydata12, samplerate)
        r = sr.Recognizer()
        with sr.AudioFile(filename12) as source:
            # listen for the data (load audio to memory)
            audio_data12 = r.record(source)
            # recognize (convert from speech to text)
            text1 = r.recognize_google(audio_data12)
            #rint(text1)

        
        if text1[:3].lower() == 'yes' and digits:
            confirm = True
            break  

    return sentotp
text1234 = func()

time.sleep(5)
element12 = driver.find_element_by_id("code")
element12.send_keys(text1234)

elem1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span')))
action = ActionChains(driver)
action.move_to_element(elem1).click().perform()
time.sleep(9)

driver.find_element_by_id("phoneNumberId").clear()



element = driver.find_element_by_name("recoveryEmail")
element.send_keys("")
sel = Select(driver.find_element_by_xpath("//select[@id='month']"))
sel.select_by_visible_text(month_dob)
element = driver.find_element_by_id("day")
element.send_keys('1')
element = driver.find_element_by_name("year")
element.send_keys('2000')
sel = Select(driver.find_element_by_xpath("//select[@id='gender']"))
sel.select_by_visible_text("Male")
time.sleep(15)


elem2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
action = ActionChains(driver)
action.move_to_element(elem2).click().perform()

time.sleep(10)

elem2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')))
action = ActionChains(driver)
action.move_to_element(elem2).click().perform()
