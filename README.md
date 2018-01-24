# friendlyphrases 
program to help curb the urge of using profanity/negativity in speech by suggesting sentences with greater positive connotation, implemented using sentiment analysis via afinn python package index, apis (thesaurus, google natural language) 

**warning**
cursewords.json is **NSFW.** 
cursewords.json is a self-crafted database of profane words and their synonyms. this self-crafted database was created to handle Resource Not Found error with big thesaurus API, as thesauruses typically either have no synonyms for profanity, or inaccurate ones. 

## Running the program 
run python3 scoring.py in the console 

### Input 
``` I hate this weather. It makes me feel cr*ppy. ```

### Output 

``` 
Rather, try the following:
50% positive: I dislike this weather. It makes me feel down.
28% positive: I don't like this weather. It makes me feel low.
16% positive: I detest this weather. It makes me feel lousy.
``` 

## Built With 
* [Afinn Python Index]
* [bighugelabs thesaurus api]
