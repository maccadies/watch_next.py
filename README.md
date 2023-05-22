# watch_next.py

Movie Recommendation Engine
Overview
This project utilizes the power of Natural Language Processing (NLP) to create a basic movie recommendation system.
By comparing a provided movie description to a database of movies, the system is able to suggest a similar movie to watch next.

Installation
To run this project, you need to have Python and Spacy installed.

How It Works
The core functionality of the recommendation engine is built upon the Spacy library and its similarity function. It uses the English multi-task CNN trained on OntoNotes (en_core_web_md) to compare movie descriptions.

The engine reads a list of movies along with their descriptions from a text file. For each movie, it compares its description with the description of the recently watched movie using Spacy's similarity function. The movie with the highest similarity score is recommended to watch next.

Usage
You can run the recommendation system with a description of the movie you have just watched. For example:

python
Copy code
description = "Your movie description goes here"
print("The next Movie that's recommended to Watch is: " + watch_next(description))

Limitations
Please note that this is a basic movie recommendation system and it does not take into account other important factors like user preferences, ratings, genres etc.
It purely works based on the similarity of movie descriptions.

Future Enhancements
Future versions of this project could include improvements such as integration with a larger movie database, factoring in user ratings and preferences, and expanding the recommendation criteria.
