"use-strict"


const renderGraph = (animeData) => {
    const xValue = animeData.map(ele => ele.title)
    const yValue = animeData.map(ele => ele.averageRating)
    const data = [
        {
            x: xValue,
            y: yValue,
            type: "bar",
            marker: {
                color: 'rgb(142,124,195)'
            },
            textposition: 'auto',
        }
    ]
    const layout = {
        title: 'Popular Anime',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45
        },
        yaxis: {
            zeroline: false,
            gridwidth: 2
        },
        bargap: 0.05
    };
    const config = { responsive: true }
    Plotly.newPlot('popularAnime', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/trend"
fetch(url)
    .then(res => res.json())
    .then(data => {
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
    })
    .catch(err => console.error(err))

