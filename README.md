## Visualizing Research Trends in AI Conference Proceedings
### Introduction
Citation indexes are databases that comprise research contributions published in a variety of academic sources, most importantly journals, books and conference proceedings.

There is broad variance in the relative importance of proceedings papers across different fields of study. Computer science has been identified as a field in which conference proceedings are a major venue for communicating research findings.

The aim of this project is to study global trends scholarly literature using Scopus, to highlight apparent publishing patterns. As a result, the conclusion suggests that scholars inComputer Science show a preference for publishing conference papers as it is quicker to publish relative to journal articles or book chapters and hence might be a preferred indicator of academic output. 


### Data Cleaning and Preprocessing
The data cleaning process was as follows:
- Cleaning missing values which involved dropping columns with more than 20% missing values
- Enforcing the appropriate datatypes for object types to avoid ambiguity in values or unexpected behaviour
- Dropping of duplicates, redundant columns and unused columns
- Imputing of categorical variables 
- Formatting and extracting values using regex

**Imputing of categorical variables **\
Miaaing values in categorical variables such as author names, and country names were recoded as "Unkown"

**Extracting and Cleaning Data Using Regex**\
Regex was used to extract string values 
from text-based numeric columns (e.g., Affiliations).
The following regex was used to match each country name  out of a list of addresses in the `Affiliations` column. Each address entry consisted of roughly 2 to over 10 parts separated by commas ending with a semicolon. The country name
was typically the last part of the address before the semicolon. The pattern below was used to extract the relevant names and then subsequent filtering was applied to remove invalid matches
`r',\s([^,;]+)(?=;|$)'`

Regex was also used to produce a table of author names with their IDs and publication counts. The regex used was as follows:
`r'([\w\s]+),\s*([\w\s]+)\s*\((\d+)\)'`

Each extracted name had capitalization applied to it to maintain a consistent format for all values nad the IDs andcounts were stored as int values. The following regex was used for extraction:
`r"(.+) (\w+ \w+)$"\`


### Exploratory Data Analysis (EDA) and Aggregations
**Key Insights**\
Key insights highlighted in this analysis include:

- There might be growing interest in conference proceedings as the prefered mode of scholarly output for authors in the field of Artiifcial Intelligence. This is evidenced by a steady growth rate and approximate growth in pblication counts per year from 10,000 in 2016 to a peak of roughly 50,000 publications in 2023. A possible reason being that they are quicker and easier to publish than journal articles or book chapters. This could also be due to a combination of government investment in science, ministry guidelines incentivising publishing

- Trends in collaboration also reveal that attitudes towards multi-collaborative works have only slightly changed as the global average number of authors per publication has increased from 3 to 4

- Single-author publications remained the popular mode of collaboration for publications observed within the period studied. Multi-author publications  over the period 2019 to 2022 decreased possibly due to the COVID-19 pandemic but returned to pre-2019 proportions after 2022.

- The global trend of the productivity of authors broadly increased over the period under study. The growth in productivity did see a decrease over the  2019 to 2022 period but then picked up going into 2023.

- Share of yearly publications output was dominated by Asian multi-author collaborations,which were observed to be the leading proportion of international collaborations, followed by North American and then European collaborations. 
