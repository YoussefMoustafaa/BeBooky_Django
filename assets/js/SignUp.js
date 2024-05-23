let password = document.querySelector("#password"),
username = document.querySelector("#username"),
email = document.querySelector('#email'),
confirmPassword = document.querySelector("#ConfirmPassword"),
show = "visibility",
unshow = "visibility_off";

// Visibility icon of password field
let ToggleVisibility = () => {
    if(password.type === "password") {
        password.type = "text";
        document.querySelector("#visibile").textContent = unshow;
    } else {
        password.type = "password";
        document.querySelector("#visibile").textContent = show;
    }
} 

const visibleIcon = document.getElementById('visibile')

visibleIcon.addEventListener('click', ToggleVisibility)


// Visibility icon of confirm password field
let confirmToggleVisibility = () => {
    if(confirmPassword.type === "password") {
        confirmPassword.type = "text";
        document.querySelector("#visibileConfirm").textContent = unshow;
    } else {
        confirmPassword.type = "password";
        document.querySelector("#visibileConfirm").textContent = show;
    }
}

const visibleConfirm = document.getElementById('visibileConfirm')

visibleConfirm.addEventListener('click', confirmToggleVisibility)


// check if checkbox is checked as admin or user
let isChecked = () =>{
    let Admin = document.querySelector("#isAdmin");
    return(Admin.checked)? true : false;
}

const checkAdmin = document.getElementById('isAdmin')

checkAdmin.addEventListener('click', isChecked)


// var count = 4;

// let AddUser = () => {
//     let username = document.querySelector("#username").value,
//     email = document.getElementById('email').value;
//     let newUser = new User(
//         count++,
//         username,
//         password.value,
//         [],
//         isChecked()
//     );
//     let storedUsers = JSON.parse(localStorage.getItem('users'))
//     if(storedUsers == null){
//         storedUsers = [];
//     }
//     storedUsers.push(newUser)
//     localStorage.setItem('users', JSON.stringify(storedUsers))
// }

let min = document.querySelector(".min");
let PassMin = () => {
    if(password.value != ''){
        if(password.value.length < 8){
            min.innerHTML = `Password Must contain at least 8 charcaters`;
        } else {
            min.innerHTML = ``;
        }
    } else {
        min.innerHTML = ``;
    }
}

const passwordRequirement = document.getElementById('password')

passwordRequirement.addEventListener('keyup', PassMin)




let message = document.querySelector(".message");
let PassCheck = () => {
    if(password.value != '' && confirmPassword.value != ''){
        if(password.value.length >= 8 && confirmPassword.value.length >= 8){
            if(confirmPassword.value === password.value){
                message.innerHTML = `<i class="material-icons" style = "color: green;">check_circle</i> Password Matches`;
                message.style.color = "green";
                return true;
            } else {
                message.innerHTML = `<i class="material-icons" style = "color: red;">error</i> Password not Match`;
                message.style.color = "red";
                return false;
            }
        } else {
            message.innerHTML = `Password Must contain at least 8 charcaters`;
            message.style.color = "black";
            return false;
        }
    } else {
        message.innerHTML = ``;
        return false;
    }
}

confirmPassword.addEventListener('keyup', PassCheck)

let form = document.getElementById('sign-up-form')

form.addEventListener('submit', e => {
    e.preventDefault()

    if(!passwordStrength()){
        alert('Please make sure your password is strong enough.');
        return;
    }

    if (!PassCheck()) {
        alert('Please make sure your passwords match.');
        return;
    }

    const isAdmin = isChecked()

    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: new URLSearchParams({
            'username': username.value,
            'password': password.value,
            'email': email.value,
            'isAdmin': isAdmin
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success'){
            window.location.href = '/'
            alert('Account Created Successfully!')
        }
        else
            alert('Failed to register user', data.error)
    })
    .catch(error => {
        // console.error('Error:', error)
        console.log(error);
    })

})


function getCookie(name) {
    let cookieValue = null
    if (document.cookie !== '') {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieValue
}

let strength = document.getElementById("pass-strength-loader"); 
let passwordStrength = () => {
    let i = 0;
    let x = password.value;
    let strengthWidth = ["1%", "25%", "50%", "75%", "100%"];
    let strengthColor = ["#D73F40", "#DC6551", "#F2B84F", "#BDE952", "#3ba62f"];

    if (x.length > 0) {
        let arrayTest = [/[0-9]/, /[a-z]/, /[A-Z]/, /[^0-9a-zA-Z]/];
        arrayTest.forEach((item) => {
            if (item.test(x)) {
                i += 1;
            }
        });
    }

    strength.style.width = strengthWidth[i];
    strength.style.backgroundColor = strengthColor[i];

    if(strength.style.width === "100%") {
        return true;
    }
    else {
        return false;
    }
};
password.addEventListener('input', passwordStrength);
