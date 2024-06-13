import xml.etree.ElementTree as ET

def generate_form_from_simple_types(schema_file, output_file):
    # Парсим XML схему
    tree = ET.parse(schema_file)
    root = tree.getroot()

    # Создаем список для хранения HTML форм
    forms = []

    # Проходим по каждому элементу в корне схемы
    for simple_type in root.findall('.//{http://www.w3.org/2001/XMLSchema}simpleType'):
        type_name = simple_type.get('name')  # Получаем название типа
        annotation_element = simple_type.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
        annotation = annotation_element.text if annotation_element is not None else ""
        options = [enumeration.get('value') for enumeration in simple_type.findall('.//{http://www.w3.org/2001/XMLSchema}enumeration')]

        # Создаем HTML форму для каждого простого типа данных
        options_html = ''.join([f'<option value="{option}">{option}</option>' for option in options])
        form = f'<form><label for="{type_name}">{type_name} - {annotation}</label><select id="{type_name}" name="{type_name}">{options_html}</select></form>'

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
output_file = '3.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_simple_types(schema_file, output_file)
