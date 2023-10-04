function loadSobre() {
    var iframeContainer = document.getElementById('iframeContainer');
    var iframe = document.getElementById('sobreFrame');
    
    if (iframeContainer.style.display === 'none' || iframeContainer.style.display === '') {
      iframeContainer.style.display = 'block';
      document.body.style.overflow = 'hidden'; // Disable scrolling when iframe is shown
      iframe.src = 'sobre.html'; // Substitua 'sobre.html' pelo caminho real do seu arquivo sobre.
    } else {
      iframeContainer.style.display = 'none';
      document.body.style.overflow = 'auto'; // Enable scrolling when iframe is hidden
      iframe.src = 'sobre.html';
    }
}