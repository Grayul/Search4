#!/usr/bin/env python3
import requests, json, sys, time, os

def banner():
	print("""
	                         _    _  _   
	                        | |  | || |  
	 ___  ___  __ _ _ __ ___| |__| || |_ 
	/ __|/ _ \/ _` | '__/ __| '_ \__   _|
	\__ \  __/ (_| | | | (__| | | | | |  
	|___/\___|\__,_|_|  \___|_| |_| |_|  
	                                     
	A script find to user accounts on various social platforms
	by 7rillionaire and ZishanAdThandar
		""")
banner()
username = input("Enter users username : ")
localtime = time.asctime( time.localtime(time.time()) )
print("\nStarted at : {}\n" .format(localtime))


#link checker
def result(url, site, username):
	address = (url+username)
	try:
		r = requests.head(address)
		if r.status_code == 200:
			print("{} (VOILA)  : Account found on {}\n" .format(site, address))
		else: print("{} : Account not found on {}\n" .format(site, address))
	except: print("{} : Account not found on {}\n" .format(site, address))

result("https://github.com/", "Github", username) # Github
result("https://twitter.com/", "Twitter", username) # Twitter
result("https://www.youtube.com/c/", "YouTube", username) # YouTube
result("https://www.facebook.com/", "facebook", username) # facebook
result("https://instagram.com/", "Instagram", username) # Instagram
result("https://www.reddit.com/r/", "Reddit", username) # Reddit
# Telegram Indian Error 
# Discord problem
result("https://m.twitch.tv/", "Twitch", username) # Twitch
# LinkedIn problem
# google+ error
# flickr not found
result("https://www.quora.com/profile/", "Quora", username) # Quora
# my Space error
result("https://m.vk.com/", "VK", username) # VK
result("https://www.pinterest.com/", "Pinterest", username) # Pinterest
# Snapchat error
# stakoverflow it has a unique id plus username
result("https://vimeo.com/", "Vimeo", username) # Vimeo
result("https://hackerone.com/", "Hackerone", username.lower()) # hackerone
result("https://BugCrowd.com/", "BugCrowd", username) # BugCrowd
# Tumblr
tumblr = requests.get(f"https://{username.lower()}.tumblr.com")
tumblrres = (tumblr.status_code)
tumblraddress = (f"https://{username.lower()}.tumblr.com")
json_response = (tumblr.json)

if tumblrres == 200:
	if json_response == 'Account not found ':
		print("Tumblr : Account not found on {}" .format(tumblradress))
	else:
		print("Tumblr (VOLA) : Account found on {}" .format(tumblraddress))
else:
	print("Tumblr (404) : Error page not found")

print("\n \n")
print("DONE..! \n ")
print("Use ctrl+c to exit")
print("\n \n")
exit = input("Want to exit script or continue yes or no? : ")
if exit == "yes":
        os.system("exit()")
elif exit == "no":
        os.system("python Search4.py")
else :
        print("Enter yes or no only")
