$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});
$(function(){
  $('.table tr[data-href]').each(function(){
    $(this).css('cursor','pointer').hover(
      function(){
        $(this).addClass('active');
      },
      function(){
        $(this).removeClass('active');
      }).click( function(){
        window.open($(this).attr('data-href'));
      }
    );
  });
});

function mainIt() {
  const Http = new XMLHttpRequest();
  const url='https://jsonplaceholder.typicode.com/posts';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }
}
