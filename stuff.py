import random
from time import time

# NORMIES GET OUT
def rreee(phenny, input):
	if input.admin:
		phenny.say("4RRRRRRREEEEEEEEEEEEEEEEEEEEEEE")
rreee.commands = ['normiesgetout', 'rreee', 'pepe']
rreee.priority = 'medium'

# ULEH ULEH ULEH ULEH ULEH ULEH
def uleh(phenny, input):
	if input.admin:
		phenny.say("4ULEH ULEH ULEH ULEH ULEH ULEH ")
uleh.commands = ['uleh']
uleh.priority = 'medium'

# INTENSIFY
def intensify(phenny, input):
	# Cancel if timeout hasn't ended yet and handle exceptions
	if input.admin == False:
		try:
			if time() < globals().get(input.sender + "timeout") or time() < globals().get(input.nick + "nicktimeout"): return
		except: pass

	# INTENSIFY
	try:
		phenny.say("4[%s INTENSIFIES]" % input.group(2).upper())
	except:
		phenny.say("4[NONETYPE ERROR INTENSIFIES]")

	if input.sender == "#/g/technology":
		globals()[input.sender + "timeout"] = time() + 240
		globals()[input.nick + "nicktimeout"] = time() + 240
	else:
		globals()[input.sender + "timeout"] = time() + 8
		globals()[input.nick + "nicktimeout"] = time() + 30
intensify.commands = ['intensify', 'int']
intensify.priority = 'medium'

# Join us now and share the software~
def freesoftware(phenny, input):
	phenny.say('https://youtu.be/9sJUDx7iEJw')
freesoftware.commands = ['freesoftware']
freesoftware.priority = 'medium'

# #rekt
def rekt(phenny, input):
	rekt = ["#rekt", "REKT", "#REKT", "rekt", "REKTangle", "SHREKT", "REKT-it Ralph", "Total REKTall", "The Lord of the REKT", "The Usual SesREKTs", "North by NorthREKT", "REKT to the Future", "Once Upon a Time in the REKT", "The Good, the Bad, and the REKT", "LawREKT of Arabia", "Tyrannosaurus REKT", "eREKTile dysfunctio "]
	phenny.say("4" + random.choice(rekt))
rekt.commands = ['rekt']
rekt.priority = 'medium'

# Tip fedora
def tip(phenny, input):
	msg = '\x01ACTION tips fedora :^)\x01'
	phenny.msg(input.sender, msg)
tip.commands = ['tip']
tip.priority = 'medium'

# Be triggered
def trigger(phenny, input):
	phenny.say('TRIGGERED')
trigger.commands = ['trigger']
trigger.priority = 'medium'

# Interject for a moment
def interject(phenny, input):
	if input.admin:
		phenny.say("I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux.")
interject.commands = ['interject']
interject.priority = 'medium'
