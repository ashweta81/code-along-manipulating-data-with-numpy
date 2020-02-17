# --------------
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 
with open(path) as f:
    adm = csv.reader(f, delimiter=',')
    adm = list(adm)

#Remove the header
adm.remove(adm[0])
#print(adm)

# Store the data in an array
data = np.array(adm)

# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter
adcam = data[:,1]
print('The unique ad campaigns are', np.unique(adcam))
print('The number of unique ad campaigns are', np.unique(adcam).size)
print('The number of times each campaign was run are', Counter(adcam))

# What are the age groups that were targeted through these ad campaigns?
print('The age groups targeted through the ad campaigns are', np.unique(data[:,3]))

# What was the average, minimum and maximum amount spent on the ads?
amount = data[:,8].astype(float)
print('The average amount spent on the ads are', np.mean(amount))
print('The minimum amount spent on the ads are', np.min(amount))
print('The maximum amount spent on the ads are', np.max(amount))

# What is the id of the ad having the maximum number of clicks ?
clicks = data[:,7].astype(int)
max_clicks = np.max(clicks)
max_clicks_id = data[:,0][clicks == max_clicks]
print('The id of the ad having maximum number of clicks is', max_clicks_id)

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
purchase_mostclicks = data[:,-1][clicks == max_clicks]
print('The number of people who bought the product after seeing the ad are', purchase_mostclicks)

max_purchases = data[:,-1].astype(int).max()
print('The maximum number of purchases are', max_purchases)

if (max_purchases == purchase_mostclicks):
    print('True')
else:
    print('False')
 
# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 
CTR = ((data[:,7].astype(int)) * 100 )/(data[:,6].astype(int))
print(CTR.shape)
print(data.shape)

CTR = CTR.reshape(-1,1)
print(CTR.shape)

data = np.concatenate((data, CTR), axis=1)
print(data.shape)
# Create a new column that represents Cost Per Mille (CPM) 

CPM = (data[:,8].astype(float))*100 / (data[:,6].astype(int))
print(CPM.shape)
print(data.shape)

CPM = CPM.reshape(-1,1)
print(CPM.shape)

data = np.concatenate((data, CPM), axis=1)



