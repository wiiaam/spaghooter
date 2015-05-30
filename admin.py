# Join and leave channels
def sjoin(phenny, input):
		if "," in input.group(2):
			phenny.reply('no')
			return
		if "#" in input.group(2):
			phenny.write(['JOIN'], input.group(2))
		else:
			phenny.write(['JOIN'], '#' + input.group(2))
sjoin.commands = ['sjoin', 's-join']
sjoin.priority = 'medium'

def sleave(phenny, input):
	if input.admin:
		if input.group(2):
			if "#" in input.group(2):
				phenny.write(['PART'], input.group(2))
			else:
				phenny.write(['PART'], '#' + input.group(2))
		else:
			phenny.write(['PART'], input.sender)
sleave.commands = ['sleave', 'spart', 's-leave', 's-part']
sleave.priority = 'medium'

# Change nick
def snick(phenny, input):
	if input.admin:
		phenny.write(['NICK'], input.group(2))
snick.commands = ['snick', 's-nick']
snick.priority = 'medium'

# Allow admins to make spaghooter say shit
def msg(phenny, input):
	if input.admin:
		inputArray = input.group(2).split(', ')
		phenny.msg(inputArray[0], inputArray[1])
msg.commands = ['smsg', 's-msg', 'spaghetti-say', 's-say', 'ssay']
msg.priority = 'medium'