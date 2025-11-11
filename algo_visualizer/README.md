# Algorithm Visualizer

A simple Python application to visualize common algorithms and data structures, including mazes and pathfinding.

## Features
- Visualizes algorithms step-by-step
- Maze generation and solving
- Modular UI components
- Easy to extend with new algorithms

## Requirements
- Python 3.8+
- Tkinter (usually included with Python)

## Getting Started
1. Clone this repository or copy the folder.
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   Or use `pyproject.toml` with Poetry:
   ```bash
   poetry install
   ```
3. Run the visualizer:
   ```bash
   python main.py
   ```

## File Structure
- `main.py` — Entry point for the application
- `algorithms.py` — Algorithm implementations
- `maze.py` — Maze generation and solving
- `ui_components.py` — UI elements
- `visualizer.py` — Visualization logic
- `constants.py` — App constants

## How to Use
- Launch the app and select an algorithm to visualize.
- Watch the step-by-step execution in the UI.
- Experiment with different mazes and algorithms.

## Algorithm Explanations

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. Imagine walking through a maze and always going forward until you hit a dead end, then stepping back to try a new path. It's good for exploring all possible paths.

### Breadth-First Search (BFS)
BFS explores all neighbors at the current depth before moving deeper. Think of it as searching level by level, like ripples spreading out in water. BFS is great for finding the shortest path in an unweighted graph or maze.

### A* Search
A* is a smart pathfinding algorithm that uses both the actual cost to reach a point and an estimate (heuristic) of the cost to reach the goal. It chooses paths that seem promising and usually finds the shortest route quickly. It's like using a map and guessing which roads will get you to your destination fastest.

## License
MIT
