# Campus Navigation and Resource Management System
**Course Unit:** Data Structures and Algorithms (BCS 2105)  
**Institution:** Mountains of the Moon University — Faculty of Science, Technology and Innovation  
**Department:** Department of Computer Science  
**Lecturer:** Samuel Ocen  

## Group Members (The Fantastic Three)

| Name | Registration Number |

| Asiimwe Bright Kamara | 2025/U/MMU/BCS/00060 |
| Mpagi Shafiq | 2025/U/MMU/BCS/00062 |
| Kasozi Hafizu | 2025/U/MMU/BCS/00068 |

---

## Project Overview
This repository contains the Python implementations and integrated prototype for the **Campus Navigation and Resource Management System**. The system applies linear and non-linear data structures alongside sorting, searching, hashing, and graph algorithms to model campus buildings, pathways, room lookups, and shuttle schedules.

## Repository Structure

```text
DSA-group-coursework/
├── README.md
├── requirements.txt
├── Task_2a_stack_in_python.ipynb
├── Task_2b_Queue_in_python.ipynb
├── Task_3a_SinglyLinkedList.py
├── Task_3c_CycleDetection.py
├── Task_3e_CircularLinkedList.py
├── Task_4a_bst_campus_buildings.py
├── Task_4b_bst_traversals.py
├── Task_5a_insertion_and_merge_sort.ipynb
├── Task_5c_binary_sort.ipynb
├── Task_5d_hash_table.ipynb
└── Task_6c_Campus_Navigation_Capstone_project.ipynb
```

### File Descriptions
- **Task 2 (Stacks & Queues):**
  - `Task_2a_stack_in_python.ipynb`: LIFO stack implementation for tracking user navigation history.
  - `Task_2b_Queue_in_python.ipynb`: FIFO queue implementation for managing campus shuttle dispatch schedules.
- **Task 3 (Linked Lists & Variants):**
  - `Task_3a_SinglyLinkedList.py`: Singly linked list storing ordered shuttle stops with head/tail insertion, deletion by value, and traversal.
  - `Task_3c_CycleDetection.py`: Floyd's cycle-finding algorithm (Tortoise and Hare) tested on acyclic and cyclic shuttle routes.
  - `Task_3e_CircularLinkedList.py`: Circular linked list modeling a continuous shuttle loop from any starting stop.
- **Task 4 (Trees & Heaps):**
  - `Task_4a_bst_campus_buildings.py`: Binary Search Tree (BST) storing 10 campus buildings keyed by building code.
  - `Task_4b_bst_traversals.py`: Inorder, preorder, and postorder tree traversals on the campus BST.
- **Task 5 (Sorting, Searching & Hashing):**
  - `Task_5a_insertion_and_merge_sort.ipynb`: Step-by-step traces of Insertion Sort and Merge Sort.
  - `Task_5c_binary_sort.ipynb`: Binary search implementation on sorted campus building codes.
  - `Task_5d_hash_table.ipynb`: Fixed-size hash table (`size = 11`) using division hashing `h(k) = k mod 11` and linear probing.
- **Task 6 (Integrated Capstone System):**
  - `Task_6c_Campus_Navigation_Capstone_project.ipynb`: Interactive CLI prototype integrating the weighted campus graph (DFS, BFS, Dijkstra's shortest path), BST and Hash Table room lookup, Min-Heap busiest location ranking, Navigation Stack, and Shuttle Queue.

---

## Prerequisites & Setup
- **Python Version:** Python 3.10 or higher (tested on Python 3.12.8).
- **Dependencies:** Uses only the Python Standard Library (`heapq`). No external third-party packages are required to run the core algorithms.

Clone the repository:
```bash
git clone https://github.com/The-fantastic-three/DSA-group-coursework.git
cd DSA-group-coursework
```

## How to Run the Code

### 1. Standalone Python Scripts (`.py`)
Run any `.py` script directly from the terminal:
```bash
python Task_3a_SinglyLinkedList.py
python Task_3c_CycleDetection.py
python Task_3e_CircularLinkedList.py
python Task_4a_bst_campus_buildings.py
python Task_4b_bst_traversals.py
```

### 2. Jupyter Notebooks (`.ipynb`)
Open any `.ipynb` file (including the integrated capstone system `Task_6c_Campus_Navigation_Capstone_project.ipynb`) in **VS Code** or **Jupyter Notebook** and click **Run All**.

#### Capstone Menu Options (`Task_6c_Campus_Navigation_Capstone_project.ipynb`)
1. **Find Shortest Route (Dijkstra):** Computes the shortest walking path and time between two buildings (e.g., `GATE` to `SPT`).
2. **View Campus Traversals:** Displays Depth-First Search (DFS) and Breadth-First Search (BFS) orders starting from `GATE`.
3. **Lookup Room:** Queries room codes (e.g., `ICT-101`, `LIB-202`, `ADM-01`) across both the BST and Separate-Chaining Hash Table.
4. **View Top 3 Busiest Locations:** Uses a Min-Heap to display the top 3 highest-footfall campus buildings.
5. **View Navigation History:** Uses a bounded Stack (last 10 actions) to view recent routes and room lookups.
6. **Manage Shuttle Queue:** Uses a FIFO Queue to add or dispatch shuttle trips.
