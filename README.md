# DataMining
Data Mining Project

read_csv.py - read data from "reviews_Amazon_Instant_Video.json.gz"(approx. 80%) then delete unused key, and write to the csv file.

item_to_item_CF.py - read csv file that get from read_csv.py then put the movie with more than 500 reviews from user into dataframe. Transform dataframe to utility matrix then normalize the data and compute the cosine similarity. Rank the top 10 highest similarity, then write to the output file.


** reviews_Amazon_Instant_Video.json.gz can be download from http://jmcauley.ucsd.edu/data/amazon/links.html
