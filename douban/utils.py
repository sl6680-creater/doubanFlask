# -*- coding: utf-8 -*-


# 创建停用词list
def stopwords_list(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


if __name__ == '__main__':
    stopwords_list = stopwords_list('./data/stopwords.txt')
    print(stopwords_list)

