#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


people_count = len(enron_data)
print("people count: "+str(people_count))


feature_count = len(enron_data.values()[0])
print("feature count: "+str(feature_count))

poi_count = sum( [x["poi"] for x in enron_data.values() ] )
print("poi count: "+str(poi_count))

quant_sal_count = len( [x for x in enron_data.values() if x["salary"] != 'NaN' ] )
print("quantified sal count: "+str(quant_sal_count))

email_address = len( [x for x in enron_data.values() if x["email_address"] != 'NaN' ] )
print("known email addresses: "+str(email_address))

total_payments_nan = len( [x for x in enron_data.values() if x["total_payments"] == 'NaN' ] )
print("total payment = nan count: "+str(total_payments_nan))

tpn_percent = float(total_payments_nan)/float(people_count)
print("percent: "+str(tpn_percent))

total_payments_nan_poi = len( [x for x in enron_data.values() if x["total_payments"] == 'NaN' and x["poi"] == True ] )
print("total payment = nan count for poi: "+str(total_payments_nan_poi))

poi_count = len( [x for x in enron_data.values() if x["poi"] == True ] )
print("poi count: "+str(poi_count))

tpn_poi_percent = float(total_payments_nan_poi)/float(poi_count)
print("total_payments_nan_poi/poi_count: "+str(tpn_poi_percent))

print(enron_data["SKILLING JEFFREY K"])
#print(enron_data["FASTOW ANDREW S"]["total_payments"])
#print(enron_data["LAY KENNETH L"]["total_payments"])
 


import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

#using some tools given to convert the dict to np array
feature_list = ["poi", "salary", "bonus"] 
data_array = featureFormat( enron_data, feature_list )
label, features = targetFeatureSplit(data_array)