import requests
import pandas as pd
import os.path
import json


def youdao_api_url(words):
    """
    get api_url
    """
    key = '186038048'  #有道接口
    keyfrom = '1personal1'  #有道接口id
    doctype = 'json'  #从有道返回json格式的文本

    url = 'http://fanyi.youdao.com/openapi.do?' \
          'keyfrom={}&key={}&type=data&doctype={}&version=1.1&q={}'\
        .format(keyfrom, key, doctype, words)
    return url


def judge_word(word, file='words.csv'):
    """
    判断查询的单词是否在file中，若在，次数+1，否，写入file
    """
    if os.path.getsize(file):
        df_word = pd.DataFrame.from_csv(file, encoding='utf8')
        #pandas的index属性是不可变对象

        if word in df_word['Query'].values:
            #values属性返回np.array数组
            df_word.loc[df_word['Query'] == word, ['Frequency']] += 1
        else:
            df_word.loc[len(df_word.index)] = [word, 1]
    else:
        df_word = pd.DataFrame(columns=['Query', 'Frequency'])
        df_word.loc[0] = [word, 1]
    df_word.to_csv(file, encoding='utf8')


def main(words):
    try:
        api_url = youdao_api_url(words)
        try:
            response = requests.get(api_url)
            result = response.json()['basic']['explains']

            print(u'-------本地释义-----')

            for basic in result:
                print(basic)
            web_trans = response.json()['web'][0]['value']
            print('')
            print(u'-------网络释义-----')

            for value in web_trans:
                print(value)
            judge_word(words)
        except KeyError as e:
            print(u'{} ===>没有找到翻译'.format(words), e)
    except json.decoder.JSONDecodeError as Jerror:
        #导入json用于判定输入返回json返回异常
        print(Jerror, '输入无效')
    return True

while True:
    question = input('输入查询的单词or输入quit退出查询:')
    if question == 'quit':
        break
    main(question)
