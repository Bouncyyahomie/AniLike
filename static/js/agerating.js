"use-strict"


const renderGraph = (animeData) => {
    const xValue = animeData.map(ele => ele.title)
    console.log(xValue)
    const yValue = animeData.map(ele => ele.mediaCount)
    console.log(yValue)
    const data = [
        {
            labels: xValue,
            values: yValue,
            type: "pie",
        }
    ]
    const layout = {
        title: 'Age Rating',
        font: {
            family: 'Raleway, sans-serif'
            },
        height: 600,
        width: 500
        }
    const config = { responsive: true }
    Plotly.newPlot('agerating', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/agerating"
fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data)
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
    })
    .catch(err => console.error(err))