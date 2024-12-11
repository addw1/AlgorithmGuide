# Graph DFS && BFS

## DFS

Process:

The most notable feature of DFS is that it calls itself recursively.

```python
DFS(u):
	for all edges in u:
		v = edge(u)
		if v is not visited:
			dfs(v)
		end
	end
end
```

:clock1:  **Time:**O(m + n)
:parasol_on_ground:  **Space：**O(n)



## BFS

```python
bfs(s) {
  q = new queue()
  q.push(s), visited[s] = true
  while (!q.empty()) {
    u = q.pop()
    for each edge(u, v) {
      if (!visited[v]) {
        q.push(v)
        visited[v] = true
      }
    }
  }
}
```

>All the vertexs in the  queue are visited.

:clock1:  **Time:**O(m + n)
:parasol_on_ground:  **Space：**O(n)



## Double-ended queue BFS

```python
while (queue is not empty) {
  int u = queue.pop()
  for (neibours in u) {
    update
    if (...)
     	add to the front of the queue
    else
     	add to the end of the queue
  }
}
```



**Example Harry potter** 

"The Chamber of Secrets has been opened again" — this news has spread all around Hogwarts and some of the students have been petrified due to seeing the basilisk. Dumbledore got fired and now Harry is trying to enter the Chamber of Secrets. These aren't good news for Lord Voldemort. The problem is, he doesn't want anybody to be able to enter the chamber. The Dark Lord is going to be busy sucking life out of Ginny.

The Chamber of Secrets is an *n* × *m* rectangular grid in which some of the cells are columns. A light ray (and a basilisk's gaze) passes through the columns without changing its direction. But with some spell we can make a column magic to reflect the light ray (or the gaze) in all four directions when it receives the ray. This is shown in the figure below.

![img](https://espresso.codeforces.com/ad83cb7d3b23b415d6160c210d666149c240cfba.png)

The left light ray passes through a regular column, and the right ray — through the magic column.

The basilisk is located at the right side of the lower right cell of the grid and is looking to the left (in the direction of the lower left cell). According to the legend, anyone who meets a basilisk's gaze directly dies immediately. But if someone meets a basilisk's gaze through a column, this person will get petrified. We know that the door to the Chamber is located on the left side of the upper left corner of the grid and anyone who wants to enter will look in the direction of its movement (in the direction of the upper right cell) from that position.

![img](https://espresso.codeforces.com/f2def2cc555f3cb8d9ad5c8601c9e256126b5df7.png)

This figure illustrates the first sample test.

Given the dimensions of the chamber and the location of regular columns, Lord Voldemort has asked you to find the minimum number of columns that we need to make magic so that anyone who wants to enter the chamber would be petrified or just declare that it's impossible to secure the chamber.

**Input**

The first line of the input contains two integer numbers *n* and *m* (2 ≤ *n*, *m* ≤ 1000). Each of the next *n* lines contains *m* characters. Each character is either "." or "#" and represents one cell of the Chamber grid. It's "." if the corresponding cell is empty and "#" if it's a regular column.

```
3 3
.#.
...
.#.
```

**Output**

Print the minimum number of columns to make magic or -1 if it's impossible to do.

```
2
```

**0 -1 BFS  (Shortest Path in a Binary Weight Graph)**

**Lemma:** During the excution of BFS, the queue holding the vertices only contains elements from at max two successive levels of the BFS tree.

![image-20241211030540990](C:\Users\52068\AppData\Roaming\Typora\typora-user-images\image-20241211030540990.png)

Form the figure, we can know that, if the weight between two vertexs is zero, it should be viewed as the same level. Otherwise, it is in diff levels. For the same level vertexs, it should be added to **the front of** the queue, for the diff level vertexs, it should be added to **the end of** the queue.