from __future__ import print_function

import re


new_data = [{"text": "How are you?",
             "percent_correct": 0.8551724137931034},
            {"text": "What is your name?",
             "percent_correct": 0.71379310344827586},
            {"text": "Where do you live?",
             "percent_correct": 0.6779661016949152},
            {"text": "How old are you?",
             "percent_correct": 0.5016949152542372},
            {"text": "Do you drink coffee?",
             "percent_correct": 0.4932203389830508},
            {"text": "Do you like salt?",
             "percent_correct": 0.3217391304347826},
            {"text": "What is the thing you do best?",
             "percent_correct": 0.2101449275362319},
            {"text": "Is she your sibling?",
             "percent_correct": 0.1246376811594203}]

def get_clean_data(r):
    '''
    Process data to clean up leading and trailing spaces and applies a regex to
    eliminate unwanted characters in this case ( ) { } - < > and empty spaces
    in-between words.  More characters can be added as needed.
    '''
    clean_r = []
    for i in r:
        i = re.sub('[\(\)\{\}<>\-\?]', '', i)
        i = i.strip()
        clean_r.append(i.lower())
    return clean_r

def count_words(clean_above_fortynine, clean_below_fifty):
    '''
    Counts how many times a value is being passed from a list object
    '''
    # Used to keep a unique list of all the values passed via new_data
    above_fortynine = []
    below_fifty = []
    # keeps a dict of all the values passed via new_data and the
    # number of times each value has been seen throughout the iterations
    above_fortynine_count = {}
    below_fifty_count = {}
    # Process data for values associated with a score above 49 precentile
    for i in clean_above_fortynine:
        #print(i) # delete at will
        i = i.split()
        #print(i)
        # If the values has already been processed once, up the count by 1
        for s in i:
            #print(s)
            if s in above_fortynine:
                above_fortynine_count[s] = above_fortynine_count[s] + 1
                # delete at will
                #print(s + " is already in here; up-ing the count!")
                #print(above_fortynine_count) # delete at will
            # If this is the first time seeing the value, add it to the dict,
            # and initate its count to 1
            else:
                above_fortynine.append(s)
                above_fortynine_count[s] = 1
                #print(above_fortynine_count) # delete at will
    print("Word Count Above FORTY NINE %: ")
    print(above_fortynine_count)
    print(max(above_fortynine_count.iterkeys(), key=(lambda key: above_fortynine_count[key])))

    # Process data for values associated with a score below 50 precentile
    for i in clean_below_fifty:
        #print(i) # delete at will
        i = i.split()
        #print(i)
        # If the values has already been processed once, up the count by 1
        for s in i:
            #print(s)
            if s in below_fifty:
                below_fifty_count[s] = below_fifty_count[s] + 1
                # delete at will
                #print(s + " is already in here; up-ing the count!")
                #print(below_fifty_count) # delete at will
            # If this is the first time seeing the value, add it to the dict,
            # and initate its count to 1
            else:
                below_fifty.append(s)
                below_fifty_count[s] = 1
                # delete at will
                #print(below_fifty_count)
    print("Word Count Below FIFTY %: ")
    print(below_fifty_count)
    print(max(below_fifty_count.iterkeys(), key=(lambda key: below_fifty_count[key])))


above_fortynine = []
below_fifty = []
# Show us what's in the data-set - delete at will
#print(new_data)
for i in new_data:
    # If the values has already been processed once, up the count by 1
    if i["percent_correct"] > 0.499:
        above_fortynine.append(i["text"])
    elif i["percent_correct"] < 0.500:
        below_fifty.append(i["text"])
#print(above_fortynine)
#print(below_fifty)
clean_above_fortynine = get_clean_data(above_fortynine)
clean_below_fifty = get_clean_data(below_fifty)
count_words(clean_above_fortynine, clean_below_fifty)
