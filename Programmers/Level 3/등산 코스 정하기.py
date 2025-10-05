from heapq import heappop, heappush
from math import inf


def solution(n, paths, gates, summits):
    def dijkstra(gates):
        heap = [(0, gate) for gate in gates]

        while heap:
            w, v = heappop(heap)

            if intensities[v] < w or v in summits:
                continue

            for next_v, next_w in adjacencies[v]:
                next_w = max(intensities[v], next_w)

                if next_w < intensities[next_v]:
                    intensities[next_v] = next_w
                    heappush(heap, (next_w, next_v))

    adjacencies = [[] for _ in range(n + 1)]
    intensities = [inf for _ in range(n + 1)]
    summits = set(summits)

    for v1, v2, w in paths:
        adjacencies[v1].append((v2, w))
        adjacencies[v2].append((v1, w))

    for gate in gates:
        intensities[gate] = 0

    dijkstra(gates)

    answer = min(((summit, intensities[summit]) for summit in sorted(summits)), key = lambda x: x[1])

    return answer