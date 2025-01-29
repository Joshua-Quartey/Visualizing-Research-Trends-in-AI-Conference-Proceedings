## Project Proposal

## Introduction
Conference proceedings\
Conferences are a major mechanism in the professional lives of  researchers facilitating the dissemination of research findings and the advancement of the field through collaboration. 

Information is typically delivered through presentations, posters, workshops  or panel discussions.
Work presented gets published in research literature in the form of conference proceedings or journal articles.

Views on how conference proceedings are weighed as evidence of scholarly activity vary by discipline considering they are generally subjected to different review standards compared to journals, are structured differently,  and cited less frequently.

Conference publications in computer science, however seem to have high scholarly impact, unlike other disciplines where journals are dominantly used for communicating scientific findings.

The Conference and Workshop on Neural Information Processing Systems (NeurIPS), the International Conference on Machine Learning(ICML) and International Conference on Learning Representations(ICLR) are three of the primary conferences of high impact in machine learning and artificial intelligence research.

## Motivation
Analysing the contribution of conference papers to the scientific literature is not that well documented and is the  aim of this project.

Insights from this analysis can help 
explore the impact of proceedings papers on future research as well as help researchers identify potential collaborators and experts who are working on complementary areas of research and presenting new research at scholarly events.

This project aims to measure the interest in topics to help document how publications are being used by the academic community

The insights of this project might also be useful to policy makers responsible for recruitment, academic promotion, or research grant awards by providing them some form of quantitative assessment of their publication output and citation impact when taking decisions


## Guiding Questions
- How has the distribution of papers across different conferences changed over the years, and are there emerging or declining venues? 

- What are the patterns of collaboration between institutions based on author affiliations, and which institutions are the most active contributors? 

- What is the geographical diversity of research contributions, analyzing author affiliations by country/region over time? 

- How has the average number of authors per paper evolved across different conferences and years? 

- Are there identifiable trends in research topics based on paper titles using text analysis? 

- What is the rate of single-institution versus multi-institution collaborative papers, and how has this changed over time? 

- What is the distribution of papers between academic, industry, and mixed academic-industry affiliations?

## Datasets 
The dataset consists of conference proceedings scraped from the web apis of the conferences NeurIPS, ICML and ICMR. It consists of 103,933 records and 5 columns namely  `Conference`, `Year`, `Title`, `Topic`, and `Affiliation`

**Collection period**\
NeurIPS : 2006 - 2023\
ICML : 2017 - 2023\
ICLR : 2018 - 2023\

## Tasks 
**Software and libraries**
Analysis will be performed using the python libraries numpy, pandas, scipy, matplotlib, wordcloud and seaborn

**EDA Techniques**
Data wrangling will include recoding of categorical variables, column datatype conversion and removing duplicates. 

Univariate exploration of each field in the raw dataset will be performed to assess its sample distributions using summary statistics.

Bivariate visualizations and summary statistics will be used to assess the relationship between each variable in the dataset and the target variable

Example visualizations to be used include stem and leaf plots, histograms, word count clouds, bar charts, pie charts,scatter plots, bubble charts, heatmaps, and run charts


## References
Drott, M.C., 1995. Reexamining the role of conference papers in scholarly communication. Journal of the American Society for Information Science, 46(4), pp.299-305.

Google Scholar. *'Artificial Intelligence h-index Google Scholar Metrics'*. Available at: https://scholar.google.es/citations?view_op=top_venues&hl=en&vq=eng_artificialintelligence(Accessed 26th JAn 2025)

Lienen. (2023). *'Papers, Authors and Author Affiliations from ICML, NeurIPS and ICLR 2006-2023'*. Available at:
https://github.com/martenlienen/icml-nips-iclr-dataset.git (accessed 25 Jan 2025)