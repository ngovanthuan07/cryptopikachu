
const formatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
});
function removeTableBody() {
  $('#myTableId tbody').empty();
}
function updateTable() {
    async function fetchData() {
        const url = 'http://127.0.0.1:5000/api/crypto'
        const response = await fetch(url)
        const data = await response.json()
        return data
    }
    fetchData().then(data => {
        // remove all element child tbody
        removeTableBody()
        let myData = data['listCrypto']
        let tableCrypto = document.getElementById("tableCrypto")
        myData.forEach((d, index) => {
          tableCrypto.innerHTML += `
              <tr>
                  <th scope="row">${index + 1}</th>
                      <td style="display: flex; align-items: center">
                        <div><img src="https://www.cryptocompare.com/${d.image_url}" alt="${d.fullname}" style="width: 25px; object-fit: cover"></div>
                        &nbsp; &nbsp; 
                        <div><b>${d.fullname}</b> <br> <b style="color: #666">${d.name}</b></div>
                  </td>
                  <td>${formatter.format(d.price)}</td>
                  <td>${formatter.format(d.top_tier_volume_24_hour_to)}</td>
                  <td>${ formatter.format(d.total_volume_24h_to) }</td>
                  <td>${formatter.format(d.total_top_tier_volume_24h_to)}</td>
                  <td>${formatter.format(d.mktcap)}</td>
                  <td>${Math.round(d.change_pct_24_hour * 100) / 100} %</td>
            </tr>`
          })
    })
}

export {updateTable}