# 203Hotline 📞

Welcome to **203hotline**.

This project focuses on analyzing the probability of line overload in a telecommunication system using binomial and Poisson distributions.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** When necessary, via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 203hotline

## Project Overview 🔎

The goal of 203hotline is to create a program that computes the probability of hotline overload using statistical distributions.

The project involves calculating combinations and assessing overload probabilities for a given number of simultaneous calls.

### Key Features

- **Combinations Calculation:** Compute the number of combinations for a given set size.
- **Binomial Distribution:** Calculate and display the binomial distribution for a given number of simultaneous calls.
- **Poisson Distribution:** Compute and display the Poisson distribution as an alternative to binomial distribution.
- **Overload Analysis:** Analyze and report the probability of line overload.
- **Performance Measurement:** Compute and display the computation time for each distribution.

### Usage

```
∼> ./203hotline -h
USAGE
./203hotline [n k | d]
DESCRIPTION
n   n value for the computation of C(n, k)
k   k value for the computation of C(n, k)
d   average duration of calls (in seconds)

```

### Exemples

```
∼> ./203hotline 100 18
18-combinations of a set of size 100:
30664510802988208300

∼> ./203hotline 180
Binomial distribution:
0 -> 0.000 1 -> 0.000 2 -> 0.000 3 -> 0.000 4 -> 0.000
5 -> 0.000 6 -> 0.000 7 -> 0.000 8 -> 0.000 9 -> 0.001
10 -> 0.002 11 -> 0.004 12 -> 0.008 13 -> 0.013 14 -> 0.021
15 -> 0.030 16 -> 0.041 17 -> 0.053 18 -> 0.065 19 -> 0.075
20 -> 0.082 21 -> 0.085 22 -> 0.085 23 -> 0.081 24 -> 0.074
25 -> 0.064 26 -> 0.054 27 -> 0.044 28 -> 0.034 29 -> 0.026
30 -> 0.019 31 -> 0.013 32 -> 0.009 33 -> 0.006 34 -> 0.004
35 -> 0.002 36 -> 0.001 37 -> 0.001 38 -> 0.000 39 -> 0.000
40 -> 0.000 41 -> 0.000 42 -> 0.000 43 -> 0.000 44 -> 0.000
45 -> 0.000 46 -> 0.000 47 -> 0.000 48 -> 0.000 49 -> 0.000
50 -> 0.000
Overload: 21.4%
Computation time: 1.71 ms
Poisson distribution:
0 -> 0.000 1 -> 0.000 2 -> 0.000 3 -> 0.000 4 -> 0.000
5 -> 0.000 6 -> 0.000 7 -> 0.000 8 -> 0.000 9 -> 0.001
10 -> 0.002 11 -> 0.004 12 -> 0.008 13 -> 0.013 14 -> 0.021
15 -> 0.030 16 -> 0.042 17 -> 0.053 18 -> 0.065 19 -> 0.075
20 -> 0.082 21 -> 0.085 22 -> 0.085 23 -> 0.081 24 -> 0.073
25 -> 0.064 26 -> 0.054 27 -> 0.044 28 -> 0.034 29 -> 0.026
30 -> 0.019 31 -> 0.013 32 -> 0.009 33 -> 0.006 34 -> 0.004
35 -> 0.002 36 -> 0.001 37 -> 0.001 38 -> 0.001 39 -> 0.000
40 -> 0.000 41 -> 0.000 42 -> 0.000 43 -> 0.000 44 -> 0.000
45 -> 0.000 46 -> 0.000 47 -> 0.000 48 -> 0.000 49 -> 0.000
50 -> 0.000
Overload: 21.5%
Computation time: 0.34 ms
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `./203hotline [n k | d]`.
4. For detailed guidelines, refer to `203hotline.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
