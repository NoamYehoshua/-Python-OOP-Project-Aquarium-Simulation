# 🐟 Python Project – OOP Aquarium Simulation

## 📌 Project Overview

This academic project simulates an aquarium environment using **Object-Oriented Programming (OOP)** principles in Python.  
Users can add fish and crustaceans to a 2D aquarium grid, simulate their movement, feed them, and observe their status over time.

> It demonstrates inheritance, polymorphism, abstraction, and encapsulation via interactive terminal simulation.

---

## 🧠 Main Concepts Demonstrated

- **OOP design** using class hierarchies (`Animal → Fish/Crab → Molly, Scalar, Shrimp, Ocypode`)
- **2D text-based visualization** of an aquarium grid
- **Polymorphism** via overridden `get_animal()` functions
- **Encapsulation** of animal behavior
- **Exception handling** for invalid inputs and logic errors
- **Simulation control** with steps, feeding, and aging

---

## 🧱 Project Folder Structure

```
HomeWork5/
├── main.py                       # Main simulation script with menu
├── Animal.py                    # Abstract base class for all animals
├── Aquarium.py                  # Manages the 2D aquarium and animal placement
├── Crab.py                      # Crab base class
├── Fish.py                      # Fish base class
├── Molly.py                     # Molly fish class
├── Scalar.py                    # Scalar fish class
├── Shrimp.py                    # Shrimp class (inherits from Animal)
├── Ocypode.py                   # Ocypode crab class
├── Exceptions.py                # Custom exceptions for validation
├── Animals_lists.py             # Optional: helper functions for managing lists
├── main_example_v1.txt          # Sample input file for a full simulation
├── scalar_example_v1.txt        # Sample input with scalar
├── several_steps_example_v1.txt # Input file for multi-step simulation
├── test_Molly.py                # Unit test script for Molly
└──  OOP GIF.gif                  # Demo animation (optional)
```


---

## 🕹️ Features

- Add animals (name, type, direction, position)
- Render aquarium grid and visualize animal placement using ASCII art
- Step simulation forward (1 or multiple steps)
- Drop food into the aquarium and watch animals feed
- Track animal age and food status
- Remove animals upon starvation
- Input validation and error handling

---

## 📷 Sample Interaction

```
Main menu
------------------------------
1. Add an animal
2. Print all animals
3. Drop food into the aquarium
4. Take a step forward
5. Take several steps
6. Exit

```

---

## 🚀 How to Run

1. Make sure you have Python 3.7+ installed.
2. Open terminal inside the project folder and run:

```bash
python main.py
```

3. To run with input files:

```bash
python main.py < main_example_v1.txt
```

---

## 🔗 Notes

- Animals are drawn using 2D character matrices from `get_animal()` method.
- Each species has its own visual, behavior, and direction logic.
- You can use `test_Molly.py` to test a single animal's behavior in isolation.

---

## 🧾 Summary

This project showcases:
- Clean OOP design in Python
- Text-based rendering and simulation
- Class inheritance and polymorphism
- Input-driven and time-based logic
- Exception-safe and modular architecture

