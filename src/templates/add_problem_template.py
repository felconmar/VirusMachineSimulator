from src.core.problem_scheme import *
import json
import jsonpickle

from core import problem_scheme

#Grupo de hosts
h0 = Host("h0", 0)
h1 = Host("h1", 5)
h2 = Host("h2", 5)

#Grupo de instrucciones
i1 = Instruction("i1", "h1", "not empty", "-", ["ch1"])
i2 = Instruction("i2", "h2", "not empty", "-", ["ch2"])
i3 = Instruction("i3", "-", "stop", "-",[])

#Grupo de aristas
ch1 = Edge("ch1", "h1", "h0", 1)
ch2 = Edge("ch2", "h2", "h0", 1)
ch3 = Edge("ch3", "i1", "i1", 2)
ch4 = Edge("ch4", "i1", "i2", 1)
ch5 = Edge("ch5", "i2", "i2", 2)
ch6 = Edge("ch6", "i2", "i3", 1)


hosts = {"h1" : h1, "h2" : h2, "h0" : h0}
instructions = {"i1" : i1, "i2" : i2, "i3" : i3}
edges = {"ch1" : ch1, "ch2" : ch2, "ch3" : ch3, "ch4" : ch4, "ch5" : ch5, "ch6" : ch6}


#Carga del problema
pr1 = Problem(hosts, instructions, edges)
#Ejecución del problema
pr1.run_iterative()
print('\nSolution: ' ,pr1.virus_in_environment(), '\n')

pr1_encode = pr1.json_dump()
print("JSON dump\n", pr1_encode)

#pr1_copy = Problem.json_decode(pr1_encode)
#pr1_copy.run()
#print(pr1_copy.virus_in_environment())

#add_json = open("src/json/in/add.json")
#pr1_f_copy = Problem.json_decode_f(add_json)
#pr1_f_copy.run()
#print(pr1_f_copy.virus_in_environment())
