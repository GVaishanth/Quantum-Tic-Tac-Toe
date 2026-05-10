# Quantum Tic Tac Toe with AI

A Python-based implementation of Tic Tac Toe enhanced with **quantum simulation concepts** and an **AI opponent**, creating a non-deterministic and strategically rich gameplay experience.

---

## Table of Contents
- Overview
- Features
- System Design
- Technologies Used
- Installation
- Game Flow
- Project Structure
- Limitations
- Future Enhancements
- Author

---

## 🧠 Overview

This project extends the traditional Tic Tac Toe game by introducing **quantum-inspired state simulation** using Qiskit.  
Unlike classical versions, the final board configuration is determined after executing **multiple quantum simulations**, making outcomes probabilistic rather than fixed.

An AI opponent is implemented using the **Minimax algorithm with Alpha-Beta pruning**, ensuring optimal move selection.

---

## ✨ Features

### Core Features
- Quantum-inspired move representation using Qiskit circuits
- Multi-simulation system to determine final board state
- AI opponent using Minimax with Alpha-Beta pruning
- Two gameplay modes:
  - Player vs Player
  - Player vs Computer

### Advanced Features
- Non-deterministic outcomes (same moves can yield different results)
- Mid-game state tracking with classical projection
- Neighbour-based scoring system for tie resolution

---

## 🏗️ System Design

### 1. Quantum Representation
Each move applies quantum gates to a circuit:
- `Hadamard (H)` → introduces superposition
- `Z gate` → encodes player X
- `X gate` → encodes player O

### 2. State Simulation
- Circuit is measured after all moves
- Multiple simulations (shots) are executed
- Most probable states are selected

### 3. Winner Evaluation
1. Standard Tic Tac Toe win conditions
2. If no winner:
   - Neighbour-based scoring determines outcome

---

## 🛠️ Technologies Used

| Category        | Tools/Concepts |
|----------------|--------------|
| Language       | Python |
| Quantum        | Qiskit, Qiskit Aer |
| AI             | Minimax Algorithm, Alpha-Beta Pruning |
| Concepts       | Game Theory, Simulation, Probabilistic Systems |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+

### Install Dependencies
bash
```pip install qiskit qiskit-aer```

---

## Game Flow

1. Select game mode:
   - Player vs Player  
   - Player vs Computer  

2. Choose player symbol (X or O)

3. Players take turns selecting positions (1–9)

4. After all positions are filled:
   - Quantum simulations are executed  
   - Final board state is generated  

5. Winner is determined using:
   - Standard rules  
   - OR Neighbour scoring system  

---


## ⚠️ Limitations

- CLI-based interface (no graphical UI)  
- Requires Qiskit installation (can be heavy for some systems)  
- Quantum simulation is conceptual (not real quantum hardware)  

---

## 🚀 Future Enhancements

- Graphical interface (Tkinter / Web-based)  
- Integration with real quantum hardware (IBM Quantum)  
- Difficulty levels for AI  
- Multiplayer over network  
- Visualization of quantum states  

---

## 👤 Author

**G. Vaishanth**
