import nltk
import os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from snownlp import SnowNLP
from snownlp import sentiment

os.getcwd()
os.chdir('C:\\Users\\yzhon_000\\PycharmProjects\\ChineseNLP\\csenticnet')

with open('csenticnet.txt', 'r', encoding='UTF-8') as text:
    content = text.readlines()
    content = [x.strip() for x in content]
text.close()

# print(content)

os.chdir('C:\\Users\\yzhon_000\\Documents\\IST664')
text1 = open('1999chen.txt', encoding='utf-8').read()

# read text into sentences
s = SnowNLP(text1)
sentences = s.sentences
sentiment_list = []

os.chdir('C:\\Users\\yzhon_000\\PycharmProjects\\ChineseNLP\\venv\\lib\\site-packages\\snownlp\\sentiment\\')

sentiment.train('neu.txt', 'pos.txt', 'scared.txt', 'angry.txt')
sentiment.save('sentiment.marshal')
data_path=os.path.join(os.path.dirname(os.path.abspath('C:\\Users\\yzhon_000\\PycharmProjects\\ChineseNLP\\venv\\Lib\\site-packages\\snownlp\\sentiment')),'sentiment.marshal')

for sent in sentences:
    s = SnowNLP(sent)
    line = sent + ',' + str(s.sentiments)
    sentiment_list.append(line)

print(sentiment_list)

# start counting different types of emotions
count_positive = 0
count_neutral = 0
count_scared = 0
count_angry = 0
total_count = 0
sentiment_only = []
summary_list = []

for sent in sentences:
    s = SnowNLP(sent)
    total_count = total_count + 1
    if 0.8 < s.sentiments <= 1:
        count_positive = count_positive + 1
    elif 0 <= s.sentiments <= 0.8:
        count_neutral = count_neutral + 1
    elif 1 < s.sentiments <= 2:
        count_scared = count_scared + 1
    elif 2 < s.sentiments <= 3:
        count_angry = count_angry + 1
    line = sent + ', ' + str(s.sentiments)
    sentiment_only.append(s.sentiments)
    summary_list.append(line)

summary_list.append("Positive" + " " + str(count_positive))
summary_list.append("Neutral" + " " + str(count_neutral))
summary_list.append("Scared" + " " + str(count_scared))
summary_list.append("Angry" + " " + str(count_angry))
summary_list.append("Total Sentences" + " " + str(total_count))

print(summary_list)

# output graphs
# Login Plot
plotly.tools.set_credentials_file(username='YuhuiZhong', api_key='bIrTWCOmZIlDw8B5h5mY')

x_index = list(range(1, total_count + 1))
y_number = sentiment_only

print(x_index)
print(y_number)

'''
trace0 = go.Bar(
    x=x_index,
    y=y_number,
    text=y_number,
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

data = [trace0]
layout = go.Layout(
    title='Sentiment Variation',
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig)

'''

pos_list = []
neu_list = []
scared_list = []
angry_list = []

for i in sentiment_only:
    if 0.8 < i <= 1:
        pos_list.append(i)
    else:
        pos_list.append(0)

for i in sentiment_only:
    if 0 < i <= 0.8:
        neu_list.append(i)
    else:
        neu_list.append(0)

for i in sentiment_only:
    if 1 < i <= 2:
        scared_list.append(i)
    else:
        scared_list.append(0)

for i in sentiment_only:
    if 2 < i <= 3:
        angry_list.append(i)
    else:
        angry_list.append(0)

trace = go.Heatmap(z=[pos_list, neu_list, scared_list, angry_list],
                   x=x_index,
                   y=['Positive', 'Neutral', 'Scared', 'Angry'],
                   colorscale=[[0, 'rgb(255,255,255)'], [0.264, 'rgb(192,192,192)'], [0.33, 'rgb(106,190,69)'],
                               [0.66, 'rgb(253,210,46)'], [1, 'rgb(204,32,40)']],
                   )
# colorscale='Viridis', )
data = [trace]
py.plot(data)
