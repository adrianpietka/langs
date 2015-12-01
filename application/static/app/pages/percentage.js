function pagePercentage(successCallback) {
  if ($('#page-percentage-data').html() !== '') {
    successCallback();
    return;
  }

  api.languagesStats(function(data) {
    var languageStatsData = [];
    var colorsPie = ['#2484c1', '#0c6197', '#4daa4b', '#90c469', '#daca61', '#e4a14b',
      '#e98125', '#cb2121', '#830909', '#923e99', '#ae83d5', '#b0ec44', '#a4a0c9',
      '#bf273e', '#ce2aeb', '#bca44a', '#618d1b', '#1ee67b', '#322849', '#86f71a',
      '#d1c87f', '#7d9058', '#44b9b0', '#7c37c0', '#cc9fb1', '#e65414', '#8b6834',
      '#248838', '#248838'];
 
    $.each(data, function(index, item) {
      languageStatsData.push({
          'label': item.language,
          'value': item.repositories,
          'color': colorsPie[index]
      });
    });

    var percentRepositoriesPie = new d3pie('#page-percentage-data', {
      'size': {
        'canvasWidth': 700,
        'pieOuterRadius': '99%'
      },
      'data': {
        'sortOrder': 'value-desc',
        'smallSegmentGrouping': {
          'enabled': true
        },
        'content': languageStatsData
      },
      'labels': {
        'outer': {
          'pieDistance': 32
        },
        'inner': {
          'hideWhenLessThanPercentage': 3
        },
        'mainLabel': {
          'fontSize': 14
        },
        'percentage': {
          'color': '#ffffff',
          'decimalPlaces': 0
        },
        'value': {
          'color': '#adadad',
          'fontSize': 14
        },
        'lines': {
          'enabled': true
        },
        'truncation': {
          'enabled': true
        }
      },
      'effects': {
        'pullOutSegmentOnClick': {
          'effect': 'linear',
          'speed': 400,
          'size': 8
        }
      },
      'misc': {
        'gradient': {
          'enabled': true,
          'percentage': 100
        }
      }
    });

    successCallback();
  });
}