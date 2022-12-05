import {updateChart} from "./chart_crypto.js";
import {updateTable} from "./table_crypto.js";

setInterval(function () {
    updateChart()
    updateTable()
}, 3000)