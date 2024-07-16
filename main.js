function changeBackgroundColor() {
    var currentColor = document.body.style.backgroundColor;

    if (currentColor === 'cyan') {
        document.body.style.backgroundColor = 'lightgreen';
    } else {
        document.body.style.backgroundColor = 'cyan';
    }
}