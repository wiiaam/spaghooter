import random

# NORMIES GET OUT
def rreee(phenny, input):
	phenny.say("4RRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
rreee.commands = ['normiesgetout', 'rreee', 'normie', 'normy', 'normies', 'normys', 'betauprising']
rreee.priority = 'medium'

# 'PASTA'
def pasta(phenny, input):
	if input.admin == False: return

	phenny.say("3>  ## ##   ########     ###     ######  ########    ###    ")
	phenny.say("3>  ## ##   ##     ##   ## ##   ##    ##    ##      ## ##   ")
	phenny.say("3>######### ##     ##  ##   ##  ##          ##     ##   ##  ")
	phenny.say("3>  ## ##   ########  ##     ##  ######     ##    ##     ## ")
	phenny.say("3>######### ##        #########       ##    ##    ######### ")
	phenny.say("3>  ## ##   ##        ##     ## ##    ##    ##    ##     ## ")
	phenny.say("3>  ## ##   ##        ##     ##  ######     ##    ##     ## ")
	
	phenny.say("4~~~~-BEST CHANNEL EVER!!!-~~~~")
	phenny.say("4~~---BEST CHANNEL EVER!!!---~~")
	phenny.say("4-----BEST CHANNEL EVER!!!-----")

pasta.commands = ['pasta']
pasta.priority = 'medium'

# ULEH ULEH ULEH ULEH ULEH ULEH
def uleh(phenny, input):
	phenny.reply("4ULEH ULEH ULEH ULEH ULEH ULEH ULEH ULEH ULEH ULEH ULEH ULEH")
uleh.commands = ['uleh']
uleh.priority = 'medium'

# INTENSIFY
def intensify(phenny, input):
	try:
		phenny.say("4[ %s INTENSIFIES ]" % input.group(2).upper())
	except:
		phenny.say("4[ NONETYPE ERROR INTENSIFIES ]")

intensify.commands = ['intensify', 'int']
intensify.priority = 'medium'

# Join us now and share the software~
def freesoftware(phenny, input):
	phenny.reply('https://youtu.be/9sJUDx7iEJw')
freesoftware.commands = ['freesoftware']
freesoftware.priority = 'medium'

# #rekt
def rekt(phenny, input):
	rekt = ["#rekt", "REKT", "rekt", "REKTangle", "SHREKT", "REKT-it Ralph", "Total REKTall", "The Lord of the REKT", "The Usual SesREKTs", "North by NorthREKT", "REKT to the Future", "Once Upon a Time in the REKT", "The Good, the Bad, and the REKT", "LawREKT of Arabia", "Tyrannosaurus REKT", "eREKTile dysfunctio "]
	if input.group(2) > 0:
		phenny.say(input.group(2) + ": 4#" + random.choice(rekt))
	else:
		phenny.say("4#" + random.choice(rekt))
rekt.commands = ['rekt']
rekt.priority = 'medium'

# Tip fedora
def tip(phenny, input):
	msg = '\x01ACTION tips fedora :^)\x01'
	phenny.msg(input.sender, msg)
tip.commands = ['tip']
tip.priority = 'medium'

# give sauce
def sauce(phenny, input):
	phenny.reply('https://github.com/installgen2/spaghooter p-pls gib star ;-;')
sauce.commands = ['sauce', 'source', 'spaghooter', 'halp']
sauce.priority = 'medium'

# Be triggered
def trigger(phenny, input):
	phenny.reply('4TRIGGERED')
trigger.commands = ['trigger']
trigger.priority = 'medium'

# Interject for a moment
def interject(phenny, input):
	if input.group
	phenny.say("I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux.")
interject.commands = ['interject']
interject.priority = 'medium'
