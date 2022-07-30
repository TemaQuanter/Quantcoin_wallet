import sys
import glob
import json
from nft_processor import get_nft_hash_from_binary_file


def nft_minter(file_name):
    nft_token = get_nft_hash_from_binary_file(file_name)

    print(str('-' * (len(nft_token) + 2)))
    print('-' + nft_token + '-')
    print(str('-' * (len(nft_token) + 2)))

    number_of_blocks = len(glob.glob('Blockchain/[0-9]*.json'))

    for index in range(number_of_blocks - 1, -1, -1):
        with open(f'Blockchain/{index}.json') as file:
            buf = json.load(file)
            for i in range(len(buf['transactions'])):
                buf['transactions'][i] = buf['transactions'][i].strip()
                split_transaction = buf['transactions'][i].split(';')
                if split_transaction[2] == nft_token:
                    print('This particular NFT is already owned by this account:')
                    print(split_transaction[1])
                    return ''

    print('This NFT is not owned by anyone yet.')
    print('Be the first!')
    return nft_token