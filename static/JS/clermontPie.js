console.log(senateData[12]);
console.log(govData[12].fipscode);


var trace1 = {
   labels: ['Less than High School', 'High School', 'Some College','College Graduate'],
   values: [senateData[12].less_than_HighSchool,senateData[12].has_HighSchool,senateData[12].some_College,senateData[12].Undergrad_plus],

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