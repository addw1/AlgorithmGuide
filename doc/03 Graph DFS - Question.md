# 03 Graph  - Question 

### Count Unreachable Pairs of Nodes in an Undirected Graph

You are given an integer `n`. There is an **undirected** graph with `n` nodes, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [ai, bi]` denotes that there exists an **undirected** edge connecting nodes `ai` and `bi`.

Return *the **number of pairs** of different nodes that are **unreachable** from each other*.

 **Example 1:**

![img](https://assets.leetcode.com/uploads/2022/05/05/tc-3.png)

```
Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/05/05/tc-2.png)

```
Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14
```



```python
class Solution:
    def __init__(self):
        self.isVis = []
        self.graph = []
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.isVis = [False for i in range(n)]
        # create graph
        self.graph = [[] for i in range(n)]
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        # find the number of sub graphs
        return self.findSubGraph(n)


    def findSubGraph(self, n: int) -> List[int]:
        total = 0
        res = 0
        for i in range(n):
            count = self.dfs(i)
            res += total * count
            total += count
        return res
    def dfs(self, cur: int):
        # base case
        if self.isVis[cur]:
            return 0

        # update status
        self.isVis[cur] = True

        # dfs
        count = 1
        for nextEle in self.graph[cur]:
            count += self.dfs(nextEle)
        return count

```



**:one: Build graph** 

Do not use `edges: List[List[int]]` to store your graph, it is very inefficient. And because it is an undirected graph, you should add edges for two nodes.

```python
    for edge in edges:
        self.graph[edge[0]].append(edge[1])
        self.graph[edge[1]].append(edge[0])
```



:two: Use `DFS` to calculate the number of **isolation graphs**

:three: How to calculate **total pairs?**

One Tips：

**Original Version**

Use counts to store the number of vertexes for each isolation graph.

time complexity: $$O(n^2)$$

```
        for i in range(len(counts)):
            for j in range(i + 1, len(counts)):
                res += counts[i] * counts[j]
```



**Updated Version**

time complexity: $$O(n + m)$$

```python
        total = 0
        res = 0
        for i in range(n):
            count = self.dfs(i)
            res += total * count
            total += count
        return res
```

![image-20241212013451361](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241212013451361.png)



### 

### Shortest Distance After Road Addition Queries I

You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [ui, vi]` represents the addition of a new **unidirectional** road from city `ui` to city `vi`. After each query, you need to find the **length** of the **shortest path** from city `0` to city `n - 1`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` is the *length of the shortest path* from city `0` to city `n - 1` after processing the **first** `i + 1` queries.

 

**Example 1:**

**Input:** n = 5, queries = [[2,4],[0,2],[0,4]]

**Output:** [3,2,1]

**Explanation:**

![img](https://assets.leetcode.com/uploads/2024/06/28/image8.jpg)

After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.

![img](https://assets.leetcode.com/uploads/2024/06/28/image9.jpg)

After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

![img](https://assets.leetcode.com/uploads/2024/06/28/image10.jpg)

After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

**Example 2:**

**Input:** n = 4, queries = [[0,3],[0,2]]

**Output:** [1,1]

**Explanation:**

![img](https://assets.leetcode.com/uploads/2024/06/28/image11.jpg)

After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.

![img](https://assets.leetcode.com/uploads/2024/06/28/image12.jpg)

After the addition of the road from 0 to 2, the length of the shortest path remains 1.

****

**Optimization BFS**

```python
class Solution:
    def __init__(self):
        self.graph = None
        self.target = 0
        self.level = None
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # build graph
        self.target = n - 1
        self.graph = [[] for i in range(n)]
        self.level = [n - 1 - i for i in range(n)]
        for i in range(n - 1):
            self.graph[i+1].append(i)
        res = []
        for query in queries:
            # update graph
            self.graph[query[1]].append(query[0])
            if self.level[query[0]] > self.level[query[1]] + 1:
                self.level[query[0]] = self.level[query[1]] + 1
                # update level
                q = [query[0]]
                while len(q) != 0:
                    cur = q.pop()
                    for prev in self.graph[cur]:
                        if self.level[prev] > self.level[cur] + 1:
                            self.level[prev] = self.level[cur] + 1
                            q.append(prev)
            res.append(self.level[0])
        return res

    def bfs(self, n: int) -> int:
        q = []
        # curIndex and level
        q.append(n)
        q.append(0)
        while len(q) != 0:
            cur = q.pop(0)
            level = q.pop(0)
            # add neibors
            for nei in self.graph[cur]:
                if nei == self.target:
                    return level + 1
                q.append(nei)
                q.append(level + 1)
        return -1
```

**Original Version**

Query onetime, run BFS onetime.

**<font color = red>So slow!</font>**

​                                         ![image-20241212031627360](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241212031627360.png)



```python
if self.level[query[0]] > self.level[query[1]] + 1:
```

Use such way to check whether current node need to update.

**Tips: Store reverse graph, so that you can know the prev nodes of the current node. And update them**



### Dijkstra

### Network Delay Time

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

**Example 2:**

```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Example 3:**

```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

 

**Constraints:**

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- All the pairs `(ui, vi)` are **unique**. (i.e., no multiple edges.)

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = [[] for _ in range(n)]
        for edge in times:
            graph[edge[0] - 1].append((edge[2], edge[1]))
        isVis = [ False for _ in range(n)]
        # init pq
        pq = []
        heapq.heappush(pq, (0, k))
        dis = 0
        cur = 0
        count = 0
        while len(pq) != 0 and count != n:
            # print(pq)
            dis, cur = heapq.heappop(pq)
            if isVis[cur - 1] is not True:
                count += 1
                isVis[cur - 1] = True
                # add neibour
                for nei in graph[cur - 1]:
                    if isVis[nei[1] - 1] is not True:
                        newPair = (nei[0] + dis, nei[1])
                        heapq.heappush(pq, newPair)
        if count == n:
            return dis
        else:
            return -1
```

**How to know you update how many nodes?**

```
if isVis[cur - 1] is not True:
                count += 1
```

You should check  whether you have visited this node before you increase the `count`.

Some nodes will add into the queue multiple times. So you can not direclty add the `count`  after the `pop` operation.

![image-20241212051119269](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241212051119269.png)

