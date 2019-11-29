import networkx as nx
G_fb = nx.read_weighted_edgelist('output_departed.csv',delimiter=',', create_using = nx.Graph(), nodetype=str)
print(nx.info(G_fb))

import matplotlib.pyplot as plt

pos = nx.spring_layout(G_fb)
betCent = nx.betweenness_centrality(G_fb, normalized=True, endpoints=True)
node_color = [20000.0 * G_fb.degree(v) for v in G_fb]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G_fb, pos=pos, with_labels=True,
                 node_color=node_color,font_size=8,
                 node_size=node_size )
fig1 = plt.gcf()
plt.axis('off')
plt.show()
fig1.savefig('Departed_2.png')

import community
parts = community.best_partition(G_fb)
values = [parts.get(node) for node in G_fb.nodes()]
plt.axis("off")
plt.figure(figsize=(20,20))
nx.draw_networkx_labels(G_fb, pos, font_size=2, alpha=0.8)
nx.draw_networkx(G_fb, pos = pos,cmap=plt.cm.RdYlBu, node_color = values, node_size =600, with_labels = True,font_size=7)
nx.draw_networkx_edges(G_fb, pos, alpha=0.3)
fig2 = plt.gcf()
plt.show()
fig2.savefig('Departed_communities_2.png')