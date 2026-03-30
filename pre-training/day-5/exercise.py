import pandas as pd

df = pd.read_csv('titanic.csv')

# Question 01. How many passengers survived vs. didn't? Show as counts and percentages.

# counts = df['Survived'].value_counts()

# total =  len(df)

# percentages = (counts/total) * 100

# summery = pd.DataFrame({
#     'Count': counts,
#     'Precentage': percentages
# })

# print(summery)


# Question 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?

# grouped = df.groupby("Pclass")["Survived"]

# total = grouped.count()
# survived = grouped.sum()

# rate = (survived / total) * 100
# print(rate)

#Question 03. Average age of survivors vs. non-survivors.

# grouped = df.groupby("Survived")["Age"]

# total = grouped.count()
# age_sum = grouped.sum()

# average_age = (age_sum / total).round(0)
# print(average_age)

# Question 04. Which embarkation port had the highest survival rate?

# grouped = df.groupby('Embarked')['Survived']

# total = grouped.count()
# survived = grouped.sum()

# survival_rate = (survived / total) * 100
# print(survival_rate)

# Question 05. How many passengers have missing age values? Fill missing ages with the median age for that passenger class.

# missing_ages = df['Age'].isnull().sum()
# print(f"Number of passengers with missing age: {missing_ages}")

# df['Age']  = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))

# missing_ages_count_after = df['Age'].isnull().sum()
# print(f"Number of passengers with missing Age values after filling: {missing_ages_count_after}")

# Question 06. Who was the oldest surviving passenger? Print their name, age, class.

# survivors = df[df['Survived'] == 1]
# max_age = survivors['Age'].max()

# old_survivors = survivors[survivors['Age'] == max_age]

# print("Oldest surviving passenger(s):")
# print(old_survivors[['Name', 'Age', 'Pclass']])

# Questiuon 07. What % of women survived vs. what % of men?

# total_by_sex = df['Sex'].value_counts()
# print("Total passengers by sex:\n", total_by_sex)

# survivors_by_sex = df[df['Survived'] == 1]['Sex'].value_counts()
# print("Survivors by sex:\n", survivors_by_sex)

# survival_percent = (survivors_by_sex / total_by_sex) * 100
# print("Survival percentage by sex:\n", survival_percent)


# Question 08. Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group.\

# df['AgeGroup'] = df['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult' if x <= 60 else 'Senior')
# survival_rate_by_agegroup = df.groupby('AgeGroup')['Survived'].mean() * 100

# print(survival_rate_by_agegroup)

# Question 09. Among 3rd class passengers, what was the survival rate for men vs. women?

# third_class = df[df['Pclass'] == 3]
# survival_3rd_class = third_class.groupby('Sex')['Survived'].mean() * 100
# print("3rd class survival rate by sex (%):")
# print(survival_3rd_class)

# Question 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?

# missing_cabin = df['Cabin'].isnull().sum()
# print(f"Missing Cabin values: {missing_cabin}")

# df_cabin = df.dropna(subset=['Cabin'])
# rows_remaining = df_cabin.shape[0]
# print(f"Rows remaining after dropping missing Cabin: {rows_remaining}")

# original_rows = df.shape[0]
# percent_kept = (rows_remaining / original_rows) * 100
# print(f"Percentage of original data kept: {percent_kept:.2f}%")
