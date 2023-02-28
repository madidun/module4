#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending 645-675 per student actually underperformed compared to schools with smaller budgets (585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# In[1]:


# Dependencies and Setup
import pandas as pd


# In[5]:


school_spending = pd.DataFrame({
    "School Type":school_types,
    "Total Students": per_school_counts,
    "Total School Budget":per_school_budget,
    "Per Student Budget":per_school_capita,
    "Average Math Score":per_school_math,
    "Average Reading Score":per_school_reading,
    "% Passing Math":per_school_passing_math,
    "% Passing Reading":per_school_passing_reading,
    "% Overall Passing":overall_passing_percentage
})
school_spending


# In[2]:


# File to Load (Remember to Change These)
school_data_path = "Resources/schools_complete.csv"
student_data_path = "Resources/students_complete.csv"


# In[3]:


# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_path)
student_data = pd.read_csv(student_data_path)
school_data


# In[4]:


student_data


# In[5]:


# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# ## District Summary

# In[6]:


# Calculate the total number of unique schools
school_count = school_data_complete.nunique()["school_name"]
school_count


# In[7]:


# Calculate the total number of students
student_count = school_data_complete["student_name"].count()
student_count


# In[8]:


# Calculate the total budget
total_budget = school_data["budget"].sum()
format(total_budget,".1E")


# In[9]:


# Calculate the average (mean) math score (78.98537145774827)
average_math_score = school_data_complete["math_score"].mean()
average_math_score


# In[10]:


# Calculate the average (mean) reading score
average_reading_score = school_data_complete["reading_score"].mean()
average_reading_score


# In[11]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_series = school_data_complete["math_score"] >= 70
passing_math_count = school_data_complete[passing_math_series].count()["student_name"]
passing_math_percentage = 100 * (passing_math_count / student_count) 
passing_math_percentage


# In[12]:


school_data_complete[passing_math_series]


# In[13]:


# Calculate the percentage of students who passeed reading (hint: look at how the math percentage was calculated)  
passing_reading_count = school_data_complete["reading_score"] >= 70
passing_reading_percentage = 100 * (passing_reading_count / student_count) 
passing_reading_percentage


# In[18]:


# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_percentage = passing_math_reading_count /  float(student_count) * 100
overall_passing_percentage


# In[22]:


# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame({
    "Total School":[school_count],
    "Total Students":[student_count],
    "Total Budget":[total_budget],
    "Average Math Score":[average_math_score],
    "Average Reading Score":[average_reading_score],
    "% Passing Math":[passing_math_percentage],
    "% Passing Reading":[passing_reading_percentage],
    "% Overall Passing":[overall_passing_percentage]
})
# Display the DataFrame
district_summary


# In[25]:


district_summary = pd.DataFrame({
    "Total School":[school_count],
    "Total Students": [student_count],
    "Total Budget":[total_budget],
    "Average Math Score":[average_math_score],
    "Average Reading Score":[average_reading_score],
    "% Passing Math":[passing_math_percentage],
    "% Passing Reading":[passing_reading_percentage],
    "% Overall Passing":[overall_passing_percentage]
})

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)
# Display the DataFrame
district_summary


# ## School Summary

# In[27]:


# Use the code provided to select the school type
school_types = school_data.set_index(["school_name"])["type"]
school_types


# In[28]:


# Calculate the total student count
per_school_counts = school_data_complete["student_name"].count()
per_school_counts


# In[29]:


# Calculate the total school budget 
per_school_budget = school_data["budget"].sum()
per_school_budget


# In[40]:


# Calculate the per capita spending
per_school_capita = total_budget / per_school_counts
per_school_capita


# In[30]:


# Calculate the average test scores
per_school_math = school_data_complete["math_score"].mean()
per_school_math


# In[31]:


# Calculate the average test scores
per_school_reading = school_data_complete["reading_score"].mean()
per_school_reading


# In[32]:


# Calculate the number of schools with math scores of 70 or higher
school_passing_math = school_data_complete[(school_data_complete["math_score"] >=70)].groupby (["school_name"]).count()
school_passing_math


# In[33]:


# Calculate the number of schools with reading scores of 70 or higher
school_passing_reading = school_passing_math = school_data_complete[(school_data_complete["reading_score"] >=70)].groupby (["school_name"]).count()
school_passing_reading


# In[34]:


# Use the provided code to calculate the schools that passed both math and reading with scores of 70 or higher
passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)
]
passing_math_and_reading 


# In[35]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_passing_math.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
per_school_passing_reading = school_passing_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100
overall_passing_rate = passing_math_and_reading.groupby(["school_name"]).count()["student_name"] / per_school_counts * 100


# In[41]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.per_school_summary = pd.DataFrame({
per_school_summary = pd.DataFrame({
    "School Type":school_types,
    "Total Students": per_school_counts,
    "Total School Budget":per_school_budget,
    "Per Student Budget":per_school_capita,
    "Average Math Score":per_school_math,
    "Average Reading Score":per_school_reading,
    "% Passing Math":per_school_passing_math,
    "% Passing Reading":per_school_passing_reading,
    "% Overall Passing":overall_passing_percentage
})
# Display the DataFrame
per_school_summary


# ## Highest-Performing Schools (by % Overall Passing)

# In[45]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
high_performing=per_school_summary.sort_values("% Overall Passing", ascending = False)
high_performing                               


# ## Bottom Performing Schools (By % Overall Passing)

# In[47]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_performing=per_school_summary.sort_values("% Overall Passing", ascending = False)
bottom_performing 


# ## Math Scores by Grade

# In[53]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"] 


# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade=pd.DataFrame({
    "9th": ninth_graders_scores,
    "10th": tenth_graders_scores,
    "11th": eleventh_graders_scores,
    "12th": twelfth_graders_scores
})

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# ## Reading Score by Grade 

# In[54]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by "school_name" and take the mean of each.
ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"] 

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade=pd.DataFrame({
    "9th": ninth_graders_scores,
    "10th": tenth_graders_scores,
    "11th": eleventh_graders_scores,
    "12th": twelfth_graders_scores
})

# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# ## Scores by School Spending

# In[66]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[57]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()
school_spending_df


# In[1]:


# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(df["Spending Ranges"], bins, labels=group_names, include_lowest=True)
df


# In[67]:


#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame
spending_summary = 

# Display results
spending_summary


# ## Scores by School Size

# In[ ]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.

per_school_summary["School Size"] = 


# In[ ]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores = per_school_summary.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math = per_school_summary.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary.groupby(["School Size"]).mean()["% Overall Passing"]


# In[ ]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = pd.DataFrame({
    "S"

# Display results
size_summary


# ## Scores by School Type

# In[6]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
type_math_scores = df.groupby("School Type")
type_reading_scores = df.groupby("School Type")
type_passing_math = df.groupby("School Type")
type_passing_reading = df.groupby("School Type")
type_overall_passing = df.groupby("School Type")

# Use the code provided to select new column data
average_math_score_by_type = type_math_scores["Average Math Score"]
average_reading_score_by_type = type_reading_scores["Average Reading Score"]
average_percent_passing_math_by_type = type_passing_math["% Passing Math"]
average_percent_passing_reading_by_type = type_passing_reading["% Passing Reading"]
average_percent_overall_passing_by_type = type_overall_passing["% Overall Passing"]


# In[ ]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame({
average_math_score_by_type = type_math_scores
average_reading_score_by_type = type_reading_scores
average_percent_passing_math_by_type = type_passing_math
average_percent_passing_reading_by_type = type_passing_reading
average_percent_overall_passing_by_type = type_overall_passing
({
# Display results
type_summary


# In[ ]:




