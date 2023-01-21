# collatz-conjecture
> Research based around a simple yet fascinating, repetitive piecewise function.

This repository contains multiple scripts that help explore and perform tests on numbers to try and prove the collatz-conjecture. I tried to optimize the scripts as best I could to be able to run more operations for testing, however, there is no discovered real way to test all numbers quickly.

Since most scripts in the repository are built with Python 3.10, I would suggest using PyPy3 for faster run-times. <br>
PyPy is a python compiler which compiles the python scripts and runs the compiled scripts making it as fast as any other low-level programming language like C.

## Collatz Conjecture
The simple piecewise function, caused such large commotion and has gone unsolved for over 8 decades. The simple 3x + 1 problem was rumored to be a Soviet trap designed to slow down American mathematics and science during the space race between the two nations. It was proven ot be effective because even after 8 decades, mathematicians are still working towards the problem by writing scripts to test numbers and catch any edge cases which break the conjecture.

The piecewise function for the 3x+1 problem looks like this: <br>
![collatz](https://user-images.githubusercontent.com/47650058/213839714-65a8a625-9bfb-4924-92df-64a67f2875a9.png) <br>
*If x is even, `f(x) = x/2`, but if x is odd, `f(x) = 3x+1`. This function is infinitely recursed upon to form a sequence of numbers.*

*For Example: <br>
f(3) = 10 -> <br>
f(10) = 5 -> <br>
f(5) = 16 -> <br>
f(16) = 8 -> <br>
f(8) = 4 -> <br>
f(4) = 2 -> <br>
f(2) = 1 -> <br>
f(1) = 4 -> <br>
...this then falls into a never-ending loop of `4 - 2 - 1`*

### Definitions
Dropping Time / Delay = Amount of steps to reach 1 from n in the sequence. <br>
Glide = Amount of steps to reach a number stricly less than n in the sequence. <br>

Convergent Sequence = The sequences reaches 1 eventually. <br>
Divergent Sequence = The sequence infinitely increases. <br>
Cyclic Sequence = The sequence never reaches 1 nor is it increasing towards infinity. <br>

### Operations
`& (Bitwise AND Operation)` = Performs AND Operation over the binary expression of 2 base-10 integers. (`101001 & 1 = 1`) <br>
`>> (Bitwise Right Shift Operation)` = Right shifts the binary expression of a base-10 integer. (`10110 >> 2 = 101`) <br>
`n & 1` => Determines whether n is even or odd. If `n&1 = 0`, n is even, but if `n&1 = 1`, n is odd. <br>
`n >> 1` => Basically divides n by 2. By removing the last digit in the binary expression, all bits were shifted down by 1 and divided the value of each bit by 2. This divides the value of the whole number by 2.

*The main reason I used these operations rather than traditional and conventional operations was for faster runtime speeds.*

### Conjecture Verification
The Collatz conjecture states that the orbit of every number under function f eventually reaches 1. This has been proven to be true for the first 2^68 whole numbers after computational testing and verification. Despite being a large number, this covers almost nothing on the real number line and it is not sufficient to prove the conjecture entirely.

I have written some scripts for Collatz Conjecture Verification in Python3 and C++ to test some numbers on my own.

`conjecture_verification.py` and `conjectureVerification.cpp` is just optimized brute-forcing towards the problem with a little bit of Dynamic Programming involved since we use the dropping time/delay (*amount of steps to reach 1 from n*) of previous values to find the dropping time of our current value. For Example:
Lets say D(n) = the dropping time for the value of n. <br>
When we are calculating for D(4), we can find the next number in the sequence which is `n=2`. If D(2) has already been calculated, we can correctly say that D(4) is equal to `D(2) + C`, `C` being the amount of steps to get from n to that already calculated value.

`convergence_verification.py` uses a much more optimized algorithm which only verifies whether numbers are convergent. This removes the necessity to calculate each number's dropping time. The algorithm also uses sieves (sliding windows) to check smaller ranges over time and build a list of numbers with abnormally large glide values instead of checking the dropping times of all numbers in the sieve. With the threshold limit of 2^8, and a sieve size of 2^20, the convergence algorithm was able to successfully verifiy 2^22 numbers in `3.02` seconds with normal Python 3.10 compilers. Using this algorithm with C++ or PyPy3 compilers could reduce the runtime significantly.

### Graphing Visualizations
`benfords_law.py` attempts to grab all the frequencies of the first digits in the step numbers and adds them to a histogram. For the first 100000 numbers, if you track the frequencies of the first digits of numbers in each step and draw a histogram we see a unique shape. 1 being the most frequent and 9 being the least frequent and there's an exponential curve in between. This curvature is more commonly known as Benford's Law and can be found in many use cases in our daily lives. *Sorry for the weird formatting! I couldn't figure out how to fix it...* <br>
![image](https://user-images.githubusercontent.com/47650058/206950303-edd5a2ba-06e4-458f-ab60-fcc2d77a09d0.png) <br>

`delay_graph.py` graphs the relation between n (x-axis) and n's delay (y-axis). This relationship creates a weird graph which has no distinctive shape and we can't express their relation with just 1 simple math expression because of it's complexity. <br>
![image](https://user-images.githubusercontent.com/47650058/207048613-27a3a445-303c-4211-9a0e-596b62153d00.png)

`glide_graph.py` graphs the relation between n (x-axis) and n's glide (y-axis). This relationship shows a very frequent pattern of occuring between powers of 2. A glide of 1 shows up for every even number since it's first move returns a step that is lower than itself, so it occurs every 2^1. Similarly, a glide value of 3 shows up in a pattern of every 2^2. A glide value of 6 shows up in a pattern that occurs every 2^4 and this pattern continues on forever with the glide values. <br>
![image](https://user-images.githubusercontent.com/47650058/207049744-2e985e6e-e2a3-4d9f-be53-3e918eca870d.png)

### Glide Patterns
We notice the pattern in `glide_graph.py` script but the steps in the glide seem almost random. It jumps from 1 to 3 to 6 to 8 to 11 and so on. So, I decided to create a table of every glide value of n (within a range of 0-10000) in order to find any patterns with the glide values. So, I recursed through all numbers in the range and added their glide values to a set (to remove duplicates). After adding all glide values to a set, I sorted the set and indexed every glide values from 1-10000. I found a noticeable pattern in the sorted set of glide values lying within the differences between each glide. The differences between each glide formed a `2-3-2-3-2-3-3-2-3-2-3-3` pattern which is also commonly known as a 12-layer octave pattern (found in piano keys). This proves that all glide values must be finite. For a second, you might think "the conjecture hasn't been proven because even though all glide values are finite the glide step could be divergent." But in fact, that is incorrect because if the number at the glide step is divergent, then the glide for that number is infinite which can be proven to be false. If this does actually prove that real numbers can't be divergent, there is still the possibility of a number being cyclic so this doesn't prove the collatz conjecture. The glide sequence has also been compiled down to this single function: `f(n+1) = floor(1 + n + n*log(3)/log(2))`

### Calculator
If you want to test numbers of your own quickly, the `collatz_calculator.py` script is what you are looking for. You can calculate and measure information about any number (as large as you want) rapidly. Given a number through input, it will calculate the numbers, delay, glide, residue, strength, level, shape of its path, etc. <br>
*The number is most likely divergent if the calculator takes more than 3 seconds to measure all parameters for a number.* <br>
![image](https://user-images.githubusercontent.com/47650058/207081206-84279d2d-543f-4943-b096-f5796f34c024.png)

### Terras Theorem
**Statement**: Let M be a positive integer. Let D(M) be the fraction of numbers < M that do not have finite stopping time. Then the limit of D(M) for M → ∞ is equal to 0. <br>
Essentially, the Terras Theorem states that the Delay Record as n approaches infinity decreases towards 0.
`terras_theorem.py` returns a number's glide value and the parity vector of its stepping sequence. You can then check these with the [Delay Records Table](http://www.ericr.nl/wondrous/delrecs.html) that has already been compiled for large numbers and find the Delay Record.

### Arithmetic Mean
`arithmetic_mean.py` generates all points for each step in the number sequence from n with the x-axis being the step count and the y-axis being the value of the number in the sequence at that step count. <br>
For example, if `n=4` the points generated would be: `(1,4), (2,2), (3,1)` <br>
With these coordinates, we would like to find the average amount of decrease or increase between each step that is taken in the sequence to see if we can prove that every number is bound to decrease. To find the average amount of increase/decrease between each step, we draw a line of best fit for all coordinates in each step and then find the slope of that line. We have to find the slope of this line for multiple numbers to find the average over all values. For the first 10000 natural numbers, the average amount of decrease is calculated to be roughly about `-0.13792251144898038`

## Installation
Some scripts such as `delay_graph.py`, `glide_graph.py` and `benfords_law.py` use the matplotlib package for the graphing user interface which is very useful and simple to use.

To be able to use the `matplotlib` library with the python scripts, you have to install the package. This can be done through a package installer with the `matplotlib` package available like pip. Learn how to install a stable version of [pip](https://pip.pypa.io/en/stable/installation/). <br>
You can run either of the following commands to install the `matplotlib` package onto your virtual environment (venv): <br>
```console
$ pip install matplotlib
$ python -m pip install matplotlib
$ python3 -m pip install matplotlib
```
If you are using a Python version that comes with your Linux distributation, you can also install the `matplotlib` package via your distribution's package manager.
```console
$ sudo apt-get install python3-matplotlib  # Debian / Ubuntu
$ sudo dnf install python3-matplotlib  # Fedora
$ sudo yum install python3-matplotlib  # Red Hat
$ sudo pacman -S python-matplotlib  # Arch Linux
```

## Sources
http://www.ericr.nl/wondrous/ <br>
https://oeis.org/A122437 <br>
https://youtu.be/094y1Z2wpJg <br>
https://youtu.be/i4OTNm7bRP8 <br>

----

*Created by BooleanCube :]*
