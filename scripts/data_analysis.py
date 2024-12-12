import pandas as pd

# read data
df = pd.read_csv('data/interim_data/IPED_clean.csv')

# Top 50 universities that have the most library staff
top_50_staff = df.sort_values('Librarians FTE staff',ascending=False)[:50].reset_index(drop=True)
top_50_staff.to_csv('results/top_50_staff.csv', index=False)

# Top 50 universities that have the highest average salary for library staff
top_50_salary = df.sort_values('Avg_Salary',ascending=False)[:50].reset_index(drop=True)
top_50_salary.to_csv('results/top_50_salary.csv', index=False)

# Number of libary jobs offered by each State (ranked)
number_of_staff_ranked_by_state = (
    df.groupby('State abbreviation')['Total library FTE staff'].sum()
    .sort_values(ascending=False)
    .reset_index(name='Sum_of_Libary_Staff')
)
number_of_staff_ranked_by_state['Sum_of_Libary_Staff'] = number_of_staff_ranked_by_state['Sum_of_Libary_Staff'].astype(int)
number_of_staff_ranked_by_state.to_csv('results/number_of_staff_ranked_by_state.csv', index=False)

# Salary by State (ranked)
salary_by_state_ranked = df.groupby('State abbreviation')['Avg_Salary'].mean().sort_values(ascending=False).reset_index(name='Avg_Salary')
salary_by_state_ranked['Avg_Salary'] = salary_by_state_ranked['Avg_Salary'].astype(int)
salary_by_state_ranked.to_csv('results/salary_by_state_ranked.csv', index=False)

