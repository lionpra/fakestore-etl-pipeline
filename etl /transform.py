import pandas as pd 

def transform_product(product_df):
    df = product_df.copy()

    df = df.rename(colums = {
        'id' : 'product_id',
        'title' : 'product_name',
        'price' : 'prouct_price',
        'category' : 'product_category',
        'description' : 'product_description'
    })

    df = df [['product_id', 'product_name', 'prouct_price', 'product_category', 'product_description'
    ]]

    df['product_price'] = df['product_price'].astype(float)

    return df


def transform_user(user_df):

    df = user_df.copy()

    df['firstname'] = df['name'].apply(lambda x: x['firstname'])
    df['lastname'] = df['name'].apply(lambda x: x['lastname'])

    df['city'] = df['address'].apply(lambda x: x['city'])
    df['street'] = df['address'].apply(lambda x: x['street'])
    df['number'] = df['address'].apply(lambda x: x['number'])
    df['zipcode'] = df['address'].apply(lambda x: x['zipcode'])



    df = df.rename(colums = {
        'id' : 'user_id',
        'username' : 'username',
        'email' : 'user_email'
    })

    df = df[['user_id', 'username', 'user_email', 'first_name', 'last_name', 'city', 'street', 'zipcode']]

    return df 


