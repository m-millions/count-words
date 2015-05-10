
WHAT the CODE DOES
------------------
FIRST MAJOR VERSION as of 05/09/2015

SAMPLE IN-PUT:

    {"questions":
    [
        {"text": "YUP-YUP--YUP YUP-YUP--YUP YUP-YUP--YUP",
         "percent_correct": 0.3889655172413793},
        {"text": "What can we conclude the • president hoped to gain by inviting   \
         the people that he did to the State of the Union address?",
         "percent_correct": 0.6551724137931034},
        {"text": "Read this sentence from the passage.  <blockquote>\"Every dollar \
         we invest in high-quality early education can save more than             \
         seven dollars later on –                                                 \
         boosting graduation rates, reducing stuff,                               \
         reducing even more stuff that needs to be reduced.\"</blockquote>        \
         What can we conclude is the BEST reason the; president makes this claim?",
        "percent_correct": 0.5862068965517241},
       {"text": "Which of the following claims made by the president in his       \
         speech BEST supports the argument that this change                  will \
         benefit businesses and boost the economy?",
        "percent_correct": 0.41379310344827586},
       {"text": "In the section \"What's the Fuss?\" What is GOING on here?",
        "percent_correct": 0.8135593220338984}
    ]
    }


STANDARD PROCESSING:

    These are the raw values passed in, after a clean-up:
    ['which statement best supports the presidents goal for    eating ice cream in the winter', 'yupyupyup yupyupyup yupyupyup', 'what can we conclude the  president hoped to gain by inviting   the people that he did to the state of the union address', 'read this sentence from the passage  every dollar we invest in highquality early education can save more than             seven dollars later on                                                  boosting graduation rates reducing stuff                               reducing even more stuff that needs to be reduced                                   what can we conclude is the best reason the president makes this claim', 'in the section whats the fuss what is going on here', 'maybe', 'what can we infer is the best reason why companies are           choosing to have their products made overseas rather than                at home', 'how will bringing companies back home restore the economy', 'which of the following best describes why raising the ceiling on the new house is a good thing']

...

    These are the same values with associated counts per word:
    {'restore': 1, 'sentence': 1, 'dollar': 1, 'passage': 1, 'to': 4, 'going': 1, 'highquality': 1, 'save': 1, 'good': 1, 'read': 1, 'early': 1, 'every': 1, 'bringing': 1, 'inviting': 1, 'did': 1, 'companies': 2, 'stuff': 2, 'reduced': 1, 'the': 16, 'people': 1, 'house': 1, 'back': 1, 'are': 1, 'choosing': 1, 'home': 2, 'best': 4, 'even': 1, 'what': 4, 'for': 1, 'section': 1, 'ice': 1, 'state': 1, 'new': 1, 'supports': 1, 'be': 1, 'we': 4, 'eating': 1, 'here': 1, 'reason': 2, 'boosting': 1, 'by': 1, 'on': 3, 'of': 2, 'dollars': 1, 'graduation': 1, 'thing': 1, 'products': 1, 'makes': 1, 'whats': 1, 'conclude': 2, 'presidents': 1, 'address': 1, 'reducing': 2, 'from': 1, 'union': 1, 'their': 1, 'describes': 1, 'rates': 1, 'statement': 1, 'more': 2, 'ceiling': 1, 'that': 2, 'hoped': 1, 'gain': 1, 'than': 2, 'raising': 1, 'he': 1, 'made': 1, 'this': 2, 'will': 1, 'yupyupyup': 3, 'can': 4, 'invest': 1, 'following': 1, 'claim': 1, 'seven': 1, 'is': 4, 'at': 1, 'have': 1, 'in': 3, 'education': 1, 'cream': 1, 'needs': 1, 'winter': 1, 'rather': 1, 'how': 1, 'which': 2, 'infer': 1, 'economy': 1, 'fuss': 1, 'president': 2, 'why': 2, 'goal': 1, 'a': 1, 'maybe': 1, 'later': 1, 'overseas': 1}

...

    In the percentile:  ABOVE FORTY-NINE-NINE-NINE
    These are the words, not found in the exclusions list, which have the highest top-two counts:
    {'can': 4, 'best': 4}

- AND -

    In the percentile:  BELOW FIFTY
    No SIGNIFICANT repeatable words were found:
    {}


SAMPLE OUT-PUT:

    The words with the highest count in the ABOVE FORTY-NINE percentile are:
        {'can': 4, 'best': 4}

    All The words with the highest count in the BELOW FIFTY percentile were in
    the exclusions list. All other values appear exactly once.  There is nothing
    to return.

    {
      'above_fortynine':
                      {
                       'can': 4,
                       'best': 4
                      },
      'below_fifty': ''
    }


CONFIGURE
---------


INSTALL
-------
Clone or dowload the project to your environment and install all project
dependencies, as detailed above.


RUN
---


KNOWN BUGS
----------
There are no none bugs to report, as of this version.


TROUBLESHOOT
------------
Console-level messaging for the script.


TESTING METHODOLOGY
-------------------


WAYS TO IMPROVE ON THIS CODE
----------------------------


COPYRIGHT and LICENSING
-----------------------
Use and extend at will - credit the author.


CREDITS and ACKNOWLEDGEMENTS
----------------------------
    www.google.com
    http://www.giantflyingsaucer.com/ - Chad Lung, who continues to be an
    incredible mentor on all things tech and I am forever grateful.


REVISIONS and CODE VERSIONING
-----------------------------
FIRST MAJOR VERSION as of 05/09/2015

    The last commit for the first major version of the script is associated with
    the following SHA-1 hash value: 536eef87b3955605ea62ed6a0057682d209a52a8

    The commit's description is: "Updated descriptions and TO Dos."

SAMPLE IN-PUT:

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

STANDARD PROCESSING:

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

SAMPLE OUT-PUT:

    All The words with the highest count in the ABOVE FORTY-NINE percentile were
    in the exclusions list. All other values appear exactly once.  There is
    nothing to return.

...

    The words with the highest count in the BELOW FIFTY percentile are:
    {'anthem': 2, 'york': 3}


AUTHOR(S)
-------
Claudia Ventresca


CONTACT INFO
------------
Feel free to contact me via this github account to disucuss potential business
opportunities.