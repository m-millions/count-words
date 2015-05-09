from __future__ import print_function

import re


new_data = [{"text": "What is the average life-span of a house fly?",
             "percent_correct": 0.8551724137931034},
            {"text": "What is the capital of Washington state?",
             "percent_correct": 0.71379310344827586},
            {"text": "Where do fire ants live?",
             "percent_correct": 0.6779661016949152},
            {"text": "How old was George Washington when he died?",
             "percent_correct": 0.5016949152542372},
            {"text": "What is the number one coffee roaster in North America?",
             "percent_correct": 0.4932203389830508},
            {"text": "Can penguins fly?",
             "percent_correct": 0.3217391304347826},
            {"text": "What is the capital of New York state?",
             "percent_correct": 0.2101449275362319},
            {"text": "Who composed the American National Anthem?",
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

def count_words(words):
    '''
    Counts how many times a value is being passed from a list object
    '''
    print(words)
    exclusions = ["a", "an", "the", "and", "but", "or", "for", \
                  "nor", "etc", "on", "at", "to", "from", "by"]
    # Used to keep a unique list of all the values passed via new_data
    clean_words = []
    # keeps a dict of all the values passed via new_data and the
    # number of times each value has been seen throughout the iterations
    clean_words_count = {}
    # Process data for values associated with a score above 49 precentile
    top_count = {}
    for i in words:
        #print(i) # delete at will
        i = i.split()
        #print(i)
        # If the values has already been processed once, up the count by 1
        for s in i:
            #print(s)
            if s in clean_words:
                clean_words_count[s] = clean_words_count[s] + 1
                # delete at will
                #print(s + " is already in here; up-ing the count!")
                #print(above_fortynine_count) # delete at will
            # If this is the first time seeing the value, add it to the dict,
            # and initate its count to 1
            else:
                clean_words.append(s)
                clean_words_count[s] = 1
    print(clean_words_count) # delete at will
    # pull MAX but make sure it is greater than 1
    # TODO: Turn this into a function that can run x times
    # as long as clean_words_count[ii] > 1
    ii = (max(clean_words_count.iterkeys(), \
              key=(lambda key: clean_words_count[key])))
    if clean_words_count[ii] > 1:
        #print(ii, clean_words_count[ii])
        top_count[ii] = clean_words_count[ii]
        print(top_count)
        del clean_words_count[ii]
        print(clean_words_count)
        # pull MAX but make sure it is greater than 1
        ii = (max(clean_words_count.iterkeys(), \
              key=(lambda key: clean_words_count[key])))
        if clean_words_count[ii] > 1:
            #print(ii, clean_words_count[ii])
            top_count[ii] = clean_words_count[ii]
            print(top_count)
            del clean_words_count[ii]
            print(clean_words_count)
        else:
            print("Value found was NOT GREATER THAN 1!")
    else:
        print("Value found was NOT GREATER THAN 1!")
    return top_count


above_fortynine = []
below_fifty = []
top_above_fortynine = {}
top_below_fifty = {}
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

top_above_fortynine = count_words(clean_above_fortynine)
top_below_fifty = count_words(clean_below_fifty)
print(top_above_fortynine, top_below_fifty)

