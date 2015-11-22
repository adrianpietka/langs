function tabulate(container, data, columns) {
  var table = d3.select(container).append('table').attr('class', 'table table-bordered table-hover'),
      thead = table.append('thead'),
      tbody = table.append('tbody');

  // append the header row
  thead.append('tr')
      .selectAll('th')
      .data(columns)
      .enter()
      .append('th')
          .attr('class', function(column) { return column; })
          .text(function(column) { return column; });

  // create a row for each object in the data
  var rows = tbody.selectAll('tr')
      .data(data)
      .enter()
      .append('tr');

  // create a cell in each row for each column
  var cells = rows.selectAll('td')
      .data(function(row) {
          return columns.map(function(column) {
              return {column: column, value: row[column]};
          });
      })
      .enter()
      .append('td')
          .text(function(d) { return d.value; });
  
  return table;
}