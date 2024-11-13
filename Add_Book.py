# -*- coding: utf-8 -*-

import argparse
import codecs
import json
import sqlite3

# Load JSON
def load_Json(json_file_dir):
    with codecs.open(json_file_dir, 'r', encoding='utf-8') as chapters_file:
        content_json = json.load(chapters_file)
    return content_json

# Add the new book
def load_into_database(json_file, qr_code):
    content = load_Json(json_file)
    
    # JSON to string
    json_string = json.dumps(content)
    
    conn = sqlite3.connect('chapters.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO chapters (QR_code, Json_File)
        VALUES (?, ?)
    ''', (qr_code, json_string))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Please insert the QR code and the Json File of the book")
    parser.add_argument('user_Json_File', type=str, help='Json file with the book info')
    parser.add_argument('user_QR_code', type=str, help='QR code of the book that it is going to be added to the NAO')

    args = parser.parse_args()
    
    load_into_database(args.user_Json_File, args.user_QR_code)
    print("The book with the QR code: '{}' succesfully added to database".format(args.user_QR_code))
