#!/usr/bin/env python
# coding: utf-8

# **Python Refresher Exercises**
# 
# Lab 1 -- Please submit your exercises as a link to the file in your github account. If you have a private repository, [please follow the instructions](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository) to add a collaborator to the repository. You should add bingcode@binghamton.edu as the collaborator.
# 
# Make sure that you link any resources you use in a comment or docstring!

# 1. See the list below. Please write a program that will tell you what the longest word is in the list. Package your program inside of a function.  

# In[ ]:


list = ["apple", "chestnut", "gargoyle", "pandas", "sheep", "raptor"]

def length(list):
  max_length = len(list[0])
  long_word = list[0]

  for i in list:
    if (len(i) > max_length):
      max_length = len(i)
      long_word = i
      print(" the longest word is " + i)

length(list)


# 2. Now that you have built the program above, in a new cell, edit your program: import a .txt file of a list of words and have your program randomly choose 7 words from the file to add to a list, and then have the program determine the longest word as you did above. 

# In[ ]:


import random
rando_word = "/content/random_words_txt.txt"

def list():
  filename = rando_word
  f = open(filename, "r", encoding = "utf8")
  words = f.readlines()                       # loading in txt file (colab requires upload every time environment is restarted)
  f.close()

  return random.choices(words, k=7) # k=7 selects 7 distinct words

list()
# calls function to select random word

new_list = list()     # store new word selection function into variable

def length(new_list):
  max_length = len(new_list[0])
  long_word = new_list[0]

  for i in new_list:
    if (len(i) > max_length):
      max_length = len(i)
      long_word = i
      print(" the longest word is " + i)

length(new_list)


# 3. Pretend that you're going to be leading a review session on dictionaries. Build a program that uses dictionaries and incorporates at least 4 built-in methods. [See full list on W3Schools](https://www.w3schools.com/python/python_ref_dictionary.asp) 

# In[ ]:


# in this example, a coach is recording the team's first name and number
roster = {"kim" : 4, "malia":13, "stephanie":8, "carol":5, "stacey":1,
          "mary":17, "maria":9}
# the method "keys()" will print a list of all of the player's names
roster.keys()


# In[ ]:


# to get a complete list of the team's numbers we use "values()"
roster.values()


# In[ ]:


# to find out a specific player's number lets use the "get()" method
roster.get("stephanie")


# In[ ]:


# A player just switched numbers, lets update the roster
roster.update({"carol":19})
print(roster)


# 4. Using OOP, I want you to build one of the following things. As part of the excerise, please write out your brainstorming process in a comment or markdown cell:
# 
# 
# *   A system to manage a student's school record (would need a way to gather/store personal information, record grades, record GPA, etc.)
# *   A class that allows you to create your own flashcards & then allows you to review them (this would work best with language cards - like one word is in Spanish, one in English)
# *   A class (or series of classes) to correspond with a gameplay (for example, a fighter class, a bard class, a wizard class)
# 
# 

# I will be coding a class that allows me to create my own flashcards and allow for review
# --
# Elements needed:
# - dictionary storing english word and spanish word
# - class to show one flashcard from the set

# In[22]:


class Card:
  def __init__(self, english, spanish):
    self.english = english
    self.spanish = spanish
    
  def greeting(self):
    print(self.english +" --> " + self.spanish)

  def departing(self):
    print(self.english + " --> " + self.spanish)
      
      
s1 = Card("hello", "hola")
s2 = Card("Bye","Adios")

s1.greeting()
s2.departing()


# 5. Finalize your Hangman program and submit it. Include any necessary comments and explain what you had "refreshed" by building it in class. If appropriate, use functions or OOP to package the pieces of your code. 

# I got stuck with iterating through the word locate where each character was located and to represent such in the program for the viewer to see what they guessed correctly and where the letetr goes. I also had a tough time figuring out how to iterate through the code until the word was complet but working in class my group developed a variable called tries and compared it with count to make the game repeat and not stop after asking for one letter.

# In[2]:


import time

correct = ["c","a","n","d","y"]
word = []
alphabet = []
incorrect = []
tries = 10
count = 0

for i in range(len(correct)):                      
  word.append("__")

while tries > 0:
  if "__" not in word:
    print("You got it! The word is " + str(correct) + "!")
    break
  letter = input("Guess a Letter: ")

  if letter not in alphabet:
    alphabet.append(letter)                                 
  elif letter in alphabet:
    print("You already guessed that letter.")
  print(f"These are the letters you've guessed: {alphabet}")
  time.sleep(1)
  if correct.count(letter) == 1:          
    letter_place = correct.index(letter)
    # locates letter placement within empty string
    word[letter_place] = letter
    print("You guessed one of the letters!")
    print("Number of tries left: " + str(tries - 1))
    print(word)
    print(" ")

  elif correct.count(letter) >= 2:
  #code for if there is more than one letter in the display
    count = 0
    index_list = []
    for i in correct:
      if i == letter:
        index_list.append(correct.index(i, count))
        count = index_list[-1] + 1
    print(index_list)
    for x in index_list:
      word[x] = letter
    print("You guessed one of the letters!")
    if tries > 0: 
      print("Number of tries left: " + str(tries - 1))
    print(word)
    print(" ")

  elif letter not in word:        
    print("The letter you picked is not in the word!")
    tries -= 1
    print("Number of tries left: " + str(tries - 1))
    print(word)
    print(" ")

    if tries == 0:
      print("game over!")
      print("The secret word was: " + correct)
      break
      # the player runs out of tries, stopping the game

