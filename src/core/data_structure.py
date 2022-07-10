from importlib.resources import contents


class Channel():
    def __init__(self, id, origin, to, weight):
        self.id = id
        self.origin = origin
        self.to = to
        self.weight = weight

    def __str__(self):
        return f'Channel({self.id}, origin:{self.origin}, to:{self.to}, weight:{self.weight})'



class Host():
    def __init__(self, id, virus):
        self.id = id
        self.virus = virus

    def __str__(self):
        return f'Host({self.id}, virus:{self.virus})'

    def setVirus(self, virus):
        self.virus = virus


class Instruction():
    def __init__(self, id, first, condition, second, channels):
        self.id = id
        #options: 'INSTRUCTION', 'stop'
        self.first = first
        self.condition = condition
        self.second = second
        self.channels = channels

    def __str__(self):
        return f'Instruction({self.id}, condition:{self.first + " " + self.condition + " " + self.second})'


class Controller():
    def __init__(self, instruction, channel):
        self.instruction = instruction
        self.channel = channel

    def __str__(self):
        return f'Controller(instruction:{self.instruction}, channel:{self.channel})'