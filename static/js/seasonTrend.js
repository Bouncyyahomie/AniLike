"use-strict"

const url = "http://127.0.0.1:5050/api/v1/season_trend"
// const url = "https://09mals.deta.dev/season-trend"

const seasons = document.getElementById("seasons")
const submitBtn = document.getElementById("submit")
const inputYears = document.getElementById("years")
document.getElementById("loading").style.display = "none"



const renderGraph = (animeData) => {
    const titleValues = animeData.map(ele => ele.title)
    const ratingValue = animeData.map(ele => ele.rating)
    const data = [
        {
            labels: titleValues,
            values: ratingValue,
            type: "pie",
        }
    ]
    const layout = {
        title: 'Trending anime in selected season',
        font: {
            family: 'Raleway, sans-serif'
            },
        }
    const config = { responsive: true }
    Plotly.newPlot('anime-season', data, layout, config);
}

submitBtn.onclick = (event) => {
    event.preventDefault();
    let years = inputYears.value
    years = parseInt(years);
    if (isNaN(years)) {
        inputYears.value= ""
        return
    }
    let selectedOption = seasons.options[seasons.selectedIndex]
    let selectedValue = selectedOption.value
    console.log(`${url}/${selectedValue}/${years}`)
    document.getElementById("loading").style.display = "block"
    fetch(`${url}/${selectedValue}/${years}`)
        .then(res => res.json())
        .then(data => {
            renderGraph(data)
            document.getElementById("loading").style.display = "none"
        })
        .catch(err => console.error(err))
}



