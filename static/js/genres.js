"use-strict"

"use-strict"


const renderGraph = (animeData) => {
    const xValue = animeData.map(ele => ele.title)
    const yValue = animeData.map(ele => ele.total_media_count)
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
        title: 'Anime Catagories',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            ticks: "outside",
            tick0: 0,
            dtick: 0.1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 2,
            rangemode: 'tozero',
            range:[0,10000]
        },
        bargap: 0.05
    };
    const config = { responsive: true }
    Plotly.newPlot('catagoriesCount', data, layout, config);
}

const url = "http://127.0.0.1:5050/api/v1/genres" // local
// const url = "https://09mals.deta.dev/api/v1/genres"
fetch(url)
    .then(res => res.json())
    .then(data => {
        renderGraph(data)
        document.getElementById("loading").style.display = "none"
    })
    .catch(err => console.error(err))

