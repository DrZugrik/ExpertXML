import xml.etree.ElementTree as ET

def generate_form_from_schema(schema_file, output_file):
    # Парсим XML схему
    tree = ET.parse(schema_file)
    root = tree.getroot()

    # Создаем список для хранения HTML форм
    forms = []

    # Проходим по каждому элементу в корне схемы
    for element in root.findall('.//{http://www.w3.org/2001/XMLSchema}element'):
        element_name = element.get('name')  # Получаем название элемента
        annotation_element = element.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
        annotation = annotation_element.text if annotation_element is not None else ""

        # Создаем HTML форму для каждого элемента с именем и аннотацией
        form = f'<form><label for="{element_name}">{element_name} - {annotation}</label><input type="text" id="{element_name}" name="{element_name}"></form>'

        # Добавляем форму в список
        forms.append(form)

    # Объединяем все формы в одну строку
    all_forms = '\n'.join(forms)

    # Создаем минимальный HTML файл с созданными формами
    html_content = f'<!DOCTYPE html><html><head><title>Generated Forms</title></head><body>{all_forms}</body></html>'

    # Сохраняем HTML файл
    with open(output_file, 'w') as f:
        f.write(html_content)

# Пример использования
schema_file = 'explanatorynote-01-03.xsd'  # Укажите путь к вашему файлу схемы
output_file = '1.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_schema(schema_file, output_file)
