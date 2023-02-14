# import spacy
import spacy
# This will return a Language object 'en_core_web_md'
nlp = spacy.load('en_core_web_md')
def watch_next(info):
    #open and load file contents
    movies = open("movies.txt", "r")
    #initialize an empty list
    split_list = []
    #split movies into title and description and store
    for i in movies:
        split_list.append(i.split(':')) # split list by :
    #count number of movies in text file
    count = len(split_list)
    #declare and initialize list to store similar values
    sim_list = []
    model_sentence = nlp(info)
    #iterate as many times as the number of movies in the text file using range
    for i in range(0, count):
        #check similarity between the movie description with the recently watched description
        sim_list.append(nlp(split_list[i][1]).similarity(model_sentence))
    #get the max similarity value
    max_sim = max(sim_list)
    #get index of highest similarity value
    max_sim_movie = sim_list.index(max_sim)
    #return movie title similar to watched movie
    return split_list[max_sim_movie][0]
#movie description to comapare with
description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

#call function that gets the next movie description
print("The next Movie thats recommended to Watch is: " + watch_next(description))