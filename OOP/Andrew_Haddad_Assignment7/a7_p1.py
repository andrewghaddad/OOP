#Andrew Haddad
#OOP Section 02
#Assignment 7 Part 1


word = input("Enter a word to test: ") 

total_count = 0 
total_sum = 0 

with open ("movie_reviews.txt") as t_file: 
   for line in t_file.readlines(): 
      if (word.lower() in [x.lower() for x in line.split()]):
         total_count += 1 
         total_sum += int(line.split()[0])

if (total_count != 0):
   print("'",word,"'appears",total_count,"times")
   print("The average score for the reviews containing the word '"+word+"' is",total_sum/total_count)
   
   if (total_sum/total_count >= 2): 
      print("This is a positive word") 
   else:
      print("This is a negative word") 
else: 
   print("'",word,"' appears 0 times")
   print("There is no average score for reviews containing the word '",word,"'")
   print("Cannot determine if this word is positive or negative")