let email = document.getElementById('id_email')
let linkBtn = document.getElementById('link_btn')
let firstEmail = email.value

if(email.value == firstEmail) {
    linkBtn.disabled = true
}

email.addEventListener('keyup', event => {
    if(email.value == firstEmail) {
        linkBtn.disabled = true
    } else {
        linkBtn.disabled = false
    }
})