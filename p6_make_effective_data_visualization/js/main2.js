function draw_bubble(data) {
  
  // D3.js setup code
  "use strict";
  var margin = 75,
      width = 1400 - margin,
      height = 600 - margin;
 
 // Add the chart svg element
  var svg = d3.select("div#bubble")
              .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin)
              .append('g')
              .attr('class','chart');
   
   // Dimple.js Chart construction code
          
  var myChart = new dimple.chart(svg, data);

  // Contruct the x-axis that represents average delay time
  var x_axis = myChart.addMeasureAxis("x", "AveDelay");
      x_axis.title = "Average Flight Delay Time In Minutes";
      x_axis.fontSize = "auto";
      x_axis.showGridlines = false; //remove the x grids
            
  // Contruct the y-axis that represents the delayed flight percentages
  var y_axis = myChart.addMeasureAxis("y", "Percentages");
      y_axis.title = "Percentages of Delayed Flights";
      y_axis.fontSize = "auto";
      y_axis.tickFormat = "%";
      y_axis.showGridlines = false; //remove the y grids

  var z_axis = myChart.addMeasureAxis("z", "DepDelay");

               
  var mySeries = myChart.addSeries("UniqueCarrier", dimple.plot.bubble);
      myChart.addLegend(0, 60, 100, 600) // add a legend
      myChart.draw();
};  

function draw_barplot(data) {

  // D3.js setup code
  "use strict";
  var margin = 75,
      width = 1400 - margin,
      height = 600 - margin;
 
 // Add the chart svg element
  var svg = d3.select("div#bar")
              .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin)
              .append('g')
              .attr('class','chart');
   
   // Dimple.js Chart construction code
          
  var myChart = new dimple.chart(svg, data);

  // Contruct the x-axis that represents day of week
  var x_axis = myChart.addCategoryAxis("x", "DayOfWeek");
      x_axis.title = "The Day of Week";
      x_axis.fontSize = "auto";
      x_axis.addOrderRule(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
            
  // Contruct the y-axis that represents the delayed flight percentages
  var y_axis = myChart.addMeasureAxis("y", "Percentages");
      y_axis.title = "Percentages of Delayed Flights";
      y_axis.fontSize = "auto";
      y_axis.tickFormat = "%";
               
  var mySeries = myChart.addSeries(null, dimple.plot.bar);
      myChart.draw();
};  