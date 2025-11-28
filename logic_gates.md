# A Course in Basic Propositional Logic

Welcome! This document provides a foundational course in propositional logic, the branch of logic that studies the relationships between propositions (statements that can be true or false).

## Chapter 1: The Building Blocks of Logic

### 1.1 Propositions and Truth Values

In logic, a **proposition** (or statement) is a sentence that can be definitively classified as either **True** or **False**. It cannot be both or neither.

-   **Examples of propositions:**
    -   "The sky is blue." (True)
    -   "The Earth is flat." (False)
    -   "2 + 2 = 4." (True)
-   **Examples of non-propositions:**
    -   "What time is it?" (This is a question)
    -   "Close the door." (This is a command)
    -   "This statement is false." (This is a paradox)

### 1.2 Basic Logical Operations

We can perform operations on propositions to create more complex ones, much like we use `+` or `-` in arithmetic. The truth of these complex statements depends entirely on the truth of their parts. Let's use `P` and `Q` as our example propositions.

---

#### **Conjunction (AND)**

**The `AND` operation is about meeting all conditions.** A compound statement using `AND` is only true if **every single part** of it is true.

-   **Analogy:** To get a driver's license, you must pass the written test (P) **AND** pass the practical driving test (Q). If you only do one, you don't get the license.
-   **Symbol:** $\land$
-   **Reads:** "P and Q"
-   **Truth Table:**
| P | Q | P $\land$ Q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

---

#### **Disjunction (OR)**

**The `OR` operation is about meeting at least one condition.** A compound statement using `OR` is true if **one or more** of its parts are true.

-   **Analogy:** A university might accept students with high grades (P) **OR** excellent extracurriculars (Q). A student gets in if they satisfy one, the other, or both.
-   **Symbol:** $\lor$
-   **Reads:** "P or Q"
-   **Truth Table:**
| P | Q | P $\lor$ Q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

---

#### **Negation (NOT)**

**The `NOT` operation simply flips the truth value.**

-   **Analogy:** If "The sky is blue" (P) is true, then "The sky is **not** blue" ($\neg$P) is false.
-   **Symbol:** $\neg$
-   **Reads:** "not P"
-   **Truth Table:**
| P | $\neg$ P |
|:---:|:---:|
| T | F |
| F | T |

---

## Chapter 2: Advanced Logical Concepts

### 2.1 Conditional Statements

#### **Implication (IF... THEN)**

**The `IF...THEN` operation is about a promise.** "If P, then Q" means if P is true, Q must also be true. The only way the promise is broken is if P is true, but Q is false.

-   **Analogy:** "IF you clean your room (P), THEN you can have dessert (Q)." The promise is only broken if you clean your room but get no dessert.
-   **Symbol:** $\implies$
-   **Reads:** "If P, then Q"
-   **Truth Table:**
| P | Q | P $\implies$ Q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

#### **Converse, Inverse, and Contrapositive**

From an implication "If P, then Q", we can create three related statements:
-   **Converse:** "If Q, then P" ($f{Q \implies P}$)
-   **Inverse:** "If not P, then not Q" ($f{\neg P \implies \neg Q}$)
-   **Contrapositive:** "If not Q, then not P" ($f{\neg Q \implies \neg P}$)
**Important:** An implication and its contrapositive are logically equivalent!

### 2.2 Equivalence

#### **Biconditional (IF AND ONLY IF)**

**The `Biconditional` is about equivalence.** "P if and only if Q" is true only if **P and Q have the same truth value**.

-   **Analogy:** "The light is on (P) if and only if the switch is up (Q)." The two states are locked together.
-   **Symbol:** $\iff$
-   **Reads:** "P if and only if Q"
-   **Truth Table:**
| P | Q | P $\iff$ Q |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

#### **Logical Equivalence**
Two statements are logically equivalent if they always have the same truth value.
-   **De Morgan's Laws:** A famous example.
    -    $\neg(P \land Q)$ is equivalent to $(\neg P \lor \neg Q)$
    -    $\neg(P \lor Q)$ is equivalent to $(\neg P \land \neg Q)$
-   **Double Negation:** $\neg(\neg P)$ is equivalent to $P$.

### 2.3 Statement Classifications

-   **Tautology:** A statement that is **always true**, regardless of the truth values of its components. (e.g., $P \lor \neg P$)
-   **Contradiction:** A statement that is **always false**. (e.g., $P \land \neg P$)
-   **Contingency:** A statement that can be either true or false.

### 2.4 Operator Precedence
When evaluating complex statements, follow this order:
1.  Parentheses `( )`
2.  Negation `¬`
3.  Conjunction `∧`
4.  Disjunction `∨`
5.  Implication `→`
6.  Biconditional `↔`

---

## Chapter 3: Practice Exercises

Test your knowledge! Determine the truth value of the following complex statements.

Let P = "It is raining." (True)
Let Q = "I have an umbrella." (False)
Let R = "I will get wet." (True)

1.  $P \land Q$
2.  $P \lor Q$
3.  $Q \implies R$
4.  $\neg Q \implies R$
5.  $(P \land \neg Q) \implies R$

---
### Solutions

1.  **False**. (True AND False is False)
2.  **True**. (True OR False is True)
3.  **True**. (False implies True is True - the promise wasn't broken)
4.  **True**. (True implies True is True)
5.  **True**. (P is True, not Q is True -> (True AND True) is True. So, True implies R (True) is True.)
