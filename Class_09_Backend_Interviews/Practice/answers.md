**CI/CD Questions**

1. What is CI/CD? What are some good CI/CD practices?
    - CI stands for continuous integration. This concept ensures the regular building and testing of a program. CD stands for continuous delivery. This concept refers to the ongoing development of a program ahead of production. Good practices include the following principles:
        - Commit early, commit often
        - Keep the builds green
        - Build only once
        - Streamline your tests
        - Clean your environments
        - Make it the only way to deploy to production
        - Monitor and measure your pipeline
        - Make it a team effort

2. What are the differences between continuous integration, continuous delivery, and continuous deployment?
    - Continuous integration ensures the regular building and testing of a program. Continuous delivery ensures the ongoing development of a program ahead of production. Lastly, continuous deployment ensures your code is constantly being deployed to dev, stage, and prod environments with appropriate test checks.

3. What is blue/green deployment?
    - This is a continuous integration technique that consists of having two identical production environments. One of the environments is deployed and is in immediate use. The other environment is updated with new features and also tested. When the tests are successful the team will swithc from the first environment to the second environment.

**Cloud Questions**

1. What does high availability mean?
    - The ability of a system to be running with no failures for a given amount of time.

2. What does high durability mean?
    - The ability of a storage service to safely store data without losing data.

3. What does cloud hosting mean?
    - The use of computer system resources without direct management by a user.

**Containerization Questions**

1. What is containerization?
    - Containerization is a form of virtualization in which programs are run in contianers that utilize the underlying power of an operating system.

2. What are the benefits of Docker?
    - Docker allows you to run applications across varying operating systems without needing to constantly change code and configurations. It also allows applications to be deployed and scaled with relative ease.

**Database and SQL Questions**

1. What is a NoSQL database and what are some use cases for one?
    - Unlike a relational database, a NoSQL database does not use tables to organize its data. Data is stored in objects that can vary in size, structure, and types.
    - NoSQL databases are a good choice when:
        - You have a large volume and variety of data
        - Scalability is a top priority
        - You need continuous availability
        - Working with big data or performing real-time analytics
    - For example a NoSQL database would be good for Internet of things (IoT) and sensor data or a messaging service.

2. What is SQL injection?
    - SQL injection is the placement of malicious code in SQL statements, via web page input.
    - SQL injection is a code injection technique that might destroy your database.
    - SQL injection is one of the most common web hacking techniques.

3. What is the difference between JOIN and UNION?
    - A JOIN is used to combine data from two tables based off a related column. On the otherhand, a UNION is used to combine two result SELECT statements together.

4. If you have a limited amount of memory, how would you handle a large amount of data?
    - When processing the data one could split the data into smaller portions. However, at a certain point you might need to allocate more memory to process a large amount of data. You could also use a big data platform such as Hadoop.

5. What does normalization mean in reference to datbases?
    - Normalization is the restructuring of a relational databases based on a series of rules called forms. 
        - First Normal Form: Each table cell should contain a single value. Each record needs to be unique.
        - Second Normal Form: Be in first normal form. Single Column Primary Key that are not functionally dependant on any subset of candidate key relations.
        - Third Normal Form: Be in first two normal forms. Also, the database has no transitive functional dependencies.

7. How do you improve a database query?
    - Avoid multiple joins in a single query
    - Eliminate cursors from the query 
    - Creation and use of indexes
    - Drop unused indexes

8. What is an ORM?
    - ORM stands for Object Relational Mapping. An ORM convert incompatible data types. An ORM creates virtual objects. For example, MYSQL is transformed into an object that can be stored and altred in a programming language.

9. What is DOA?
    - DOA provides an abstract interface for a database. By mapping application calls by an additional layer, the DAO provides data operations without exposing details of the database.

10. What is the ACID property of a system?
    - ACID stands for atomicity, consistency, isolation, and durability. These principles are applied to databases and their transactions. Atomicity means that each transaction is a single unit that happens once or doesn't happen at all. Consistency means the database should be consistent before and after a transaction. Isolation means that multiple transactions can happen the same time on a database without changing the consistency of a database. Durability means the data of a database or stored and peristent after transactions.

**Data Structure Questions**

1. What is and what are the benefits of using a graph?
    - A graph is a set of nodes (vertices) and a set of connections (edges) which define relations between nodes. The graph allows one to represent spefic domains such as city layouts or networks as a data structure. A major advantage of using a graph is one can apply graph algorithms to the graph.
        - Space Complexity
            - Adjacency Matrix: O(V^2)
            - Adjacency List: O(V+E)
            - Edges List: O(E)
        - Time Complexity
            - Connection Checking
                - Adjacency Matrix: O(1)
                - Adjacency List: O(N)
                - O(E)
            - Neighbors Findiing
                - Adjacency Matrix: O(V)
                - Adjacency List: O(N)
                - Edges List: O(E)

2. What is and what are the benefits of using a binary tree?
    - A binary tree is a hierarchical tree-based data structure in which each node has at most two children. The root node is the top most node of the tree. Each node can have a left or right node. Links between nodes are called branches. A node without children nodes are called leaf nodes. The main advantage of a binary tree is simplicity. They are used to reflect relationships between data and can store an arbitrary number of data values.
        - Access: O(log(n))
        - Search: O(log(n))
        - Insertion: O(log(n))
        - Deletion O(log(n))

3. What is and what are the benefits of using a tuple?
    - A tuple is a fixed data structure that usually allows one to store two values. The data structure is often immutable and cannot be changed once they are assigned. Python has a built in tuple data structure.
        - Time Complexity
            - Find an element: O(1)

4. What is and what are the benefits of using a set?
    - A set is a data structure that can store any number of unique values. The major benefit of a set is that it does not store duplicate values. Sets reduce the amount of need to check for duplicates. 
        - Time Complexity
            - O(log(n)) or O(1)

5. What is and what are the benefits of using a dictionary?
    - A dictionary is a data structure used for storing a group of objects. A dictionary is a set of keys and their associated values. A dictionary is also called a hash, a map, or a hashmap depending on the language. Dictionaries are often extremely efficient in regards to accessing, searching, inserting, and deleting. They also are formatted in a readable way with key-value pairs.
        - Access: O(1)
        - Search: O(1)
        - Insertion: O(1)
        - Deletion O(1)

6. What is and what are the benefits of using a linked list?
    - A linked list is a data structure that contains elements that are not stored at contiguous memory locations. The elements in a linked list are linked using pointers. A linked list consists of nodes. Each node contains a data value and a reference to the next node in the list. A linked list is a dynamic data structure that can shrink and grow at runtime. Linked lists efficiently use memory. They are also good for implementing a stack or a queue. Insertion and deletion are also extremely fast. However, linked lists use more memory than an array because you must store a pointer. They also take longer than an 
        - Access: O(N)
        - Search: O(N)
        - Insertion: O(1)
        - Deletion O(1)

7. What is and what are the benefits of using a doubly linked list?
    - A doubly linked list is a linked list that not only has a pointer to the next node, but also a pointer to the previous node. Doubly linked lists make reversing the linked list much easier. The traversal of the linked list is also bidirectional. However, it uses more memory than an array or a normal linked list.
        - Access: O(N)
        - Search: O(N)
        - Insertion: O(1)
        - Deletion O(1)

8. What is and what are the benefits of using an array?
    - An array is a data structure that consists of a collection of elements, which are identified by an index. Arrays are easier to declare and use, can be used with most data types, and are useful for representing metrixs. However, depending on the language, an array may waste memory if all array elements are not used. Some arrays also can't accomodate new values. Arrays also are difficult to search because the entire array must be iterated through.
        - Access: O(1)
        - Search: O(N)
        - Insertion: O(N)
        - Deletion O(N)

9. What is the difference between a breadth-first search and a depth-first search?
    - Breadth First Search is a vertex based technique for finding a shortest path in graph. It uses a Queue data structure which follows first in first out. One vertex is selected at a time when it is visited and marked then its adjacent vertexs are visited and stored in the queue. It is slower than Depth First Search. In short, Breadth First Search goes level by level in a tree.
    - Depth First Search is a edge based technique. It uses the Stack data structure, performs two stages, first visited vertices are pushed into stack and second if there is no vertices then visited vertices are popped. In short, Depth First Search goes down the left side completely than back up to follow the same proceduce one path to its left until completed. 

10. How does a merge sort work? What is its time complexity?
    - Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves.
        - Time Complexity: O(NlogN)

11. How does a quick sort work? What is its time complexity?
    - QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.
        - Time Complexity: O(NlogN)

12. What is a stack overflow?
    - A stack overflow occurs when a computer or processor memory also called a stack is filled more than its capacity. 

13. How does an array differ from a stack?
    - Stacks are based on the LIFO principle whereas array is based on indexes. Stacks can insert at only at the top of the stack whereas arrays can be inserted at any index. Stacks are dynamic and arrays usually have a fixed size. A stack can only do linear search, but arrays can do linear and binary search. 

14. What is the difference between FIFO and LIFO?
    - FIFO stands for first in first out. A queue is an example of the FIFO principle. Elements are placed in a queue and the first element place in the queue is the next to be removed. LIFO stands for last in first out. A stack is an example of the LIFO principle. Elements are placed on the stack and the most recently placed element is the element next removed from a stack.

15. What is and what are the benefits of using an queue?
    - A queue is based on the FIFO so the element inserted at the first of the queue, is the first element to come off the queue. Queues are more flexible than an array. However, a queue can remove only elements from the beginning of the queue. 

**Framework Questions**

1. What does REST stand for?
    - REST stands for Representational State Transfer. After a client requests a resource, a RESTful API will transfer a representation of the state of the requested resource to the client. 

2. What are the DRY and DIE principles? Give an example.
    - DRY stands for Don't Repeat Yourself and DIE stands for Duplication is evil. In short, these two principles suggest that a developer should create efficient code that does not repeat itself.

3. Name some best practices for RESTful API design?
    - Accept and respond with JSON
    - Use nouns instead of verbs in endpoint paths
    - Name collections with plural nouns
    - Nesting resources for hierarchical objects
    - Handle errors gracefully and return standard error codes
    - Allow filtering, sorting, and pagination
    - Maintain Good Security Practices
    - Cache data to improve performance
    - Version your API

4. What is an MVC framework? Pros and cons?
    - MVC stands for Model View Controller. The Model is data, the View is the user interface, and the Controller is the business logic that bridges the View with the Model. 
    - Pros:
        - Development of the application becomes fast
        - Easy for multiple developers to collaborate on the application
        - Easy to update the application 
        - Easy to debug as there are multiple isolated levels
    - Cons:
        - It is hard to understand the MVC architecture
        - Must have strict rules on methods

5. What is an MVVM framework? Pros and cons?
    - MVVM stands for Model View ViewModel. Like MVC, the View is the user interface and the Model is the data for the application. MVVM differs from MVC though in how it implements the connection between the Model and the View. The ViewModel contains commands the View can initiate to interact with the Model. The major difference between MVVM and MVC is that MVVM does not allow the View to have direct contact with the Model. 
    - Pros:
        - Provide less direct connection between View and Model
        - Allows greater testability of view states
        - Allows better maintenance of complex view
    - Cons:
        - Overhead of writing binding code
        - Implementation can be more complex than MVC
        - Increases overall cost for a simple application

6. What is CAP theorem?
    - First, CAP stands for Consistency (all reads receive the most recent write), Availability (all reads contain data), Partition tolerance (system continues to operate despite network failures). However, the CAP theorem states that when a system hits a network faliure it can provide either consitency or availability, but not both. High consistency comes at the cost of lower availability and vise versa. One must make a choice when creating a system. 

7. What does SOLID mean?
    - SOLID is a collection of five common software design principles. The acronym stands for Single Responsibility Property, Open-Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.
        - Single Responsibility Property: Every class and module should only have one responsibilty.
        - Open-Closed Principle: Classes should be built in a way that one does not need to change the class, but just extend the class.
        - Liskov Substitution Principle: Every derived class should be substitutable for its parent class.
        - Interface Segregation Principle: It is better to have a lot of smaller interfaces than a few larger interfaces.
        - Dependency Inversion Principle: This principle offers a way to decouple software modules. Developers should depend on abstractions (use of intefaces), not on concretions (direct use of classes).

8. What is Agile development?
    - The agile development refers to a software development methodolgy, which focuses on iteration. Requirements and solutions are developed with each iteration of the project. The agile approach delivers value faster and the projects that utilize this methodology have a greater ability to respond to change.

**Language Questions**

1. How is Python interpreted?
    - Python is an interpreted language, which means the source code of a Python program is converted into bytecode that is then executed by the Python virtual machine.
    
2. How is C interpreted?
    - C is a compiled language, which means they are converted directly into machine code that the processor can execute.
 
3. How is Java interpreted?
    - Java does both compilation and interpretation, In Java, programs are not compiled into executable files. They are compiled into bytecode, which the JVM (Java Virtual Machine) then interprets and executes at runtime.

5. What is strong-typing and weak-typing? Which is preferred? Why?
    - Strongly typed languages do type checking such as C and Java. Weakly typed languages do not do type checking such as Javascript. Typed languages are often preferred because they protect against bugs and errors in a system.

**Miscellaneous Questions**

1. What is regex?
    - Regex stands for regular expression. Regex is a sequence of characters that specifies a search pattern in text. The expression is used to match, locate, and adjust text. The following is a regex example that can be used to match a phone number: ^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$. 

2. What is the difference between git fetch and git rebase, and git pull?
    - git fetch is a command that tells your local git to grab the latest meta-data info from the original. It does not do a file transfer, but checks for changes. git rebase changes the base of one's branch from one commit to another making it appear as if one had created your branch from a different commit. git pull copies changes from the remote repository.

**Object Oriented Programming Questions**

1. What is encapsulation? Give an example.
    - Encapsulation refers to the capturing of data and methods that alter that data into a single unit. The primary example of encapsulation is a class. A class is a structure that holds data and methods to alter that data. Encapsulation allows one to hide data. Encapsulation also makes code easier to reuse. This principle can also refer to restricting direct access to certain components of an object.

2. What is inheritance? Give an example.
    - Inheritance refers to one class inheriting the attributes and methods from another class. The original class is called the parent class and the class that inherits the parent classes properties is called the child class. For example, the car class could inherit from the vehical class or the cow class could inherit from the mammal class.

3. What is abstraction? Give an example.
    - Abstraction refers to the principle of handling complexity by hiding unnecessary details from the user. 
    Regarding object oriented programming, abstraction that hides the internal implementation details. For example, a developer would not see all the code behind the scenes for the python sort() function when they use it.

4. What is polymorphism? Give an example.
    - Polymorphism refers to the concept that one can access objects of different types through the same interface. Each type can provide its own independent implementation of this interface. For example, one class name can be used to reference multiple kinds of subtypes at the same time. A developer could create the object class Animal and define multiple subtypes such as cow, dog, cat, and bear. They all have the property color and the method eat(). 

5. What do you think makes object-oriented design the preferred approach?
    - There are several reasons that object-oriented design is desired. First, one can reuse code through inheritance. Also, the modularity of object-oriented design leads to easier testing. The design also simplifies the whole appliation by breaking it into manageable pieces.

**Opinion Questions**
1. What is difficult about writing code?
    - Writing code can be difficult because we often think faster than we can write code. Often when writing code one comes up with an overall solution but are unable to implement the solution because they do not break down the steps in a way for a computer to handle the problem.

2. What programming languages do you like to work with and why?
    - I like working with Python because it is simple to read and write. The language has tons of libraries and extensions to help one accomplish their programming goals. The language also is great for creating web APIs with powerful frameworks such as Django and Flask.

3. What is your approach to debugging?
    - First, I hopefully have logging set up, which can help me identify where my error is occuring. I will look at the error call stack to see what error is occuring and walk backwards through the call stack to find the general location of the error. Then I usually look at the code and determine what the code should be doing. After determining what the code should do I run through each line of code recording what is happening to find the error in the logic.

4. What is your most challenging project?
    - The most challenging project I have encountered was figuring out how to reduce the time a deployment pipeline was taking to execute. I had to monitor and analyze the pipeline to find major bottle necks. Then, I had to research possible solutions to reduce the time. I ended up parallelizing both the linting and testing processes. I also added improvements to Jenkins to parallelize builds. The project was challenging because I needed to understand a major code base and some complicated code to correctly improve the deployment process. However, I was able to gain help from co-workers to overcome this challenge. There were also a lot of possible solutions, but I was able to overcome that challenge by thorough research and addtional communication with co-workers.

5. Why would you use microservice architecture?
    - Microservices allow for continuous delivery. Each service is isolated, which makes it significantly easier to upate and improve individual services. Likewise, microservices help maximize deployment velocity. In addition, each service is in its own container, which gives developers the ability to dynamically change each service. Each service can be written in the language that is ideal for it. Microservices are also easier to maintain compared to a monolithic application. Monolithic projects can also be expensive to maintain and microservices can be much cheaper.

6. What’s important when checking a team member’s code?
    - First of all, one should check their team member's code to ensure quality and reduce bugs, errors, and code smells. When checking a team member's code one should first make sure the logic is correct. They should ask their team member what the goal of the code is to ensure the logic is sound. Additionally, the reviewer should go through each line of code and look at the codes dependencies.  

**Programming Questions**

1. What is a class?
    - A class is an object oriented structure that holds data and methods to alter that data.

2. What is a closure?
    - A closure is a function that can be stored as a variable also known as a referred to as a "first-class function. A closure has special ability to access other variables local to the scope it was created in.

3. What do classes and closures have in common?
    - Classes let you define fields and methods whereas closures store information about local variables from a function call. Closures is often more related to functional programming and classes are more related to object oriented programming.

4. What is an interface?
    - An interface is a structure or design that allows a program to enforce rules onto a class. An interface is a roadmap for a class that it must follow. For instance, a car must could implement a vehicle and the vehicle interface could state that the car must have certain attributes such as four wheels.

5. What is a ternary operator?
    - A ternary operator or ternary function is a short cut if else statement in lanugages such as Javascript, Python, Swift, ect. This operator allows for convient conditional statements in varying situations.

6. What is the difference between a function and a method?
    - Function is a set of instructions that perform a task where as a method is a set of instructions that are associated with an object.

7. What is an anynomous function? Why are they useful?
    - An anonymous function is a one-line function with no attached name or identifier. The advantage of an anonymous function is that it does not have to be stored in a separate file. Anonymous functions reduces the number of code files necessary for an application.

8. What is a callback function?
    - A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

9. What is functional programming?
    - Functional programming is a programming strategy that focuses on using function to run a program. It is a declarative programming structure where function definitions map values to other values. Functional programming does not focus on updating the running state of the program.

10. What is a generic?
    - Generics mean parameterized types. The idea is to allow type (Integer, String, … etc, and user-defined types) to be a parameter to methods, classes, and interfaces. Using Generics, it is possible to create classes that work with different data types. An entity such as class, interface, or method that operates on a parameterized type is called a generic entity. For example, you create a linkedlist of integers, but instead of repeating the code for a linkedlist of strings you can use a generic to create a linkedlist that passes in a type upon creating the linkedlist.

11. What is an abstract class?
    - In Java, an abstract class is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class). For example, an animal abstract class cannot be used to create an animal object, but a dog class could implement an animal class and that dog class could be used to make dog objects.

**Software Design Questions**

1. What is asynchronous programming?
    - Asynchronous programming is a form of parallel programming that allows a unit of work to run separately from the primary application thread. For example, you could have a main function running code that calls another function inside of it. Instead of pausing to have the inner function finish the outer function will continue running at the same time as the inner function.

2. What does the term seperation of concerns mean?
    - Seperation of concerns is a design principle that seperates components of a program into sections. This makes an application more readable and easier to maintain. 

3. What is the difference between Request/Reply and Publish/Subscribe models?
    - In the request-response model, a client requests data or services, and a server responds to the request by providing the data. Whereas in a publish-subscribe model a central source called a broker (also sometimes called a server) receives and distributes all data. Pub-sub clients can publish data to the broker or subscribe to get data from it—or both.

4. What does it mean to scale up vs scale down?
    - Scaling up or vertical scaling means adding more compute power to a specific server or instance. Scaling down or horizontal scaling means adding more servers or instances to your infrastructure. 

5. Why would you choose a microservice approach vs a monolithic app?
    - A microservice approach has independent components, which makes maintenence an individual components much easier. Also, microservices are easier to understand for developers working on them. In addition, each component in a microservice structure application can be scaled independently. 

6. Explain the differences between a Thread and a Process?
    - A process is a program which is dispatched from the ready state and are scheduled in the CPU for execution. A thread is the segment of a process. This means a process can have multiple threads and these multiple threads are contained within a process. A thread has three states: Running, Ready, and Blocked. 

7. What is the meaning of high cohesion?
    - Cohesion is the degree to which the elements inside a module belong together. A module is said to have high cohesion if it contains related elements. Modules with a single, well-defined purpose are easy to understand and much more readable.

8. What is a reverse proxy?
    - A reverse proxy server is a type of proxy server that typically sits behind the firewall in a private network and directs client requests to the appropriate backend server. A reverse proxy provides an additional level of abstraction and control to ensure the smooth flow of network traffic between clients and servers.

9. What is the meaning of loose coupling?
    - Coupling is the degree of interdependence between software modules. Two modules have low coupling or loose coupling if they are loosley connected. Loosely coupled modules are easier to develop and maintain. Since they are independent of each other, we can develop and test them in parallel. 

10. What is lazy loading? Give an example of using this principle.
    - Lazy loading (also called on-demand loading) is an optimization technique for the online content, be it a website or a web app. Instead of loading the entire web page and rendering it to the user in one go as in bulk loading, the concept of lazy loading assists in loading only the required section and delays the remaining, until it is needed by the user. For example, images at the top of a page are loaded first and only if a user scrolls down are other images loaded.

11. What is tight coupling?
    - Coupling is the degree of interdependence between software modules. Two modules have high coupling or tight coupling if they are tightly connected.

12. When should one use memoization?
    - Memoization is a programming technique that accelerates performance by caching the return values of expensive function calls. For example, you may have a function that you need to call frequently with certain input values, you can cache the output to accelerate the responses.

13. What is caching?
    - A cache is a data storage layer which stores a subset of data, so that future requests for that data can be accessed faster than through the data’s primary storage location.

**Software Design Pattern Questions**

1. What is a singleton? Give an example of when to use this principle
    - A singleton is a design pattern, which restricts the instantiation of a class to a single instance. This provides coordinated access to that one resource. Use cases for this pattern include factories, builders, and objects that hold program state. For example, a singleton can be used for a single database object shared by different parts a program. Another common example of using a singleton is a logger object that needs to be share among all parts of a program.

2. What is a factory? Give an example of when to use this principle.
    - 

3. What is an adapter design pattern? Give an example of when to use this principle.
    - 

4. What is a builder design pattern? Give an example of when to use this principle.
    - 

5. What is an observer design pattern? Give an example of when to use this principle.
    - 

6. What is a strategy design pattern? Give an example of when to use this principle.
    - 

**Test Questions**

1. What is a unit test?
    - A unit test tests one element or module in a computer program or application.

2. What is an integration test?
    - An integration test tests a group of elements or modules in a computer program or application. The test combines modules in order to validate the interactions between varying components.

3. What does it mean to mock a test? When should or shouldn't you mock a test?
    - 

**Web Questions**

1. What is a JWT? How does it work?
    - 

2. What are advantages of Web Services?
    - 

3. What is a sticky session?
    - 

4. What are and how does SSL/TLS work?
    - 

5. What is JavaScript and why is it used?
    - 

6. Define and explain these nine server response error codes: 200, 201, 204, 301, 400, 401, 404, 409 and 500
    - 200: 'Okay' or successful.
    - 201: 'Created'. The message means a resource was created at the client's request.
    - 204: 'No Content'. The message means the server didn't send back a status.
    - 301: 'Moved Permanently'. The message means a client-triggered action changed the resource location.
    - 400: 'Bad Request'. The error refers to a client-side error. 
    - 402: 'Unathorized'. The client did provide the correct authentication.
    - 404: 'Not Found'. The error means no mapped resource was found. 
    - 409: 'Conflict'. An inconsistent or impossible state.
    - 500: 'Internal Server Error'. This error indicates a server-side issue.

7. What does statelessness mean in regards to web services?
    - 

8. What is a TCP socket?
    - TCP sockets provide an open bi-directional connection between a client and server socket. The connection is uniquely identified using the combination of the client socket and server socket. The combination contains four elements: the client IP address and port, and the server IP address and port. For example, an HTTP request can be sent from the client socket 120.1.1.1:3022 from to the server socket 189.1.1.1:80. Major advantages of a TCP socket connection is that packets dropped in the network are detected and retransmitted by the sender and data is read in the order it was written by the sender.

9. What are some ways to make websites faster?
    - 

The following websites were used to gather questions as well as answer the provided questions:
- https://procoders.tech/blog/back-end-engineer-interview-questions
- https://www.jetbrains.com/teamcity/ci-cd-guide/ci-cd-best-practices
- https://github.com/arialdomartini/Back-End-Developer-Interview-Questions
- https://en.wikipedia.org/wiki/Cloud_computing
- https://www.datastax.com/blog/sql-vs-nosql-whats-the-difference
- https://www.w3schools.com/sql/sql_injection.asp
- https://www.indeed.com/career-advice/interviewing/back-end-interview-questions
- https://machinelearningmastery.com/large-data-files-machine-learning
- https://www.sqlshack.com/what-is-database-normalization-in-sql-server
- https://www.guru99.com/database-normalization.html
- https://www.developer.com/database/10-ways-to-improve-sql-query-performance
- https://en.wikipedia.org/wiki/Data_access_object
- https://www.redhat.com/en/topics/api/what-is-a-rest-api
- https://www.geeksforgeeks.org/acid-properties-in-dbms
- https://www.bmc.com/blogs/solid-design-principles
- https://www.codementor.io/@zmitry/graph-data-structure-for-web-developers-10xf9a93hs
- https://www.baeldung.com/cs/graphs
- https://www.baeldung.com/cs/binary-trees-vs-linked-lists-vs-hash-tables
- https://intellipaat.com/blog/tutorial/python-tutorial/python-tuple
- https://www.howtouselinux.com/post/tcp-socket
- https://en.wikipedia.org/wiki/Regular_expression
- https://ihateregex.io/expr/phone
- https://aws.amazon.com/caching
- https://www.sumologic.com/glossary/encapsulation
- https://www.analyticsvidhya.com/blog/2020/10/inheritance-object-oriented-programming
- https://stackify.com/oop-concept-abstraction
- https://www.geeksforgeeks.org/benefit-of-using-mvc
- https://betterprogramming.pub/what-is-a-singleton-2dc38ca08e92 
- https://refactoring.guru/design-patterns
- https://www.interserver.net/tips/kb/mvc-advantages-disadvantages-mvc
- https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design
- https://www.bmc.com/blogs/cap-theorem
- https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_1/Fundamentals_of_data_structures/Dictionaries
- https://www.geeksforgeeks.org/advantages-and-disadvantages-of-linked-list
- https://www.geeksforgeeks.org/advantages-disadvantages-and-uses-of-doubly-linked-list
- https://dare2compete.com/blog/advantages-and-disadvantages-of-arrays
- https://www.geeksforgeeks.org/merge-sort
- https://www.geeksforgeeks.org/quick-sort
- https://www.geeksforgeeks.org/difference-between-stack-and-array
- https://www.quora.com/What-are-the-advantages-and-disadvantages-of-a-queue-and-a-circular-queue
- https://www.cprime.com/resources/what-is-agile-what-is-scrum
- https://stackoverflow.com/questions/1326071/is-java-a-compiled-or-an-interpreted-programming-language
- https://www.roberthalf.com/blog/salaries-and-skills/4-advantages-of-object-oriented-programming
- https://shadow-soft.com/why-microservice-architecture
- https://stackoverflow.com/questions/3368713/whats-the-difference-between-closures-and-traditional-classes
- https://www.cs.utah.edu/~germain/PPS/Topics/interfaces.html
- https://www.codecademy.com/article/fwd-js-methods-functions
- https://www.sciencedirect.com/topics/computer-science/anonymous-function
- https://developer.mozilla.org/en-US/docs/Glossary/Callback_function
- https://en.wikipedia.org/wiki/Functional_programming
- https://www.geeksforgeeks.org/generics-in-java
- https://www.w3schools.com/java/java_abstract.asp
- https://stackify.com/when-to-use-asynchronous-programming
- https://blog.opto22.com/optoblog/request-response-vs-pub-sub-part-1
- https://opsani.com/blog/scale-up-vs-scale-out-whats-the-difference
- https://www.geeksforgeeks.org/difference-between-process-and-thread
- https://www.nginx.com/resources/glossary/reverse-proxy-server
- https://www.geeksforgeeks.org/what-is-lazy-loading