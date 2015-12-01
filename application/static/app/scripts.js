var cache = {
  '_data': {},
  'get': function(name) {
    if (typeof(cache._data[name]) !== 'undefined') {
      return cache._data[name];
    }

    return false;
  },
  'set': function(name, value) {
    cache._data[name] = value;
  }
};

var api = {
  '_execute': function(key, url, callback) {
    var cachedData = cache.get(key);
    if (cachedData === false) {
      $.getJSON(url, function(response) {
        callback(response.data);
        cache.set(key, response.data);
      });
    } else {
      callback(cachedData);
    }
  },
  'stats': function(callback) {
    api._execute('stats', '/github/stats', callback);
  },
  'languagesStats': function(callback) {
    api._execute('languages-stats', '/github/languages/stats', callback);
  },
  'newRepositoriesMonthly': function(callback) {
    api._execute('new-repositories-monthly', '/github/new-repositories/monthly', callback);
  }
};

function globalStats() {
  api.stats(function(data) {
    var gitHubUrl = 'https://github.com/';

    $('#global-stats .loading').hide();
    $('#global-stats .content').show();

    $('#global-stats .latest a').attr('href', gitHubUrl + data.latest.name).html(data.latest.name);
    $('#global-stats .latest span').html(data.latest.created);

    $('#global-stats .oldest a').attr('href', gitHubUrl + data.oldest.name).html(data.oldest.name);
    $('#global-stats .oldest span').html(data.oldest.created);

    $('#global-stats .processed b').html(data.processed);
    $('#global-stats .processed span').html(Math.round((data.processed * 100) / data.total));
    $('#global-stats .total b').html(data.total);
  });
}

$(document).ready(function() {
  globalStats();

  $('#stats a').click(function() {
    var pageLink = this;
    var pageId = '#page-' + $(pageLink).attr('href').replace('/#', '');
    var pageCallback = $(pageId).data('callback');

    $('#stats .active').removeClass('active');
    $(pageLink).parent().addClass('active');
    $('#pages .loading').show();
    $('#pages .page').hide();
    
    window[pageCallback](function() {
      $('#pages .loading').hide();
      $(pageId).show();
    }, function() {
      alert('Loading error - try again.');
    });
  });

  $('#stats a:first').click();
});