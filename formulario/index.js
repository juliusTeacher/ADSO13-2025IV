const formulario = document.getElementById('formRegistro');
const usuario = document.getElementById('txtUsuario');
const email = document.getElementById('txtCorreo');
const pass = document.getElementById('txtPassword');
const pass2 = document.getElementById('txtPassword2');

formulario.addEventListener('submit', e=>{
    e.preventDefault();
    validarInputs();
});

const setError = (element, message)=>{
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
}

const setSuccess = element =>{
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
}

const isValidEmail = email =>{
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

/* Método para validar los INPUTS */
const validarInputs = () =>{
    
    const usuarioValue = usuario.value.trim();
    const emailValue = email.value.trim();
    const passValue = pass.value.trim();
    const pass2Value = pass2.value.trim();

    if(usuarioValue === ''){
        setError(usuario, 'El usuario es obligatorio');
    }
    else{
        setSuccess(usuario);
    }

    if(emailValue === ''){
        setError(email, 'El correo electrónico es obligatorio');
    }
    else{
        setSuccess(email);
    }
    
    if(passValue === ''){
        setError(pass, 'La contraseña es obligatoria');
    }
    else if(passValue.length < 8){
        setError(pass, 'La contraseña debe ser mínimo de 8 caracteres');
    }
    else{
        setSuccess(pass);
    }

    if(pass2Value === ''){
        setError(pass2,'Por favor, confirme la contraseña');
    }
    else if(pass2Value != passValue){
        setError(pass2,'No coinciden las contraseñas');
    }
    else{
        setSuccess(pass2);
    }
}