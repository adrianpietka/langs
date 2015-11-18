function globalStats() {
  $.getJSON('/github/stats', function(response) {
    var gitHubUrl = 'https://github.com/';

    $('#gitHubStats .loading').hide();
    $('#gitHubStats .content').show();

    $('#gitHubStats .latest a').attr('href', gitHubUrl + response.data.latest.name).html(response.data.latest.name);
    $('#gitHubStats .latest span').html(response.data.latest.created);

    $('#gitHubStats .oldest a').attr('href', gitHubUrl + response.data.oldest.name).html(response.data.oldest.name);
    $('#gitHubStats .oldest span').html(response.data.oldest.created);

    $('#gitHubStats .processed b').html(response.data.processed);
    $('#gitHubStats .processed span').html(Math.round((response.data.processed * 100) / response.data.total));
    $('#gitHubStats .total b').html(response.data.total);
  });
}