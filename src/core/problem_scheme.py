from data_structure import *
#from core.condition_dictionary import *
import random
import logging
import jsonpickle
import json



class Problem():
    def __init__(self, hosts, instructions, edges, ):
        self.hosts = hosts
        self.edges = edges
        self.instructions = instructions

    def get_hosts(self):
        return self.hosts

    def get_edges(self):
        return self.edges

    def get_instructions(self):
        return self.instructions

    def virus_in_environment(self):
        return self.hosts["h0"].virus

    def json_dump(self):
        return jsonpickle.dumps(self.__dict__)
        
    #Used for loading from string
    def json_decode(pr_json):
        pr_json_aux = json.loads(pr_json)
        hosts_aux = {h_str["id"]:Host(h_str["id"], int(h_str["virus"])) \
            for h_str in pr_json_aux["hosts"].values()}
        instructions_aux = {i_str["id"]:Instruction(i_str["id"], i_str["first"], i_str["condition"], i_str["second"], i_str["edges"]) \
            for i_str in pr_json_aux["instructions"].values()}
        edges_aux = {c_str["id"]:Edge(c_str["id"], c_str["origin"], c_str["to"], int(c_str["weight"])) \
            for c_str in pr_json_aux["edges"].values()}
        return Problem(hosts_aux, instructions_aux, edges_aux)

    #Used for loading from file
    def json_decode_f(pr_json):
        pr_json_aux = json.load(pr_json)
        hosts_aux = {h_str["id"]:Host(h_str["id"], int(h_str["virus"])) \
            for h_str in pr_json_aux["hosts"].values()}
        instructions_aux = {i_str["id"]:Instruction(i_str["id"], i_str["first"], i_str["condition"], i_str["second"], \
            i_str["edges"]) for i_str in pr_json_aux["instructions"].values()}
        edges_aux = {c_str["id"]:Edge(c_str["id"], c_str["origin"], c_str["to"], int(c_str["weight"])) \
            for c_str in pr_json_aux["edges"].values()}
        return Problem(hosts_aux, instructions_aux, edges_aux)

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
    
    def run_iterative(self):
        instruction = self.instructions["i1"]
        while(instruction.condition != "stop"):
            edges_sorted = [v for k, v in self.edges.items() if v.origin == instruction.id]
            edges_sorted.sort(key=lambda edge: edge.weight, reverse=True)
            instr_edge_id = self.apply(instruction, edges_sorted)
            instruction = self.instructions[instr_edge_id.to]    
        return self
    
    def run_R(self):
        return self.run_recursive("i1")

    
    def run_recursive(self, instruction_id):
        #Preparar la condición de la instrucción
        instruction = self.instructions[instruction_id]
        condition = instruction.condition
        if condition == "stop":
            return self
        else:    
            #Preparar los canales posibles de la instrucción
            #edges = list(filter(lambda edge: edge.origin == instruction_id, self.edges))
            edges_sorted = [v for k, v in self.edges.items() if v.origin == instruction_id]
            edges_sorted.sort(key=lambda edge: edge.weight, reverse=True)
            instr_edge_id = self.apply(instruction, edges_sorted)
            return self.run_recursive(instr_edge_id.to)

        
    def run_recursive_2(self, instruction_id):
        #Preparar la condición de la instrucción
        instruction = self.instructions[instruction_id]
        condition = instruction.condition
        if condition == "stop":
            return self
        else:
            #Preparar los canales posibles de la instrucción
            #edges = list(filter(lambda edge: edge.origin == instruction_id, self.edges))
            edges_sorted = [v for k, v in self.edges.items() if v.origin == instruction_id]
            edges_sorted.sort(key=lambda edge: edge.weight, reverse=True)
            instr_edge_id = self.apply_2(instruction, edges_sorted)
            return self.run_recursive_2(instr_edge_id.to)


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
    def apply(self, instruction, edges):
        #controllers = [c for c in self.controllers if c.instruction.id == instruction_id]
        hosts_edges = instruction.edges
        for h_ch in hosts_edges:
            h_edge = self.edges[h_ch]
            from_host = self.hosts[h_edge.origin]
            to_host = self.hosts[h_edge.to]
            try:
                run_method = self.instruction_function_dict[instruction.condition]
                if from_host.virus == 0:
                    return edges[len(edges)-1]
                elif run_method(self, instruction):
                    from_host.setVirus(from_host.virus-1)
                    edge_weight = h_edge.weight
                    to_host.setVirus(to_host.virus + (edge_weight * self.virus_transmission))
                return edges[0]
            except KeyError:
                print("Check the format of the instruction's condition -> " + instruction)

        else:
            return "ERROR"

    def apply_2(self, instruction, edges):
        try:        
            run_method = self.instruction_function_dict[instruction.condition]
            return run_method(self, instruction, edges)
        except KeyError:
            print("Check the format of the instruction's condition -> " + instruction)


            