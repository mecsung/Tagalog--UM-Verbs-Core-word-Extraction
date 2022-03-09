# Lemmatization of Tagalog - UM Verbs using Affix Removal and Rule-based Method

NLP course group project resulted in a core-word extraction analyzer that accepts Tagalog -UM verbs as inputs and analyzes them to produce the dictionary form of the word. The system was fed with a file containing 842 Tagalog -UM verbs. The results produced by the analysis using Affix Removal and Rule-based Methods shows 97.86% accuracy.

Installation:<br />
-- pip install numpy<br />
-- pip install nltk<br />

![](https://github.com/mecsung/Tagalog--UM-Verbs-Core-word-Extraction/blob/main/um.gif)

## Results and Discussion
The system was fed with 1000 Tagalog -UM verbs created by the researchers. The results produced by the analysis is compared to the expected output. The total correct outcomes is divided to the total words in the corpus. Table 1 shows 99.4 percent accuracy by using Affix Removal and Rule-based Method for determining the base form of Tagalog -UM verbs with a 0.6 percent margin of error.

Partly, some of the errors were caused by typographical inputs. However, most of the errors were caused by words with first two duplicated letters (eg. “bumaba”, “baba”, “ba”). By refining the rule-based method, many of these type of errors will be considerably reduced.

## Conclusion and Future Works
The system was tested with 1000 -UM verbs created by the researchers conjugated in two different tenses (eg. "lumulundag" - present tense, "lumundag" - past tense). The accuracy rate is expected to improve when certain rules are refined. The researchers will also add more types of verbs such as -IN, -AN, MA-, NAG-, and MAG-. The corpus will also be increased for future testing and data mining implementation.

