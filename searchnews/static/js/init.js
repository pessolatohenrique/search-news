$(document).ready(function() {
  $(".dropdown-trigger").dropdown();
  $(".sidenav").sidenav();
  $(".btn-search").on("click", function(event) {
    event.preventDefault();
    $(".card-search").toggle();
  });
});
