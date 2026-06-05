# Computer Science Fundamentals: Course Objectives & Q&A

This document provides a comprehensive overview of the course goals and a set of practice questions and answers to reinforce the learning material across all modules.

---

## 🎯 Overall Course Objective
To equip students with a solid foundation in computer science, moving from basic problem-solving and programming to advanced data structures, algorithmic analysis, and mathematical foundations. By the end of this course, students will be able to design, implement, and optimize efficient software solutions.

---

## 📌 Module-Specific Objectives

1.  **Introduction to CS**: Define computer science, understand its history, and recognize its role as a problem-solving discipline.
2.  **Programming Fundamentals**: Master the basics of Python syntax, environment setup, and writing functional code.
3.  **Algorithmic Thinking**: Learn to decompose problems, recognize patterns, and analyze efficiency using Big O notation.
4.  **Data Structures**: Understand the trade-offs between different ways of organizing data (Arrays, Lists, Stacks, Queues, Hash Tables, Trees, Graphs).
5.  **Algorithms**: Implement and compare fundamental sorting (Bubble, Merge, Quick) and searching (Linear, Binary, BFS, DFS) techniques.
6.  **Discrete Mathematics**: Understand the mathematical underpinnings of computation, including Linear Algebra and Probability.
7.  **Debugging & Testing**: Develop a systematic approach to finding, fixing, and preventing software errors.

---

## ❓ Questions & Answers

### Module 1: Introduction to Computer Science
**Q: Is Computer Science primarily about learning how to program?**
**A:** No. While programming is a vital tool, Computer Science is the study of computational systems, problem-solving, and the theory behind how software works. Programming is the implementation of those solutions.

**Q: What is the core goal of "Computational Thinking"?**
**A:** To break down complex problems into smaller, manageable parts (decomposition), identify patterns, and create step-by-step solutions (algorithms) that a computer can execute.

---

### Module 2: Programming Fundamentals (Python)
**Q: Why is Python considered "dynamically typed"?**
**A:** Because you don't need to declare the type of a variable (like integer or string) when you create it; the interpreter determines the type at runtime based on the value assigned.

**Q: What does "Batteries Included" mean in the context of Python?**
**A:** It refers to Python's extensive standard library, which comes with many pre-written modules for common tasks like math, file handling, and web communication, so developers don't have to write everything from scratch.

---

### Module 3: Algorithmic Thinking & Big O
**Q: What is the benefit of using Big O Notation?**
**A:** It provides a standardized way to describe how an algorithm's runtime or memory usage scales as the input size (n) grows, allowing developers to compare efficiency regardless of hardware.

**Q: What is the time complexity of a nested loop where both loops run 'n' times?**
**A:** O(n²), also known as Quadratic Time.

---

### Module 4: Data Structures
**Q: When would you use a Linked List instead of an Array?**
**A:** Use a Linked List when you need to frequently insert or delete elements from the beginning or middle of the list, as these operations are O(1) if you have the reference, whereas Arrays require O(n) time to shift elements.

**Q: What is the main advantage of a Hash Table?**
**A:** It allows for extremely fast (average O(1)) lookups, insertions, and deletions using a key-value mapping system.

---

### Module 5: Algorithms
**Q: How does Bubble Sort get its name?**
**A:** It comes from the way smaller (or larger, depending on sort order) elements "bubble up" to their correct positions at the end of the list during each pass.

**Q: Why is Binary Search faster than Linear Search, and what is the requirement to use it?**
**A:** Binary Search is O(log n) because it halves the search area each step, while Linear Search is O(n). However, Binary Search **requires** the data to be sorted beforehand.

---

### Module 6: Discrete Mathematics
**Q: Why is Linear Algebra important in Computer Science?**
**A:** It is fundamental for computer graphics (transformations), machine learning (processing large datasets as matrices), and cryptography.

---

### Module 7: Debugging & Error Handling
**Q: What are the three questions every developer should ask when debugging?**
**A:** 1. What happened? 2. Why did it happen? 3. How do we fix it without breaking anything else?

**Q: What is "Rubber Duck Debugging"?**
**A:** The practice of explaining your code line-by-line to an inanimate object (like a rubber duck). The act of verbalizing the logic often reveals the flaw in your reasoning.

---
*Created for the CS Fundamentals Course - May 2026*
