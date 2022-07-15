Question 1. Use the `data.info()` and ` data.head()` commands to examine the columns of
the dataframe. The dataset contains:

- [] a) only numerical features
- [] b) only categorical features
- [x] c) both numerical and categorical features

_Select a single answer_

---

Question
Why do we need two sets: a train set and a test set?

- [] a) to train the model faster
- [x] b) to validate the model on unseen data
- [x] c) to improve the accuracy of the model


_Select all answers that apply_

---
Question
The generalization performance of a scikit-learn model can be evaluated by:

- [x] a) calling `fit` to train the model on the **training set**, `predict` on the
  **test set** to get the predictions, and compute the score by passing the
  predictions and the true target values to some metric function
- [] b) calling `fit` to train the model on the **training set** and `score` to compute
  the score on the **test set**
- [x] c) calling `cross_validate` by passing the model, the data and the target
- [] d) calling `fit_transform` on the data and then `score` to compute
  the score on the **test set**

_Select all answers that apply_

---
Question
When calling `cross_validate(estimator, X, y, cv=5)`, the following happens:

- [x] a) `X` and `y` are internally split five times with non-overlapping test sets
- [] b) `estimator.fit` is called 5 times on the full `X` and `y`
- [x] c) `estimator.fit` is called 5 times, each time on a different training set
- [] d) a Python dictionary is returned containing a key/value containing a NumPy
  array with 5 scores computed on the **train sets**
[x] e) a Python dictionary is returned containing a key/value containing a NumPy
  array with 5 scores computed on the **test sets**

_Select all answers that apply_

---
Question
Cross-validation allows us to:

- [] a) train the model faster
- [x] b) measure the generalization performance of the model
- [] c) reach better generalization performance
- [x] d) estimate the variability of the generalization score

_Select all answers that apply_

---
