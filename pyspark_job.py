from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def clean_data(df: DataFrame) -> DataFrame:
    """
    Cleans the input DataFrame by:
    - Removing rows where amount <= 0
    - Removing rows where name is NULL
    - Adding 'amount_with_tax' column (amount * 1.20)
    """
    return (
        df.filter(col("amount") > 0)
        .filter(col("name").isNotNull())
        .withColumn("amount_with_tax", col("amount") * 1.20)
    )
