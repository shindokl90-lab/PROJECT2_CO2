function LoadCharts()
{
    d3.json("/loadcharts").then(response => {
        console.log(countrytotals)
    })
}

function ReLoadCharts()
{
    d3.json("/reloadcharts").then(response => {
        console.log(countrytotal)
    })
}