import json
from pathlib import Path
import re

import matplotlib.pyplot as plt
import pandas as pd


def load_stream_data(file_path):
    with open(file_path, 'r') as f:
        raw_data = json.load(f)
    dataframe = pd.DataFrame(raw_data)
    assert dataframe.isnull().sum().sum() == 0
    return dataframe


def extract_grade_factor_feature(dataframe):
    delta_adjusted_distance = dataframe['grade_adjusted_distance'].diff()
    delta_distance = dataframe['distance'].diff()
    return delta_adjusted_distance / delta_distance


def make_individual_scatterplots():
    _, ax = plt.subplots()

    for file_path in Path('out/').glob('streams_*.json'):
        data = load_stream_data(file_path)
        
        data['grade_factor'] = extract_grade_factor_feature(data)

        activity_id = re.match(r'streams_(.*).json', file_path.name).group(1)
        data.plot(kind='scatter', x='grade_smooth', y='grade_factor')
        plt.savefig(f'plots/{activity_id}.png')
        ax.clear()


def make_group_scatterplot():
    _, ax = plt.subplots()

    for file_path in Path('out/').glob('streams_*.json'):
        data = load_stream_data(file_path)
        data['grade_factor'] = extract_grade_factor_feature(data)
        ax.scatter(data['grade_smooth'], data['grade_factor'], alpha=0.1, s=10)

    plt.savefig('plots/group.png')


if __name__ == '__main__':
    make_individual_scatterplots()
    make_group_scatterplot()
    # make_subplots()