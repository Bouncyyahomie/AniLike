"use-strict"

const renderGraph = (animeData) => {
    const xValue = animeData.map(ele => ele.title)
    const yValue = animeData.map(ele => ele.average_rating)
    const data = [
        {
            x: xValue,
            y: yValue,
            type: "bar",
            marker: {
                color: 'rgb(142,124,195)'
            },
        }
    ]
    console.log(data)
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
            gridwidth: 2,
            rangemode: 'tozero',
            range:[0,100]
        },
        bargap: 0.05
    };
    const config = { responsive: true }
    Plotly.newPlot('popularAnime', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/popular-anime"
// const url = "https://09mals.deta.dev/api/v1/popular-anime"
fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data)
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
    })
    .catch(err => console.error(err))

