# nourhan-mahmoud-
## Daily Steps Tracker
Problem Description:
Given a list of daily step counts, this program calculates:
 * Maximum steps: The highest daily step count.
 * Minimum steps: The lowest daily step count.
 * Average steps: The average daily step count.
 * Sorted steps: The daily step counts sorted in descending order.
Example:
Input:
5000 3000 2000 4000

Output:
Maximum steps: 5000
Minimum steps: 2000
Average steps: 3500
Sorted steps: 5000 4000 3000 2000
code [teps=input("enter the number of steps sperator by space : ")
steps_list=list(map(int,steps.split()))
max_step=max(steps_list)
min_step=min(steps_list)
average_step=sum(steps_list)/len(steps_list)
order_steps=sorted(steps_list,reverse=True)
print("max: ",max_step)
print("min: ",min_step)
print("avg: ",average_step)
print("the step counts in descending order",order_steps)]
(problem1)[https://drive.google.com/drive/folders/1ERUUyiWS460hIj95DQzfN_xeLISI0lm1]









## Library Book Borrowing Analysis

Problem Description:
Given a list of books and their corresponding borrowing durations, this program aims to:
 * Calculate statistics:
   * Most and least borrowed book: Identify the books with the highest and lowest number of borrowing days.
   * Average borrowing time: Determine the average duration of book borrowings.
 * Analyze unique titles: Find all unique book titles in the dataset.
 * Sort books by borrowing duration: Arrange the books in descending order based on their borrowing duration.
Input Format:
Each line of input should be in the format: Book Title Days Borrowed
Example Input:
The Lord of the Rings 10
Pride and Prejudice 7
To Kill a Mockingbird 12
The Lord of the Rings 8

Output:
Most borrowed book: The Lord of the Rings (18 days)
Least borrowed book: Pride and Prejudice (7 days)
Average borrowing time: 9.25 days
Unique book titles: The Lord of the Rings, Pride and Prejudice, To Kill a Mockingbird
Books sorted by borrowing duration:
  1. The Lord of the Rings (18 days)
  2. To Kill a Mockingbird (12 days)
  3. Pride and Prejudice (7 days)

Implementation Approach:
 * Read input: Read the input data, parsing each line into book title and borrowing days.
 * Create a dictionary: Use a dictionary to store book titles as keys and their total borrowing days as values.
 * Calculate statistics:
   * Most and least borrowed book: Find the key-value pair with the highest and lowest value in the dictionary.
   * Average borrowing time: Calculate the average of all values in the dictionary.
   * Unique book titles: Use a set to store unique book titles from the dictionary keys.
 * Sort books: Sort the dictionary items by value in descending order.
Code[book_days = {}
unique_titles = set()
borrowed_books = [
    "Book A - 10",
    "Book B - 5",
    "Book C - 15",
    "Book A - 8",
    "Book B - 3",
    "Book D - 7",
]

for book_info in borrowed_books:
    title, days_str = book_info.split(" - ")
    days = int(days_str)
    book_days[title] = book_days.get(title, 0) + days

most_borrowed = max(book_days, key=book_days.get)
print("Most borrowed book:", most_borrowed)

least_borrowed = min(book_days, key=book_days.get)
print("Least borrowed book:", least_borrowed)

average_days = sum(book_days.values()) / len(book_days)
print("Average borrowing days:", average_days)

print("Unique book titles:", unique_titles)

sorted_books = sorted(book_days.items(), key=lambda x: x[1], reverse=True)
print("Books sorted by borrowing days:")
for title, days in sorted_books:
    print(f"{title}: {days} days")
]
(problem2)[https://drive.google.com/drive/folders/12hQw7YjBkzqhO5AO1XEXQs38YIhLWid-]



## Word Scramble Game
How to Play:
 * Random Word Selection: The computer selects a word randomly from a predefined list.
 * Word Scrambled: The selected word is scrambled by shuffling its letters.
 * Guessing Phase: The player is prompted to guess the original word.
 * Attempt Limit: The player has a limited number of attempts (usually 5) to guess correctly.
 * Feedback: After each guess, the player is informed whether the guess is correct or incorrect and how many attempts remain.
 * Game Over: If the player guesses correctly within the allotted attempts, they win. Otherwise, the game ends, and the original word is revealed.
Example:
 * Scrambled Word: pleap
 * Original Word: apple
Implementation:
A possible implementation in Python could involve:
 * Creating a word list: Define a list of words to be used in the game.
 * Random word selection: Use a random module to select a word from the list.
 * Word scrambling: Shuffle the characters in the word using a random shuffling algorithm.
 * User input: Prompt the user to enter their guess.
 * Guess checking: Compare the user's guess to the original word.
 * Attempt tracking: Keep track of the number of remaining attempts.
 * Win/lose conditions: Determine the game outcome based on the number of attempts and correct guesses.

   (problem3)[https://drive.google.com/drive/folders/16QS3Hvo4qmb-KFvVf8IhdblpZRdP3kbs]
