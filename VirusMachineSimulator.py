from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from src.core.problem_scheme import *
import matplotlib.pyplot as plt
import networkx as nx
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivy  #https://stackoverflow.com/questions/54758416/how-to-fix-modulenotfounderror-kivy-garden-matplotlib-backend-kivyagg
from kivy.uix.image import Image
import ntpath

class Window(GridLayout):
    pass

class Machine(GridLayout):
    PATH = StringProperty('')
    def run(self):
        try:
            json = open(self.PATH)
            pr = Problem.json_decode_f(json)
            pr.run_iterative()
            virus = pr.virus_in_environment()
            self.ids.solution.text = str(virus)
        except:
            self.ids.solution.text = "ERROR"
    
    def selected(self, filename):
        self.ids.graph.clear_widgets()
        try:
            #Json path
            self.PATH = filename[0]
            self.ids.filepath.text = ntpath.basename(filename[0])
            plt.close()
            #Graph design
            g = nx.MultiDiGraph()
            #content
            graph_json = json.load(open(filename[0]))
            options = {"edgecolors": "tab:gray", "node_size": 400}
            #nodes
            hosts_array = [h_str["id"] for h_str in graph_json["hosts"].values()]
            g.add_nodes_from(hosts_array)
            instructions_array = [i_str["id"] for i_str in graph_json["instructions"].values()]
            g.add_nodes_from(instructions_array)
            #edges
            controllers_array = [(i_str["id"], edge) for i_str in graph_json["instructions"].values() for edge in i_str["edges"]]
            controller_edges = [controller[1] for controller in controllers_array]
            for edge in controllers_array: g.add_edge(edge[0], edge[1], weight=1, minlen=5)

            edges_aux = [(c_str["id"], c_str["origin"], c_str["to"], int(c_str["weight"])) for c_str in graph_json["edges"].values()]
            for edge in edges_aux:
                if edge[0] in controller_edges:
                    g.add_edge(edge[1], edge[0], weight=edge[3], minlen=5)
                    g.add_edge(edge[0], edge[2], weight=1, minlen=5)
                else:    
                    g.add_edge(edge[1], edge[2], weight=edge[3], minlen=5)

            #nx.draw_networkx_edges(g, pos, edgelist=edges_aux, arrows=True)
            pos = nx.nx_pydot.graphviz_layout(g, prog='neato')   #‘dot’, ‘twopi’, ‘fdp’, ‘sfdp’, ‘circo’
            nx.draw(g, pos, with_labels= True)
            nx.draw_networkx_nodes(g, pos, nodelist=hosts_array, node_shape="s", node_color="#b2ffff", **options)
            nx.draw_networkx_nodes(g, pos, nodelist=instructions_array, node_color="red", **options)
            nx.draw_networkx_nodes(g, pos, nodelist=controller_edges, node_color="white", node_size=350, label="")
            nx.draw_networkx_edges(g, pos, edgelist=g.edges(), arrows=True)
            #labels = {e: g.edges[e]['weight'] for e in g.edges}
            #nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, verticalalignment="bottom")
            plt.figure(1, figsize=(20,20))
            self.ids.graph.add_widget(FigureCanvasKivy(plt.gcf()))

        except:
            self.ids.graph.add_widget(Image(source ="src/resources/sorry.png"))

class VirusMachineSimulator(App):
    def build(self):
        return Window()



if __name__ == "__main__":
    window = VirusMachineSimulator()
    window.run()
