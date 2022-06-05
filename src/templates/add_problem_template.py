from core import *

#Grupo de hosts
h0 = Host("h0", 0)
h1 = Host("h1", 5)
h2 = Host("h2", 5)

#Grupo de instrucciones
i1 = Instruction("i1", "h1 not empty")
i2 = Instruction("i2", "h2 not empty")
i3 = Instruction("i3", "stop")

#Grupo de canales
ch1 = Channel("ch1", "h1", "h0", 1)
ch2 = Channel("ch2", "h2", "h0", 1)
ch3 = Channel("ch3", "i1", "i1", 2)
ch4 = Channel("ch4", "i1", "i2", 1)
ch5 = Channel("ch5", "i2", "i2", 2)
ch6 = Channel("ch6", "i2", "i3", 1)

#Grupos de controladores
crt1 = Controller(i1, ch1)
crt2 = Controller(i2, ch2)

hosts = {"h1" : h1, "h2" : h2, "h0" : h0}
instructions = {"i1" : i1, "i2" : i2, "i3" : i3}
channels = {"ch1" : ch1, "ch2" : ch2, "ch3" : ch3, "ch4" : ch4, "ch5" : ch5, "ch6" : ch6}
controllers = [crt1, crt2]

#Carga del problema
pr1 = Problem(hosts, instructions, channels, controllers)
#Ejecución del problema
pr1.run()

print('\nSolution: ' ,pr1.virus_in_environment(), '\n')




