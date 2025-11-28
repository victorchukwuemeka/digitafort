# Basic Logical Operations (Version 2)

In mathematical logic, a statement (or proposition) is a declarative sentence that is either **true** or **false**, but not both. We can combine or modify these statements using logical operations to form more complex statements.

The truth value of a compound statement is determined by the truth values of its constituent parts. We can use truth tables to summarize the results. In these tables, `T` stands for "true" and `F` stands for "false".

Let `P` and `Q` be two logical statements.

---

## 1. Conjunction (AND)

A conjunction is a compound statement formed by joining two statements with the word "and". The conjunction "P and Q" is true only if both P and Q are true.

-   **Symbol:** $\land$
-   **Reads:** "P and Q"
-   **Truth Table:**

| P | Q | P $\land$ Q |
|:---:|:---:|:-----------:|
| T | T | T           |
| T | F | F           |
| F | T | F           |
| F | F | F           |

---

## 2. Disjunction (OR)

A disjunction is a compound statement formed by joining two statements with the word "or". The disjunction "P or Q" is true if at least one of the statements P or Q is true. This is also known as an "inclusive or".

-   **Symbol:** $\lor$
-   **Reads:** "P or Q"
-   **Truth Table:**

| P | Q | P $\lor$ Q |
|:---:|:---:|:----------:|
| T | T | T          |
| T | F | T          |
| F | T | T          |
| F | F | F          |

---

## 3. Negation (NOT)

A negation is a statement that has the opposite truth value of the original statement.

-   **Symbol:** $\neg$
-   **Reads:** "not P"
-   **Truth Table:**

| P | $\neg$ P |
|:---:|:--------:|
| T | F        |
| F | T        |

---

## 4. Exclusive OR (XOR)

The exclusive or "P XOR Q" is true if exactly one of the statements P or Q is true, but not both.

-   **Symbol:** $\oplus$
-   **Reads:** "P xor Q"
-   **Truth Table:**

| P | Q | P $\oplus$ Q |
|:---:|:---:|:------------:|
| T | T | F            |
| T | F | T            |
| F | T | T            |
| F | F | F            |

---

## 5. Implication (Conditional)

An implication is a conditional statement of the form "if P, then Q". It is only false when the first statement (P) is true and the second statement (Q) is false.

-   **Symbol:** $\implies$
-   **Reads:** "if P, then Q" or "P implies Q"
-   **Truth Table:**

| P | Q | P $\implies$ Q |
|:---:|:---:|:--------------:|
| T | T | T              |
| T | F | F              |
| F | T | T              |
| F | F | T              |

---

## 6. Biconditional (If and Only If)

A biconditional statement "P if and only if Q" is true when both P and Q have the same truth value (both true or both false).

-   **Symbol:** $\iff$
-   **Reads:** "P if and only if Q"
-   **Truth Table:**

| P | Q | P $\iff$ Q |
|:---:|:---:|:-----------:|
| T | T | T           |
| T | F | F           |
| F | T | F           |
| T | T | T           |

---

## 7. Exclusive-NOR (XNOR)

The Exclusive-NOR (XNOR) gate is the logical negation of the XOR gate. Its output is true if the inputs are the same, and false if the inputs are different. It is equivalent to the biconditional operator.

-   **Symbol:** $\odot$ or $\overline{P \oplus Q}$
-   **Reads:** "P xnor Q"
-   **Truth Table:**

| P | Q | P $\odot$ Q |
|:---:|:---:|:------------:|
| T | T | T            |
| T | F | F            |
| F | T | F            |
| F | F | T            |
