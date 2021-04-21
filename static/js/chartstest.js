var canvas = document.getElementById("barChart");
var ctx = canvas.getContext('2d');

// Global Options:
Chart.defaults.global.defaultFontColor = 'black';
Chart.defaults.global.defaultFontSize = 16;
var valData = name_y;
var valVal = valVal0;
var test1 = test_var;
var nameVal1 = name_val;
console.log(test1)

var data = {
  labels: valData,
  datasets: [{
      label: "Stock A",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(225,0,0,0.4)",
      borderColor: "red", // The main line color
      borderCapStyle: 'square',
      borderDash: [], // try [5, 15] for instance
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "black",
      pointBackgroundColor: "white",
      pointBorderWidth: 1,
      pointHoverRadius: 8,
      pointHoverBackgroundColor: "yellow",
      pointHoverBorderColor: "brown",
      pointHoverBorderWidth: 2,
      pointRadius: 4,
      pointHitRadius: 10,
      // notice the gap in the data and the spanGaps: true
      data: valVal,
      spanGaps: true,}
  ]
};

// Notice the scaleLabel at the same level as Ticks
var options = {
  scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                },
                scaleLabel: {
                     display: true,
                     labelString: 'Moola',
                     fontSize: 20
                  }
            }],
        }
};

// Chart declaration:
var myBarChart = new Chart(ctx, {
  type: 'line',
  data: data,
  options: options
});

function addData(chart, dateVal, timeVal) {
    chart.data.datasets[0].data = dateVal
    chart.update();
}


function testVal(nameVal){
    console.log(nameVal)
    let res_arr = [];
    let time_arr = [];
    test1.forEach(function(item, i, test1) {
        res_arr.push(Number(item[nameVal]));
        time_arr.push(item.date)
});
    addData(myBarChart, res_arr, time_arr)
    // console.log(res_arr)
    console.log(time_arr)
}


