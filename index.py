python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Load dataset
data = pd.read_excel('Distribution_of_Pensioners_2022.xlsx')

# Data preprocessing
data['Quarter'] = data['Quarter'].astype(str)
data['Percentage'] = data['Percentage'].apply(lambda x: x * 100)

@app.route('/')
def index():
    # Create a bar chart for gender distribution
    fig = px.bar(
        data,
        x='Quarter',
        y='Count',
        color='Type',
        title='Pensioners Distribution by Gender and Quarter',
        labels={'Count': 'Number of Pensioners', 'Quarter': 'Quarter'},
        barmode='group'
    )

    # Convert Plotly figure to HTML
    graph = fig.to_html(full_html=False)

    return render_template('index.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)
