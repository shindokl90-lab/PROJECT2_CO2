function LoadAll()
{
    d3.json("/loadall").then(response => {
        console.log(countrytotals)
    })
}

function LoadOne()
{
    d3.json("/loadone").then(response => {
        console.log(singlecountry)
    })
}