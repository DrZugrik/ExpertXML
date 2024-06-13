import xml.etree.ElementTree as ET

def generate_form_from_schema(schema_file, output_file):
    # Парсим XML схему
    tree = ET.parse(schema_file)
    root = tree.getroot()

    # Создаем список для хранения HTML форм
    forms = []

    # Проходим по каждому комплексному типу данных в корне схемы
    for complex_type in root.findall('.//{http://www.w3.org/2001/XMLSchema}complexType'):
        complex_type_name = complex_type.get('name')  # Получаем имя комплексного типа данных

        # Ищем аннотацию для комплексного типа данных
        annotation_element = complex_type.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
        annotation = annotation_element.text if annotation_element is not None else ""

        # Создаем HTML форму для каждого комплексного типа данных с именем и аннотацией
        form = f'<h3>{complex_type_name} - {annotation}</h3>'
        form += '<form>'
        
        # Проходим по каждому элементу внутри комплексного типа данных
        for element in complex_type.findall('.//{http://www.w3.org/2001/XMLSchema}element'):
            element_name = element.get('name')  # Получаем название элемента

            # Ищем аннотацию для элемента
            element_annotation_element = element.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
            element_annotation = element_annotation_element.text if element_annotation_element is not None else ""

            # Добавляем поля для заполнения данных
            form += f'<label for="{element_name}">{element_name} - {element_annotation}</label>'
            form += f'<input type="text" id="{element_name}" name="{element_name}"><br>'

        form += '</form>'

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
output_file = '2.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_schema(schema_file, output_file)
