function validateInput() {
  const imageInput = document.getElementById('soilImage').files.length;
  const videoInput = document.getElementById('soilVideo').files.length;
  const errorMessage = document.getElementById('errorMessage');

  if (imageInput > 0 && videoInput > 0) {
      errorMessage.classList.remove('hidden');
      return false; // Prevent form submission
  } else {
      errorMessage.classList.add('hidden');
      return true;
  }
}

// Optional: You can add tabs or other toggles if needed for image/video selection
function toggleInputType(type) {
  const imageInput = document.getElementById('imageInput');
  const videoInput = document.getElementById('videoInput');

  if (type === 'image') {
      imageInput.style.display = 'block';
      videoInput.style.display = 'none';
  } else {
      imageInput.style.display = 'none';
      videoInput.style.display = 'block';
  }
}
