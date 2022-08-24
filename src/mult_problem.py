from core import *

#Grupo de hosts
h0 = Host("h0", 0)
h1 = Host("h1", 5)
h2 = Host("h2", 5)
h3 = Host("h3", 0)
h4 = Host("h4", 0)


#Grupo de instrucciones
i1 = Instruction("i1", "h2", "not empty", "-", ["e1"])
i2 = Instruction("i2", "h1", "not empty", "-", ["e2"])
i3 = Instruction("i3", "h3", "not empty", "-", ["e3"])
i4 = Instruction("i4", "h3", "not empty", "-", ["e4"])
i5 = Instruction("i5", "-", "stop", "-",[])

#Grupo de canales (hosts)
e1 = Edge("e1", "h2", "h4", 1)
e2 = Edge("e2", "h1", "h3", 2)
e3 = Edge("e3", "h3", "h1", 1)
e4 = Edge("e4", "h3", "h0", 1)

#Grupo de canales (Instrucciones) 
e5  = Edge("e5", "i1", "i2", 2)
e6  = Edge("e6", "i1", "i5", 1)
e7  = Edge("e7", "i2", "i2", 2)
e8  = Edge("e8", "i2", "i3", 1)
e9  = Edge("e9", "i3", "i4", 2)
e10 = Edge("e10", "i3", "i1", 1)
e11 = Edge("e11", "i4", "i3", 1)


hosts = {"h1" : h1, "h2" : h2, "h3" : h3, "h4" : h4, "h0" : h0}
instructions = {"i1" : i1, "i2" : i2, "i3" : i3,  "i4" : i4, "i5" : i5}
edges = {"e1" : e1, "e2" : e2, "e3" : e3, "e4" : e4, "e5" : e5, "e6" : e6, "e7" : e7, "e8" : e8, "e9" : e9, "e10" : e10, "e11" : e11}



#Carga del problema
pr = Problem(hosts, instructions, edges)
#Ejecución del problema
pr.run_iterative()
print('\nSolution: ' ,pr.virus_in_environment(), '\n')


mult_json = open("src/json/in/mult_245_374.json")
pr = Problem.json_decode_f(mult_json)
pr.run_iterative()
print('\nSolution: ' ,pr.virus_in_environment(), '\n')
