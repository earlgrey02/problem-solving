from collections import deque


def solution(begin, target, words):
    def bfs(v):
        queue = deque([v])
        visited[v] = 0

        while queue:
            v = queue.popleft()

            if v == target:
                return visited[v]
            else:
                for word in words:
                    if visited[word] == -1 and sum(i != j for i, j in zip(v, word)) == 1:
                        visited[word] = visited[v] + 1
                        queue.append(word)

        return 0

    visited = {word: -1 for word in words}
    answer = bfs(begin)

    return answer