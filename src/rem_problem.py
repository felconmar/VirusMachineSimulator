from core import *


#Grupo de hosts
h0 = Host("h0", 0)
h1 = Host("h1", 22)
h2 = Host("h2", 5)
h3 = Host("h3", 0)
h4 = Host("h4", 0)
h5 = Host("h5", 0)


#Grupo de instrucciones
i1 = Instruction("i1", "h2", "not empty", "-", ["e1"])
i2 = Instruction("i2", "h1", "not empty", "-", ["e2"])
i3 = Instruction("i3", "h4", "not empty", "-", ["e3"])
i4 = Instruction("i4", "h3", "not empty", "-", ["e4"])
i5 = Instruction("i5", "h3", "not empty", "-", ["e5"])
i6 = Instruction("i6", "-", "stop", "-",[])

#Grupo de canales (hosts)
e1 = Edge("e1", "h2", "h4", 1)
e2 = Edge("e2", "h1", "h3", 1)
e3 = Edge("e3", "h4", "h2", 1)
e4 = Edge("e4", "h3", "h5", 1)
e5 = Edge("e5", "h3", "h0", 1)

#Grupo de canales (Instrucciones) 
e6  = Edge("e6", "i1", "i2", 2)
e7  = Edge("e7", "i1", "i3", 1)
e8  = Edge("e8", "i2", "i1", 2)
e9  = Edge("e9", "i2", "i5", 1)
e10 = Edge("e10", "i3", "i3", 2)
e11 = Edge("e11", "i3", "i4", 1)
e12 = Edge("e12", "i4", "i4", 2)
e13 = Edge("e13", "i4", "i1", 1)
e14 = Edge("e14", "i5", "i5", 2)
e15 = Edge("e15", "i5", "i6", 1)



hosts = {"h1" : h1, "h2" : h2, "h3" : h3, "h4" : h4, "h5" : h5, "h0" : h0}
instructions = {"i1" : i1, "i2" : i2, "i3" : i3,  "i4" : i4, "i5" : i5, "i6" : i6}
edges = {"e1" : e1, "e2" : e2, "e3" : e3, "e4" : e4, "e5" : e5, "e6" : e6, "e7" : e7, "e8" : e8, "e9" : e9, "e10" : e10, "e11" : e11, "e12" : e12, "e13" : e13, "e14" : e14, "e15" : e15}



#Carga del problema
pr = Problem(hosts, instructions, edges)
#Ejecución del problema
pr.run()
print('\nSolution: ' ,pr.virus_in_environment(), '\n')
