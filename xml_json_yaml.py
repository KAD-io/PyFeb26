import json
import xml.etree.ElementTree as ET
import yaml


PRODUCTS = {
    'name': ['27" Monitor'
             'Mechanical Keyboard',
             'Wireless Mouse',
             'Gaming Mouse Pad L',
             '1080p Webcam',
             'Gaming Headset',
             '4-Port USB Hub',
             'External HDD 1TB',
             'Power Strip',
             'Laptop Stand'],
    'price': [275, 80, 40, 15, 55, 70, 18, 65, 12, 28],
    'quantity': [5, 12, 20, 15, 8, 10, 25, 7, 18, 6]
}


FOOTBALL_CLUBS = [
    {"name": "Al Ahly", "country": "Egypt", "trophies": 155},
    {"name": "Celtic", "country": "Scotland", "trophies": 120},
    {"name": "Rangers", "country": "Scotland", "trophies": 118},
    {"name": "Nacional", "country": "Uruguay", "trophies": 117},
    {"name": "Peñarol", "country": "Uruguay", "trophies": 116},
    {"name": "Real Madrid", "country": "Spain", "trophies": 102},
    {"name": "Barcelona", "country": "Spain", "trophies": 100},
    {"name": "Benfica", "country": "Portugal", "trophies": 86},
    {"name": "Porto", "country": "Portugal", "trophies": 86},
    {"name": "Bayern Munich", "country": "Germany", "trophies": 84}
]


BOOKS = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Master and Margarita", "author": "Mikhail Bulgakov", "year": 1967},
    {"title": "Flowers for Algernon", "author": "Daniel Keyes", "year": 1966},
    {"title": "The Martian", "author": "Andy Weir", "year": 2011},
    {"title": "Sapiens: Brief History of Humankind", "author": "Yuval Noah Harari", "year": 2011},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]


def create_xml(xml_file, products):
    """hm15_job1"""
    root = ET.Element("products")

    for name, price, quantity in zip(products['name'], products['price'], products['quantity']):
        item = ET.SubElement(root, "item")
        ET.SubElement(item, "name").text = name
        ET.SubElement(item, "price").text = str(price)
        ET.SubElement(item, "quantity").text = str(quantity)

    ET.indent(root)
    tree = ET.ElementTree(root)
    tree.write("hm15_job1.xml", encoding="utf-8", xml_declaration=True)
    tree.write(xml_file)


def parse_xml(xml_file):
    return (sum(int(item.find('price').text) * int(item.find('quantity').text)
                for item in ET.parse(xml_file).getroot().findall("item")))


def create_json(json_file, clubs_data):
    """hm15_job2"""
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(clubs_data, f, indent=4)


def parse_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        clubs_data = json.load(f)

    return max(clubs_data, key=lambda club: club["trophies"])


def save_yaml(yaml_file, books_data):
    """hm15_job3"""
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(books_data, f, sort_keys=False)


def load_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def add_book(books_data):
    print("\nAdding a new book:")
    new_book = {
        "title": input("Enter name: "),
        "author": input("Enter author: "),
        "year": int(input("Enter year of release: "))
    }
    print(f'new book: {new_book}')
    books_data.append(new_book)
    return books_data


if __name__ == "__main__":

    create_xml("hm15_job1.xml", PRODUCTS)
    print(f'total cost: {parse_xml("hm15_job1.xml")}')

    create_json("hm15_job2.json", FOOTBALL_CLUBS)
    print(parse_json("hm15_job2.json"))

    save_yaml("hm15_job3.yaml", BOOKS)
    books = load_yaml("hm15_job3.yaml")
    save_yaml("hm15_job3.yaml", add_book(books))
