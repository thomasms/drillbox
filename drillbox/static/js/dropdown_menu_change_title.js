$(document).ready(function(){
    var dropdown_name = "#tool_dropdown"

    $(dropdown_name).on('click', 'li a', function(){
      $(dropdown_name + " .btn:first-child").html($(this).text() + ' <span class="caret"></span>');
      $(dropdown_name + " .btn:first-child").val($(this).text());
   });

});