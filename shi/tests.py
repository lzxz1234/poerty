# -*- coding:utf-8 -*-
import sqlite3
import os
import json
from zhtools.langconv import Converter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conn = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))


if __name__ == '__main__':
    print conn.execute("SELECT count(1) from ci_ci")
    cursor = conn.cursor()
    convert = Converter('zh-hans')
    for root, _, file_names in os.walk('F:\\json'):
        for file_name in file_names:
            if file_name.startswith('poet'):
                file_contents = json.load(open(os.path.join(root, file_name)))
                for each in file_contents:
                    author = each.get('author')
                    content = each.get('paragraphs')
                    title = each.get('title')

                    author = convert.convert(author)
                    content = convert.convert('\r\n'.join(content))
                    title = convert.convert(title)
                    cursor.execute('INSERT into shi_shi(title, content, author) VALUES (?, ?, ?)', (title, content, author))
                conn.commit()
