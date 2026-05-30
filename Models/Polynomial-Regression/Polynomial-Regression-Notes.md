# Polynomial Regression

## What is Polynomial Regression?

Polynomial Regression is used when the relationship between input and output is **curved instead of straight**.

Basic idea:

> If a straight line cannot fit the data properly, use a curve.

It is still a type of regression and predicts **continuous numerical values**.

Examples:

* Population growth
* Temperature variation
* Curved sales trends
* Motion under acceleration

---

## Why do we need Polynomial Regression?

Linear Regression assumes:

```text id="p1"
Straight-line relationship
```

But real-world data is often curved.

Example:

Suppose marks improve quickly at first and later slow down.

A straight line may miss this pattern.

Polynomial Regression helps capture such curves.

Simple idea:

```text id="p2"
Curved Data → Curved Model
```

---

## Basic Equation

Linear Regression:

```text id="p3"
y = (m * x) + c
```

Polynomial Regression:

Degree 2:

```text id="p4"
y = (a * x^2) + (b * x) + c
```

Degree 3:

```text id="p5"
y = (a * x^3) + (b * x^2) + (c * x) + d
```

General form:

```text id="p6"
y = a0 + (a1 * x) + (a2 * x^2) + (a3 * x^3) + ...
```

where:

* x → input
* y → prediction
* coefficients (a,b,c...) → learned weights
* power of x creates curvature

---

## Main Idea

Polynomial Regression does NOT mean multiple variables.

It means:

> Same feature, but raised to higher powers.

Example:

Original feature:

```text id="p7"
x = Area
```

Polynomial features:

```text id="p8"
x
x^2
x^3
```

So the model gets extra flexibility.

---

## Is it really different from Linear Regression?

Interesting fact:

> Polynomial Regression is still Linear Regression underneath.

Why?

Because the model is still linear in terms of **weights**.

Example:

```text id="p9"
y = (a * x^2) + (b * x) + c
```

Weights:

```text id="p10"
a, b, c
```

These are still learned linearly.

So Polynomial Regression =

```text id="p11"
Linear Regression + Polynomial Features
```

---

## Cost Function (MSE)

Polynomial Regression also uses Mean Squared Error.

Simple idea:

```text id="p12"
MSE = Total Squared Error / Number of Samples
```

Meaning:

* find prediction error
* square it
* add all squared errors
* divide by total samples

Goal:

> Minimize MSE.

Lower MSE means better fit.

---

## How Polynomial Regression Learns

Learning process is almost same as Linear Regression.

Steps:

1. Create polynomial features
2. Make predictions
3. Calculate error
4. Update weights
5. Repeat until error becomes small

Gradient Descent idea:

```text id="p13"
New Weight
=
Old Weight
-
(Learning Rate * Error Direction)
```

So the learning mechanism stays mostly unchanged.

---

## Degree of Polynomial

Degree controls curve complexity.

### Degree 1

Same as Linear Regression.

```text id="p14"
Straight Line
```

---

### Degree 2

Can model simple curves.

```text id="p15"
U-shape or curved trend
```

---

### Degree 3

More flexible.

Can model:

```text id="p16"
S-shaped curves
```

---

Higher degree:

```text id="p17"
More flexibility
```

But also:

```text id="p18"
Higher overfitting risk
```

---

## Choosing Degree

Choosing degree is important.

Too small:

```text id="p19"
Model too simple
```

Too large:

```text id="p20"
Model memorizes noise
```

Goal:

> Find a balance.

Simple intuition:

```text id="p21"
Enough curve to learn pattern
But not so much that it memorizes data
```

---

## Underfitting vs Overfitting

### Underfitting

Model is too simple.

Example:

Straight line trying to fit curved data.

Signs:

* high error
* poor predictions

---

### Overfitting

Model becomes too complex.

It memorizes training data instead of learning general pattern.

Signs:

* very low training error
* poor test performance

Example:

Degree 15 model on small dataset.

---

## When to Use Polynomial Regression

Use it when:

* output is continuous
* data shows curved trend
* Linear Regression performs poorly
* relationship is nonlinear but smooth

Examples:

* growth trends
* physics motion problems
* price trends
* biological measurements

---

## Strengths

* captures nonlinear patterns
* simple extension of Linear Regression
* easy to understand
* flexible

---

## Weaknesses

* degree selection is tricky
* can overfit easily
* sensitive to outliers
* high degree models may behave strangely outside training range

---

## When NOT to Use Polynomial Regression

Avoid it when:

### 1. Data is already linear

Then Polynomial Regression adds unnecessary complexity.

Linear Regression is usually enough.

---

### 2. Degree becomes too large

Very high degree models may:

```text id="p22"
memorize data
follow noise
overfit
```

---

### 3. Too Few Samples

High-degree polynomial needs enough data.

Otherwise:

```text id="p23"
Too many parameters
Too little information
```

Poor generalization happens.

---

### 4. Relationship is Highly Complex

Some problems are not smooth curves.

Examples:

* complex interactions
* discontinuities
* irregular patterns

Better choices:

* Decision Trees
* Random Forest
* Neural Networks

---

## Quick Comparison

Linear Regression:

```text id="p24"
Straight Line
```

Polynomial Regression:

```text id="p25"
Curved Line
```

Memory trick:

```text id="p26"
Linear = straight fit
Polynomial = curved fit
```

---

## One-Line Summary

> Polynomial Regression = Linear Regression with curved features to fit nonlinear patterns.
