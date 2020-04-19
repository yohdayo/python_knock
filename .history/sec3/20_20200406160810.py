import gzip
import json

def read_wiki(fname, title):
    """指定のタイトルの記事本文を表示
    """
    # ファイルを解凍して読み込む
    with gzip.open(fname, 'rt') as data_file: # テキストモード読み込み
        for line in data_file:
            # json to dict
            data_json = json.loads(line)
            # 指定のタイトルの本文を探す
            if data_json['title'] == title:
                return data_json['text']
            
if __name__ == '__main__':
    fname = '../../datas/jawiki-country.json.gz'
    print(read_wiki(fname, 'イギリス'))