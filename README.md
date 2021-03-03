# Fortune Companies DE&I Analysis

Analysis of DE&I (diversity, equity and inclusion) on Fortune companies. 

## Business Objective

This project is designed to evaluate DE&I on Fortune companies by utilizing NLP and public data. In US, all employers that have at least 100 employees are required EEO reports annually with the EEOC (Equal Employment Opportunity Commission). EEO reports are important documents for EEOC to keep track of the composition of employees for each companies in terms of gender, race, age and so on. However, most of the EEOreports do not go public, which makes it hard for company manangements to evaluate their DE&I performance in contrast to other companies. On the other hand, job seekers also have difficulties to review the DE&I performance of candidate companies before applying the job. Here, I make an app to evaluate DE&I performance of 661 fortune companies based on the review comments from major job searching platforms.

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
2. For Pros part and Cons part, I count how many comments are in each part. The count number generated two features, postive score and negative score, each comment is counted as 1.
3. For Review Title and Advice to Management, I use pretrained NLP sentiment analysis tool, vader, to get score for each comment. For each company, I sum up all compound scores for each part. Now I have two new columns, Review Title Score and Advice to Management Score.
4. If Review Title Score or Advice to Management Score is negative, meaning they contains negative sentiment in terms of DE&I, it will be added up to above negative score. And if postive, they will be added up to above positive score.
5. Use a customized formular, ratio = log((positive score + 1)/


### Data Analysis

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
