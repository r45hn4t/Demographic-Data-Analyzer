import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df["age"].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df["education"] == "Bachelors"]
                            ["education"].count()/df["education"].count())*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mask1 = (df["education"] == "Bachelors") | (df["education"]
                                                == "Masters") | (df["education"] == "Doctorate")
    mask2 = df["salary"] == ">50K"
    mask3 = (mask1) & (mask2)
    higher_education = mask3.sum()
    higher_education_rich = ((mask3.sum())/(mask1.sum()))*100
    mask1 = df['education'] != "Bachelors"
    mask2 = df['education'] != "Masters"
    mask3 = df['education'] != "Doctorate"
    mask4 = df["salary"] == ">50K"
    mask = (mask1) & (mask2) & (mask3) & (mask4)
    lower_education = mask.sum()
    lower_education_rich = (
        (mask.sum())/(((mask1) & (mask2) & (mask3)).sum()))*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask1 = df["hours-per-week"] == df["hours-per-week"].min()
    mask2 = df['salary'] == ">50K"
    mask3 = (mask1) & (mask2)
    percentt = ((mask3.sum())/(mask1.sum()))*100
    num_min_workers = mask3.sum()

    rich_percentage = percentt

    # What country has the highest percentage of people that earn >50K?
    country_list = df["native-country"].unique()
    df2 = pd.DataFrame(country_list)
    df2.replace("?", np.NAN, inplace=True)
    df2 = df2.dropna()
    mask = df["salary"] == ">50K"
    cl = dict()
    tot = []
    for i in country_list:
        mask1 = df["salary"] == ">50K"
        mask2 = (df["native-country"] == i)
        mask3 = (mask1) & (mask2)
        count1 = mask3.sum()
        cl[i] = count1
        tot.append(mask2.sum())
    values = cl.values()
    indexx = cl.keys()
    dfr = pd.DataFrame(values, index=indexx, columns=[">50k_count"])
    dfr['total'] = tot
    dfr["percent"] = (dfr[">50k_count"]/dfr["total"])*100
    dfr = dfr.dropna()
    dfr["country"] = dfr.index
    result = dfr[dfr["percent"] == dfr["percent"].max()]["country"]
    highest_earning_country = f"{result}"
    highest_earning_country_percentage = dfr["percent"].max()

    # Identify the most popular occupation for those who earn >50K in India.
    mask1 = df["native-country"] == "India"
    mask2 = df["salary"] == ">50K"
    mask = (mask1) & (mask2)
    dfrr = df[mask]["occupation"].value_counts()
    dfrr = pd.DataFrame(dfrr)
    dfrr["occ"] = dfrr.index
    result = dfrr[dfrr["occupation"] == dfrr["occupation"].max()]["occ"]
    top_IN_occupation = f"{result}"

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()