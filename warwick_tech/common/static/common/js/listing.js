$(document).ready(function(){

  var date = $('div.job-deadline-num-wrap > strong').data('date');

  $('div.job-deadline-num-wrap > strong').text(date.split(' ')[0]);

});
