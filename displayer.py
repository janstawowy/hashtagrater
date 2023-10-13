import pandas as pd
import plotly.express as px

class Displayer:


    def __init__(self,dataframe):
        self.dataframe = dataframe

    def display_sentiment(self):
        # Create an interactive pie chart with text labels
        result = self.dataframe.groupby('final_verdict')['text'].apply(lambda x: '<br>'.join(x)).reset_index().rename(columns={'text': 'concat_text'})
        self.dataframe = self.dataframe.merge(result, on='final_verdict', how='left')
        fig = px.pie(self.dataframe, names='final_verdict',title='Categorical Data Distribution',
                     hover_name='final_verdict', hover_data={"concat_text": True})

        # Set how text labels are displayed on the chart
        fig.update_traces(textposition='inside', textinfo='percent+label')

        # Show the interactive chart
        fig.show()