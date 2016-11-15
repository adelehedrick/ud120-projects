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

#print(enron_data["SKILLING JEFFREY K"]["total_payments"])
#print(enron_data["FASTOW ANDREW S"]["total_payments"])
#print(enron_data["LAY KENNETH L"]["total_payments"])