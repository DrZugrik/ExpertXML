document.addEventListener("DOMContentLoaded", function() {
    Dropzone.autoDiscover = false; // Отключаем автоматическое обнаружение

    // Инициализируем Dropzone
    let dropArea = document.getElementById("drop-area");

    if (dropArea) {
        // Устанавливаем Dropzone для элемента с id="drop-area"
        let myDropzone = new Dropzone("#drop-area", {
            url: "/upload/", // URL для загрузки файлов
            paramName: "file", // Имя параметра, используемое для отправки файлов
            maxFilesize: 2, // Максимальный размер файла в MB
            acceptedFiles: ".pdf", // Разрешенные типы файлов
            init: function() {
                this.on("success", function(file, response) {
                    // Обработка успешной загрузки
                    fetch('/get_schemas/')
                        .then(response => response.json())
                        .then(data => {
                            displayFiles([file], data.schemas);
                        })
                        .catch(error => console.error('Ошибка при получении списка схем:', error));
                });

                this.on("error", function(file, errorMessage) {
                    console.error('Ошибка при загрузке файлов:', errorMessage);
                });
            }
        });

        // Подключение обработчика для изменения файлов через input
        let fileUploader = document.getElementById("fileUploader");
        fileUploader.addEventListener("change", function(e) {
            let files = e.target.files;
            for (let i = 0; i < files.length; i++) {
                myDropzone.addFile(files[i]); // Добавляем файлы в Dropzone
            }
        });
    } else {
        console.error("Element with ID 'drop-area' not found.");
    }
});

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

    document.getElementById("fileTable").style.display = "table";
    updateRowNumbers();
}

function detectSchema(file, schemas) {
    var selectHtml = '<select class="form-select">';
    schemas.forEach(function(schema) {
        selectHtml += `<option value="${schema[0]}">${schema[1]}</option>`;
    });
    selectHtml += '</select>';
    return selectHtml;
}

function removeFile(button) {
    let row = button.parentElement.parentElement;
    row.remove();
    updateRowNumbers();
}

function updateRowNumbers() {
    let tableBody = document.getElementById("fileTableBody");
    for (let i = 0; i < tableBody.children.length; i++) {
        tableBody.children[i].getElementsByTagName('td')[0].innerText = i + 1;
    }
}

function calculateCRC(file) {
    return "12345678";
}
