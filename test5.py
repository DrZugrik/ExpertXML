import xml.etree.ElementTree as ET

def generate_form_from_complex_types(schema_file, output_file):
    # Парсим XML схему
    tree = ET.parse(schema_file)
    root = tree.getroot()

    # Создаем список для хранения HTML форм
    forms = []

    # Функция для обработки элементов схемы
    def process_element(element, form_elements):
        for child in element:
            if child.tag.endswith('complexType'):
                process_complex_type(child, form_elements)
            elif child.tag.endswith('element'):
                process_root_element(child, form_elements)

    # Функция для обработки комплексных типов данных
    def process_complex_type(complex_type, form_elements):
        # Получаем аннотацию комплексного типа, если она есть
        annotation_element = complex_type.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
        annotation = annotation_element.text if annotation_element is not None else "No annotation available"
        # Добавляем заголовок с аннотацией в HTML форму
        form_elements.append(f'<h2>{annotation}</h2>')

        # Обработка дочерних элементов
        for child in complex_type.findall('{http://www.w3.org/2001/XMLSchema}sequence/{http://www.w3.org/2001/XMLSchema}element'):
            element_name = child.get('name')
            element_type = child.get('type')
            annotation_element = child.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
            annotation = annotation_element.text if annotation_element is not None else ""

            # Проверяем, существует ли простой тип данных с таким именем
            simple_type_element = get_simple_type(element_type)
            if simple_type_element is not None:
                # Получаем список возможных вариантов ответов на выбор
                options = [(enumeration.get('value'), enumeration.findtext('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')) for enumeration in simple_type_element.findall('.//{http://www.w3.org/2001/XMLSchema}enumeration')]
                if options:
                    # Если есть опции выбора, создаем выпадающий список с аннотациями
                    options_html = ''.join([f'<option value="{value}">{value} - {annotation}</option>' for value, annotation in options])
                    form_elements.append(f'<label for="{element_name}">{element_name} - {annotation}</label><select id="{element_name}" name="{element_name}">{options_html}</select><br>')
                else:
                    # Если нет опций выбора, создаем поле ввода текста
                    form_elements.append(f'<label for="{element_name}">{element_name} - {annotation}</label><input type="text" id="{element_name}" name="{element_name}" value="" placeholder="{annotation}"><br>')
            else:
                # Если простой тип данных не найден, создаем поле ввода текста
                form_elements.append(f'<label for="{element_name}">{element_name} - {annotation}</label><input type="text" id="{element_name}" name="{element_name}" value="" placeholder="{annotation}"><br>')

    # Функция для обработки корневого элемента
    def process_root_element(root_element, form_elements):
        annotation_element = root_element.find('{http://www.w3.org/2001/XMLSchema}annotation/{http://www.w3.org/2001/XMLSchema}documentation')
        if annotation_element is not None:
            annotation_text = annotation_element.text
            form_elements.append(f'<h2>{annotation_text}</h2>')
        element_type = root_element.find('{http://www.w3.org/2001/XMLSchema}complexType')
        if element_type is not None:
            process_complex_type(element_type, form_elements)

    # Функция для получения простого типа по его имени
    def get_simple_type(type_name):
        return root.find(f'.//{{http://www.w3.org/2001/XMLSchema}}simpleType[@name="{type_name}"]')

    # Проходим по каждому элементу в корне схемы
    process_element(root, forms)

    # Объединяем все формы в одну строку
    all_forms = '\n'.join(forms)

    # Создаем минимальный HTML файл с созданными формами
    html_content = f'<!DOCTYPE html><html><head><title>Generated Forms</title><style>h2 {{font-weight: bold;}}</style></head><body>{all_forms}</body></html>'

    # Сохраняем HTML файл
    with open(output_file, 'w') as f:
        f.write(html_content)

# Пример использования
schema_file = 'explanatorynote-01-03.xsd'  # Укажите путь к вашему файлу схемы
output_file = '5.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_complex_types(schema_file, output_file)
