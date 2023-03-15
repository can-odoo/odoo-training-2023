url = "https://fakestoreapi.com/products"
let table_container = document.getElementById('table_container')
let next = document.getElementById('next')
let prev = document.getElementById('prev')

let page = 0;

function check(data) {

    if (((page+1)*10) >= data.length) {
        next.disabled = true
    } else {
        next.disabled = false
    }

    if (page == 0) {
        prev.disabled = true
    } else {
        prev.disabled = false

    }
}

async function apifetch() {

    res = await fetch(url)
    data = await res.json()

    check(data)

    let htmlString = "<table><tr> <th> Title </th><th>Image</th><th>Price</th></tr>"
    for (let i = 0; i < 10; i++) {
        htmlString += "<tr> <td>" + data[i + 10*page].title + "</td><td> <img src='" + data[i + 10*page].image + "'/></td><td>" + data[i + 10*page].price + "</td></tr>";
    }
    htmlString += "</table>"

    table_container.innerHTML = htmlString
}

next.addEventListener('click', () => {
    page++;
    apifetch();
})

prev.addEventListener('click', () => {
    page--;
    apifetch();
})

apifetch();