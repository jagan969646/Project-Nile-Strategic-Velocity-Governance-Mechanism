import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
def load_employee_data():
    df = pd.read_csv("data/raw/employees.csv")
    return df


# -------------------------
# SPAN OF CONTROL
# -------------------------
def calculate_span_of_control(df):
    """
    Calculates number of ICs reporting to each manager.
    Returns dataframe with column 'span_of_control'
    """

    # Only employees who have a manager
    ic_df = df[df["manager_id"].notna()]

    span_df = (
        ic_df
        .groupby("manager_id")
        .size()
        .reset_index(name="span_of_control")  # IMPORTANT NAME
    )

    return span_df
