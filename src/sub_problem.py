from core import *


#Grupo de hosts
h0 = Host("h0", 0)
h1 = Host("h1", 11)
h2 = Host("h2", 5)
h3 = Host("h3", 0)

#Grupo de instrucciones
i1 = Instruction("i1", "h2", "not empty", "-", ["e1"])
i2 = Instruction("i2", "h1", "not empty", "-", ["e2"])
i3 = Instruction("i3", "h1", "not empty", "-", ["e3"])
i4 = Instruction("i4", "-", "stop", "-",[])

#Grupo de canales (hosts)
e1 = Edge("e1", "h2", "h3", 1)
e2 = Edge("e2", "h1", "h3", 1)
e3 = Edge("e3", "h1", "h0", 1)

#Grupo de canales (Instrucciones)
e4 = Edge("e4", "i1", "i2", 2)
e5 = Edge("e5", "i1", "i3", 1)
e6 = Edge("e6", "i2", "i1", 2)
e7 = Edge("e7", "i2", "i4", 1)
e8 = Edge("e8", "i3", "i3", 2)
e9 = Edge("e9", "i3", "i4", 1)


hosts = {"h1" : h1, "h2" : h2, "h3" : h3, "h0" : h0}
instructions = {"i1" : i1, "i2" : i2, "i3" : i3, "i4" : i4}
edges = {"e1" : e1, "e2" : e2, "e3" : e3, "e4" : e4, "e5" : e5, "e6" : e6, "e7" : e7, "e8" : e8, "e9" : e9}



#Carga del problema
pr = Problem(hosts, instructions, edges)
#Ejecución del problema
pr.run()
print('\nSolution: ' ,pr.virus_in_environment(), '\n')

