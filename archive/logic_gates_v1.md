# Logic Gates for Pure Mathematics (Version 1)

Logic gates are fundamental building blocks of digital systems and are based on Boolean algebra. They perform basic logical functions and are often represented by truth tables and symbols.

## 1. AND Gate (Conjunction)

The AND gate outputs true (1) only if all of its inputs are true (1).

-   **Symbol:** $\land$ or $\cdot$
-   **Truth Table:**

| A | B | A $\land$ B |
|---|---|-------------|
| 0 | 0 | 0           |
| 0 | 1 | 0           |
| 1 | 0 | 0           |
| 1 | 1 | 1           |

## 2. OR Gate (Disjunction)

The OR gate outputs true (1) if at least one of its inputs is true (1).

-   **Symbol:** $\lor$ or $+$
-   **Truth Table:**

| A | B | A $\lor$ B |
|---|---|------------|
| 0 | 0 | 0          |
| 0 | 1 | 1          |
| 1 | 0 | 1          |
| 1 | 1 | 1          |

## 3. NOT Gate (Negation)

The NOT gate (inverter) outputs the opposite of its input. If the input is true (1), the output is false (0), and vice versa.

-   **Symbol:** $\neg$ or $\bar{A}$
-   **Truth Table:**

| A | $\neg$ A |
|---|----------|
| 0 | 1        |
| 1 | 0        |

## 4. XOR Gate (Exclusive OR)

The XOR gate outputs true (1) if an odd number of its inputs are true (1). For two inputs, it outputs true if the inputs are different.

-   **Symbol:** $\oplus$
-   **Truth Table:**

| A | B | A $\oplus$ B |
|---|---|--------------|
| 0 | 0 | 0            |
| 0 | 1 | 1            |
| 1 | 0 | 1            |
| 1 | 1 | 0            |

## 5. Implication (Conditional)

The implication $A \implies B$ is false only if A is true and B is false. Otherwise, it is true.

-   **Symbol:** $\implies$
-   **Truth Table:**

| A | B | A $\implies$ B |
|---|---|----------------|
| 0 | 0 | 1              |
| 0 | 1 | 1              |
| 1 | 0 | 0              |
| 1 | 1 | 1              |

## 6. Biconditional (Equivalence)

The biconditional $A \iff B$ is true if A and B have the same truth value.

-   **Symbol:** $\iff$
-   **Truth Table:**

| A | B | A $\iff$ B |
|---|---|------------|
| 0 | 0 | 1          |
| 0 | 1 | 0          |
| 1 | 0 | 0          |
| 1 | 1 | 1          |
