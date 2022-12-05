import {handleDateHistory} from './handle.js'
import {myColor} from "./color.js";

const data = {
  labels: [],
  datasets: [{
    label: '',
    backgroundColor: '',
    borderColor: '',
    data: [],
  }]
};
function configFunc () {
    return {
      type: 'line',
      data: data,
      options: {}
    };
}

let myChartOne = new Chart(
    document.getElementById("myChartOne"),
    configFunc()
);
let myChartTow = new Chart(
    document.getElementById("myChartTow"),
    configFunc()
);
let myChartThree = new Chart(
    document.getElementById("myChartThree"),
    configFunc()
);
let myChartFour = new Chart(
    document.getElementById("myChartFour"),
    configFunc()
);
let myChartFive = new Chart(
    document.getElementById("myChartFive"),
    configFunc()
);

// let myChart = [myChartOne, myChartTow, myChartThree, myChartFour, myChartFive]

function updateChart() {
    async function fetchData() {
        const url = 'http://127.0.0.1:5000/api/history'
        const response = await fetch(url)
        const datapoints = await response.json()
        return datapoints
    }
    fetchData().then(datapoints => {
        const historys = datapoints.map((datapoint) => {
            const {listLabels, listDataPoints} = handleDateHistory(datapoint['Data'])
            return {
                "name": datapoint.Name,
                listLabels,
                listDataPoints,
            }
        })
        myChartOne.config.data = dataSet(historys,0)
        myChartTow.config.data = dataSet(historys,1)
        myChartThree.config.data = dataSet(historys,2)
        myChartFour.config.data = dataSet(historys,3)
        myChartFive.config.data = dataSet(historys,4)
        myChartOne.update();
        myChartTow.update();
        myChartThree.update();
        myChartFour.update();
        myChartFive.update();

        let dateTime = new Date().toLocaleString('en-GB', { hour:'numeric', minute:'numeric', second:'numeric', hour12:false})
        console.log("Time update ", dateTime)
    })
}

function dataSet(historys, index) {
    return {
              labels: historys[index].listLabels,
              datasets: [{
                label: historys[index].name,
                backgroundColor: myColor(index),
                borderColor: myColor(index),
                data: historys[index].listDataPoints,
              }]
    }
}

export {updateChart}
