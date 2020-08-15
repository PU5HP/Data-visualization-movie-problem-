import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

'''A CSV file (Comma Separated Values file) is a type of plain text file
 that uses specific structuring to arrange tabular data. Because it's a plain 
 text file, it can contain only actual text data—in other words, printable ASCII
  or Unicode characters. The structure of a CSV file is given away by its name.'''

#READING A .csv file
df = pd.read_csv("movie_metadata.csv")
#print(df.head(n=10))

#listing all the columns.
print(df.columns)

#selecting only the movie_title column and type casting in the list class to apply furthur functions
titles = df.movie_title
#print(titles)
x=list(titles)
#print(type(x))
#print(x)

freqt ={}

for title in titles:
  lenght =len(title)
  if freqt.get(lenght) is None:
    freqt[lenght]=1
  else:
    freqt[lenght]=freqt[lenght]+1

print(freqt)
'''in the above code if the lenght of the movie of the title does not exist then set lenght as 1
else increment the dicitonary'''

X = np.array(list(freqt.keys()))
Y =np.array(list(freqt.values()))
plt.bar(X,Y)
plt.xlabel('lenght of the title')
plt.ylabel('frequency of the title')
plt.title('movie graph')
plt.show()
