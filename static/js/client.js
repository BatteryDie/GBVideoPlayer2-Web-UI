window.onload = function() {
    document.getElementById('downloadButton').classList.add('disabled');
};
var fileNameWithoutExtension;
document.addEventListener('DOMContentLoaded', function() {
     document.getElementById('uploadButton').addEventListener('click', function() {
        // Find and remove extension from filename
        var fileInput = document.getElementById('uploadFile');
        var file = fileInput.files[0];
        var uploadedFilename = file.name;
        fileNameWithoutExtension = uploadedFilename.replace(/\.[^/.]+$/, "");

        // Get the value of the optionQuality input field
        var optionQuality = document.getElementById('optionQuality').value;
        var formData = new FormData();
        formData.append('file', file);
        formData.append('optionQuality', optionQuality); // Append optionQuality to FormData

        document.getElementById('uploadButton').disabled = true;
        showLoadingSpinner();
        document.body.style.cursor = 'wait';

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload');
        xhr.responseType = 'text';
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Handle successful upload
                var logTextarea = document.getElementById('webLog');
                logTextarea.value += xhr.responseText; // Append response to webLog
                document.getElementById('downloadButton').classList.remove('disabled');
                document.getElementById('uploadButton').disabled = false;
                document.body.style.cursor = 'auto';

                // Add gbc extension on filename
                var compiledFileNameInput = document.getElementById('compiledfileName');
                compiledFileNameInput.value = fileNameWithoutExtension + '.gbc';
                hideLoadingSpinner();
            } else {
                // Handle upload error
                alert('Upload failed. Please try again.');
                document.getElementById('uploadButton').disabled = false;
                document.body.style.cursor = 'auto';
                hideLoadingSpinner();
            }
        };
        xhr.send(formData);
    });
});
function downloadFile() {
    var downloadUrl = '/cache/' + fileNameWithoutExtension + '.gbc';
    window.location.href = downloadUrl;
}
function showLoadingSpinner() {
    document.getElementById('overlay').style.display = 'flex';
}
function hideLoadingSpinner() {
    document.getElementById('overlay').style.display = 'none';
}