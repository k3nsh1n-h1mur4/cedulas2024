const form = document.getElementById('loginForm')
function ValidateForm() {
    form.addEventListener(onSubmit, (e) => {
    e.preventDefault()
    username = form.username.vaue;
    password = form.password.value;
    if (username === '' || password=== ''){
        alert('Campo vacío');
    }
})}