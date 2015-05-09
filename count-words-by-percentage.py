from __future__ import print_function

import re


#TO DO: Import data from a file containing a JSON object
new_data = [{"text": "What is the average life-span of a house fly?",
             "percent_correct": 0.8551724137931034},
            {"text": "What is the capital of any state?",
             "percent_correct": 0.71379310344827586},
            {"text": "Where do fire ants live?",
             "percent_correct": 0.6779661016949152},
            {"text": "How old was the first president when he died?",
             "percent_correct": 0.5016949152542372},
            {"text": "What is the number one coffee roaster in North America?",
             "percent_correct": 0.4932203389830508},
            {"text": "Can penguins fly?",
             "percent_correct": 0.3217391304347826},
            {"text": "What is the capital of New York York York state?",
             "percent_correct": 0.2101449275362319},
            {"text": "Who composed the American National Anthem Anthem?",
             "percent_correct": 0.1246376811594203}]


def count_words(words, percentile):
    '''
    Main Function: Counts how many times a value is being passed from a list
    object
    '''
    # TO DO: (1) Update description
    #        (2) Write exceptions/errors/processing-messages to a log file(s)
    print(" ")
    print("These are the raw values passed in, after a clean-up:")
    print(words)
    print(" ")
    # Used to keep a unique list of all the values passed via new_data
    clean_words = []
    # keeps a dict of all the values passed via new_data and the
    # number of times each value has been seen throughout the iterations
    clean_words_count = {}
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
            else:
                # If this is the first time seeing the value, add it to the dict,
                # and initate its count to 1
                clean_words.append(s)
                clean_words_count[s] = 1
    print("These are the same values with associated counts per word:")
    print(clean_words_count) # delete at will
    print(" ")
    top_count = get_max_count(clean_words_count, percentile)
    return top_count

def get_clean_data(r):
    '''
    Processes data to clean up leading and trailing spaces and applies a regex to
    eliminate unwanted characters in this case ( ) { } - < > and empty spaces
    in-between words.  More characters can be added as needed.
    '''
    # TO DO: Update function description
    clean_r = []
    for i in r:
        i = re.sub('[\(\)\{\}<>\-\?]', '', i)
        i = i.strip()
        clean_r.append(i.lower())
    return clean_r

def get_max_count(clean_words_count, percentile):
    '''
    Get all words with top-two highest number of occurances, as long as
    said words are not included in the 'exclusions' list
    '''
    # TO DO: (1) Update description
    #        (2) Write exceptions/errors/processing-messages to a log file(s)
    # Add/Delete to/from exclusions list at will
    exclusions = ["a", "an", "the", "and", "but", "or", "for", \
                  "nor", "etc", "on", "at", "to", "from", "by", \
                  "is", "what", "of"]
    top_count = {}
    # capture passed values and shorten
    # used to mutate dict outside of the iteration
    clean_words_count_copy = {}
    clean_words_count_copy = dict.copy(clean_words_count)
    ii_count = 0
    # pull MAX but make sure that max is greater than 1
    # and run x times as long as clean_words_count[ii] > 1 and two top values
    # have not been found yet.
    # Will iterate through every value in the collection and aler if the value
    # associated with the key is not greater than 1 and will igonore any values
    # which are matched successfully against the values in the 'exclusions' list
    # TO DO: Modify the code so that it doesnt alert for every single value,
    #       which is not greater than one, instead it should alert once and show
    #       all values which were not in the 'exclusions' list but had a value
    #       of only 1 <<< this may be over-kill for larger data sets, but cool
    #       to show in this example
    for x in clean_words_count:
        if ii_count < 2:
           # print(ii_count)
            ii = (max(clean_words_count_copy.iterkeys(), \
                      key=(lambda key: clean_words_count_copy[key])))
            if clean_words_count_copy[ii] > 1:
                #print(ii, clean_words_count_copy[ii])
                if ii not in exclusions:
                    top_count[ii] = clean_words_count_copy[ii]
                    #print(top_count)
                    del clean_words_count_copy[ii]
                    #print(clean_words_count)
                    # pull MAX but make sure it is greater than 1
                    ii_count = ii_count + 1
                    #print(ii_count)
                else:
                    del clean_words_count_copy[ii]
            else:
                print("Value found was NOT GREATER THAN 1!")
    print(" ")
    print("In the percentile: ", percentile)
    print("These are the words, not found in the exclusions list, which have " +
          "the highest top-two counts:")
    print(top_count)
    print(" ")
    return top_count

# TO DO: (1) Add description here ...
#        (2) Write exceptions/errors/processing-messages to a log file(s)
#        (3) Write final results to a JSON object (dict)
#        (4) Write final JSON object to file:
#            "top-two-counts-per-precentile.json"
above_fortynine = []
below_fifty = []
top_above_fortynine = {}
top_below_fifty = {}
# Show us what's in the new data-set - delete at will
#print(new_data)
for i in new_data:
    # If the values has already been processed once, up the count by 1
    if i["percent_correct"] > 0.499:
        above_fortynine.append(i["text"])
    elif i["percent_correct"] < 0.500:
        below_fifty.append(i["text"])
#print(above_fortynine)
#print(below_fifty)
# Clean-up data of undesired characters
clean_above_fortynine = get_clean_data(above_fortynine)
clean_below_fifty = get_clean_data(below_fifty)

# Get all words with top-two counts
# Pass in "percentile" just for clarity not needed for logic execution
percentile = "ABOVE FORTY-NINE"
top_above_fortynine = count_words(clean_above_fortynine, percentile)
# Pass in "percentile" just for clarity not needed for logic execution
percentile = "BELOW FIFTY"
top_below_fifty = count_words(clean_below_fifty, percentile)

# Pring what was found, even if there were no legitimate counts
if bool(top_above_fortynine) == True:
    print("The words with the highest count in the ABOVE FORTY-NINE " +
          "percentile are: ", top_above_fortynine)
    print(" ")
else:
    print("All The words with the highest count in the ABOVE FORTY-NINE " +
          "percentile were in the exclusions list. All other values appear " +
          "exactly once.  There is nothing to return.")
    print(" ")

if bool(top_below_fifty) == True:
    print("The words with the highest count in the BELOW FIFTY percentile " +
          "are: ", top_below_fifty)
    print(" ")
else:
    print("All The words with the highest count in the BELOW FIFTY " +
          "percentile were in the exclusions list. All other values appear " +
          "exactly once.  There is nothing to return.")
    print(" ")

