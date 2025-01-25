# Monday - 20/01/2025

## Q1. Transformers and their role in the creation of chat gpt and how the chats have evolved to mimic human intelligence

Transformers are neural networks used in Chatgpt capable of processing enormous data streams through an Attention Mechanism, to provide useful answers in natural language processing tasks.They transform or change an input sequence into an output sequence.

- ChatGPT organizes concepts through simple geometric relationships. These atomic connections are the foundation for AI’s ability to understand context and analogies.

- ChatGPT assigns different tasks to distinct areas. Some parts excel at grammar, others at problem-solving, while others focus on technical knowledge like coding.

## Q2. List all the subsets of AI and provide examples of each and how the different subsets mimic human senses/intelligence.

#### SUBSETS OF AI

1. Machine Learning
   Machine learning focuses on developing algorithms that enable computers to learn from data and make predictions or decisions without being explicitly programmed. It encompasses various techniques such as supervised learning, unsupervised learning, and reinforcement learning.

2. Deep Learning
   Deep learning is a subset of machine learning that involves the use of artificial neural networks with multiple layers

3. Artifical Neural Networks
   ANNs are computational models inspired by the structure and function of the human brain. They are used in various AI applications, including pattern recognition, speech recognition, and predictive modeling.

4. Natural Language Processing
   NLP involves the interaction between computers and human language. It includes tasks such as speech recognition, text understanding, sentiment analysis, and language translation.

## Q3. Research on data structures and algorithms

Data structures are “containers” that organize and group data according to type.The basic Python data structures include list, set, tuples, and dictionary.

1. Lists are used to store multiple items in a single variable and are created using square brackets.

```
mylist = ["apple", "banana", "cherry"]

```

2. Sets are used to store multiple items in a single variable and are written with curly brackets.

```
thisset = {"apple", "banana", "cherry"}
print(thisset)

```

3. Tuples are used to store multiple items in a single variable and are written with round brackets.

```
mytuple = ("apple", "banana", "cherry")

```

Dictionaries are used to store data values in key:value pairs.

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```
# TUESDAY - 21/01/2025

## Q1.What is the difference between while and (do...while)loops

With the while loop we can execute a set of statements as long as a condition is true.

In some programming languages, a "do-while" loop ensures that the code within the loop executes at least once before checking the condition.A practical use of do-while loop in python is User Input Validation.

## Q2. Research and learn about nested loops 

Nested loops mean loops inside a loop. For example, while loop inside the for loop, for loop inside the for loop, etc.

it's syntax looks like this.

```
Outer_loop Expression:
    Inner_loop Expression:
        Statement inside inner_loop
    Statement inside Outer_loop
```

## Q3. What is the difference between Return statement and print statement

print is a function you call. Calling print will immediately make your program write out text for you to see. Use print when you want to show a value to a human.

return is a keyword. When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. Use return when you want to send a value from one point in your code to another.

Using return changes the flow of the program. Using print does not.


## Q4. Learn about functions, files(how to read and write on them), classes

A function is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.A function can return data as a result.

In Python a function is defined using the def keyword:

e.g. 

```
def my_function():
  print("Hello from a function")
```

To call a function, use the function name followed by parenthesis:

```
def my_function():
  print("Hello from a function")

my_function()
```

Information can be passed into functions as arguments.

