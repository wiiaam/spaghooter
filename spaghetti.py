import random
from time import time

def spaghetti(phenny, input):
	# Cancel if timeout hasn't ended yet and ignore exceptions
	if input.admin == False:
		try:
			if time() < globals().get(input.sender + "timeout") or time() < globals().get(input.nick + "nicktimeout"): return
		except: pass

	spaghetti = ["... mom's spaghetti ...",
	"His palms spaghetti,",
	"knees weak, arms spaghetti",
	"There's vomit on his sweater spaghetti Mom's spaghetti",
	"He's nervous, but on the surface he looks calm spaghetti to drop bombs",
	"but he keeps on spaghetti what he wrote down",
	"The whole crowd goes spaghetti",
	"He opens his mouth, but spaghetti won't come out",
	"Spaghetti's run out",
	"Snap back to spaghetti",
	"Oh - there goes spaghetti",
	"Oh - there goes spaghetti Blaugh!",
	"He's so mad, but he won't give up spaghetti",
	"He knows he keeps on forgetting that mom's spaghetti's dope",
	"He knows when he goes back to his mom's spaghetti",
	"This whole spaghetti better go capture spaghetti and hope it don't pass him",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"Mom's spaghetti's mine for the taking",
	"Make me spaghetti as we move toward a new world order",
	"but mom's spaghetti's close to post mortem",
	"Spaghetti grows hotter He vomits all over",
	"Spaghetti's all on him Coast-to-coast shows",
	"He goes home and barely knows his own mom's spaghetti",
	"There's vomit on his mom's spaghetti",
	"These hoes don't want him no more He's cold spaghetti",
	"It unfolds I suppose it's old spaghetti",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"No more games I'mma change what you call spaghetti",
	"Tear this motherfuckin' roof off like two mom's spaghettis",
	"Spaghetti chewed up and spit out, and there's vomit on his sweater",
	"that I keep on forgetting to make spaghetti",
	"And provide the right type of spaghetti for my family",
	"'Cause man these god damn food stamps don't buy spaghetti",
	"And there's no movie There's no mom's spaghetti",
	"Mom's spaghetti He's nervous - blaugh!",
	"I'm like a mom, I've got to formulate spaghetti",
	"Spaghetti is my only motherfuckin' option Vomit's not",
	"This may be the only mom's spaghetti that I got",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"You better lose yourself in ya mom's spaghetti",
	"You only get one spaghetti",
	"'Cause spaghetti comes once in a lifetime, yo",
	"Mom's spaghetti can do anything, man"]

	# Set channel and user timeout
	globals()[input.sender + "timeout"] = time() + 8
	globals()[input.nick + "nicktimeout"] = time() + 30

spaghetti.commands = ['spaghetti']
spaghetti.priority = 'medium'
