function loadDistances(selectorId){
    $.ajax({
         "url" : ROOT_PATH + "/api/distances",
         "method" : "GET",
         "contentType": "application/json",
         "dataType": "json",
         success : function(response) {
             response.forEach(function(distance){
                $("#"+selectorId).append(
                    $(
                        '<option>',
                        {
                            value : distance.value,
                            text : distance.text
                        }
                    )
                );
             });
         },
         error : function(xhr, options, error){
            console.log(error);
         }
    })
}