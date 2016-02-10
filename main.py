import os
from selenium import webdriver

driver=webdriver.Firefox()

try:
        input = raw_input
except NameError:
	pass

def waitForNextMessage():
	messageList=driver.find_elements_by_css_selector('.null')
	command=''
	print('Ready!')
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
	cmd=command.split(' ')
	if(len(cmd)==2):
		fpath=os.getcwd()+'/'+cmd[1]
	if cmd[0] == 'cd':
		if os.path.isdir(fpath):
			os.chdir(fpath)
			output=os.getcwd()
		else : output='No such file or directory: '+fpath
	if cmd[0] == 'send':
		if os.path.isfile(fpath):
			driver.find_element_by_id('js_1').send_keys(fpath)
			output=fpath
		else:
			output='File not found : '+fpath
	driver.find_element_by_css_selector('.uiTextareaNoResize.uiTextareaAutogrow._1rv').send_keys(output)
	driver.find_element_by_id('u_0_y').click()

def init():
	email=input('Email : ')
	password=input('Password : ')
	print('Loading...\n')
	driver.get('https://www.facebook.com/')
	inputs=driver.find_elements_by_css_selector('.inputtext')
	inputs[0].send_keys(email)
	inputs[1].send_keys(password)
	driver.find_element_by_id('u_0_l').click()

	profile=driver.find_element_by_css_selector('._2dpe._1ayn').get_attribute('href').split('/')[3]
	driver.get('https://www.facebook.com/messages/'+profile)
	if not(driver.find_element_by_id('u_0_y').is_displayed()):
		driver.find_element_by_css_selector('._1s0').click()

	while True :
		waitForNextMessage()

	driver.quit()

if __name__ == '__main__':
	init()
