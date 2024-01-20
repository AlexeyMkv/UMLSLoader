import psycopg2
from datetime import datetime
import json
from CUILoader import AtomCUILoader

with open('../UMLSLoader/json_data.json') as f:
    atom_data = json.load(f)
conn = psycopg2.connect(host="localhost", database="database", user="name", password="password")
cursor = conn.cursor()

for data in atom_data:
    cursor.execute(
        'INSERT INTO atoms (page_size, page_number, ui, name, date_added, semantic_types_name, '
        'semantic_types_uri,atoms, atom_count, cv_member_count, attribute_count, relation_count)'
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (
            data["pageSize"],
            data["pageNumber"],
            data["result"]["ui"],
            data["result"]["name"],
            data["result"]["dateAdded"],
            data["result"]["semanticTypes"][0]["name"],
            data["result"]["semanticTypes"][0]["uri"],
            data["result"]["atoms"],
            data["result"]["atomCount"],
            data["result"]["cvMemberCount"],
            data["result"]["attributeCount"],
            data["result"]["relationCount"]
        )
    )
    conn.commit()

cursor.close()
conn.close()
