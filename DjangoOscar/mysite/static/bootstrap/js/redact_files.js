document.addEventListener("DOMContentLoaded", function() {
    // Получаем XML-фрагмент
    const xmlString = `
    <xs:element name="ExplanatoryNote">
        <xs:annotation>
            <xs:documentation xml:lang="ru">Корневой элемент - пояснительная записка</xs:documentation>
        </xs:annotation>
        <xs:element name="Field1">
            <xs:annotation>
                <xs:documentation xml:lang="ru">Описание поля 1</xs:documentation>
            </xs:annotation>
        </xs:element>
        <xs:element name="Field2">
            <xs:annotation>
                <xs:documentation xml:lang="ru">Описание поля 2</xs:documentation>
            </xs:annotation>
        </xs:element>
    </xs:element>
    `;

    // Создаем парсер XML
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlString, "text/xml");

    // Получаем элемент ExplanatoryNote из XML
    const explanatoryNoteElement = xmlDoc.getElementsByTagName("ExplanatoryNote")[0];

    // Создаем форму на основе XML-шаблона
    const formContainer = document.getElementById("form-container");
    const form = document.createElement("form");

    // Обходим дочерние элементы ExplanatoryNote
    for (const childElement of explanatoryNoteElement.children) {
        if (childElement.tagName === "xs:element") {
            // Получаем атрибуты элемента
            const elementName = childElement.getAttribute("name");
            const annotationElement = childElement.getElementsByTagName("xs:annotation")[0];
            const label = annotationElement.getElementsByTagName("xs:documentation")[0].textContent;

            // Создаем соответствующее поле формы
            const inputElement = document.createElement("input");
            inputElement.setAttribute("type", "text");
            inputElement.setAttribute("name", elementName);
            inputElement.setAttribute("placeholder", label);

            // Добавляем поле формы в контейнер
            const divWrapper = document.createElement("div");
            divWrapper.appendChild(inputElement);
            form.appendChild(divWrapper);
        }
    }

    // Добавляем форму на страницу
    formContainer.appendChild(form);
});
