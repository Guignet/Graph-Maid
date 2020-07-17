#Graph'Maid'

## What is Graph'Maid'
Graph'Maid' is basicaly a code that can translate an adjancy matrix of a Graph in mermaid.
It can use a matrix from a file or directly from your code.
It write on a file which name is Graph.md by default

## How to use it
Write an adjency matrix in the file name Graph.matrix in the form :
[edge,edge,edge...,edge]
[edge,edge,edge...,edge]
...
[edge,edge,edge...,edge]
with only number (edge = 12 for example)
If you put only 0 for an edge it will skip it.

Then juste do make in a linux terminal in the Folder src/.
It will write in the file Graph.md the mermaid representation of the Graph in the form :

```mermaid
A ((0))
B ((1))
...
Z ((25))
A -->|1| B
etc ...
```

## Problem not fixed yet 
if you have more than 26 vertices it will name it in the ASCII order (example: A = 65 so if you have 30 vertices your last one will be ^)
