import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', names=['age', 'workclass', 'fnlwgt', 
                                              'education', 'education-num', 'marital-status', 
                                              'occupation', 'relationship', 'race', 
                                              'sex', 'capital-gain', 'capital-loss', 
                                              'hours-per-week', 'native-country', 'salary'])

    # Convert columns to numeric where needed
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

    # Drop rows with missing data
    df.dropna(inplace=True)

    # Race count
    race_count = df['race'].value_counts().sort_values(ascending=False)

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage earning >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Minimum work hours
    min_work_hours = int(df['hours-per-week'].min())

    # Rich percentage among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with highest percentage of rich
    earning_by_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / 
                          df['native-country'].value_counts()) * 100
    earning_by_country.dropna(inplace=True)
    highest_earning_country = earning_by_country.idxmax()
    highest_earning_country_percentage = round(earning_by_country.max(), 1)

    # Top occupation in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0] if not india_rich.empty else None

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }