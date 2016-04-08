# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:01:20 2016

@author: Yutthana
"""

import gzip
import csv
  
#read file from json.gz to csv and delete unused key       
def parsecsvNorm(path):
    f = open("instance_movie_80%.csv", 'wb')
    unusedKey = ['helpful', 'reviewText', 'reviewerName', 'summary', 'unixReviewTime', 'reviewTime']
    g = gzip.open(path, 'r') 
    count = 1
    for l in g:
        data = eval(l)
        #delete unusedkey
        for key in unusedKey:
            if key in data:
                del data[key]
        
        #set header
        if count == 1:
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            
        #chunk size (approx. 80% of data)
        count += 1
        if count == 450000:
            break
        #write data
        w.writerow(data)
        
    f.close()
    return 0     
    
parsecsvNorm("reviews_Amazon_Instant_Video.json.gz")


