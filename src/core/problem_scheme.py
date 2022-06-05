from core.data_structure import *


class Problem():
    def __init__(self, hosts, instructions, channels, controllers, ):
        self.hosts = hosts
        self.channels = channels
        self.instructions = instructions
        self.controllers = controllers

    def get_hosts(self):
        return self.hosts

    def get_channels(self):
        return self.channels

    def get_instructions(self):
        return self.instructions

    def get_controllers(self):
        return self.controllers

    def virus_in_environment(self):
        return self.hosts["h0"].virus

    def run(self):
        return self.run_recursive("i1")

    
    def run_recursive(self, instruction_id):
        #Preparar la condición de la instrucción
        instruction = self.instructions[instruction_id]
        condition = instruction.condition
        condition_list = condition.split(" ")
        #Preparar los canales posibles de la instrucción
        #channels = list(filter(lambda channel: channel.origin == instruction_id, self.channels))
        channels_sorted = [v for k, v in self.channels.items() if v.origin == instruction_id]
        channels_sorted.sort(key=lambda channel: channel.weight, reverse=True)
        if condition_list[0] == "stop":
            return self
        else:
            instr_channel_id = self.apply(condition_list, channels_sorted)
            return self.run_recursive(instr_channel_id.to)


    '''
    -not empty
	-empty
	-bigger than n
	-smaller than
	-equals
	-not equals
    --------------------
    -divisibilidad (%)
    '''
    def apply(self, condition_list, channels):
        #controllers = [c for c in self.controllers if c.instruction.id == instruction_id]
        if condition_list[1] == "not" and condition_list[2] == "empty":
            main_host = self.hosts[condition_list[0]]
            if main_host.virus == 0:
                return channels[len(channels)-1]
            elif main_host.virus > 0:
                main_channels_to = [v for k, v in self.channels.items() if v.origin == main_host.id]
                main_host.setVirus(main_host.virus-1)
                channel_weight = main_channels_to[0].weight
                to_host = [v for k, v in self.hosts.items() if v.id == main_channels_to[0].to] 
                to_host[0].setVirus(to_host[0].virus + (channel_weight * 1))
                return channels[0]
            else:
                return "ERROR"

        





        

