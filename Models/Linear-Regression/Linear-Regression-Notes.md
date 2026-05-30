# Linear Regression

## What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used when the output is **continuous (numerical value)**.

Basic idea:

> Find a straight line (or hyperplane) that best fits the relationship between input and output.

Examples:

* Hours studied → Marks
* House size → Price
* Experience → Salary

---

## Basic Equation

For one feature:

```text id="l1q8a"
y = (m * x) + c
```

where:

* y → predicted output
* x → input feature
* m → slope (weight)
* c → intercept (bias)

---

For multiple features:

```text id="p7m2k"
y = (w1 * x1) + (w2 * x2) + (w3 * x3) + ... + b
```

Matrix form:

```text id="x9t4n"
y = (X * W) + b
```

---

## What is the model trying to do?

The model:

* makes predictions
* compares them with actual values
* measures how wrong it is

Goal:

> Reduce the difference between actual and predicted values as much as possible.

---

## Best Fit Line Idea

Linear Regression does NOT try to pass through every point.

Instead, it finds:

> the line that gives the smallest total error across all points.

So it is basically a **balancing line**, not a perfect-fit line.

---

## Cost Function (MSE)

We measure error using Mean Squared Error.

Simple idea:

```text id="mse1"
MSE = Total Squared Error / Number of Samples
```

Expanded meaning:

* Take error for each point
  (Error = Actual - Predicted)
* Square each error
* Add all squared errors
* Divide by number of samples

So:

```text id="mse2"
MSE = (Sum of all squared errors) / n
```

Why square?

* removes negative signs
* makes big mistakes more important
* makes optimization smooth

Goal:

> Lower MSE = better model

---

## Minimum Sample Requirement

For **m features**, minimum required samples:

```text id="min1"
m + 1
```

Why?

Because we need enough points to define the model properly.

Example:

For:

```text id="min2"
y = (m * x) + c
```

We have:

* m (slope)
* c (intercept)

So we need at least:

```text id="min3"
2 points
```

---

## How Linear Regression Learns

### 1. Gradient Descent

Idea:

* start with random values
* check error
* adjust weights step by step
* repeat until error becomes small

Update rule:

```text id="gd1"
New Weight = Old Weight - (Learning Rate * Error Direction)
```

Meaning:

* Learning Rate → how big each step is
* Error Direction → tells where error increases

So we move in the opposite direction of error.

---

### 2. Normal Equation

Direct formula method:

```text id="ne1"
W = inverse(X-transpose * X) * X-transpose * y
```

Meaning:

* calculates best weights directly
* no iterations needed

Downside:

* slow for large datasets

---

## When to use Linear Regression

Use it when:

* output is continuous
* relationship is roughly linear
* you want a simple model

Examples:

* price prediction
* salary prediction
* demand forecasting
* trend analysis

---

## Strengths

* very simple
* fast
* easy to understand
* good baseline model
* works well for linear relationships

---

## Weaknesses

* cannot handle complex patterns
* sensitive to outliers
* unstable when features are highly correlated
* may underfit complex data

---

## One-Line Summary

> Linear Regression = finding the straight line that gives minimum total error.
