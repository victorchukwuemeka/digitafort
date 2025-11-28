# An Introduction to Basic Logical Operations

In logic, a statement (or proposition) is a sentence that can be definitively classified as either **True** or **False**. We can perform operations on these statements to create more complex ones, much like we use `+` or `-` in arithmetic. The truth of these complex statements depends entirely on the truth of their parts.

Let's explore the fundamental logical operations, using `P` and `Q` as our example statements.

---\n

### 1. Conjunction (AND)

**The `AND` operation is about meeting all conditions.** A compound statement using `AND` is only true if **every single part** of it is true. If even one part is false, the whole statement is false.

-   **Analogy:** To get a driver's license (Statement R), you must pass the written test (Statement P) **AND** pass the practical driving test (Statement Q). If you only do one or the other, you don't get the license. Both must be true for the final outcome to be true.
-   **Formal Name:** Conjunction
-   **Symbol:** $\land$
-   **Reads:** "P and Q"
-   **Truth Table:**

| P | Q | P $\land$ Q |
|:-------:|:-------:|:-----------:|
| True    | True    | True        |
| True    | False   | False       |
| False   | True    | False       |
| False   | False   | False       |

---\n

### 2. Disjunction (OR)

**The `OR` operation is about meeting at least one condition.** A compound statement using `OR` is true if **one or more** of its parts are true. It's only false when all parts are false. This is also called an "inclusive or".

-   **Analogy:** A university might accept students who have high grades (P) **OR** have excellent extracurricular achievements (Q). A student can get in if they satisfy one condition, the other, or both. The only way they are rejected is if they satisfy neither.
-   **Formal Name:** Disjunction
-   **Symbol:** $\lor$
-   **Reads:** "P or Q"
-   **Truth Table:**

| P | Q | P $\lor$ Q |
|:-------:|:-------:|:----------:|
| True    | True    | True       |
| True    | False   | True       |
| False   | True    | True       |
| False   | False   | False      |

---\n

### 3. Negation (NOT)

**The `NOT` operation simply flips the truth value.** It makes a true statement false, and a false statement true.

-   **Analogy:** If the statement "The sky is blue" (P) is true, then "The sky is **not** blue" ($\neg$P) is false.
-   **Formal Name:** Negation
-   **Symbol:** $\neg$
-   **Reads:** "not P"
-   **Truth Table:**

| P | $\neg$ P |
|:-------:|:--------:|
| True    | False    |
| False   | True     |

---\n

### 4. Exclusive OR (XOR)

**The `XOR` operation is about meeting exactly one condition.** A compound statement using `XOR` is true only if **one part is true and the other is false**. If both are true or both are false, the `XOR` statement is false.

-   **Analogy:** At a restaurant, a meal special might include a soup **OR** a salad, but not both. You must choose exactly one. You can't have both, and you can't have neither.
-   **Formal Name:** Exclusive Disjunction
-   **Symbol:** $\oplus$
-   **Reads:** "P xor Q"
-   **Truth Table:**

| P | Q | P $\oplus$ Q |
|:-------:|:-------:|:------------:|
| True    | True    | False        |
| True    | False   | True         |
| False   | True    | True         |
| False   | False   | False        |

---\n

### 5. Implication (IF... THEN)

**The `IF...THEN` operation is about a promise or a condition.** The statement "If P, then Q" means that **if P is true, then Q must also be true**. The only way this "promise" is broken is if P is true, but Q is false.

-   **Analogy:** Your parents say, "IF you clean your room (P), THEN you can have dessert (Q)."
    -   If you clean your room (P is True) and get dessert (Q is True), the promise was kept.
    -   If you clean your room (P is True) but don't get dessert (Q is False), the promise was broken. This is the only false case.
    -   If you don't clean your room (P is False), the promise isn't broken whether you get dessert or not. The condition wasn't met, so the promise is technically not violated.
-   **Formal Name:** Material Implication / Conditional
-   **Symbol:** $\implies$
-   **Reads:** "If P, then Q"
-   **Truth Table:**

| P | Q | P $\implies$ Q |
|:-------:|:-------:|:--------------:|
| True    | True    | True           |
| True    | False   | False          |
| False   | True    | True           |
| False   | False   | True           |

---\n

### 6. Biconditional (IF AND ONLY IF)

**The `Biconditional` operation is about equivalence.** The statement "P if and only if Q" is true only if **P and Q have the same truth value**. They are either both true or both false.

-   **Analogy:** The statement "The light is on (P) if and only if the switch is up (Q)" means the two states are locked together. If the switch is up, the light is on. If the switch is down, the light is off. You can't have one without the other.
-   **Formal Name:** Biconditional / Material Equivalence
-   **Symbol:** $\iff$
-   **Reads:** "P if and only if Q"
-   **Truth Table:**

| P | Q | P $\iff$ Q |
|:-------:|:-------:|:-----------:|
| True    | True    | True        |
| True    | False   | False       |
| False   | True    | False       |
| False   | False   | True        |

---\n
### 7. Exclusive-NOR (XNOR)

**The `XNOR` operation is the negation of `XOR` and is about being the same.** It is true only if both inputs are the same (both true or both false). This is logically equivalent to the biconditional.

-   **Analogy:** Imagine a game where two players win if they both press their button at the same time (both True) OR if they both don't press it (both False). They lose if one player presses it and the other doesn't.
-   **Formal Name:** Exclusive-NOR
-   **Symbol:** $\odot$
-   **Reads:** "P xnor Q"
-   **Truth Table:**

| P | Q | P $\odot$ Q |
|:-------:|:-------:|:------------:|
| True    | True    | True         |
| True    | False   | False        |
| False   | True    | False        |
| False   | False   | True         |