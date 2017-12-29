import pandas as pd

# Read chords dataframe from pickle
csv = pd.read_pickle('processed_chords.dump')

# Initialization
title = csv['Title'][0]
sentence = ''
chart = csv['ChartData'][0]
bar = ''

# Append chords
for index, row in csv.iterrows():
    if row['Chord_in_c'].find('NaN') == -1:
        if chart != row['ChartData']:
            if title == row['Title']:
                sentence = sentence + bar + ' '
            else:
                sentence = sentence + bar + '. '
            bar = ''
            title = row['Title']
        bar = bar + row['Chord_in_c']
        chart = row['ChartData']

f = open('chords_sentence.txt', 'w') # 書き込みモードで開く
f.writelines(sentence) # シーケンスが引数。
f.close()

print('Generated successfully!!!!!')