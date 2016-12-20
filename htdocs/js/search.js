var $search = $("#search");

$search.select2({
  placeholder: "Select a video event",
  minimumResultsForSearch: Infinity
});

$search.on("change", function(){
  var page = $(this).val().toString();
  if (page) {
    window.location.href = "/" + page + ".html";
  }
});
