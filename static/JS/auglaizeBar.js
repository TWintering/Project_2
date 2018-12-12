console.log(senateData[5]);
console.log(govData[5].fipscode);


var trace1 = {
   x: ['Senate','Governor'],
   y: [senateData[5].dem_percent,govData[5].dem_percent],
   name: "Dem",
  type:"bar"
};

var trace2 = {
	x: ['Senate','Governor'],
	y: [senateData[5].gop_percent,govData[5].gop_percent],
	name: "GOP",
	marker:{color:"red"},
	type:"bar"
};

var data = [trace1,trace2]

// var layout = {
  // height: 400,
  // width: 500
// };

var layout = {
  title: "Two Party Vote Share"
};


// var PIE = document.getElementById('pie')


Plotly.newPlot("bar", data, layout);;