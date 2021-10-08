#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：viewmap -> networkx_map
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/7/17 15:23
@Desc   ：
==================================================
"""

import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g2 = nx.DiGraph()

g2.add_edges_from([
    ('运算法则（0.63）', '极限运算（0.61）'),
    ('重要极限（0.61）', '极限运算（0.61）'),
    ('函数连续性（0.61）', '极限运算（0.61）'),
    ('极限运算（0.61）', '函数求导（0.57）'),
    ('导数概念（0.58）', '函数求导（0.57）'),
    ('高阶导数（0.57）', '函数求导（0.57）'),
    ('微分（0.58）', '函数求导（0.57）'),
    ('函数求导（0.57）', '不定积分（0.56）'),
    ('不定积分性质（0.56）', '不定积分（0.56）'),
    ('不定积分公式（0.56）', '不定积分（0.56）'),
    ('常用积分方法（0.56）', '不定积分（0.56）'),
    ('不定积分（0.56）', '定积分（0.54）'),
    ('定积分定义（0.55）', '定积分（0.54）'),
    ('定积分性质（0.54）', '定积分（0.54）'),
    ('定积分应用（0.55）', '定积分（0.54）'),
])

g.add_edges_from([
    ('函数关系（0.86）', '函数(0.86)'),
    ('初等函数（0.86）', '函数(0.86)'),
    ('集合（0.87）', '函数(0.86)'),
    ('函数(0.86)', '极限(0.87)'),
    ('重要极限(0.87)', '极限(0.87)'),
    ('函数连续性(0.87)', '极限(0.87)'),
    ('极限(0.87)', '函数求导（0.85）'),
    ('导数概念(0.86)', '函数求导（0.85）'),
    ('导数运算法则(0.89)', '函数求导（0.85）'),
    ('高阶导数(0.87)', '函数求导（0.85）'),
    ('微分(0.88)', '函数求导（0.85）'),
    ('中值定理(0.81)', '函数求导（0.85）'),
    ('函数单调性(0.81)', '函数求导（0.85）'),
    ('函数求导（0.85）', '不定积分（0.88）'),
    ('不定积分公式（0.86）', '不定积分（0.88）'),
    ('不定积分（0.88）', '定积分（0.88）'),
    ('定积分定义（0.89）', '定积分（0.88）'),
    ('定积分性质（0.91）', '定积分（0.88）'),
    ('定积分应用（0.87）', '定积分（0.88）'),
])

for n in list(g2.nodes):
    if n in ['极限运算（0.61）', '函数求导（0.57）', '不定积分（0.56）', '定积分（0.54）']:
        g2.nodes[n]['color'] = '#336699'
        g2.nodes[n]['size'] = 800
    else:
        g2.nodes[n]['color'] = '#cccccc'
        g2.nodes[n]['size'] = 400

for n in list(g.nodes):
    if n in ['函数(0.86)', '极限(0.87)', '函数求导（0.85）', '不定积分（0.88）', '定积分（0.88）']:
        g.nodes[n]['color'] = '#336699'
        g.nodes[n]['size'] = 800
    else:
        g.nodes[n]['color'] = '#cccccc'
        g.nodes[n]['size'] = 400

node_colors2 = []
node_sizes2 = []
node_colors2 = nx.get_node_attributes(g2, 'color').values()
node_sizes2 = list(nx.get_node_attributes(g2, 'size').values())

node_colors = []
node_sizes = []
node_colors = nx.get_node_attributes(g, 'color').values()
node_sizes = list(nx.get_node_attributes(g, 'size').values())
# print(type(node_sizes))
plt.figure(figsize=(10, 5))
plt.rcParams['font.sans-serif'] = ['YouYuan']
img1 = plt.subplot(121)
img1.set_title(u'主观题', y=-0.1)
pos = nx.spring_layout(g)
nx.draw(g, pos, font_size=10, with_labels=False, node_color=node_colors, node_size=node_sizes)
for p in pos:  # raise text positions
    pos[p][1] -= 0.15
nx.draw_networkx_labels(g, pos, font_size=8, font_family='YouYuan')

img2 = plt.subplot(122)
img2.set_title(u'客观题', y=-0.1)
pos2 = nx.spring_layout(g2)
nx.draw(g2, pos2, font_size=10, with_labels=False, node_color=node_colors2, node_size=node_sizes2)
for p in pos2:  # raise text positions
    pos2[p][1] -= 0.15
nx.draw_networkx_labels(g2, pos2, font_size=8, font_family='YouYuan')
plt.show()