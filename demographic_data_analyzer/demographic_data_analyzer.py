import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    people_with_bachelors = df.loc[df["education"] == "Bachelors", "education"].count()
    # percentage_bachelors = round((people_with_bachelors / df.shape[0]) * 100, 1)
    percentage_bachelors = (people_with_bachelors / df.shape[0]) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_mask = (
        (df["education"] == "Bachelors")
        | (df["education"] == "Masters")
        | (df["education"] == "Doctorate")
    )
    higher_education = df[higher_education_mask]
    high_edu_count = higher_education.shape[0]
    high_salary_count = higher_education[higher_education["salary"] == ">50K"].shape[0]
    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~higher_education_mask]
    lower_edu_count = lower_education.shape[0]
    lower_salary_count = lower_education[lower_education["salary"] == ">50K"].shape[0]
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # percentage with salary >50K
    higher_education_rich = round((high_salary_count / high_edu_count) * 100, 1)
    lower_education_rich = round((lower_salary_count / lower_edu_count) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_people = df[df["hours-per-week"] == min_work_hours]
    num_min_workers = min_work_people.shape[0]
    min_work_people_high_salary = min_work_people[min_work_people["salary"] == ">50K"]
    min_work_people_high_salary_count = min_work_people_high_salary.shape[0]

    rich_percentage = round(
        (min_work_people_high_salary_count / num_min_workers) * 100, 1
    )

    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df["salary"] == ">50K"]
    native_country_series = df["native-country"].value_counts()
    rich_people_of_country_series = rich_people["native-country"].value_counts()
    rich_people_ratio_of_each_country_series = (
        rich_people_of_country_series / native_country_series
    )
    highest_earing_ratio = rich_people_ratio_of_each_country_series.max()
    highest_earning_country = rich_people_ratio_of_each_country_series.sort_values(
        ascending=False
    ).index[0]
    highest_earning_country_percentage = round(highest_earing_ratio * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_people_of_india_mask = (df["native-country"] == "India") & (
        df["salary"] == ">50K"
    )
    rich_people_of_india = df[rich_people_of_india_mask]
    top_IN_occupation = (
        rich_people_of_india["occupation"]
        .value_counts()
        .sort_values(ascending=False)
        .index[0]
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }


calculate_demographic_data()
