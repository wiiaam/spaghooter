import random
from time import time
import json
from HTMLParser import HTMLParser
import urllib2

# implication fetching. Originally feel fetching by AtaK. (thnx)

html_parser = HTMLParser()

chan_urls = {
	"4chan" : "http://a.4cdn.org/",
	"8chan" : "http://8ch.net/",
	"wiz"   : "http://wizchan.org/",
	"lain"  : "http://lainchan.org/"
}

hdrs = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
	"Accept": "text/html,application/json",
	"Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
	"Accept-Encoding": "none",
	"Accept-Language": "en-US,en;q=0.8",
	"Connection": "keep-alive"
}

def strip_html_shit(post):
	search_start = 0
	while(post.find("<",search_start) != -1):
		tag_start = post.find("<",search_start)
		tag_end = post.find(">",tag_start)
		if tag_end == -1 :
			tag_end = len(post) - 2
		post = post.replace(post[tag_start : tag_end+1],"")
		search_start = tag_end + 1
	return post

def find_implications(post):
	implications = []
	temp = ""
	inside_spoiler = False
	search_start = 0
	while(post.find("implying", search_start) != -1):
		implication_start = post.find("implying", search_start)
		implication_end = implication_start
		while(post.find("<", implication_end) != -1):
			implication_end = post.find("<", implication_end)
			if not inside_spoiler:
				if(post[implication_end:implication_end+22] == "<span class=\"spoiler\">"):
					inside_spoiler = True
				else:
					break
			else:
				if(post[implication_end:implication_end+7] == "</span>"):
					inside_spoiler = False
				else:
					break
			implication_end += 1
		if implication_end == implication_start:
			implication_end = len(post)
		implications.append(strip_html_shit(post[implication_start : implication_end]))
		search_start = implication_end
	return implications

def get_threads(board, chan):
	global chan_urls, hdrs
	if chan not in chan_urls:
		return []
	try :
		threads_str = urllib2.urlopen(urllib2.Request(chan_urls[chan] + board + "/threads.json", headers = hdrs)).read()
	except urllib2.HTTPError:
		return []
	return json.loads(threads_str)

def get_posts(thread, board, chan):
	global chan_urls, hdrs
	posts_url = chan_urls[chan] + board
	if(chan == "4chan"):
		posts_url += "/thread/"
	else:
		posts_url += "/res/"
	posts_url += str(thread["no"]) + ".json"
	try :
		posts_str = urllib2.urlopen(urllib2.Request(posts_url, headers = hdrs)).read()
	except urllib2.HTTPError:
		return []
	return json.loads(posts_str)

def get_implications(board = "g", chan = "4chan"):
	global html_parser
	implications = []
	threads_json = get_threads(board, chan)
	for page in threads_json:
		for thread in page["threads"]:
			posts_json = get_posts(thread, board, chan)
			for post in posts_json["posts"]:
				try:
					clean_post = html_parser.unescape(post["com"]).encode('ascii', 'ignore')
				except:
					continue
				new_implications = find_implications(clean_post)
				implications += new_implications
	return implications

def imply(phenny, input):
	# Cancel if timeout hasn't ended yet and ignore exceptions
	if input.admin == False:
		try:
			if time() < globals().get(input.sender + "timeout") or time() < globals().get(input.nick + "nicktimeout"): return
		except: pass

	# Cancel if re-feeling not done
		if refeeling == True:
		phenny.say("Still re-feeling, please wait.")
		return

	# Actual implication outputting
	try:
		# if parameters are given
		if input.group(2):
			# split params and store in array
			inputArray = input.group(2).split(' ')
			# if more than one param is given
			if len(inputArray) > 1:
				# get implication from board=param1 chan=param2
				implication = random.choice(globals().get(inputArray[0] + inputArray[1] + "implications"))
			else:
				# get implication from board=param1 chan=4chan
				implication = random.choice(globals().get(inputArray[0] + "4chanimplications"))
		else:
			# get implication from board=r9k chan=4chan
			implication = random.choice(r9k4chanimplications)

		# output the implication
		phenny.say('3>' + str(implication))
	except:
		# There was an error finding the implication
		phenny.say("3>implying there is no error")

	# Set channel and user timeout
	globals()[input.sender + "timeout"] = time() + 8
	globals()[input.nick + "nicktimeout"] = time() + 30

imply.commands = ['imply', 'implying']
imply.priority = 'low'

def reimply(phenny, input):
	# If you are not admin
	if input.admin == False: return

	# Cancel if re-feeling
	if refeeling == True:
		phenny.say("Already re-feeling!")
		return
	# Set refeeling status to be true
	globals()[refeeling] = True

	# if parameters are given
	if input.group(2):
		# split params and store in array
		inputArray = input.group(2).split(' ')
		# if more than one param is given
		if len(inputArray) > 1:
			# download implication from board=param1 chan=param2
			phenny.say("Loading implications from " + inputArray[1] + "/" + inputArray[0] + "/")
			globals()[inputArray[0] + inputArray[1] + "implications"] = get_implications(inputArray[0], inputArray[1])
		else:
			# download implication from board=param1 chan=4chan
			phenny.say("Loading implications from 4chan/" + inputArray[0] + "/")
			globals()[inputArray[0] + "4chanimplications"] = get_implications(inputArray[0])
	else:
		# download implication from board=g chan=4chan
		phenny.say("Loading implications from 4chan/g/")
		globals()["r9k4chanimplications"] = get_implications()

reimply.commands = ['re-imply', 'reimply']
reimply.priority = 'low'
