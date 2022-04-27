# Data structure

A Data Structure is a way to store, organize, and manage information in a way that allows the programmer to easily access or modify values within them.

- Goal of a data structure:
    - Store information
    - Access and Manipulate that information

# BigO Notation

- A way to basically "Score" a data structure based on 4 criteria
- The most common function you might want from a data structure
    - Accesing elements
    - Searching for an element
    - Inserting an element
    - Deleting an element

Measuring those 4 things we can create a report card to decide which data structure is quicker, better for this algorithm.

A **Time Complexity equation** works by inserting the **size** of the data-set as an integer n, and returning the number of operations that need to be conducted by the computer before the function can finish.

N = The size of the data set (amount of elements contained within the data structure)

We always use the worst-case scenario when judging these data structures.

## Fastest
Best score a data structure can get is O(1).
No matter what the size of your data is, the task will be completed in a single instructio:
- when we graph volume of data vs # of instructions required,the # of oeprations remains constant

## Next fastest
O(log n)

Gets more efficient as the size of the data set increases

Binary search

## 3rd fastest
O(n)

Linear, every element added, the amount of operations increases by the same amount.
10 elements, 10 operations required etc...

## First with bad efficiency

O(n log n)

If size of the dataset increases the operations needed increases with the amount of volume provided.

## Very bad efficiency

O(n^2) O(2^n)

The larger the dataset, the more inefficient.

# Stack

LIFO Principle

Last in first Out

Last elemenet pushed, first element popped of.

Last one added is the first to go out too.

**Recursion

Methods: Pop, Push, Peek, Contains

Common stack usages: Redo/undo buttons, go back button, stacking the history of browsing (Facebook, Twitter, Instagram), when going back it just removes the last added (Facebook, Twitter)

# Queue

FIFO Principle

First in first out

First element addded to the queue is the first one to be removed.

First element in the list is the first to go out

Methods: Enqueue, dequeue, peek, contains

Common queue usages: Job scheduling, printer queueing, modern cameras

# Linked list

Only able to traverse forwards

**Sequential access** linear data structure in which every element is a seperate **object** called a **Node**, which has 2 parts
- The **data**
- The **reference** (or **pointer**), which points to the next **Node** in the **List**

Node = data (strings, integers) + reference/pointer (where the next node in the linked list is)

# Doubly linked lists

Able to traverse both forwards and backwards using pointers

**Next**: that particular nodes pointer which points to the next object in the list
**Previous**: that particular nodes pointer which points to the previous object in the list

Each node has two pointers instead of one as a linked list.

