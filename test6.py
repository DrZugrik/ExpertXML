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

    ## Функция для проверки, является ли тип данных non-empty-string
    def is_non_empty_string_type(type_name):
        simple_type = get_simple_type(type_name)
        if simple_type is not None:
            base_type = simple_type.find('{http://www.w3.org/2001/XMLSchema}restriction').get('base')
            return base_type == 'xs:string' and type_name == 'non-empty-string'
        return False

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
                    # Если нет опций выбора, проверяем, является ли тип данных non-empty-string
                    if is_non_empty_string_type(simple_type_element.get('name')):
                        # Если да, создаем текстовое поле с желтым фоном и добавляем красную звездочку
                        form_elements.append(f'<label for="{element_name}" style="background-color: yellow;">{element_name} - {annotation}<span style="color: red;">*</span></label><input type="text" id="{element_name}" name="{element_name}" value="" placeholder="{annotation}"><br>')
                    else:
                        # В противном случае создаем поле ввода текста
                        form_elements.append(f'<label for="{element_name}">{element_name} - {annotation}</label><input type="text" id="{element_name}" name="{element_name}" value="" placeholder="{annotation}"><br>')
            else:
                form_elements.append(f'<p>Simple type "{element_type}" not found</p>')  # Сообщение об ошибке

# Пример использования
schema_file = 'explanatorynote-01-03.xsd'  # Укажите путь к вашему файлу схемы
output_file = '6.html'  # Укажите имя и путь для сохранения HTML файла
generate_form_from_complex_types(schema_file, output_file)
