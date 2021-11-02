# Mini-project report 
Members: Thomas Longuevergne
Program: Network Security 
Course: 1DV501
Date of submission: 2021-11-02

## Introduction  
This project was a part of the class 1DV501, directly following the assignment 3 by reusing in Part 1 the programs to create a list of words from a file and to count and store these words in a list depending of their number of occurrences.
Part 2 makes us go a bit further while discovering and getting familiar with two Data structures studied in class : The Binary Search Tree and the Hash Table. Finally, in the required exercises, Part 3 makes us redo part 1 while using these data structures.

## Part 1: Count unique words 1
As said in the introduction, most of the word in part one was done in the assignment 3. What was needed to do was to read the right files (here stored in src) and to select the words by length (4 characters or more.) So in a for loop iterating through my sorted list of words, I make a if statement with the condition that the length of the word should be of 4 or more, then it and its number of occurrences should be stored in a list.
for each file I got :
The text should include:
- How many words did each of the two text files 
``holy_grail`` and ``eng_news_100K-sentences`` have?
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.

## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
 	* Point out and explain any differences from the given results in ``hash_main.py``
 	
- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the max bucket size for HashSet, and the max depth for BstMap, after having added all the words in the two large word files? (Hence, four different numbers.)

## Part 4: Plotting
For each subtask:
* Describe in words and a minimum of Python code how you computed the data used in the plots. (Do not show code for actual plotting).
* Present and explain figures. Are the results as expected?

## Part 5: Measuring time
For each subtask:
* Describe in words and a minimum of Python code how you solved the problems.
* Present and explain results and figures. Are the results as expected?

## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming.
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
- How could the results be improved if you were given a bit more time to complete the task.

### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
 - What lessons have you learned? What should you have done differently if you now were facing a similar project.