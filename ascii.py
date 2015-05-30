from pyfiglet import Figlet

def banner(phenny, input):
	if len(input.group(2)) > 70:
		phenny.reply("pls... 2long4me")
		return

	bannedfonts = [
		"acrobatic",
		"calgphy",
		"calgphy2",
		"doh",
		"poison",
		"univers",
		"term",
		"hollywood",
		"dotmatrix"
	]

	inputArray = input.group(2).split(', ')

	if inputArray[0][0] == "":
		text = inputArray[0][2:]
	else:
		text = inputArray[0]

	if len(inputArray) > 1:
		if inputArray[1] in bannedfonts
			if
			phenny.say("ayy m80 %s is a banned font k?" % inputArray[1])
			return

		try:
			f = Figlet(font=inputArray[1])
			shit = f.renderText(text).split('\n')
		except:
			phenny.say("there's no font called %s" % inputArray[1])
			return
	else:
		f = Figlet(font="twopoint")
		shit = f.renderText(text).split('\n')

	for i in xrange(0,len(shit)):
		if inputArray[0][0] == "":
			phenny.say("" + inputArray[0][1] + shit[i])
		else:
			phenny.say(shit[i])

banner.commands = ['banner', 'bigtext']
banner.priority = 'medium'
