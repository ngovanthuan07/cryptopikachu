function handleDateTime(utcSeconds) {
    var d = new Date(0);
    d.setUTCSeconds(utcSeconds);
    // return d.toLocaleString('en-GB', { hour12:false } )
    return d.toLocaleString('en-GB', { hour:'numeric', minute:'numeric', second:'numeric', hour12:false})
}
function handleDateHistory(datas) {
    let listLabels = []
    let listDataPoints = []
    for(const element of datas){
        listLabels.push(handleDateTime(element['time']))
        listDataPoints.push(element['open'])
    }
    return {listLabels, listDataPoints}
}

export {handleDateHistory, handleDateTime}
