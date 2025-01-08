### Good Number

Given an array of integers `B`, and an integer `L` find number of Good .

Element `Y` is Good if there exists at least 1 element whose difference with `Y` is less than `L` i.e. an element `Y` is Good, if there is another element in the range `(Y-L, Y+L)` other than `Y` itself.

---

#### Input Format
- First line contains two integers `M` and `L` respectively.
- Second line contains `M` integers separated by space.

---

#### Output Format
- Print a single integer denoting the total number of joyous elements.

---

#### Constraints
- 1 <=`M`<= 1000
- 0 <=`L`<= 1000
- 0 <=`B[i]`<= 1000

---

#### Explanation
Let's take an example:

```
6 4
5 5 7 9 15 2
```

Other than number 15, everyone has at least 1 element in the range (Y-4, Y+4). 
Hence, they are all Good elements. 
Since these are five number, the output is 5.

---