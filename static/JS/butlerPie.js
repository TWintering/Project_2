console.log(senateData[8]);
console.log(govData[8].fipscode);


var trace1 = {
   labels: ['Less than High School', 'High School', 'Some College','College Graduate'],
   values: [senateData[8].less_than_HighSchool,senateData[8].has_HighSchool,senateData[8].some_College,senateData[8].Undergrad_plus],

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