let password = document.querySelector("#password");
console.log('helloo');
let show = "visibility";
let unshow = "visibility_off";

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


let PassMin = () => {
    if(password.value != ''){
        if(password.value.length < 8){
            document.querySelector(".min").innerHTML = `Password Must contain at least 8 charcaters`;
        } else {
            document.querySelector(".min").innerHTML = ``;
        }
    } else {
        document.querySelector(".min").innerHTML = ``;
    }
}

const passwordRequirement = document.getElementById('password')

passwordRequirement.addEventListener('keyup', PassMin)
