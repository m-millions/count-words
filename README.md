
WHAT the CODE DOES
------------------
SAMPLE INPUT:

    [{"text": "What is the average life-span of a house fly?",
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

...

    These are the raw values passed in, after a clean-up:
    ['what is the average lifespan of a house fly', 'what is the capital of
    any state', 'where do fire ants live', 'how old was the first president
    when he died']

...

    These are the same values with associated counts per word:
    {'old': 1, 'do': 1, 'house': 1, 'is': 2, 'ants': 1, 'any': 1, 'what': 2,
    'when': 1, 'state': 1, 'how': 1, 'live': 1, 'capital': 1, 'was': 1,
    'fly': 1, 'fire': 1, 'president': 1, 'died': 1, 'he': 1, 'a': 1, 'of': 2,
    'average': 1, 'lifespan': 1, 'the': 3, 'where': 1, 'first': 1}

...

    Value found was NOT GREATER THAN 1!
    Value found was NOT GREATER THAN 1!
    Value found was NOT GREATER THAN 1!

...

    In the percentile:  ABOVE FORTY-NINE
    These are the words, not found in the exclusions list, which have the
    highest top-two counts:
    {}

...

    These are the raw values passed in, after a clean-up:
    ['what is the number one coffee roaster in north america',
    'can penguins fly', 'what is the capital of new york york york state',
    'who composed the american national anthem anthem']

...

    These are the same values with associated counts per word:
    {'composed': 1, 'roaster': 1, 'is': 2, 'number': 1, 'one': 1, 'in': 1,
    'what': 2, 'anthem': 2, 'state': 1, 'capital': 1, 'new': 1, 'national': 1,
    'coffee': 1, 'north': 1, 'who': 1, 'york': 3, 'america': 1, 'fly': 1,
    'of': 1, 'american': 1, 'penguins': 1, 'can': 1, 'the': 3}

...

    In the percentile:  BELOW FIFTY
    These are the words, not found in the exclusions list, which have the
    highest top-two counts:
    {'anthem': 2, 'york': 3}

...

    All The words with the highest count in the ABOVE FORTY-NINE percentile were
    in the exclusions list. All other values appear exactly once.  There is
    nothing to return.

...

    The words with the highest count in the BELOW FIFTY percentile are:
    {'anthem': 2, 'york': 3}


CONFIGURATION INSTRUCTIONS
--------------------------


INSTALLATION INSTRUCTIONS
-------------------------
Clone or dowload the project to your environment and install all project
dependencies, as detailed above.


OPERATING INSTRUCTIONS
----------------------


KNOWN BUGS
----------


TESTING METHODOLOGY
-------------------


WAYS TO IMPROVE ON THIS CODE
----------------------------


COPYRIGHT and LICENSING
-----------------------
Use and extend at will - credit the author.


TROUBLESHOOTING
---------------
Console-level messaging for the app.


CREDITS and ACKNOWLEDGEMENTS
----------------------------
    www.google.com
    http://www.giantflyingsaucer.com/ - Chad Lung, who continues to be an
    incredible mentor on all things tech and I am forever grateful.


CHANGE LOG
---------
First major version:

    The last commit for the first major version of the script is associated with
    the following SHA-1 hash value: 536eef87b3955605ea62ed6a0057682d209a52a8

    The commit's description is: "Updated descriptions and TO Dos."




AUTHOR(S)
-------
Claudia Ventresca


CONTACT INFO
------------
Feel free to contact me via this github account to disucuss potential business
opportunities.