#!/usr/bin/python3

import re


class Graph:

    def __init__(self):
        self._num_nodes = 0
        self._num_arcs = 0
        # List for storing node objects.
        self._nodes = []
        # List of lists for storing edge objects for each node.
        self._adjacency_lists = []

    def read_graph_from_file(self, file_name, directed):
        """ Read in graph from .graph file.

        Specification of .graph file format:
            First line: number of nodes
            Second line: number of arcs
            3-column lines with node information:
                node_id latitude longitude
            4-column lines with edge information:
                tail_node_id head_node_id distance(m) max_speed(km/h)
        Comment lines (^#) are ignored

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        c_lines = 0
        with open(file_name, 'rt') as f:
            for line in f:
                cols = line.strip().split(' ')
                # Skip comment lines.
                if re.search('^#', cols[0]):
                    continue
                c_lines += 1
                if c_lines == 1:
                    if self._num_nodes != 0:
                        raise Exception('Graph already read in')
                    self._num_nodes = int(cols[0])
                elif c_lines == 2:
                    self._num_arcs = int(cols[0])
                elif c_lines <= self._num_nodes + 2:  # all node info lines.
                    if not len(cols) == 3:
                        raise Exception('Node info line with != 3 cols')
                    node = Node(int(cols[0]), float(cols[1]), float(cols[2]))
                    # Append node to list.
                    self._nodes.append(node)
                    # Append empty adjacency list for node.
                    self._adjacency_lists.append([])
                else:  # all arc info lines.
                    if not len(cols) == 4:
                        raise Exception('Arc info line with != 4 cols')
                    tail_node_id = int(cols[0])
                    arc = Arc(tail_node_id, int(cols[1]), float(cols[2]),
                              int(cols[3]))

                    if int(cols[3]) == 0:
                        print(tail_node_id)

                    if not directed:  # Create undirected graph
                        self._adjacency_lists[arc.head_node_id].append(
                            Arc(arc.head_node_id, arc.tail_node_id,
                                arc.distance, arc.max_speed))

                    # Append arc to tail node's adjacency list.
                    self._adjacency_lists[tail_node_id].append(arc)
        f.closed

    def get_num_nodes(self):
        """Return number of nodes in graph."""
        return self._num_nodes

    def get_num_arcs(self):
        """Return number of arcs in graph."""
        return self._num_arcs

    def compute_reachable_nodes(self, node_id):
        """Mark all nodes reachable from given node.

        Implemented as breadth first search (BFS)
        Returns the number of reachable nodes (incl. start node)

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test2.graph', True)
        >>> graph.compute_reachable_nodes(0)
        4
        >>> graph.compute_reachable_nodes(4)
        6
        >>> graph.compute_reachable_nodes(6)
        1
        """
        # List of nodes to visit currently.
        current_level = [node_id]
        # Create list of marked nodes, marking reachable nodes with 1.
        marked_nodes = [0] * self._num_nodes
        marked_nodes[node_id] = 1  # Mark start node as reachable.
        num_marked_nodes = 1  # Store number of reachable nodes.
        # While there are still nodes to visit.
        while len(current_level) > 0:
            # Store nodes that are conntected to current_level nodes.
            next_level = []
            # Go through all current_level nodes.
            for curr_node_id in current_level:
                # Go through arcs of current node.
                for arc in self._adjacency_lists[curr_node_id]:
                    # If head_id not marked yet.
                    if not marked_nodes[arc.head_node_id]:
                        marked_nodes[arc.head_node_id] = 1
                        num_marked_nodes += 1
                        # Add head_id to new current level nodes.
                        next_level.append(arc.head_node_id)
            current_level = next_level
        return num_marked_nodes

    def set_arc_costs_to_travel_time(self, max_vehicle_speed):
        """Set arc costs to travel time in whole seconds.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph
        [0->1(4), 0->2(8), 1->2(2), 2->3(6), 3->1(5), 4->3(2)]
        """
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                # Compute max possible speed for this arc.
                max_speed = min(arc.max_speed, int(max_vehicle_speed))
                # Compute travel time in whole seconds.
                travel_time_sec = '%.0f' % (arc.distance / (max_speed / 3.6))
                # Set costs to travel time in whole seconds.
                arc.costs = int(travel_time_sec)

    def set_arc_costs_to_distance(self):
        """Set arc costs to distance.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph.set_arc_costs_to_distance()
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                arc.costs = arc.distance

    def compute_lcc(self, marked_nodes):
        """Mark all nodes in the largest connected component.
        TODO.
        """

    def compute_shortest_paths(self, start_node_id):
        """Compute the shortest paths for a given start node.

        Compute the shortest paths from the given start node
        using Dijkstra's algorithm.
        TODO.
        """

    def __repr__(self):
        """ Define object's string representation.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph', True)
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        obj_str_repr = ''
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                obj_str_repr += repr(arc) + ', '
        if obj_str_repr:
            return '[' + obj_str_repr[:-2] + ']'
        else:
            return '[]'


class Node:

    def __init__(self, node_id, latitude, longitude):
        self._id = node_id
        self._latitude = latitude
        self._longitude = longitude

    def __repr__(self):
        """Define object's string representation."""
        return '%i' % (self._id)


class Arc:

    def __init__(self, tail_id, head_id, distance, max_speed):
        self.tail_node_id = tail_id  # ID of tail node.
        self.head_node_id = head_id  # ID of head node.
        self.distance = distance  # Distance in meter.
        self.max_speed = max_speed  # Maximum speed.
        self.costs = distance  # Set default costs to distance.

    def __repr__(self):
        """ Define object's string representation."""
        return '%i->%i(%i)' % (self.tail_node_id, self.head_node_id,
                               self.costs)
