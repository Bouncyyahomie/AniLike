"use-strict"


const renderGraph = (animeData) => {
    const xValue = animeData[0].map(ele => ele.first_introduced_by)
    console.log(xValue)
    const yValue = animeData[0].map(ele => ele.count)
    console.log(yValue)
    const data = [
        {
            labels: xValue,
            values: yValue,
            type: "pie",
        }
    ]
    const layout = {
        title: 'First Introducing to Anime method',
        font: {
            family: 'Raleway, sans-serif',
            size: 20
            },
        // width: 500
        }
    const config = { responsive: true }
    Plotly.newPlot('introdcued_by', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/first_introduced"
// const url = "https://09mals.deta.dev/api/v1/first_introduced"

fetch(url)
    .then(res => res.json())
    .then(data => {
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
        console.log(data)
    })
    .catch(err => console.error(err))