#Part 4 - Concept Questions

##1. What is the role of a class in a linked list?

A class is a blueprint/template for creating objects. In a linked list, the Node class is used to create nodes and the LinkedList class is used to manage the whole linked list

##2. What is the difference between a node and a linked list?

A node is a single element that stores data and a link to the next node while a linked list is a collection of the connected nodes

##3. Why do we use None in next?

None means there is no next node connected. When a node is first created, it is equals to none. This shows that the node is not linked to another node or its is the last node in the list

##4. How is a linked list different from a Python list?

A python list stores items in a continuous memory while a linked list stores data in separate nodes

A python list is faster to access due to its index while a linked list is slower to access

It is difficult to insert items in the middle in a python list while in a linked list, it is easier to insert nodes in the middle

##5. Why is OOP useful for data structure?

OOP lets us bundle the data and methods together in one class. It makes the code easier to reuse and extend. Therefore, it is easy to manage complex structures easily. For example, in a linked list,
a Node object stores the data and the next node and the LinkedList object contains methods like append(), display(), and search().
Instead of writing separate code everywhere, OOP groups everything neatly inside classes.