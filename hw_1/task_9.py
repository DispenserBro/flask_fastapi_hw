import random
from flask import Flask, render_template
from faker import Faker
from copy import deepcopy


app = Flask(__name__)
fake = Faker('ru-RU')


def get_items() -> list[dict]:
    """Example function to get items list for the website"""
    items_list = []
    cat_list = ['outerwear', 'pants', 'shoes']
    item_names_cat = ['Верхняя одежда', 'Штаны', 'Обувь']

    for _ in range(40):
        category = random.choice(cat_list)
        item = {
            'id': fake.unique.random_int(min=1, max=1_000_000),
            'category': category,
            'name': f'{item_names_cat[cat_list.index(category)]} {fake.ssn()}',
            'description': fake.paragraph(),
        }
        # print(item)
        items_list.append(item)
    return items_list


# In the production project this line won't be needed
# due to the fact that the upper function will be replaced by the real function
ITEMS = get_items()


@app.route('/')
def index():
    items_list = deepcopy(ITEMS)
    return render_template('index.html', context=items_list)


@app.route('/<string:category>')
def category_list(category: str):
    items_list = list(filter(lambda x: x['category'] == category, ITEMS))
    return render_template('category.html', context=items_list)


@app.route('/<string:category>/<int:id>')
def item(category: str, id: int):
    item = list(
        filter(lambda x: x['category'] == category and x['id'] == id, ITEMS)
    )[0]
    return render_template('item.html', **item)


if __name__ == '__main__':
    app.run(debug=True)
