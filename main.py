import os
from selenium import webdriver


driver=webdriver.Firefox()

def waitForNextMessage():
	messageList=driver.find_elements_by_css_selector('.null')
	print(messageList)
	command=''
	while True:
		driver.implicitly_wait(10)
		element = driver.find_elements_by_css_selector('.null')
		if not(element == messageList):
			command=element[-1].find_elements_by_css_selector("*")[0].text
			print(command)
			runCommand(command)
			break

def runCommand(command):
	driver.implicitly_wait(10)
	output=os.popen(command).read()
	try :
		if command.split(' ')[0] == 'cd':
			os.chdir(command.split(' ')[1])
	except:
		output='Error'	
	driver.find_element_by_css_selector('.uiTextareaNoResize.uiTextareaAutogrow._1rv').send_keys(output)
	driver.find_element_by_id('u_0_x').click()

def init():
	email=input("Email : ")
	password=input('Password : ')
	
	driver.get('https://www.facebook.com/')
	inputs=driver.find_elements_by_css_selector('.inputtext')
	inputs[0].send_keys(email)
	inputs[1].send_keys(password)
	driver.find_element_by_id('u_0_l').click()

	profile=driver.find_element_by_css_selector('._2dpe._1ayn').get_attribute('href').split('/')[3]
	driver.get('https://www.facebook.com/messages/'+profile)
	driver.find_element_by_css_selector('._1s0').click()

	while True :
		waitForNextMessage()

	driver.quit()

if __name__ == '__main__':
	init()
