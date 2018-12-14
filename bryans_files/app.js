function makeResponsive(){

  var svgArea = d3.select("body").select("svg");
  if (!svgArea.empty()) {
    svgArea.remove();
  }
  var svgWidth = 960;
  var svgHeight = 500;

  var margin = {
    top: 60,
    right: 60,
    bottom: 100,
    left: 100
  };

  var width = svgWidth - margin.left - margin.right;
  var height = svgHeight - margin.top - margin.bottom;
  
  // Create an SVG wrapper, append an SVG group that will hold our chart,
  // and shift the latter by left and top margins.
  var svg = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

  // Append an SVG group
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Initial Params     
  var chosenXAxis = "Undergrad_plus";
  var chosenYAxis = "votepct";

  function xScale(eduLevel, chosenXAxis) {
    // create scales
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(eduLevel, d => d[chosenXAxis]) * 0.8,
        d3.max(eduLevel, d => d[chosenXAxis]) * 1.2
      ])
      .range([0, width]);
  
    return xLinearScale;
  }
  function yScale(eduLevel, chosenYAxis){
    var yLinearScale = d3.scaleLinear()
      .domain([d3.min(eduLevel, d => d[chosenYAxis]) * 0.8,
        d3.max(eduLevel, d => d[chosenYAxis] ) * 1.2
    ])
      .range([height,0])
    //console.log(eduLevel);
    
    return yLinearScale;
  }
    // function used for updating xAxis var upon click on axis label
    function renderXAxis(newXScale, xAxis){
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
      .duration(1000)
      .call(bottomAxis);
      return xAxis;
  }
    // function used for updating yAxis var upon click on axis label
    function renderYAxis(newYScale, yAxis){
      
      var leftAxis = d3.axisLeft(newYScale);
      
      yAxis.transition()
        .duration(1000)
        .call(leftAxis);
    
      return yAxis;
  }

  // function used for updating the text in the circles group with a transition to
  // new circles when clicking on new axis
  function renderCircles(circlesGroup, newXScale, newYScale, chosenXAxis,chosenYAxis) {
    circlesGroup.transition()
      .duration(1000)
      .attr("cx", d => newXScale(d[chosenXAxis]))
      .attr("cy", d => newYScale(d[chosenYAxis]));
    return circlesGroup;
  }

  // function used for updating the text in the circles group with a transition to
  // new circles when clicking on new axis
  function renderText(textGroup, newXScale, newYScale, chosenXAxis, chosenYAxis) {
    textGroup.transition()
        .duration(1000)
        .attr("x", d => newXScale(d[chosenXAxis]))
        .attr("y", d => newYScale(d[chosenYAxis])+5); // removed "+5" inside last parenthese
    return textGroup;
  }

  // function used for updating circles group with new tooltip
  function updateToolTip(chosenXAxis, chosenYAxis, textGroup) {

    if (chosenXAxis === "Undergrad_plus") {
      var xlabel = "Voters with a degree: %";
    }
    else {
     var xlabel = "Voters with High School diploma: %";
    }

    if(chosenYAxis === "votepct"){ // should filter by party here
      var ylabel = "GOP % Votes: ";
    }
    else if (chosenYAxis === "votepct"){
      var ylabel = "Dem % Votes: ";
    }
    else {
      var ylabel = "3rd Party % Votes: ";
    }

    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`${d.County}<br>${xlabel} ${d[chosenXAxis]}`), (`${d.County}<br>${ylabel} ${d[chosenYAxis]}%`);
    });

    textGroup.call(toolTip);

    textGroup.on("mouseover", function(data, index){
      toolTip.show(data);
    })
      .on("mouseout", function(data, index){
      toolTip.hide(data);
    });

    return textGroup;
  } // CLOSES THE UPDATETOOLTIP FUNCTION

  d3.csv("working.csv",function(err, eduLevel) {
    if (err) throw err;
    //console.log(eduLevel);

   // Step 1: Parse data/Cast as numbers
   // ==================================
   for (var data in eduLevel){
     data.votepct = +data.votepct;
     data.has_HighSchool = +data.has_HighSchool;
     data.Undergrad_plus = +data.Undergrad_plus;
     data.party = data.party;
   };

  // CHECK SCALES BELOW TO MAKE SURE THEY'RE DEFINED/CALLED CORRECTLY

  // Step 2: Create scale functions
  // ==============================
  var xLinearScale = xScale(eduLevel, chosenXAxis);
  var yLinearScale = yScale(eduLevel, chosenYAxis);

  // Step 3: Create axis functions
  // ==============================
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Step 4: Append Axes to the chart
  // ==============================
  var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  var yAxis = chartGroup.append("g")
    .classed("y-axis", true)
    // .attr("transform", `translate(${width}), 0)`)
    .call(leftAxis);

  // Step 5: Create Circles
  // ==============================
  var circlesGroup = chartGroup.selectAll("circle")
    .data(eduLevel)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d[chosenYAxis]))
    .attr("r", 5)
    .style("fill", function(d){
      if (d.party === "GOP"){return "red"}
      else if (d.party === "Dem"){return "blue"}
      else {return "gray"};
    })
    .attr("opacity", ".5");

  var textGroup = chartGroup.selectAll(".label")
    .data(eduLevel)
    .enter()
    .append("text")
    .attr("class", "label")
    .attr("text-anchor", "middle")
    .text(function(d) {return d.abbr;})
    .attr("x", d => xLinearScale(d[chosenXAxis]))
    .attr("y", d => yLinearScale(d[chosenYAxis])+5) // SAME AS LINE 92-ish, REMOVED '+5'
    .attr("fill", "white")
    .attr("font-family","sans-serif");

  // Create group for 3 y-axis labels
  var ylabelsGroup = chartGroup.append("g")
    .attr("transform", "rotate(-90)")
    .attr("class", "axisText")
    .attr("x", 0 - (height / 2))
    .style("text-anchor", "middle");

  var gopLabel = ylabelsGroup.append("text")
    .attr("x",-150)
    .attr("y", -75)
    .attr("value", "GOP") // TOOK OUT CONDITIONAL HERE (data.party === GOP)
    .classed("active", true)
    .text("GOP % of Voting")

  var demLabel = ylabelsGroup.append("text")
    .attr("x",-150)
    .attr("y",-60)
    .attr("value", "Dem") // TOOK OUT CONDITIONAL HERE (data.party === Dem)
    .classed("active", true)
    .text("Dem % of Voting")

  var thirdpartyLabel = ylabelsGroup.append("text")
    .attr("x",-150)
    .attr("y", -45)
    .attr("value", "!= GOP | != Dem") // TOOK OUT CONDITIONAL HERE (data.party === GOP)
    .classed("active", true)
    .text("3rd Party % of Voting")

  // Create group for 2 x-axis labels
  var xlabelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var hsLabel = xlabelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "has_HighSchool") // value to grab for event listener
    .classed("active", true)
    .text("Percent of voters with High School education");

  var bachLabel = xlabelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "Undergrad_plus") // value to grab for event listener
    .classed("inactive", true)
    .text("Percent of voters with Bachelor's");

  // updateToolTip function above CSV import
  var textGroup = updateToolTip(chosenXAxis, chosenYAxis, textGroup);

  // x axis labels event listener
  xlabelsGroup.selectAll("text")
    .on("click", function(){
    // get value of selection
    var xvalue = d3.select(this).attr("value");
    if (xvalue !== chosenXAxis){

      // replaces chosenXAxis with value
      chosenXAxis = xvalue;
      // updates x scale for new data
      xLinearScale = xScale(eduLevel, chosenXAxis);
      // updates x axis with transition
      xAxis = renderXAxis(xLinearScale, xAxis);
      // updates circles with new x vales
      circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
      // updates text in circles with new x values
      textGroup = renderText(textGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
      // updates tooltips with new info
      textGroup = updateToolTip(chosenXAxis, chosenYAxis, textGroup);
      
      // changes classes to change bold text
      if (chosenXAxis == "Undergrad_plus") {
        bachLabel
          .classed("active", true)
          .classed("inactive", false);
        hsLabel
          .classed("active", false)
          .classed("inactive", true);
      }
      else {
        bachLabel
          .classed("active", false)
          .classed("inactive", true);
        hsLabel
          .classed("active", true)
          .classed("inactive", false);
      }
    }
    });

  // y axis labels event listener
  ylabelsGroup.selectAll("text")
    .on("click", function(){
    // get value of selection
      var yvalue = d3.select(this).attr("value");
      if (yvalue !== chosenYAxis){
        // replaces chosenYAxis with value
        chosenYAxis = yvalue;
        // updates y scale for new data
        yLinearScale = yScale(eduLevel, chosenYAxis);
        // updates y axis with transition
        yAxis = renderYAxis(yLinearScale, yAxis);
        // updates circles with new y values
        circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
        // updates text in circles with new y values
        textGroup = renderText(textGroup, xLinearScale, yLinearScale, chosenXAxis, chosenYAxis);
        // updates tooptips with new info
        text = updateToolTip(chosenXAxis, chosenYAxis, textGroup);
        // changes classes to change bold text
        console.log(chosenYAxis);
        if (chosenYAxis == "GOP"){ // deleted "d.party ===" before GOP here
          
          gopLabel
            .classed("active", true)
            .classed("inactive", false);
          demLabel
            .classed("active", false)
            .classed("inactive", true);
          thirdpartyLabel
            .classed("active", false)
            .classed("inactive", true);
          }
        else if (chosenYAxis == "Dem"){
          gopLabel
            .classed("active", false)
            .classed("inactive", true);
          demLabel
            .classed("active", true)
            .classed("inactive", false);
          thirdpartyLabel
            .classed("active", false)
            .classed("inactive", true);
          }
        else {
          gopLabel
            .classed("active", false)
            .classed("inactive", true);
          demLabel
            .classed("active", false)
            .classed("inactive", true);
          thirdpartyLabel
            .classed("active", true)
            .classed("inactive", false);
          }
      }})
  }); // THESE CLOSE THE D3.CSV, DATA-COMPILING FUNCTION
}; // THIS IS THE MASTER, 'MAKERESPONSIVE' FUNCTION
makeResponsive();
d3.select(window).on("resize", makeResponsive);