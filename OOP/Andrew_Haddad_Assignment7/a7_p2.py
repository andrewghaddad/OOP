import time 
start_time = time.time()

word_data = {}

t_file = open('movie_reviews.txt', 'r')
TotalData = str.lower(t_file.read())
t_file.close()

reviewsData = TotalData.split('\n')

print('Initializing sentiment database')

for i in reviewsData:
    words = i.split(' ')

for j in words:
   if (j not in word_data):
       word_data[j] = [1, int(words[0])]
   else:
       word_data[j][0] += 1
       word_data[j][1] += int(words[0])

ending_time = time.time()

time = format(ending_time - start_time, ".2f")

print("All Sentiment Data is taken from file and setups like a database")
print("Unique words are : ", len(word_data))
print("For analyses taken time to compelte ", time)
print("")

#asking the user to take phrase to enter phrase and converting to lower case and storing
phraseData = str.lower(input("Enter a phrase to test: "))
single_phrase = phraseData.split()

average = 0
count = 0

#count values to figure out the average score for the phrase
for j in single_phrase:
   if (j in word_data):
       score = word_data[j][1] / word_data[j][0]
       print("* \'", j, "\'appears ", word_data[j][0], " times with an average score of ", score, sep = "")
       average += score
       count += 1
   else:
       print('* \'', j, '\' does not appear in any movie reviews', sep = "")

#if no words appears
if count == 0:
   print("Not enough words to determine sentiment.")
else:
   print("Average score for this phrase is: ", average / count)
if (average / count > 2):
   print("This is a POSITIVE phrase")
else:
   print("This is a NEGATIVE phrase")
