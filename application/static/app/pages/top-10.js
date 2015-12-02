function pageTop10(successCallback) {
  if ($('#page-top-10-data').html() !== '') {
    successCallback();
    return;
  }

  api.languagesStats(function(data) {
    var lp = 1;
    var topLanguages = data.map(function(item) {
      item['lp'] = lp++;
      item['total'] = item['repositories'] + ' (' + item['percentage'] + '%)';
      return item;
    });

    var topTenTable = tabulate('#page-top-10-data', topLanguages.slice(0, 10), ['lp', 'language', 'total']);
    topTenTable.select('.lp').text('Lp.');
    topTenTable.select('.language').text('Language');
    topTenTable.select('.total').text('Total');

    successCallback();
  });
}