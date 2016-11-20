# Foreword

I'm not going to _reinvent the wheel_ so this introduction to Python will be based on already existing and great tutorials available on web.
At the beginning I have to also emphasise that some concepts and ideas are explained more on offline workshops by me, so just keep in mind that content available here is more of a reminder than a learning material _per se_. This introduction is (without bigger changes) bases on [this](https://learnxinyminutes.com/docs/python3/) introduction to Python3.

And so, without further ado, let's begin!

# Introduction
Python was created by Guido Van Rossum in the early 90s. It is now one of the most popular languages in existence, and definitely one of the most fun to code in.
We will go through fundamentals and try to solve exercises as we progress through.

1. Primitive Datatypes and Operators
2. Variables and Collections
3. Control Flow and Iterables
4. Functions
5. Modules
6. Classes
7. Advanced

# Exercises
Exercises are in order that should represent progress of each section.
You can read modules first and then try to solve exercises, or the other way. It's up to you. Just keep in mind that not always everything covered by modules will be sufficient to solve problems listed below.
**Extra** sections are short exercises that relate to problem but try to emphasise some key concepts that might be overlooked at first sight.

### 1. Factorial
_Because each and every programmer loves when things get big really fast. It's time to do so._

1. Write `rec_factorial` function **using simple recursion**.
2. Write `iter_factorial` function **using while or for loop**.
3. Write `list_factorial` function that will return **list of first n factorials inclusive**

**Extra:**

1. Try to break your code by passing an invalid value to functions. What happens, and why? What can you do to avoid this kind of errors?
2. Well, factorial of 5 is only 3 digits wide, how about 100 factorial? There should be an overflow, shouldn't it? Just like in C or Java. What happens?
3. `list_factorial` can be written in at least two ways. Which one is more efficient and why?
4. It is possible to write write factorial function in recursive form but using accumulator. Try to write `acc_factorial`

### 2. Fibonacci
_What about all time favourite programming assignment? Let's see how difficult it will be using Python._

1. Write `rec_fibonacci(n)` function **using simple recursion**.
2. Write `acc_fibonacci(n)` function **using recursion with accumulator**.
3. Write `iter_fibonacci(n)` function **using while or for loop**.
3. Write `list_fibonacci(n)` function that will return **list of first n fibonacci numbers inclusive**.

**Extra:**

1. Try to break your code by passing an invalid value. Did you implement function in such way that it won't break when passed variable is string literal?
2. There is one other way to calculate fibonacci number. Can you implement it `root_fibonacci`? _(hint: sqrt(5) )_ Can you write another function to check for which _n_ the difference between exact value and calcualted by this function is greater than some given _delta_?

### 3. Primes
_What's not to love in prime numbers? I don't know either..._

1. Write `is_prime(n)` function **in best known way**.
2. Write `erastotenes(n)` function that return **list of only prime numbers from set of 0 to n (exclusive)**.

**Extra:**

1. Try to break your code. What about negative integers?
2. Look at `range` function and check if you can use its full potential in iterating over sequences by given step.
3. Look at `map` function. Write function `only_primes([int])` that filters input list and returns list of only prime numbers from it.
4. There is a probabilistic way to check if number is prime. Try to implement Miller-Rabin primality test (`miller_rabin_test`).

### 4. Frequency counter
_We all love books, don't we? Well if you don't, you should at least pretend to do so..._

1. Write function `most_used(file, count)` that reads text file from input and returns list of _count_ most used words from _file_ and number of its occurrences. Let's assuble that we split text into words on whitespaces only. _(hint: dictionaries and sorting lists might be useful)_

**Extra:**

1. Can you write this code in fewer lines?
2. Using appropriate module you can define list of characters that will represent word separators (default `.split()` works on whitespaces). Modify your program so that words will be split on each character from defined list.

### 5. I'm terrible at remembering names...
_Well, I probably won't remember yours... `:(`_

 1. Create dictionary `friends`  where `key == name && value == special_trade` of all your friends.
 2. Create list `friend_names` that only contains only names of your friends.
 3. Create list `special_trades` that contains only those trades that no one else has.
 4. Create new dictionary that is `name: [trades]`. 
 5. Each person whom name starts with letter **A** gets new `awesome` trade.

**Extra:**
``` python
a = ["Awesome", "Awesomeness"]
b = [a for _ in range(3)]
b.append(["Awesome", "Awesomeness"])
a.append("End")
print(b)
```

### 6. First real homework
_I know it's not mandatory course, but hey! I need to know if you understand anything so far. `:)`_

 1. Copy this dictionary into your python file (module). I apologise if some data is incorrect, my memory is not perfect :)
 ```
 # Dictionary that represents students from last class.
 # Key: unique id, Value: (name, semester, list of favorite OS's) 
 students = {
    0: ("Adam", 7, ["Linux", "Windows 10", "Mac OS"]),
    1: ("Konrad", 3, ["Linux"]),
    2: ("Monika", 3, ["Linux", "Windows"]),
    3: ("Piotrek", 3, ["Linux"]),
    4: ("Kuba", 3, ["Mac OS"]),
    5: ("Krzysiek", 3, ["Linux"]),
    6: ("Krzysiek", 3, ["Windows 10"]),
    7: ("Adam", 1, ["Windows 10"]),
    8: ("Marcel", 1, ["Windows 10"]),
    9: ("Paulina", 1, ["Windows 10"]),
    10: ("Sebastian", 1, ["Windows 10"])
 }
 ```
 2. Write function `students_count(students)` that returns number of students in class
 3. write function `was_present(students, name)` that returns `True` only if someone of given `name` was on last class.
 4. Write function `unique_was_present(students, unique_id)` that returns `True` only if someone of given `unique_id` was on last class.
 5. Write function `get_all_by_name(students, name)` that returns sub-dictionary of students of given name.
 6. Write function `get_all_by_semester_range(students, sem_from, sem_to)` that returns sub-dictionary of students that are on any semester starting from `sem_from` up to `sem_to` inclusive.
 7. Write function `how_many_use(students, os_name)` that returns how many students use `os_name` operating system.
 8. Write function `get_all_names(students)` that returns list of all the names of students.
 

### 7. Like a gentleman
_With class..._

 1. Create `Classroom` class that has contains list of `Students` but has maximum number of students allowed (constructor parameter).
 2. Each `Student` has unique id number, first and last name, and list of courses in current semester.
 3. Add `add_student`, `remove_student`, `has_student` methods to `Classroom` class where argument is **object of `Student` class**.
 4. Throw  `AlreadyInClassroomException` exception if someone tries to add student of the same id as already in student list.
 5. I know that I said _list of `Students`_ but now I want to hold those objects in dictionary. (What should be used as key?)
 
``` python
class SomeClass(object):
    def __init__(self, a, b = 5, c = []):
        self.a = a
        self.b = b
        self.c = c      # This is mad!
```

