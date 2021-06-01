# Overview

This is a simple python program that connects to a given Google Firebase cloud database, and gives the option to add and view the names of people.

I wanted to be able to learn how cloud databases work, and how to modify them from my computer.

[Software Demo Video](https://youtu.be/TtxJLAUBo00)

# Cloud Database

I am using Google Firebase to store data.

The database's structure is probably a bit too simple. Each time a name is entered, the program creates a new document based on the last name, and adds the first name and last name to it.

# Development Environment

I used Python, the commandline interface, and the Firebase interface.

Aside from the Firebase and google cloud libraries, I also used os to set a local variable.

# Useful Websites

* [Firestore documentation](https://firebase.google.com/docs/firestore)

# Future Work

 * If we try to add a person with the same last name as someone else, the first person will be overwritten. This can be solved by adding a unique ID to each entry.
 * I'd like to add the ability to delete entries in the future, too.