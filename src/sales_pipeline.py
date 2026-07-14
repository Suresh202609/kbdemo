from pyspark.sql import SparkSession


def main():

    spark = SparkSession.builder \
        .appName("Retail Sales Pipeline") \
        .getOrCreate()


    df = spark.read \
        .option("header","true") \
        .csv("s3://retail-input/sales/")


    clean_df = df.dropDuplicates()


    clean_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(
        "dev_sales.sales_clean"
        )


if __name__ == "__main__":
    main()
