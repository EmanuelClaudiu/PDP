#!/usr/bin/python
import copy
from threading import Thread, Lock
import json

file = open('input.json')

GRAPH = json.load(file)
START_FROM = 1
ROADS = []

mutex = Lock()

class myThread (Thread):

    def __init__(self, node, road_so_far):
        Thread.__init__(self)
        mutex.acquire()
        for _node in GRAPH:
            if node == _node['node']:
                self.object = _node
                break
        mutex.release()
        self.node = self.object['node']
        self.children = self.object['goesInto']
        self.road_so_far = road_so_far

    def run(self):
        global ROADS
        if self.node in self.road_so_far:
            if self.road_so_far[0] == self.node and len(self.road_so_far) != 1:
                self.road_so_far.append(self.node)
                mutex.acquire()
                ROADS.append(self.road_so_far)
                mutex.release()
        if len(self.road_so_far) == 1 or self.node not in self.road_so_far:
            self.road_so_far.append(self.node)
            for child in self.children:
                r = copy.deepcopy(self.road_so_far)
                thread = myThread(child, r)
                thread.run()

thread = myThread(START_FROM, [])
thread.run()

print(ROADS)

file.close()