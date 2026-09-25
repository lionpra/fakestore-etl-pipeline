from etl.extract import extract_product, extract_user
from etl.transform import transform_product, transform_user
from etl.load import load_to_postgres

def run_pipline(): 

    print('Start')

    product_df = extract_product()
    user_df = extract_user()

    print('Extracted data from API')

    product_df = transform_product(product_df)
    user_df = transform_user(user_df)

    print('Transformed data')

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    print('Loaded data to postgres')


if __name__ == '__main__':
    run_pipline()

    