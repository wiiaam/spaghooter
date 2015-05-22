import random
from time import time
import json
from HTMLParser import HTMLParser
import urllib2

# Feel fetching stuff by AtaK. (thnx)

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

def find_feels(post):
	feels = []
	temp = ""
	inside_spoiler = False
	search_start = 0
	while(post.find("tfw", search_start) != -1):
		feel_start = post.find("tfw", search_start)
		feel_end = feel_start
		while(post.find("<", feel_end) != -1):
			feel_end = post.find("<", feel_end)
			if not inside_spoiler:
				if(post[feel_end:feel_end+22] == "<span class=\"spoiler\">"):
					inside_spoiler = True
				else:
					break
			else:
				if(post[feel_end:feel_end+7] == "</span>"):
					inside_spoiler = False
				else:
					break
			feel_end += 1
		if feel_end == feel_start:
			feel_end = len(post)
		feels.append(strip_html_shit(post[feel_start : feel_end]))
		search_start = feel_end
		# print feels[-1],"\n"
	return feels

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

def get_feels(board = "r9k", chan = "4chan"):
	global html_parser
	feels = []
	threads_json = get_threads(board, chan)
	for page in threads_json:
		for thread in page["threads"]:
			posts_json = get_posts(thread, board, chan)
			for post in posts_json["posts"]:
				try:
					clean_post = html_parser.unescape(post["com"]).encode('ascii', 'ignore')
				except:
					continue
				new_feels = find_feels(clean_post)
				feels += new_feels
	# feels = unicode(feels, 'utf-8', 'replace')
	return feels



	refeeling = False

def feel(phenny, input):
	# Cancel if timeout hasn't ended yet and ignore exceptions
	if input.admin == False:
		try:
			if time() < globals().get(input.sender + "timeout") or time() < globals().get(input.nick + "nicktimeout"): return
		except: pass

	# Cancel if re-feeling not done
	if refeeling == True:
		phenny.say("Still re-feeling, please wait.")
		return

	# Actual feel outputting
	try:
		# if parameters are given
		if input.group(2):
			# split params and store in array
			inputArray = input.group(2).split(' ')
			# if more than one param is given
			if len(inputArray) > 1:
				# get feel from board=param1 chan=param2
				feel = random.choice(globals().get(inputArray[0] + inputArray[1] + "feels"))
			else:
				# get feel from board=param1 chan=4chan
				feel = random.choice(globals().get(inputArray[0] + "4chanfeels"))
		else:
			# get feel from board=r9k chan=4chan
			feel = random.choice(r9k4chanfeels)

		# output the feel
		phenny.say('3>' + str(feel))
	except:
		# There was an error finding the feel
		phenny.say("404 Feel not Found")

	# Set channel and user timeout
	globals()[input.sender + "timeout"] = time() + 8
	globals()[input.nick + "nicktimeout"] = time() + 30

feel.commands = ['feels', 'feel', 'tfw']
feel.priority = 'low'

def refeel(phenny, input):
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
			# download feel from board=param1 chan=param2
			phenny.say("Loading feels from " + inputArray[1] + "/" + inputArray[0] + "/")
			globals()[inputArray[0] + inputArray[1] + "feels"] = get_feels(inputArray[0], inputArray[1])
		else:
			# download feel from board=param1 chan=4chan
			phenny.say("Loading feels from 4chan/" + inputArray[0] + "/")
			globals()[inputArray[0] + "4chanfeels"] = get_feels(inputArray[0])
	else:
		# download feel from board=r9k chan=4chan
		phenny.say("Loading feels from 4chan/r9k/")
		globals()["r9k4chanfeels"] = get_feels()

	# Re-feeling done, reset status
	globals()[refeeling] = False
refeel.commands = ['re-feel', 'refeel']
refeel.priority = 'low'
