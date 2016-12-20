var $search = $("#search");

$search.select2({
  placeholder: "Select a video event",
  templateResult: function(state){
    return $(
        state.text.replace(
            /^([^ ]+) (.*)/,
            '<span><strong>$1</strong> $2</span>'
        )
    );
  }
});

$search.on("change", function(){
  var page = $(this).val().toString();
  if (page) {
    window.location.href = "/" + page + ".html";
  }
});
