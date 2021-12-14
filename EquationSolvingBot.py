import pyautogui
import time
import cv2
import easyocr #this guy needs pytorch..
import numpy as np  
from PIL import Image
import random

#disclaimer
#This bot is developed for Educational purpose and NOT to be used in cheating
#any screen coordinates you'll need to change it according to your resolution and working coordinates(x,y)

def listToString(s): #it's obvious .. it converts list to string

	str1 = ""

	for ele in s:
		str1 += ele

	return str1

start_time = time.time()
reader = easyocr.Reader(['abq']) 
#Chose abq(which is a short for a language that i don't know what it is) because it's accurate for detecting numbers and symbols
#In case you do not have a GPU, or your GPU has low memory, you can run the model in CPU-only mode by adding gpu=False. (['abq'],gpu=False) 
#If you have a decent nvidia gpu you can Install CUDA and use it, it will be 300% faster!

print("--- %s seconds ---" % (time.time() - start_time))
pyautogui.click(1327, 532) #click play
time.sleep(4)
while True:
	myScreenshot = pyautogui.screenshot() #takes a screenshot
	im = np.array(myScreenshot)
	im = im[:, :, ::-1].copy()
	crop_img = im[350:480, 1220:1446] #crops the part with the equation
	result = reader.readtext(crop_img) #converts the image into text

	print(result[0][1])
	print("The final result is       \n")
	res = list(result[0][1])

	
	if ("=" in res):	#in the next section i need the result in statement form in order to evaluate (replacing "=" with "==")
		res[res.index("=")] = "=="
	
	
	print(res)
	equation = listToString(res) #String goes brrr!
	
	print(eval(equation)) #Evaluate into True Or False..
	n = random.uniform(0.0,0.1) #to make it look like a human behaviour
	time.sleep(n)
	

	if(eval(equation)==True):
		pyautogui.click(1243, 655) #click on the checkmark (right button)
	elif(eval(equation)==False): 
		pyautogui.click(1419, 656) #click on the crossmark (Wrong button)
	time.sleep(0.65) 
