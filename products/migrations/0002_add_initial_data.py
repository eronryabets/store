from django.db import migrations, models


def add_initial_data(apps, schema_editor):
    ProductCategory = apps.get_model('products', 'ProductCategory')
    Product = apps.get_model('products', 'Product')

    product_categories_data = [
        {"name": "Одежда", "description": "Описания для одежды"},
        {"name": "Обувь", "description": None},
        {"name": "Подарки", "description": ""},
        {"name": "Аксессуары", "description": ""},
        {"name": "Новинки", "description": ""},
    ]

    for category_data in product_categories_data:
        ProductCategory.objects.create(**category_data)

    products_data = [
        {"name": "Худи черного цвета с монограммами adidas Originals",
         "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни", "price": "6090.00",
         "quantity": 10, "image": "products_images/Adidas-hoodie.png", "category_id": 1},
        {"name": "Синяя куртка The North Face",
         "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
         "price": "237200.00", "quantity": 5, "image": "products_images/Blue-jacket-The-North-Face.png",
         "category_id": 1},
        {"name": "Коричневый спортивный oversized-топ ASOS DESIGN",
         "description": "Материал с плюшевой текстурой. Удобный и мягкий.", "price": "3390.00", "quantity": 13,
         "image": "products_images/Brown-sports-oversized-top-ASOS-DESIGN.png", "category_id": 1},
        {"name": "Черный рюкзак Nike Heritage", "description": "Плотная ткань. Легкий материал.", "price": "2340.00",
         "quantity": 22, "image": "products_images/Black-Nike-Heritage-backpack.png", "category_id": 1},
        {"name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
         "description": "Гладкий кожаный верх. Натуральный материал.", "price": "13590.00", "quantity": 5,
         "image": "products_images/Black-Dr-Martens-shoes.png", "category_id": 2},
        {"name": "Темно-синие широкие строгие брюки ASOS DESIGN",
         "description": "Легкая эластичная ткань сирсакер Фактурная ткань.", "price": "2890.00", "quantity": 13,
         "image": "products_images/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png", "category_id": 1},
    ]

    for product_data in products_data:
        Product.objects.create(**product_data)


class Migration(migrations.Migration):
    dependencies = [
         ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
