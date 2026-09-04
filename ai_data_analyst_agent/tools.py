import pandas as pd


def read_csv(file_path):
    df = pd.read_csv(r"C:\Users\boopa\OneDrive\AI-Agent\ai_data_analyst_agent\data.csv")

    return df


def get_columns(file_path):
    df = pd.read_csv(r"C:\Users\boopa\OneDrive\AI-Agent\ai_data_analyst_agent\data.csv")

    return list(df.columns)


def get_summary(file_path):
    df = pd.read_csv(r"C:\Users\boopa\OneDrive\AI-Agent\ai_data_analyst_agent\data.csv")

    return df.describe()


def get_average_salary(file_path):
    df = pd.read_csv(r"C:\Users\boopa\OneDrive\AI-Agent\ai_data_analyst_agent\data.csv")

    return df["Salary"].mean()


tool_mapping = {
    "read_csv": read_csv,
    "get_columns": get_columns,
    "get_summary": get_summary,
    "get_average_salary": get_average_salary
}