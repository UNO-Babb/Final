import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
  #Read in the data from the csv file
  data = pd.read_csv("billionaires.csv")

  #pull out the data column that we care about
  year = data['company.founded'].values

  #We only care about the companies founded since 1900. Create a process (loop) to move the "good data" to our clean dataset.

  cleanData = []


  #How do I bucket the data by either individual year or groups of 5-10 years? Make the graph look nice an readable. Use the matplotlib tutorials to see how to adjust the settings of a histogram.
  plt.hist(cleanData)
  plt.show()


if __name__ == '__main__':
  main()
