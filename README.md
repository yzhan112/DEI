# Fortune Companies DE&I Analysis

Analysis of DE&I (diversity, equity and inclusion) on Fortune companies. 

## Business Objective

This project is designed to evaluate DE&I on Fortune companies by utilizing NLP and public data. In US, all employers that have at least 100 employees are required EEO reports annually with the EEOC (Equal Employment Opportunity Commission). EEO reports are important documents for EEOC to keep track of the composition of employees for each company in terms of gender, race, age and so on. However, most of the EEO reports do not go public, which makes it hard for company manangements to evaluate their DE&I performance in contrast to other companies. On the other hand, job seekers also have difficulties to review the DE&I performance of candidate companies before applying the job. Here, I make an app to evaluate DE&I performance of 661 fortune companies based on the review comments from major job searching platforms.

## Data Collection, Feature Engineering and Data Analysis

### Data Collection

Data were collected by web sraping. The aim were to scrape 1000 reviews for each one of the fortune 1000 companies. Due to the time limitation, I only got reviews on 781 out of 1000 fortune companies. Each review contains 4 parts:

* Review Title
* Pros
* Cons
* Advice to Management

In addition, the number of employees in each company is also considered as a feature for this task. With web scraping, employee number for each fortune company is also collected.

### Feature Engineering

1. I pre-built a DE&I keywords list and use the list to filter all 4 parts of each review. After this step, I harvested all the information containing these DE&I keywords. 

| company | pros | cons | review title | advice to management |
| :---         |     :---:      |     :---:     |     :---:     |        ---: |
| X | good diversity | bad diversity |some words about DE&I | None|
| X | good diversity | None          |some words about DE&I | some words about DE&I |
| Y | good inclusion | bad diversity |None            | some words about DE&I |
| Y | None           | bad inclusion |some words about DE&I | some words about DE&I|

2. For Pros part and Cons part, I count how many comments are in each part. The count number generated two features, postive score and negative score, each comment is counted as 1.

| company | positive score | negative score |
| :---         |     :---:     |        ---: |
| X | 2 | 1 |
| Y | 1 | 2 |

3. For Review Title and Advice to Management, I use pretrained NLP sentiment analysis tool, vader, to get score for each comment. For each company, I sum up all compound scores for each part. Now I have two new columns, Review Title Score and Advice to Management Score.

| company | review title score | advice to management score |
| :---         |     :---:     |        ---: |
| X | 1.2 | -0.8 |
| Y | -1.0 | 1.2 |

4. If Total Review Title Score or total Advice to Management Score is negative, meaning they contains negative sentiment in terms of DE&I in general, it will be added up to above negative score. And if postive, they will be added up to above positive score.

| company | positive score | negative score |
| :---         |     :---:     |        ---: |
| X | 3.2 | 1.8 |
| Y | 2.2 | 3 |

5. Use a customized formular, ratio = log((positive score + 1)/(negative score + 1))

| company | ratio |
| :---    |  ---: |
| X | 0.18 |
| Y | -0.10 |

6. Combine with employee number, we can use K-Means to do clusters analysis.

| company | ratio | employee number |
| :---    |  :---: |	---: |

| X | 0.18 | 10000 |
| Y | -0.10 | 1000 |


### Data Analysis

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

## Deliverable

Based on above, I made an app to fulfill the goal of this project

