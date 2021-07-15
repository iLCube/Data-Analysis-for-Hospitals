import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

g_f = pd.read_csv('general.csv')
p_f = pd.read_csv('prenatal.csv')
s_f = pd.read_csv('sports.csv')

p_f.columns, s_f.columns = g_f.columns, g_f.columns
hospital = pd.concat([g_f, p_f, s_f], ignore_index=True)
hospital.drop(columns=['Unnamed: 0'], inplace=True)

hospital['gender'] = hospital['gender'].replace(['man', 'male'], 'm')
hospital['gender'] = hospital['gender'].replace(['woman', 'female', 'NaN'], 'f')

hospital['bmi'] = hospital['bmi'].fillna(0)
hospital['diagnosis'] = hospital['diagnosis'].fillna(0)
hospital['blood_test'] = hospital['blood_test'].fillna(0)
hospital['ecg'] = hospital['ecg'].fillna(0)
hospital['ultrasound'] = hospital['ultrasound'].fillna(0)
hospital['mri'] = hospital['mri'].fillna(0)
hospital['xray'] = hospital['xray'].fillna(0)
hospital['children'] = hospital['children'].fillna(0)
hospital['months'] = hospital['months'].fillna(0)


def highest_patients(df):
    patients = {'general': 0, 'prenatal': 0, 'sports': 0}
    for i in df['hospital']:
        if i == 'general':
            patients['general'] += 1
        elif i == 'prenatal':
            patients['prenatal'] += 1
        elif i == 'sports':
            patients['sports'] += 1
    return max(patients, key=patients.get)


def general_stomach_issues(df):
    count = 0
    general_patients = df[df['hospital'] == 'general']
    for i in general_patients['diagnosis']:
        if i == 'stomach':
            count += 1

    return round(count / len(general_patients), 3)


def sports_dislocation_issues(df):
    count = 0
    general_patients = df[df['hospital'] == 'sports']
    for i in general_patients['diagnosis']:
        if i == 'dislocation':
            count += 1

    return round(count / len(general_patients), 3)


def median_ages_general_sports(df):
    general_patients = df[df['hospital'] == 'general']
    sports_patients = df[df['hospital'] == 'sports']
    return general_patients['age'].median() - sports_patients['age'].median()


def highest_number_of_patients(df):
    df['hospital'].value_counts().plot(kind='bar')
    plt.show()


def most_common_diagnosis(df):
    df['hospital'].value_counts().plot(kind='bar')
    plt.show()


def growth_distribution():
    sns.violinplot(data=hospital['height'])
    plt.show()
