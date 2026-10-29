"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""



#1.In: A sentence from the user
#2.Process: Transform the sentence in four ways
#3.Out: Four different versions of the sentence
#4.My transformations: upper for capitals, lower for small letters, strip for spaces, replace for changing word

# Your code below

sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Without extra spaces:", sentence.strip())
print("Replace Paris with London:", sentence.replace("Paris", "London"))