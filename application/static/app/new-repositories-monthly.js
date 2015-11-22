function newRepositoriesMonthly() {
  $.getJSON('/github/new-repositories/monthly', function(response) {
    $('#gitHubNewRepositoriesTrend .loading').hide();
    $('#gitHubNewRepositoriesTrend .content').show();

    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 700 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
    
    var parseDate = d3.time.format("%Y-%m").parse;
    
    var x = d3.time.scale().range([0, width]);
    var y = d3.scale.linear().range([height, 0]);

    var color = d3.scale.category10();


    var xAxis = d3.svg.axis().scale(x).orient("bottom");
    var yAxis = d3.svg.axis().scale(y).orient("left");

    var line = d3.svg.line()
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.count); });

    var svg = d3.select("#gitHubNewRepositories").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var languages = [];
    for (var language in response.data) {
      var values = [];
    
      for (var perioid in response.data[language]) {
        values.push({
          'date' : parseDate(perioid),
          'count' : response.data[language][perioid]
        });
      };

      languages.push({'name' : language, 'values' : values});
      x.domain(d3.extent(values, function(d) { return d.date; }));
    }

    y.domain([
      d3.min(languages, function(l) { return d3.min(l.values, function(v) { return v.count; }); }),
      d3.max(languages, function(l) { return d3.max(l.values, function(v) { return v.count; }); })
    ]);

    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

    svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Repositories");

    var language = svg.selectAll(".language")
      .data(languages).enter()
    .append("g")
      .attr("class", "language")
    .append("path")
      .attr("class", "line")
      .attr("d", function(d) { return line(d.values); })
      .attr("data-legend",function(d) { return d.name})
      .style("stroke", function(d) { return color(d.name); });

    svg.append("g")
      .attr("class","legend")
      .attr("transform","translate(50,30)")
      .style("font-size","12px")
      .call(d3.legend);
  });
}