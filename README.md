# Title
Where to Shelf Your Career: Comparing Academic Library Staffing and Costs of Living

# Link to archival record
CodeOcean

# Contributors
- Wanheng Li: 0009-0002-4039-6567

# Summary
As an LIS student interested in working in an academic library, I want to find out which institutions hire the most librarians and which states offer the best income-to-cost-of-living ratio for librarians. This project aims to serve as a reference for fellow library science students pursuing academic library careers. It examines the staffing levels of academic institutions and states, evaluates average library staff salaries in each state, and compares these earnings to regional living costs.

Four tables are created:
- A ranked list of the top 50 universities offering the highest number of library positions
- A ranked list of the top 50 universities offering the highest average salaries for library positions
- A ranked summary of the number of library positions offered in each state
- A ranked summary of the average salary for library positions in each state

Two visualizations are created:
- The first visualization is an interactive map linked to a bar chart, illustrating the 2023 Personal Consumption Expenditures (PCE) by state. Each state is color-coded according to its overall expenditures. The accompanying bar chart provides a more detailed breakdown of these costs into specific categories like housing and food. By clicking on a state in the map, the bar chart updates to reflect that state’s data. This allows users to quickly identify which states have higher living expenses and understand how various expenditure categories contribute to the overall cost of living.

- The second visualization is a scatter plot comparing average library staff salaries to each state’s living costs. Hovering over the data points reveals the state names. This plot helps users quickly identify states offering higher average salaries combined with lower living expenses.

# Data profile 
[500-1000 words] Description of each dataset used including license/terms of use.
- `AcademicLibrary_11-12-2024.csv` is 
- `PCE.csv` is a dataset that 
- `us-state-names.tsv` is


# Findings
- Although California, Texas, Florida, and New York offer a large number of library staff positions, their high cost of living compared to salaries may reduce their overall appeal.
- Delaware presents an excellent cost-of-living-to-salary ratio, but currently offers relatively few library positions.
- Users can utilize these visualizations to explore states of interest and determine the best balance between available library positions, cost of living, and salary levels that align with their personal requirements.

# Future work
The initial analysis estimated average librarian salaries by dividing the total salary budget by the total number of library staff. However, universities have librarians and other full-time library staff, and it is likely that they have different salary levels. To obtain a more accurate estimate of average librarian salaries, future research could explore alternative data sources,

While Personal Consumption Expenditures (PCE) offer a broad overview of spending patterns, they are not the most suitable metric for estimating individual cost of living. PCE represents the total spending on goods and services in a specific region, and it doesn't account for individual variations in lifestyle and needs. For example, PCE in 2023 in California is $2526290.3, but it's unlikely that a person has to make this much to survive in California. Future research could use other data to estimiate the cost of living in each region.

Future work can also compare compare librarian salaries with other professions all to evaluate how well-compensated the job of a librarian is. One data could be untilized is Occupational Employment and Wage Statistics (OWES) Tables: https://www.bls.gov/oes/tables.htm from Bureau of Labor Statistics. I planned to use this data in the original Project Plan. However, due to the time limit, this has to be done in future work.

# Reproducing 
Sequence of steps required for someone else to reproduce your results.
1. Download the IPEDs and PCE datasets
Both datasets are not accessible through API and cannot be easily downloaded via wget. Here I desbribe the steps to download the files.
- IPEDs
1. Go to URL: https://nces.ed.gov/ipeds/datacenter/SelectVariables.aspx?stepId=1&sid=1f7ec561-a803-4ea6-8163-3761c55f451f&rtid=1
![IPEDS Data Tool]](screenshots/IPEDS1.png)
2. Go to Snakefile code 

# References
Formatted citations for any papers, datasets, or software used in your project.


wiki 

