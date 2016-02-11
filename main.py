import os
import sys
from selenium import webdriver
from getpass import getpass

driver=webdriver.Firefox()
driver.set_window_size(800,800)  #Required, removes the "element not found" bug

try:
        input = raw_input
except NameError:
	pass

def waitForNextMessage():
	messageList=driver.find_elements_by_css_selector('.null')
	command=''
	while True:
		driver.implicitly_wait(10)
		element = driver.find_elements_by_css_selector('.null')
		if not(element == messageList):
			command=element[-1].find_elements_by_css_selector("*")[0].text
			if not(command.split(' ')[0] == '@CLI'):
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
	if cmd[0] == 'quit':
		output='Session Ended'
		driver.quit()
		sys.exit(0)
	if cmd[0] == 'memory':
		output=os.popen('top -l 1 -s 0 | grep PhysMem').read()
	if cmd[0] == 'help':
		output='help                   : Displays this\nquit                    : Ends current session\nsend __filePath : Sends the file at the path specfied\nmemory             : Gives current memory stats of system\n\nRun any other command as you would on your CLI'
	driver.find_element_by_css_selector('.uiTextareaNoResize.uiTextareaAutogrow._1rv').send_keys('@CLI :\n\n'+output)
	driver.find_element_by_id('u_0_y').click()

def init():
	cont=False
	while(cont == False):
		driver.get('https://www.facebook.com/')
		email=input('Email : ')
		password=getpass('Password : ')
		inputs=driver.find_elements_by_css_selector('.inputtext')
		inputs[0].send_keys(email)
		inputs[1].send_keys(password)
		driver.find_element_by_id('u_0_l').click()
		driver.implicitly_wait(10)
		if str(driver.current_url).split('=')[0] == 'https://www.facebook.com/login.php?login_attempt':
			if os.name == 'nt':
				cl=os.system('cls')
			else : 
				cl=os.system('clear')
			print('Invalid Email/Password')
		else: 
			cont=True

	print('Loading...\n')
	profile=driver.find_element_by_css_selector('._2dpe._1ayn').get_attribute('href').split('/')[3]
	driver.get('https://www.facebook.com/messages/'+profile)
	if not(driver.find_element_by_id('u_0_y').is_displayed()):
		driver.find_element_by_css_selector('._1s0').click()
	print('Ready!')
	while True:
		waitForNextMessage()


if __name__ == '__main__':
	init()
