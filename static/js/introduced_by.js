"use-strict"


const renderGraph = (animeData) => {
    const xValue = animeData.map(ele => ele.first_introduced_by)
    const yValue = animeData.map(ele => ele.count)
    const data = [
        {
            labels: xValue,
            values: yValue,
            type: "pie",
        }
    ]
    const layout = {
        title: 'First Introduced By',
        font: {
            family: 'Raleway, sans-serif'
            },
        height: 600,
        width: 500
        }
    const config = { responsive: true }
    Plotly.newPlot('introdcued_by', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/first_introduced"
fetch(url)
    .then(res => res.json())
    .then(data => {
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
        console.log(data)
    })
    .catch(err => console.error(err))