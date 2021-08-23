# **Motivation**
In the project, we attempt to process the netflix original film dataset with CRISP-DM method and the following questions
are looked at
1. What are the top 5 films with highest IMDB scores?
2. What are the top genres in terms of number of films?
3. How does the number of released films change by year?
4. What proportions of films are available in English? and how do they change with time?
Later we create a web dashboard using flask and plotly to display our analysis result, and the web app is deployed to [Heroku](https://devcenter.heroku.com/)


# **file description**
The files in the repository include:
1. data/NetflixOriginals.csv: the netflix dataset including title, genre etc of the films
2. netflix_app: a folder containing the web app files
3. wrangling_scripts/wrangle_data.py: a python file for data preprocessing and creation of visualizations with plotly
4. Procfile: a file that is needed by Heroku to execute and run the application.
5. requirements.txt: a text file including all the libraries needed to execute and run the application


# **Results**
The created visualizations can be seen [here](https://nf-film-visualizations.herokuapp.com/)


# **Licensing and Acknowledgements**
I want to give credits to the kaggle platform for providing the dataset, and relevant license can be found [here](https://www.kaggle.com/luiscorter/netflix-original-films-imdb-scores)
