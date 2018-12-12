console.log(senateData[14]);
console.log(govData[14].fipscode);


var trace1 = {
   labels: ['Less than High School', 'High School', 'Some College','College Graduate'],
   values: [senateData[14].less_than_HighSchool,senateData[14].has_HighSchool,senateData[14].some_College,senateData[14].Undergrad_plus],

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