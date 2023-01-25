import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

file = "tweets.txt"

hand = open(file)


# sentiment function
def get_sentiment(sentence):
  try:
    analyzer = SentimentIntensityAnalyzer()
  
    vs = analyzer.polarity_scores(sentence)

    return(vs['compound'])
  except:
    return -1




#objects for counting and storing data
dict_counts = {}
dict_counts_hash = {}
rt_count = 0
username_list = []
username_counter = {}
vaccine_count = 0
sentiment_score = 0




#***************************MAIN LOOP*******************************

for line in hand:

  #finds total sentiment score
  sentiment_score = sentiment_score + get_sentiment(line)

  #total vaccine count
  if re.search("vaccine", line, re.IGNORECASE):
    vaccine_count += 1

  #splits line into words
  line = line.split()

  #checks if tweet is retweet by checking first word, first word in line will be "RT" if so
  if re.search("^RT", line[0]):
    rt_count += 1

    #adds username to username_list if retweet, username will be second word: line[1]
    username_list.append(line[1])

  #loops through words in line
  for word in line:

    #adds all words to dictionary and counts them
    if word != "RT":
       dict_counts[word] = dict_counts.get(word,0) + 1

    #adds all hashtags to dictionary and counts them
    if re.search("^#", word):
      word = word.strip(".").strip(",").strip("!").strip(":")
      dict_counts_hash[word] = dict_counts_hash.get(word,0) + 1

#*********************************************************************



      

#***********PRINTS MOST FREQUENT WORDS**************

tmp_list = []
for (key,val) in dict_counts.items():
  tmp_list.append((val,key))
  
sorted_list = sorted(tmp_list,reverse=True)

print("\n")
print("*******************")
print("Most Frequent Words")
print("*******************")

for item in sorted_list[:10]:
  print(f"{item[1]}, {item[0]}")

#*****************************************************


#***********PRINTS HASHTAGS USED**************

tmp_list_1 = []
for (key,val) in dict_counts_hash.items():
  tmp_list_1.append((val,key))
  
sorted_list_1 = sorted(tmp_list_1,reverse=True)

print("\n")
print("*******************")
print("Hashtags Used")
print("*******************")


for item in sorted_list_1:
  print(f"{item[1]}, {item[0]}")
  
#***********************************************


#***********PRINTS RETWEET COUNT**************

print("\n")
print("*******************")
print("Retweets")
print("*******************")

print(f"{rt_count} out of the 5,000 tweets are retweets")

#*********************************************


#***********PRINTS MOST RETWEETED ACCOUNTS**************

#counts usernames using dictionary
for username in username_list:
  username = username.strip("@").strip(":")
  if username not in username_counter:
    username_counter[username] = 1
  else:
    username_counter[username] += 1


tmp_list_2 = []
for (key,val) in username_counter.items():
  tmp_list_2.append((val,key))
  
sorted_list_2 = sorted(tmp_list_2,reverse=True)

print("\n")
print("*******************")
print("Most Retweeted accounts")
print("*******************") 

for item in sorted_list_2[:10]:
   print(f"{item[1]}, {item[0]}")
  
#*******************************************************


#***********PRINTS VACCINE TWEET COUNT**************
  
print("\n")
print("*******************")
print("Vaccine Tweets")
print("*******************")

print(f"{vaccine_count} out of the 5,000 tweets talk about the vaccine")

#***************************************************


#***********PRINTS SENTIMENT SCORE**************

sentiment_average = sentiment_score / 5000
rounded_sentiment_average = float("{0:.3f}".format(sentiment_average))

print("\n")
print("*******************")
print("Sentiment")
print("*******************")

print(f"The average sentiment of the 5,000 tweets is {rounded_sentiment_average}")

#************************************************