# name-num

One of the final projects for a DevOps class I'm taking has the following specification:

> There is a requirement to be able to convert an integer into words. For example, 57 needs to be converted into “fifty seven”. The objective of this project is to develop a method which can convert the numbers 1 through 999 to words. If you have time extend the range up to 2 billion. The method needs to be developed using Test Driven Development (TDD). A standalone application is also required which reads a number from the keyboard and prints out its value in words or “Invalid number”. The program should exit when the user enters 0. The application needs to be packaged as an executable jar file using Ant.

While I'm only about halfway through the class (there are about 2.5 weekends yet) and this needs to be an executable jar file packaged with Ant, I figured I'd get a head start and work out the programming logic. Rather than craft everything with pseudo-code only, I realized this would be a great opportunity to practice Python, which I'm also learning, while tackling a real problem.

Once I get closer to the course completion and complete some other projects, I'll translate this from Python to Java.

Incidentally, since this makes use of recursion, it wasn't really possible to _stop_ it from functioning past 2 billion (the extended use case describe), nor do I see a reason to. I'm elated to see the script translate 1 trillion as "1 thousand billion". Adding additional period names (I discovered each group of three numbers is called a "period") would be trivial.
