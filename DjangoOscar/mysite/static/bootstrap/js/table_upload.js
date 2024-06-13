// Функция для отображения выбранных файлов в таблице
function displayFiles(files, schemas) {
    let tableBody = document.getElementById("fileTableBody");
    let existingRowCount = tableBody.children.length;

    files.forEach((file, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `
            <td>${existingRowCount + index + 1}</td>
            <td>${file.name}</td>
            <td>${calculateCRC(file)}</td>
            <td>${detectSchema(file, schemas)}</td>
            <td><button class="btn btn-danger btn-sm" onclick="removeFile(this)">Удалить</button></td>
        `;
        tableBody.appendChild(row);
    });

    // Отображаем таблицу
    document.getElementById("fileTable").style.display = "table";
    updateRowNumbers(); // Обновляем номера строк после добавления новых строк
}

// Функция для определения схемы файла
function detectSchema(file, schemas) {
    // Создаем строку HTML для <select> с вариантами схем
    var selectHtml = '<select class="form-select">';
    schemas.forEach(function(schema) {
        selectHtml += `<option value="${schema[0]}">${schema[1]}</option>`;
    });
    selectHtml += '</select>';

    // Возвращаем строку HTML, чтобы она могла быть вставлена в ячейку таблицы
    return selectHtml;
}

function removeFile(button) {
    let row = button.parentElement.parentElement;
    row.remove();
    updateRowNumbers(); // Обновляем номера строк после удаления строки
}

function updateRowNumbers() {
    let tableBody = document.getElementById("fileTableBody");
    for (let i = 0; i < tableBody.children.length; i++) {
        tableBody.children[i].getElementsByTagName('td')[0].innerText = i + 1;
    }
}

// Функция для расчета CRC файла (простой пример)
function calculateCRC(file) {
    // Здесь может быть ваша реализация расчета CRC
    return "12345678"; // Временный заглушка
}

// Обработчик события выбора файлов
function handleFiles(files) {
    // Получаем список XML схем из Django
    fetch('/get_schemas/') // Ваш URL для получения списка схем
    .then(response => response.json())
    .then(data => {
        // Отображаем выбранные файлы и список схем в таблице
        displayFiles(files, data.schemas); 
    })
    .catch(error => console.error('Ошибка при получении списка схем:', error));
}

document.addEventListener("DOMContentLoaded", function() {
    // Код, который нужно выполнить после загрузки DOM
    let dropArea = document.getElementById("drop-area");
    if (dropArea) {
        // Подписываемся на события для dropArea только если он существует
        ["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
            dropArea.addEventListener(eventName, preventDefaults, false);
        });
    }
});

// Функция для предотвращения стандартных событий
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Ваш остальной код здесь
// Например:
function handleDragEnter(event) {
    // Обработка события drag enter
}

// Получаем область перетаскивания файлов
let dropArea = document.getElementById("drop-area");

// Предотвращаем стандартные события
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Подсвечиваем область при наведении
["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Убираем подсветку области при выходе за ее пределы или завершении перетаскивания
["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Обрабатываем событие перетаскивания файлов
dropArea.addEventListener("drop", handleDrop, false);

// Предотвращаем стандартное поведение браузера
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Подсветка области при наведении
function highlight(e) {
    dropArea.classList.add("highlight");
}

// Убираем подсветку области
function unhighlight(e) {
    dropArea.classList.remove("highlight");
}

// Обработка события перетаскивания файлов
function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;
    handleFiles(files);
}

// Назначаем событие click на область, чтобы открыть стандартный диалог выбора файлов
dropArea.addEventListener("click", () => {
    fileElem.click();
});

// Назначаем обработчик события изменения файлов на input[type=file]
let fileElem = document.getElementById("fileElem");
fileElem.addEventListener("change", function (e) {
    handleFiles(this.files);
});
