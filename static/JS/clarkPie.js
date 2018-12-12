console.log(senateData[11]);
console.log(govData[11].fipscode);


var trace1 = {
   labels: ['Less than High School', 'High School', 'Some College','College Graduate'],
   values: [senateData[11].less_than_HighSchool,senateData[11].has_HighSchool,senateData[11].some_College,senateData[11].Undergrad_plus],

  type:"pie"
};

var data = [trace1]

// var layout = {
  // height: 400,
  // width: 500
// };

var layout = {
  title: "Highest Completed"
};


// var PIE = document.getElementById('pie')


Plotly.newPlot("pie", data, layout);;