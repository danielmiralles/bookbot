from collections import Counter
from curses.ascii import isalpha


def get_num_words(content):
    return len(content.split())

def get_dict_characters(content):
    return dict(Counter(content.lower()))

def get_sorted_dict_characters(content_dict):
    dict_list = []
    for key, value in content_dict.items():
        if isalpha(key):
            dict_list.append({"char": key, "num": value})
        dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list

