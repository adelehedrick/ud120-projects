#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = [ (a, n, p-n) for p, a, n in zip(predictions, ages, net_worths) ]

    ### your code goes here
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])

    return cleaned_data[0:len(cleaned_data)-int(len(cleaned_data)/10)]

