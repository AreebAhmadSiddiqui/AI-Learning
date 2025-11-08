from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
    In our hyper-connected world, boredom is treated as a failure of stimulation, an emptiness to be filled with digital noise. We instinctively reach for our phones, seeking refuge from the quiet moment. Yet, it is in this very space of perceived idleness that creativity often sparks. When the mind is unoccupied by external inputs, it turns inward. It wanders, connects disparate ideas, and daydreams. This mental wandering is not a waste of time; it is the subconscious workshop where problems are solved and new perspectives are born. By constantly avoiding boredom, we may be sacrificing our most profound creative potential. The richest ideas often emerge not from focused effort, but from the quiet, fertile ground of a mind allowed to be adrift. Embracing occasional boredom could be the key to unlocking a deeper, more imaginative self.

    """


splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    # separators=["\n\n", "\n", ". ", " ", ""]
)

result=splitter.split_text(text)

# print(result)


code="""
import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.clean_data()
    
    def clean_data(self):
        # Remove null values
        self.data = self.data.dropna()
        
        # Standardize column names
        self.data.columns = [col.lower() for col in self.data.columns]

def calculate_metrics(dataframe):
    summary = {}
    for column in dataframe.columns:
        if dataframe[column].dtype in ['int64', 'float64']:
            summary[column] = {
                'mean': dataframe[column].mean(),
                'std': dataframe[column].std()
            }
    return summary

"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks=splitter.split_text(code)
print(chunks)