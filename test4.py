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
            elif child.tag.endswith('simpleType'):
                process_simple_type(child, form_elements)

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
            if element_type.startswith('t'):
                form_elements.append(f'<label for="{element_name}">{element_name} - {annotation} :</label><input type="text" id="{element_name}" name="{element_name}" value="" placeholder="{annotation}"><br>')
            else:
                # Handle if complex type not found
                complex_type_element = get_complex_type(element_type)
                if complex_type_element is not None:
                    process_complex_type(complex_type_element, form_elements)
                else:
                    form_elements.append(f'<p>Complex type "{element_type}" not found</p>')  # Error message

    # Функция для обработки простых типов данных
    def process_simple_type(simple_type, form_elements):
        pass

    # Функция для получения комплексного типа по его имени
    def get_complex_type(type_name):
        return root.find(f'.//{{http://www.w3.org/2001/XMLSchema}}complexType[@name="{type_name}"]')

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
output_file = '4.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_complex_types(schema_file, output_file)