#!/usr/bin/env python3
import requests, json, sys, time, argparse, datetime
startTime = datetime.now()
requests.packages.urllib3.disable_warnings() 

class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def log(lvl, col, msg):
    	logger.log(lvl, col + msg + color.END)

def banner():
	print(color.BOLD + color.RED + """
	                         _    _  _   
	                        | |  | || |  
	 ___  ___  __ _ _ __ ___| |__| || |_ 
	/ __|/ _ \/ _` | '__/ __| '_ \__   _|
	\__ \  __/ (_| | | | (__| | | | | |  
	|___/\___|\__,_|_|  \___|_| |_| |_|  
	                                     
	version 0.9.0
	A script to find user accounts on various social platforms
	by 7rillionaire and ZishanAdThandar
		""" + color.END)
banner()

parser = argparse.ArgumentParser(description='Search user on different sites.')
parser.add_argument('-v', "--version", help='Shows version number.', action="store_true")
parser.add_argument('-u', '--username', help='Search for the given username.')

args = parser.parse_args()

if args.username:
	username = (args.username)
	print(color.BOLD + color.BLUE + "Given username is {}".format(username) + color.END)
elif args.version:
	username = (args.username)
	print(color.BOLD + color.BLUE + "Verion 9.0" + color.END)
	quit()
else:
	print(color.BOLD + color.BLUE + "{} -h for helps".format(sys.argv[0]) + color.END)
	quit()
starttime = time.asctime( time.localtime(time.time()) )
print(color.BOLD + color.BLUE + "\nStarted at : {}\n" .format(starttime) + color.END)


#link checker
def result(url, site, username):
	address = (url+username)
	try:
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0"}
		r = requests.get(address, headers=headers, verify=False)
		if r.status_code == 200:
			print(color.BOLD + color.GREEN + "{} (VOILA)  : Account found on {}\n" .format(site, address) + color.END)
		else: print(color.BOLD + color.YELLOW + "[!] {} : Account not found on {}\n" .format(site, address) + color.END)
	except: print(color.BOLD + color.YELLOW + "[!] {} : Account not found on {}\n" .format(site, address) + color.END)

print(color.BOLD + color.BLUE + "Social:\n" + color.END)
result("https://www.facebook.com/", "facebook", username) # facebook
result("https://twitter.com/", "Twitter", username) # Twitter
result("https://plus.google.com/+", "Google+", username.lower()) # Google+
# result("https://t.me/", "Telegram", username) # Telegram showing 200 for non existing account
result("https://m.vk.com/", "VK", username) # VK
# Snapchat error


print(color.BOLD + color.BLUE + "Videos:\n" + color.END)
result("https://www.youtube.com/c/", "YouTube", username) # YouTube
result("https://vimeo.com/", "Vimeo", username) # Vimeo
result("https://m.twitch.tv/", "Twitch", username) # Twitch

print(color.BOLD + color.BLUE + "Photos:\n" + color.END)
result("https://www.instagram.com/", "Instagram", username+"/") # Instagram
result("https://www.pinterest.com/", "Pinterest", username) # Pinterest
result("https://flickr.com/photos/", "Flickr", username.lower()) # Flickr
result("https://", "Tumblr", username.lower()+".tumblr.com") # Tmblr

print(color.BOLD + color.BLUE + "Blogs and forums:\n" + color.END)
result("https://medium.com/@", "Medium", username) # Medium
result("https://myspace.com/", "Myspace", username.lower()) # MySpace
result("https://www.reddit.com/r/", "Reddit", username) # Reddit
result("https://www.quora.com/profile/", "Quora", username) # Quora
# Discord problem

print(color.BOLD + color.BLUE + "Professional:\n" + color.END)
result("https://github.com/", "Github", username) # Github
#result("https://gitlab.com/", "Gitlab", username) # Gitlab 200 for non-existing account
#result("https://www.linkedin.com/in/", "LinkedIn", username.lower()+"/") # LinkedIn http2/ 999
result("https://hackerone.com/", "Hackerone", username.lower()) # hackerone
result("https://www.paypal.me/", "PayPal", username.lower()) # hackerone
result("https://BugCrowd.com/", "BugCrowd", username) # BugCrowd
# result("https://www.fiverr.com/", "Fiverr", username) # Fiberr
# stakoverflow it has a unique id plus username
completetime = datetime.now() - startTime
print(color.BOLD + color.BLUE + "\nExecution Time : {}\n" .format(completetime) + color.END)
print(color.BOLD + color.BLUE + "\n\nDONE..! \n\n" + color.END)
