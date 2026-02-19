import networkx as nx

# -------------------------------
# 1) 200. Number of Islands
# -------------------------------
def lc200_num_islands(grid):
    """
    grid: List[List[str]] with '1' for land and '0' for water.
    Returns number of 4-connected land components.
    """
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    G = nx.grid_2d_graph(m, n)  # undirected 4-neighbor lattice
    land = {(r, c) for r in range(m) for c in range(n) if grid[r][c] == '1'}
    if not land:
        return 0
    H = G.subgraph(land)
    return nx.number_connected_components(H)


# -------------------------------
# 2) 547. Number of Provinces
# -------------------------------
def lc547_find_circle_num(isConnected):
    """
    isConnected: adjacency matrix (n x n), undirected.
    Returns number of connected components (provinces).
    """
    n = len(isConnected)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                G.add_edge(i, j)
    return nx.number_connected_components(G)


# -------------------------------
# 3) 695. Max Area of Island
# -------------------------------
def lc695_max_area_of_island(grid):
    """
    grid: List[List[int or str]] 1 for land, 0 for water.
    Returns size of the largest connected component of land.
    """
    ...


# -------------------------------
# 4) 1971. Find if Path Exists in Graph
# -------------------------------
def lc1971_valid_path(n, edges, source, destination):
    """
    n: number of nodes (0..n-1), edges: List[List[int]],
    returns True if path exists between source and destination.
    """
    ...


# -------------------------------
# 5) 207. Course Schedule (feasibility)
# -------------------------------
def lc207_can_finish(numCourses, prerequisites):
    """
    prerequisites: List[[a, b]] meaning b -> a
    Returns True if no cycle (i.e., DAG).
    """
    G = nx.DiGraph()
    G.add_nodes_from(range(numCourses))
    G.add_edges_from((b, a) for a, b in prerequisites)
    return nx.is_directed_acyclic_graph(G)


# -------------------------------
# 6) 210. Course Schedule II (order)
# -------------------------------
def lc210_find_order(numCourses, prerequisites):
    """
    Return a topological order (list), or [] if impossible.
    """
    ...


# -------------------------------
# 7) 1203. Sort Items by Groups Respecting Dependencies
# -------------------------------
def lc1203_sort_items(n, m, group, beforeItems):
    """
    n items (0..n-1), m groups (0..m-1), group[i] in [-1..m-1].
    beforeItems[i]: list of items that must come before i.
    Returns a valid order or [].
    Uses two DAGs: group-level and item-level, solved via topo sorts.
    """
    # Assign unique groups to ungrouped items
    next_group = m
    for i in range(n):
        if group[i] == -1:
            group[i] = next_group
            next_group += 1
    total_groups = next_group

    # Build item graph (all items)
    itemG = nx.DiGraph()
    itemG.add_nodes_from(range(n))

    # Build group graph (all groups)
    groupG = nx.DiGraph()
    groupG.add_nodes_from(range(total_groups))

    # Add edges; also add inter-group edges when dependency crosses groups
    for v in range(n):
        for u in beforeItems[v]:
            itemG.add_edge(u, v)
            if group[u] != group[v]:
                groupG.add_edge(group[u], group[v])

    # Topo sort on groups and items (check for cycles)
    if not nx.is_directed_acyclic_graph(itemG):
        return []
    if not nx.is_directed_acyclic_graph(groupG):
        return []

    item_order = list(nx.topological_sort(itemG))
    group_order = list(nx.topological_sort(groupG))

    # Bucket items by their group in item topological order
    items_in_group = {g: [] for g in group_order}
    for it in item_order:
        items_in_group[group[it]].append(it)

    # Emit groups in group order, expanding items per group
    answer = []
    for g in group_order:
        answer.extend(items_in_group.get(g, []))
    return answer


# -------------------------------
# 8) 684. Redundant Connection (undirected)
# -------------------------------
def lc684_find_redundant_connection(edges):
    """
    edges define a tree plus one extra edge; return the extra edge.
    We return the last edge that creates a cycle when processed in order.
    """
    ...


# -------------------------------
# 9) 685. Redundant Connection II (directed)
# -------------------------------
def lc685_find_redundant_directed_connection(edges):
    """
    Standard approach:
    - If some node has two parents (two incoming edges), try removing the later one;
      if DAG, that's the answer; else remove the earlier one.
    - Otherwise, remove the edge that participates in a directed cycle (pick the last such edge in input order).
    """
    ...


# -------------------------------
# 10) 2360. Longest Cycle in a Graph
# -------------------------------
def lc2360_longest_cycle(edges):
    """
    edges: List[int], edges[i] = j or -1; at most one outgoing edge per node i.
    Return the length of the longest directed cycle.
    """
    ...


# -------------------------------
# Quick sanity checks (comment out on submission)
# -------------------------------
if __name__ == "__main__":
    # lc200
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert lc200_num_islands(grid1) == 1
    assert lc200_num_islands(grid2) == 3

    # lc547
    mat = [[1,1,0],[1,1,0],[0,0,1]]
    assert lc547_find_circle_num(mat) == 2

    # lc695
    assert lc695_max_area_of_island([[0,0,0],[0,1,1],[0,1,0]]) == 3

    # lc1971
    assert lc1971_valid_path(3, [[0,1],[1,2],[2,0]], 0, 2) is True

    # lc207 / lc210
    pre = [[1,0],[2,0],[3,1],[3,2]]
    assert lc207_can_finish(4, pre) is True
    order = lc210_find_order(4, pre)
    assert len(order) == 4

    # lc1203 (tiny)
    n, m = 8, 2
    group = [-1,-1,1,0,0,1,0,-1]
    before = [[],[6],[5],[6],[3,6],[],[],[]]
    _ = lc1203_sort_items(n, m, group[:], [b[:] for b in before])

    # lc684
    assert lc684_find_redundant_connection([[1,2],[1,3],[2,3]]) == [2,3]

    # lc685
    assert lc685_find_redundant_directed_connection([[1,2],[2,3],[3,4],[4,1],[1,5]]) == [4,1]

    # lc2360
    assert lc2360_longest_cycle([3,3,4,2,3]) == 3
    assert lc2360_longest_cycle([2,-1,3,1]) == -1
