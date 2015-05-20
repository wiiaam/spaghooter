# Join and leave channels
def sjoin(phenny, input):
		if "," in input.group(2):
			phenny.say('no')
			return
		if "#" in input.group(2):
			phenny.write(['JOIN'], input.group(2))
		else:
			phenny.write(['JOIN'], '#' + input.group(2))
def sleave(phenny, input):
	if input.admin:
		if input.group(2):
			if "#" in input.group(2):
				phenny.write(['PART'], input.group(2))
			else:
				phenny.write(['PART'], '#' + input.group(2))
		else:
			phenny.write(['PART'], input.sender)
sjoin.commands = ['sjoin']
sjoin.priority = 'medium'
sleave.commands = ['sleave']
sleave.priority = 'medium'