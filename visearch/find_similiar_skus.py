import pandas as pd

from visearch import client

access_key = 'your app access key'
secret_key = 'your app secret key'

api = client.ViSearchAPI(access_key, secret_key)


def find_silimiar_skus(path, sheet_name, out_path):
    SKUs_df = pd.read_excel(path, sheetname=sheet_name)
    normalized_skus = SKUs_df['SKU'].apply(lambda x: x + '-' + x[-2:].lower())

    with open(out_path, 'w') as out_file:
        for sku in normalized_skus:
            response = api.search(sku, limit=9)
            if not response['error']:
                out_file.write(sku[:-3] + ',' + ','.join(map(lambda x: x['im_name'][:-3],response['result'])) + "\n")
            else:
                out_file.write(sku[:-3] + ',' + response['error'] + "\n")

if __name__ == '__main__':
    find_silimiar_skus('/home/hoangphan/Downloads/SKU_Sample.xlsx', 'Sheet1', '/home/hoangphan/similiar_sku.csv')