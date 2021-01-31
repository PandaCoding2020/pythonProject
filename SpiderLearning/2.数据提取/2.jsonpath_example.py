"""
@Time : 2021/1/30 13:42 
@Author : Steven Chen
@File : 2.jsonpath_example.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import jsonpath
import json

book_list = '''{
    "store": {
        "book": [
            { "category": "reference",
              "author": "Nigel Rees",
              "title": "Sayings of the Century",
              "price": 8.95
              },
            { "category": "fiction",
              "author": "Evelyn Waugh",
              "title": "Sword of Honour",
              "price": 12.99
              },
            { "category": "fiction",
              "author": "Herman Melville",
              "title": "Moby Dick",
              "isbn": "0-553-21311-3",
              "price": 8.99
              },
            { "category": "fiction",
              "author": "J. R. R. Tolkien",
              "title": "The Lord of the Rings",
              "isbn": "0-395-19395-8",
              "price": 22.99
              }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}'''
data = json.loads(book_list)
print(jsonpath.jsonpath(data, '$..title'))
print(jsonpath.jsonpath(data, '$..price'))




