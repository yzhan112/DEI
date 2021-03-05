import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import wordle
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def app():
    
    stopwords = set(STOPWORDS)
    stopwords.update([
                      'nan', 'advice', 'management', 'time', 'job', 'work', 'day', 'year', 'working', 'company', 'employee', 'employees', 
                      'take', 'even', 'well', 'good', 'know', 'place','want', 'manager', 'thing', 'hr', 'years', 'new', 'hour', 'talk', 'feel',
                      'come', 'bad', 'keep', 's', 'way', 'out', 'really', 'look', 'lot', 'week', 'made', 'level', 'little', 'make', 'position', 'issue', 'department', 'especially', 'better', 'staff', 'customer',                      'hire', 'change', 'pay', 'poor', 'team', 'sotp', 'leader', 'business', 'need', 'training', 'people', 'managers', 'promote', 'promotion', 'experience', 'upper', 'needs', 'group',
                      'low', 'leave', 'treat', 'every', 'focus', 'positions', 'leaders', 'levels', 'great' 'don t', 'action', 'n', 'care', 't', 'don', 'leadership', 'never', 'executive', 'help', 'less', 'joke',
                      'start', 'run', 'instead', 'stop', 'someone', 'office', 'sale', 'say', 'hiring', 'first', 'run', 'role', 'raise', 'number', 'promoted', 'based', 'back', 'enough', 'toward', 'u', 'hours',
                      'support', 'high', 'worker', 'please', 'hard', 'real', 'great', 'program', 'nothing', 'top', 'customers', 'sales', 'lead', 'going', 'horrible', 'still', 'us', 'roles', 'always', 'value', 
                      'long', 'policies', 'talent'
])
    
    gd = pd.read_csv('gd_vader.csv')

    gd['cons'] = gd['cons'].astype(str)
    text = " ".join(gd['cons'])
    wordcloud = wordle.WordCloud(width = 1600, height = 800, 
                                background_color ='white', 
                                stopwords = stopwords, 
                                min_font_size = 30).generate(text)

    fig = plt.figure(figsize=(10,5), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    st.pyplot(fig)
    # Generate plot

    st.title("Fortune Companies DE&I Analysis")
    st.write(f'Eric Zhang')
    
    st.markdown(""" 


 

## Business Objective

This project is designed to evaluate DE&I on Fortune companies by utilizing NLP and public data. In US, all employers that have at least 100 employees are required EEO reports annually with the EEOC (Equal Employment Opportunity Commission). EEO reports are important documents for EEOC to keep track of the composition of employees for each company in terms of gender, race, age and so on. However, most of the EEO reports do not go public, which makes it hard for company managements to evaluate their DE&I performance in contrast to other companies. On the other hand, job seekers also have difficulties to review the DE&I performance of candidate companies before applying the job. Here, I make an app to evaluate DE&I performance of 661 fortune companies based on the review comments from major job searching platforms. By using this app, company managements as well as job seekers can have a general ideal how good the company is performing in terms of DE&I.

## Data Collection and Feature Engineering

### Data Collection

Data were collected by web sraping. The aim were to scrape 1000 reviews for each one of the fortune 1000 companies. Due to the time limitation, I only got reviews on 661 out of 1000 fortune companies. Each review contains 4 parts:

* Review Title
* Pros
* Cons
* Advice to Management

In addition, the number of employees in each company is also considered as a feature for this task. With web scraping, employee number for each fortune company is also collected.

### Feature Engineering

**1.** I pre-built a DE&I keywords list and use the list to filter all 4 parts of each review. After this step, I harvested all the information containing these DE&I keywords. For example,

| company | pros | cons | review title | advice to management |
| :---:         |     :---      |     :---     |     :---     |        :--- |
| X | good diversity | bad diversity |some words about DE&I | None|
| X | good diversity | None          |some words about DE&I | some words about DE&I |
| Y | good inclusion | bad diversity |None            | some words about DE&I |
| Y | None           | bad inclusion |some words about DE&I | some words about DE&I|
  
**2.** For Pros part and Cons part, I count how many comments are in each part. The count number generated two features, postive score and negative score, each comment is counted as 1.

| company | positive score | negative score |
| :---:         |     :---:     |        :---: |
| X | 2 | 1 |
| Y | 1 | 2 |

**3.** For Review Title and Advice to Management, I use pretrained NLP sentiment analysis tool, vader, to get score for each comment. For each company, I sum up all compound scores for each part. Now I have two new columns, Review Title Score and Advice to Management Score.

| company | review title score | advice to management score |
| :---:        |     :---:     |        :---: |
| X | 1.2 | -0.8 |
| Y | -1.0 | 1.2 |

**4.** If Total Review Title Score or total Advice to Management Score is negative, meaning they contains negative sentiment in terms of DE&I in general, it will be added up to above negative score. And if postive, they will be added up to above positive score.

| company | positive score | negative score |
| :---:         |     :---:     |        :---: |
| X | 3.2 | 1.8 |
| Y | 2.2 | 3.0 |

**5.** Use a customized formular, ratio = log((positive score + 1)/(negative score + 1))

| company | ratio |
| :---:    |  :---: |
| X | 0.18 |
| Y | -0.10 |

**6.** Combine with employee number, I get the following dataset. 

| company | ratio | employee number |
| :---:    |  :---: |   :---: |
| X | 0.18 | 10000 |
| Y | -0.10 | 1000 |

**7.** If ratio is greater than zero, it means that it has more positive comments about DE&I than negative ones. Therefore, I can label companies with good DE&I or bad DE&I based on the value of ratio (This is not really bad DE&I, just for easy understanding). Based on the employee number, I can label companies with small company, medium company or large company.

| company | ratio | employee number | DE&I | company size |
| :---:    |  :---: |   :---: |  :---: |  :---:  |
| X | 0.18 | 10000 | good DE&I | Large Company |
| Y | -0.10 | 1000 | bad DE&I | Medium Company |

## Data Analysis and Deliverable

Based on above, I made an interactive plot to fulfill the goal of this project, which evaluates DE&I performance in terms of company size (number of total employees) 
    """)
    
    
    dei = pd.read_csv('dei_analysis.csv', header = 0)
    brush = alt.selection_interval()
    chart = alt.Chart(dei, title = 'Fortune Companies DE&I Analysis').mark_point().encode(
            x = 'relative num of employees',
            y = 'pos/neg log ratio',
            color = alt.condition(brush, 'desc:N', alt.value('lightgray')),
            #color = alt.Color('desc',scale=alt.Scale(scheme= 'dark2')),
            tooltip = ['company', 'pos/neg log ratio']).configure_axis(grid=False).properties(width = 750, height = 500).add_selection(brush)
    chart = chart.configure()\
                 .configure_title(fontSize = 16)\
                 .configure_axis(titleFontSize = 14, labelFontSize = 12)\
                 .configure_legend(titleFontSize = 12, labelFontSize = 10, symbolSize = 100)
    st.write(chart)

if __name__ == '__main__':
    app()
