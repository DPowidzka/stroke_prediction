import pandas as pd


def data_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Generates a DataFrame with the most important information about dataset

    Args:
        data (pd.DataFrame): dataset used in analysis

    Returns:
        pd.DataFrame: DataFrame with a summary of a data
    """
    summary_data = []
    for col_name in data.columns:
        col_dtype = data[col_name].dtype
        num_of_non_nulls = data[col_name].notnull().sum()
        num_of_nulls = data[col_name].isnull().sum()
        distinct_values_count = data[col_name].nunique()
        distinct_values = data[col_name].unique().tolist()

        summary_data.append(
            {'col_name': col_name,
             'col_dtype': col_dtype,
             'num_of_non_nulls': num_of_non_nulls,
             'num_of_nulls': num_of_nulls,
             'distinct_values_count': distinct_values_count,
             'distinct_values': distinct_values
             }
        )

    summary_df = pd.DataFrame(summary_data)
    return summary_df


