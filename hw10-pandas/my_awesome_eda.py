def run_eda(df):
    '''
    Main function which performs Exploratory Data Analysis (EDA) on the input df DataFrame and prints its statistics.
    '''
    print('🖖 Greetings, Earthling!')
    print(f"\n👨🏻‍💻According to my calculations, in the observed table \nThe number of observations/rows is {df.shape[0]} \nThe number of parameters/columns is {df.shape[1]}")

    numerical = []
    categorical = []
    string = []

    for column in df.columns:
        unique_values = df[column].nunique()
        value_type = df[column].dtype

        if (value_type == 'object' and unique_values > 5) or any(substring in column for substring in ['ID', 'Id']):
            string.append(column)
        elif unique_values < 5:
            categorical.append(column)
        else:
            numerical.append(column)
    
    print(f"\n🤖Categorical columns:{categorical}")
    print(f"🤖Numerical columns:{numerical}")
    print(f"🤖String columns:{string}")
    
    for column in categorical:
        print(f"\n🧮Counts: {df[column].value_counts()}")
        print(f"\n🧮Frequencies: {df[column].value_counts(normalize=True)}")

    for column in numerical:
        print(f"\n🔢{column} statistics:")
        print(f"📉Min: {df[column].min()}")
        print(f"📈Max: {df[column].max()}")
        print(f"😒Mean: {df[column].mean()}")
        print(f"✍🏼Std: {df[column].std()}")
        print(f"📊Q0.25: {df[column].quantile(0.25)}")
        print(f"⚖️Median: {df[column].median()}")
        print(f"📊Q0.75: {df[column].quantile(0.75)}\n")
        
    for column in numerical:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        print(f"👾{column} outliers count: {len(outliers)}")

    total_missing_values = df.isnull().sum().sum()
    rows_with_missing_values = df[df.isnull().any(axis=1)].shape[0]
    columns_with_missing_values = df.columns[df.isnull().any()].tolist()

    print(f"\n🕵️‍♂️Total missing values in the DataFrame: {total_missing_values}")
    print(f"🕵️‍♂️Number of rows with missing values: {rows_with_missing_values}")
    print(f"🕵️‍♂️Columns with missing values: {columns_with_missing_values}")

    duplicate_rows = df[df.duplicated()]
    num_duplicate_rows = len(duplicate_rows)

    print(f"\n🤌Number of duplicate rows: {num_duplicate_rows}")
    print("\nThat's all. Live long and prosper 🖖")
