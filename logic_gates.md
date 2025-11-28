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
|:-------:|:-------:|:-----------:|
| True    | True    | True        |
| True    | False   | False       |
| False   | True    | False       |
| False   | False   | False       |

---

#### **Disjunction (OR)**

**The `OR` operation is about meeting at least one condition.** A compound statement using `OR` is true if **one or more** of its parts are true.

-   **Analogy:** A university might accept students with high grades (P) **OR** excellent extracurriculars (Q). A student gets in if they satisfy one, the other, or both.
-   **Symbol:** $\lor$
-   **Reads:** "P or Q"
-   **Truth Table:**

| P | Q | P $\lor$ Q |
|:-------:|:-------:|:----------:|
| True    | True    | True       |
| True    | False   | True       |
| False   | True    | True       |
| False   | False   | False      |

---

#### **Negation (NOT)**

**The `NOT` operation simply flips the truth value.**

-   **Analogy:** If "The sky is blue" (P) is true, then "The sky is **not** blue" ($\neg$P) is false.
-   **Symbol:** $\neg$
-   **Reads:** "not P"
-   **Truth Table:**

| P | $\neg$ P |
|:-------:|:--------:|
| True    | False    |
| False   | True     |

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
|:-------:|:-------:|:--------------:|
| True    | True    | True           |
| True    | False   | False          |
| False   | True    | True           |
| False   | False   | True           |

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
|:-------:|:-------:|:-----------:|
| True    | True    | True        |
| True    | False   | False       |
| False   | True    | False       |
| False   | False   | True        |

#### **Logical Equivalence**
Two statements are logically equivalent if they always have the same truth value. This concept is central to the algebra of propositions.

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

## Chapter 3: The Algebra of Propositions (Laws of Logic)

Just like algebra with numbers, propositional logic has rules that allow us to manipulate and simplify logical statements. These rules are all based on logical equivalence. In the following laws, `T` represents a Tautology (always True) and `F` represents a Contradiction (always False).

### 3.1 Identity Laws
A statement's value is unchanged when combined with `T` (True) in a conjunction or `F` (False) in a disjunction.
-   $P \land T \iff P$
-   $P \lor F \iff P$

### 3.2 Domination Laws
A statement is dominated by (takes the value of) `T` in a disjunction or `F` in a conjunction.
-   $P \lor T \iff T$
-   $P \land F \iff F$

### 3.3 Idempotent Laws
Combining a statement with itself doesn't change its value.
-   $P \lor P \iff P$
-   $P \land P \iff P$

### 3.4 Double Negation Law
"Two negatives make a positive."
-   $\neg (\neg P) \iff P$

### 3.5 Commutative Laws
The order of statements doesn't matter for `AND` and `OR`.
-   $P \lor Q \iff Q \lor P$
-   $P \land Q \iff Q \land P$

### 3.6 Associative Laws
The grouping of statements doesn't matter for `AND` and `OR`.
-   $(P \lor Q) \lor R \iff P \lor (Q \lor R)$
-   $(P \land Q) \land R \iff P \land (Q \land R)$

### 3.7 Distributive Laws
`AND` and `OR` can be distributed over each other.
-   $P \land (Q \lor R) \iff (P \land Q) \lor (P \land R)$
-   $P \lor (Q \land R) \iff (P \lor Q) \land (P \lor R)$

### 3.8 De Morgan's Laws
These laws define how to negate a conjunction or a disjunction.
-    $\neg(P \land Q) \iff \neg P \lor \neg Q$
-    $\neg(P \lor Q) \iff \neg P \land \neg Q$

### 3.9 Absorption Laws
A statement can "absorb" a more complex one.
-   $P \lor (P \land Q) \iff P$
-   $P \land (P \lor Q) \iff P$

### 3.10 Negation Laws (Inverse Laws)
Combining a statement with its negation gives a tautology or a contradiction.
-   $P \lor \neg P \iff T$ (Law of the Excluded Middle)
-   $P \land \neg P \iff F$ (Law of Non-Contradiction)

### 3.11 Example and Proof of Logical Equivalence: De Morgan's First Law

Let's illustrate the logical equivalence of De Morgan's First Law: $\neg(P \land Q) \iff (\neg P \lor \neg Q)$.

**English Example:**

Let P be the statement: "It is sunny."
Let Q be the statement: "I am going to the beach."

**Left Side: $\neg(P \land Q)$**
"It is NOT (sunny AND I am going to the beach)."
This means it's not true that both things are happening. So, either it's not sunny, or I'm not going to the beach, or both.

**Right Side: $(\neg P \lor \neg Q)$**
"It is NOT sunny OR I am NOT going to the beach."
This also means the same thing: at least one of those conditions (not sunny, or not going to the beach) is true.

**Truth Table Proof:**

To prove this equivalence, we construct a truth table and show that the final column for $\neg(P \land Q)$ is identical to the final column for $(\neg P \lor \neg Q)$. (Here, 1 represents True, and 0 represents False).

| P | Q | P $\land$ Q | $\neg(P \land Q)$ | $\neg P$ | $\neg Q$ | $\neg P \lor \neg Q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |

As you can see, the column for $\neg(P \land Q)$ and the column for $(\neg P \lor \neg Q)$ are identical for all possible truth value combinations of P and Q. This proves their logical equivalence.

---

## Chapter 4: Practice Exercises

Test your knowledge! Determine the truth value of the following complex statements.

Let P = "It is raining." (1)
Let Q = "I have an umbrella." (0)
Let R = "I will get wet." (1)

1.  $P \land Q$
2.  $P \lor Q$
3.  $Q \implies R$
4.  $\neg Q \implies R$
5.  $(P \land \neg Q) \implies R$

---
### Solutions

1.  **0**. (1 AND 0 is 0)
2.  **1**. (1 OR 0 is 1)
3.  **1**. (0 implies 1 is 1 - the promise wasn't broken)
4.  **1**. (NOT 0 is 1. 1 implies 1 is 1)
5.  **1**. (P is 1, not Q is 1 -> (1 AND 1) is 1. So, 1 implies R (1) is 1.)
