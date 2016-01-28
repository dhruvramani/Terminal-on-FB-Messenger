# Terminal on Facebook Messenger

Allows user to take full control of the terminal of their computer through Facebook's messaging service.

![Photo](photo.PNG)

##Dependencies 
####Selenium
```
pip3 install selenium
```
####[Firefox](https://www.mozilla.org/en-GB/firefox/new/)

##Running
To use the script to full extent, make sure that you keep it at the home directory.
Run it like this :
```
python3 ~/main.py
```
![Screenshot](Screenshot1.png)
Enter your facebook username and password and wait till it sets up. To make sure that it has setup, your url should be ```'https://facebook.com/messages/*your own username*```.

##Future Improvements
- Add support for ```cd```
- Send files 
- Switch to PhantomJS
- Error Logs
- Running in backgroud thread
