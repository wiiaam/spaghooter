import random
from time import time

# NORMIES GET OUT
def rreee(phenny, input):
	phenny.say("4RRRRRRREEEEEEEEEEEEEEEEEEEEEEE")
rreee.commands = ['normiesgetout', 'rreee', 'pepe']
rreee.priority = 'medium'

# ULEH ULEH ULEH ULEH ULEH ULEH
def uleh(phenny, input):
	phenny.say("4ULEH ULEH ULEH ULEH ULEH ULEH ")
uleh.commands = ['uleh']
uleh.priority = 'medium'

# INTENSIFY
def intensify(phenny, input):
	try:
		phenny.say("4[%s INTENSIFIES]" % input.group(2).upper())
	except:
		phenny.say("4[NONETYPE ERROR INTENSIFIES]")

intensify.commands = ['intensify', 'int']
intensify.priority = 'medium'

# Join us now and share the software~
def freesoftware(phenny, input):
	phenny.reply('https://youtu.be/9sJUDx7iEJw')
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
def sauce(phenny, input):
	phenny.reply('https://github.com/installgen2/spaghooter p-pls gib star ;-;')
sauce.commands = ['sauce']
sauce.priority = 'medium'

# Be triggered
def trigger(phenny, input):
	phenny.say('TRIGGERED')
trigger.commands = ['trigger']
trigger.priority = 'medium'

# Interject for a moment
def interject(phenny, input):
	phenny.say("I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux.")
interject.commands = ['interject']
interject.priority = 'medium'
