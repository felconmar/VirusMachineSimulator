from core.data_structure import *
#from core.condition_dictionary import *
import random
import logging
import jsonpickle


class Problem():
    def __init__(self, hosts, instructions, channels, ):
        self.hosts = hosts
        self.channels = channels
        self.instructions = instructions

    def get_hosts(self):
        return self.hosts

    def get_channels(self):
        return self.channels

    def get_instructions(self):
        return self.instructions

    def virus_in_environment(self):
        return self.hosts["h0"].virus

    #TODO
    def json_dump(self):
        return 0 #jsonpickle.encode(self.__dict__)
    #TODO
    def json_decode(json_pickle):
        return 0

    virus_transmission = 1

    #Condition dictionary

    def follow_process_not_empty(self, instruction):
        first_host = self.hosts[instruction.first]
        return True if first_host.virus > 0 else False
        
    def follow_process_empty(self, instruction):
        first_host = self.hosts[instruction.first]
        return True if first_host.virus == 0 else False

    def follow_bigger_than(self, instruction):
        first_host = self.hosts[instruction.first]
        second_host = self.hosts[instruction.second]
        return True if first_host.virus > second_host.virus else False

    def follow_smaller_than(self, instruction):
        first_host = self.hosts[instruction.first]
        second_host = self.hosts[instruction.second]
        return True if first_host.virus < second_host.virus else False

    def follow_process_equals(self, instruction):
        first_host = self.hosts[instruction.first]
        second_host = self.hosts[instruction.second]
        return True if first_host.virus == second_host.virus else False

    def follow_process_not_equals(self, instruction):
        first_host = self.hosts[instruction.first]
        second_host = self.hosts[instruction.second]
        return True if first_host.virus != second_host.virus else False

    instruction_function_dict = \
    {'not empty' : follow_process_not_empty,
    'empty' : follow_process_empty,
    'bigger than' : follow_bigger_than,
    'smaller than' : follow_smaller_than,
    'equals' : follow_process_equals,                     
    'not equals' : follow_process_not_equals,
    }

    
    def run(self):
        return self.run_recursive("i1")

    
    def run_recursive(self, instruction_id):
        #Preparar la condición de la instrucción
        instruction = self.instructions[instruction_id]
        condition = instruction.condition
        if condition == "stop":
            return self
        else:    
            #Preparar los canales posibles de la instrucción
            #channels = list(filter(lambda channel: channel.origin == instruction_id, self.channels))
            channels_sorted = [v for k, v in self.channels.items() if v.origin == instruction_id]
            channels_sorted.sort(key=lambda channel: channel.weight, reverse=True)
            instr_channel_id = self.apply(instruction, channels_sorted)
            return self.run_recursive(instr_channel_id.to)

        
    def run_recursive_2(self, instruction_id):
        #Preparar la condición de la instrucción
        instruction = self.instructions[instruction_id]
        condition = instruction.condition
        if condition == "stop":
            return self
        else:
            #Preparar los canales posibles de la instrucción
            #channels = list(filter(lambda channel: channel.origin == instruction_id, self.channels))
            channels_sorted = [v for k, v in self.channels.items() if v.origin == instruction_id]
            channels_sorted.sort(key=lambda channel: channel.weight, reverse=True)
            instr_channel_id = self.apply_2(instruction, channels_sorted)
            return self.run_recursive_2(instr_channel_id.to)


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
    def apply(self, instruction, channels):
        #controllers = [c for c in self.controllers if c.instruction.id == instruction_id]
        hosts_channels = instruction.channels
        for h_ch in hosts_channels:
            h_channel = self.channels[h_ch]
            from_host = self.hosts[h_channel.origin]
            to_host = self.hosts[h_channel.to]
            try:
                run_method = self.instruction_function_dict[instruction.condition]
                if from_host.virus == 0:
                    return channels[len(channels)-1]
                elif run_method(self, instruction):
                    from_host.setVirus(from_host.virus-1)
                    channel_weight = h_channel.weight
                    to_host.setVirus(to_host.virus + (channel_weight * self.virus_transmission))
                return channels[0]
            except KeyError:
                print("Check the format of the instruction's condition -> " + instruction)

        else:
            return "ERROR"

    def apply_2(self, instruction, channels):
        try:        
            run_method = self.instruction_function_dict[instruction.condition]
            return run_method(self, instruction, channels)
        except KeyError:
            print("Check the format of the instruction's condition -> " + instruction)


            