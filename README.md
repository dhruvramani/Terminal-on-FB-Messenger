# Terminal on Facebook Messenger 
###TFM ver. 1.3
Allows user to take full control of the terminal of their computer through Facebook's messaging service.

![Photo](Screenshots/Photo1.jpg)

##Run
To use the script to full extent, make sure that you keep it at the home directory.
Run it like this :
```
python ~/main.py
```
![Screenshot](Screenshots/Screenshot1.png)
Enter your facebook username and password and wait till it sets up. To make sure that it has setup, your url should be ```'https://facebook.com/messages/*your own username*```.

To send the commands, search for your own name on the messenger and send commands to it

##Dependencies 
####Selenium
```
pip install selenium
```
####[Firefox](https://www.mozilla.org/en-GB/firefox/new/)

##Commands
 - ```memory``` - Gives The current Memory Stats of the machine
 - ```send```   - Send file at a path relative to current directory
 - ```help```   - Lists the commands that can be used
 - ```quit```   - Quit current session
 - Any other command you might normally use on your CLI.

##Updates

 - Added ```memory``` command, to get current memory stats of the machine
 - Added ```quit``` and ```help``` commands

 ```
 help : Displays the commands which can be used
 quit : quit session
 ```
 - Addded condition for proper log-in
 - Using getpass() to hide password (PR by [@idoqo](https://github.com/idoqo))
 - Support for Python 2.7 (PR by [@amitt001](https://github.com/amitt001))
 - Added support for sending files and ```cd```. Type following commands on Messenger :

```
cd __dirPath
send __filePath
```

##Future Improvements
- ~~Add support for ```cd```~~
- ~~Send files~~
- Switch to PhantomJS
- Error Logs
- Running in backgroud thread
- Fix all the bugs
