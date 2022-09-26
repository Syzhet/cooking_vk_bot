import os

from dotenv import load_dotenv

load_dotenv()

NGINX_ID = os.getenv('NGINX_ID')

DICT_FOR_INSERT_IN_DB = {
    'categories': {
        'category_muffin': {
            'name': 'Сдоба',
            'description': 'Выпечка из сдобного теста',
            'photo_id': '131647903_457239953_2d1b5cc6595a732f06'
        },
        'category_bread': {
            'name': 'Хлеб',
            'description': 'Хлебные изделия',
            'photo_id': '131647903_457239954_a6760dce59b6689e3e'
        },
        'category_cake': {
            'name': 'Пирожные',
            'description': 'Сладкие кондитерские изделия',
            'photo_id': '131647903_457239955_5d061f055d42cb0475'
        }
    },
    'products': {
        'loaf': {
            'name': 'Батон',
            'description': 'Свежий белый хлеб',
            'photo_id': '131647903_457239962_8e54b21c4e936b73e7',
            'photo_url': f'http://{NGINX_ID}/baton',
            'category_id': 2
        },
        'bread with cereals': {
            'name': 'Хлеб со злаками',
            'description': 'Вкусный хлеб с полезными злаками',
            'photo_id': '131647903_457239960_6afa8c220fbf73b24b',
            'photo_url': f'http://{NGINX_ID}/zlaki.jpg',
            'category_id': 2
        },
        'bun': {
            'name': 'Булочка',
            'description': 'Вкусная, ароматная булочка',
            'photo_id': '131647903_457239959_31ebbe4a02d9c8b7bf',
            'photo_url': f'http://{NGINX_ID}/bulochka.jpeg',
            'category_id': 1
        },
        'muffin': {
            'name': 'Маффин',
            'description': 'Маффин с шоколадной начинкой',
            'photo_id': '131647903_457239963_ed43d2dac327e67261',
            'photo_url': f'http://{NGINX_ID}/muffin',
            'category_id': 1
        },
        'basket': {
            'name': 'Корзиночка',
            'description': 'Для любителей сладкого',
            'photo_id': '131647903_457239961_3c121952f996874307',
            'photo_url': f'http://{NGINX_ID}/basket',
            'category_id': 3
        },
        'cheesecake': {
            'name': 'Чизкейк',
            'description': 'Нежнейший, творожный чизкейк',
            'photo_id': '131647903_457239958_804b86f78a58c164b5',
            'photo_url': f'http://{NGINX_ID}/cheescake.jpeg',
            'category_id': 3
        }
    }
}
