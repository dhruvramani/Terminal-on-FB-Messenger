#Author  : Dhruv Ramani (dhurvramani98@gmail.com)
#License : Apache-2.0

import os
import sys
from selenium import webdriver
from getpass import getpass

# Importing configparser both for Python 2 and 3
try:
	from configparser import SafeConfigParser
except ImportError:
	from ConfigParser import SafeConfigParser


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1080,800)  #Required, removes the "element not found" bug

try:
	input = raw_input
except NameError:
	pass

def clear():
	if os.name == 'nt':
		os.system('cls')
	else : 
		os.system('clear')

def waitForNextMessage():
	driver.implicitly_wait(10)
	messageList=driver.find_elements_by_css_selector('.null')
	command=''
	while True:
		driver.implicitly_wait(10)
		element = driver.find_elements_by_css_selector('.null')
		if not(element == messageList):
			command=element[-1].find_elements_by_css_selector("*")[0].text
			if not(command.split('\n')[0] == '@CLI'):
				print(command)
				runCommand(command)
			break

def runCommand(command):
	driver.implicitly_wait(10)
	output=os.popen(command).read()
	url=''
	fpath=''
	cmd=command.split(' ')
	if(len(cmd)==2):
		fpath=os.getcwd()+'/'+cmd[1]
		urlIden=cmd[1].split(':')[0]
		if  urlIden == 'http' or urlIden == 'https':
			url=cmd[1]
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

	if cmd[0] == 'show':
		dr=webdriver.Chrome()
		foo=True
		if url:
			dr.get(url)
		elif os.path.isfile(fpath):
			dr.get('file:///'+fpath)
		else :
			output='Invalid Path/URL : ' 
			foo=False

		if foo:
			dr.save_screenshot('ss.png')
			dr.quit()
			if url: output=url 
			else: output=fpath
			driver.find_element_by_id('js_1').send_keys(os.getcwd()+'/ss.png')

	if cmd[0] == 'memory':
		output=os.popen('top -l 1 -s 0 | grep PhysMem').read()
	if cmd[0] == 'help':
		output='help : Displays this\n\nquit : Ends current session\n\nsend __filePath : Sends the file at the path specfied\n\nmemory : Gives current memory stats of system\n\nshow __filePath/URL : Previews file/url \n\nRun any other command as you would on your CLI'
	
	if not output:
		output='(Y)'
	driver.find_element_by_css_selector('.uiTextareaNoResize.uiTextareaAutogrow._1rv').send_keys('@CLI\n\n'+output)
	driver.find_element_by_id('u_0_y').click()

def init():
	cont=False
	clear()

	credentials_from_file = False

	credentials = SafeConfigParser();
	credentials.read('settings.txt')
	if credentials.has_option('main','email') and credentials.has_option('main','password'):
		credentials_from_file = True

	while(cont == False):
		driver.get('https://www.facebook.com/')
	
		if credentials_from_file:
			email = credentials.get('main', 'email')
			password = credentials.get('main', 'password')
		else:
			email=input('Email : ')
			password=getpass('Password : ')

		inputs=driver.find_elements_by_tag_name('input')
		inputs[1].send_keys(email)
		inputs[2].send_keys(password)
		driver.implicitly_wait(10)
		inputs[3].click()
		if str(driver.current_url).split('=')[0] == 'https://www.facebook.com/login.php?login_attempt':
			clear()
			print('Invalid Email/Password')
			if credentials_from_file:
				print('Switching to manual input')
				credentials_from_file = False
		else: 
			cont=True

	print('Loading...\n')
	profile=driver.find_element_by_css_selector('._2s25').get_attribute('href').split('/')[3]
	driver.get('https://www.facebook.com/messages/'+profile)
	if not(driver.find_element_by_id('u_0_y').is_displayed()):
		driver.find_element_by_css_selector('._1s0').click()
	print('Ready!')
	while True:
		waitForNextMessage()


if __name__ == '__main__':
	init()
