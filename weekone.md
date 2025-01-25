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

## Q5. Visualize a cvs file using pandas dataframe

# WEDNESDAY - 22/01/2025

## Q1. In the data shared yesterday, sort the agent names in alphabetical order (A-Z)

## Q2. List all Python operators and their uses.

There are 7 categories of python operators.Namely:

1. Arithmetic operators
   Arithmetic operators are used with numeric values to perform common mathematical operations they include, ( + , - , \* , / , % , \*\* , // )

2. Comparison operators
   Comparison operators are used to compare two values: e.g:

```
x != y
```

3. Assignment operators

Assignment operators are used to assign values to variables: e.g

```
x = y
```

4. Logical operators

Logical operators are used to combine conditional statements:

e.g:

```
x < 5 and x < 10
```

5. Membership operators
6. Identity operators
7. Bitwise operators

## Q3. Write a function that returns the performance category of every agent and the resulting column to be added to the original dataframe.

## Q4. Construct a class (Car) in Python with attributes (make, model, and year of manufacture). The second function should be called describe. The examples to use are Honda Civic 2021 and Toyota Camry 2020.

Done in _assignment.py_ file

**With regards to question 3:**

1. Calculate performance scores (Premium and agent name)

```
  performance_scores = df.groupby('Agent_name')['Annual_Premium'].sum().reset_index(name='performance_score')

```

2. Merge the performance scores back into the original DataFrame
   ``
   df = df.merge(performance_scores, on='Agent_name')

``

3. Define performance categories based on quartiles as an example

```
performance_quartiles = df['performance_score'].quantile([0.25, 0.5, 0.75]).to_dict()

```

**_The function you are to write is step 4_**

# THURSDAY - 23/01/2025

## Q1. Write the formula of the line of best fit and state its scientific name.

The line of best fit equation is _y=m(x) + b_ and its scientific name is _regression line_

## Q2. Write the two formulas of median with regards to grouped and ungrouped data.

- grouped data
  The formula for calculating the median of grouped data is: Median = l + [(n/2 - c) / f] x h, where:
  l: is the lower limit of the median class
  n: is the total number of observations
  c: is the cumulative frequency of the class preceding the median class
  f: is the frequency of the median class
  h: is the class width (or size of each class)

- ungrouped data
  The median formula for ungrouped data is: If the number of observations (n) is odd, the median is the ((n+1)/2)th term; if n is even, the median is the average of the (n/2)th term and the (n/2+1)th term; meaning you first need to arrange the data in ascending order, then identify the middle value (or the average of the two middle values if n is even).

## Q3. Define homoscedasticity and why it's important in analysis.

Homoscedasticity is a statistical assumption that states that the variance of a random variable is the same across all values. It's also known as homogeneity of variance.

4. In the shared data, plot a histogram showing the ages of the policy holders(hint: use the date of birth column to come up with the age)

5. What is the difference between a boxplot and a countplot?

A boxplot shows the relationship between a continuous variable and a categorical variable, while a countplot shows the relationship between two categorical variables.

6. What distribution usually has the same mean, median, and mode?

When the data is perfectly normal, the mean, median and mode are identical.
