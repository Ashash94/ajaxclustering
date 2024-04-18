import pandas as pd

pd.set_option(
    "future.no_silent_downcasting", True
)  # Option that removes the warning about deprecated replace method


def format_data(data):
    data["Gender"] = data["Gender"].replace({"Male": 0, "Female": 1})
    return data
