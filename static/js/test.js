async function getText(file) {
    let x = await fetch(file)
    let y = await x.text()
    document.getElementById('ok').innerHTML = y
}