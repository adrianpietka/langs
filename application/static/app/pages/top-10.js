function pageTop10(successCallback) {
  if ($('#page-top-10-data').html() !== '') {
    successCallback();
    return;
  }

  api.languagesStats(function(data) {
    var topTenTable = tabulate('#page-top-10-data', data.slice(0, 10), ['language', 'repositories']);
    topTenTable.select('.language').text('Language');
    topTenTable.select('.repositories').text('Repositories count');
    successCallback();
  });
}