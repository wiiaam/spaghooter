# Intros
# by wiiam

def joinintro(phenny, input):
    phenny.say(read(input.nick))
joinintro.event = 'JOIN'
joinintro.rule = r'.*'


def sintro(phenny, input):
    introsplit = input.group(2).split(' ')
    if introsplit[0] == "set":
        introtoadd = ""
        for i in range(1, len(introsplit)):
            introtoadd += introsplit[1]
        phenny.say("\"" + introtoadd + "\" set as intro")
        write(input.nick, introtoadd)
    if introsplit[0] == "del":
        if delete(input.nick) is True:
            phenny.say("Your intro has been deleted")
        else:
            phenny.say("You didn't have an intro")
sintro.commands = ['sintro']
sintro.priority = 'medium'


def read(nick):
    f = open('intros', 'r')
    lines = f.readlines()
    intro = " "
    for i in range(0, len(lines), 2):
        if lines[i] == nick + "\n":
            intro = lines[i+1]

    f.close()
    if intro.endswith("\n"):
        intro = intro[:-1]
    return intro


def write(nick, intro):
    f = open('intros', 'r')
    list = f.readlines()
    foundnick = False
    f = open('intros', 'w+')

    for i in range(0, len(list), 2):
        if list[i] == nick + "\n":
            list[i+1] = intro + "\n"
            foundnick = True
            break
    if foundnick is False:
        list += [nick + "\n"]
        list += [intro + "\n"]
    for i in range(len(list)):
        f.write(list.pop(0))

def delete(nick):
    f = open('intros', 'r')
    list = f.readlines()
    foundnick = False
    f = open('intros', 'w+')
    for i in range(len(list)):
        if list[i] == nick + "\n":
            foundnick = True
            list.pop(i)
            list.pop(i)
            break

    for i in range(len(list)):
        f.write(list.pop(0))

    return foundnick
