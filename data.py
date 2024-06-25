import pandas as pd

df = pd.read_csv('test.csv', sep=';')
df.columns = df.columns.str.strip()

job_translation = {
    "admin.": "Администратор",
    "unknown": "Неизвестно",
    "unemployed": "Безработный",
    "management": "Менеджмент",
    "housemaid": "Домработница",
    "entrepreneur": "Предприниматель",
    "student": "Студент",
    "blue-collar": "Рабочий",
    "self-employed": "Самозанятый",
    "retired": "На пенсии",
    "technician": "Техник",
    "services": "Сфера услуг"
}

month_translation = {
    "apr": "Апрель",
    "aug": "Август",
    "dec": "Декабрь",
    "feb": "Февраль",
    "jan": "Январь",
    "jul": "Июль",
    "jun": "Июнь",
    "mar": "Март",
    "may": "Май",
    "nov": "Ноябрь",
    "oct": "Октябрь",
    "sep": "Сентябрь"
}

cont_translation = {
    "unknown": "Неизвестно",
    "failure": "Провал",
    "other": "Другое",
    "success": "Удачно",
}

df['poutcome'] = df['poutcome'].map(cont_translation)

df['job'] = df['job'].map(job_translation)

df['month'] = df['month'].map(month_translation)

education_translation = {
    "primary": "Начальное",
    "secondary": "Среднее",
    "tertiary": "Высшее",
    "unknown": "Неизвестно"
}
df['education'] = df['education'].map(education_translation)

df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 45, 55, 65, 100], labels=['0-25', '26-35', '36-45', '46-55', '56-65', '65+'])

marital_translation = {
    "single": "Не в браке",
    "married": "В браке",
    "divorced": "Разведен"
}

df['marital'] = df['marital'].map(marital_translation)

housing_translation = {
    "yes": "Есть",
    "no": "Нет"
}

df['housing'] = df['housing'].map(housing_translation)