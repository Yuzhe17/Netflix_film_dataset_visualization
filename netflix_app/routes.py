from netflix_app import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import return_figures

@app.route('/')
@app.route('/index')
def index():
    figure=return_figures()

    #plot ids for html id tag
    #id='figure-1'
    ids=['figure-{}'.format(i) for i,_ in enumerate(figure)]

    #convert the plotly figures to JSON for javascript
    figuresJSON=json.dumps(figure,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',ids=ids,figuresJSON=figuresJSON)
    
