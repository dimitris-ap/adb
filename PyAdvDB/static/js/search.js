$("#searchBtn").click(function() {
    var dto = {
        'searchQuery' : $("#searchQuery").val(),
        'distance' : $("#distanceSelector").val(),
        'numOfDocsToReturn' : parseInt($("#numOfDocsToReturn").val())
    };

    var requestData = JSON.stringify(dto);

    if($("#searchQuery").val() != "") {
        $.ajax({
                "url": ROOT_PATH + "/api/search",
                "method": "POST",
                "processData": false,
                "data": requestData,
                "contentType": "application/json",
                "dataType": "json",
                success: function(responseData, textStatus, jQxhr){
                    handleSuccess(responseData);
                },
                statusCode: {
                     500 : function(xhr, options, error) {
                         console(xhr.responseText);
                     }
                }
       });
    } else {
        $("#emptyQueryMsg").show(1000);
        $('#loading').hide();
        $("#searchQuery").focus();
    }
});

function handleSuccess(relevantDocsDTO) {
    //Example response data:
    //{
    //    "documents":[
    //       {
    //          "content":"Ink helps drive democracy in Asia\n\nThe Kyrgyz Republic, a small, mountainous state of the former Soviet etc!",
    //          "filename":"tch001.txt",
    //          "path":"C:\\Users\\admin\\DWS\\Advanced Topics in Databases\\PyAdvDB\\data\\bbc\\tech\\"
    //          "sample":"Ink helps drive democracy in Asia\n\nThe Kyrgyz Republic, a small, mountainous state of the former Sov",
    //          "title":"Ink helps drive democracy in Asia"
    //       },
    //       {
    //          ...
    //       }
    //   ]
    //}

    var documents = relevantDocsDTO.documents;

    //delete prev search results
    $("#results").empty();

    // append the new ones
    for(let i = 0; i < documents.length; i++) {
        var filename = documents[i].filename;
        var path = documents[i].path;
        var content = documents[i].content;
        var sample = documents[i].sample.replace("\n", " ") + "...";
        var title = documents[i].title;

        $("#results").append(
                    "      <div class=\"row\">\n" +
                    "        <div class=\"card\">\n" +
                    "          <div class=\"card-body\">\n" +
                    "            <h5 class=\"card-title\">" + title + "</h5><br>\n" +
                    "            <p class=\"card-text\">" + sample + "</p><br>\n" +
                    "            <a class=\"card-text\" style=\"cursor: pointer; color: #2996ff;\" onclick=\"openWindow('" + escape(title) + "', '" + escape(content) + "');\">Read more...</a>\n" +
                    "          </div>\n" +
                    "        </div>\n" +
                    "      </div>");
        $('#loading').hide();
    }
}

function openWindow(title, content) {
    var html = templateHtmlBuilder(unescape(title), unescape(content));
    var wnd = window.open("about:blank", "_blank");
    wnd.document.write(html);
    wnd.focus();
    wnd.document.close();
}

function templateHtmlBuilder(title, content) {
        var first_part = "<!DOCTYPE html>\n" +
                    "<html lang=\"en\">\n" +
                    "<head>\n" +
                    "  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n" +
                    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n" +
                    "  <title>" + title + "</title>\n" +
                    "  <link rel=\"shortcut icon\" href=\"images/favicon.ico\">\n" +
                    "  <!-- Bootstrap core CSS -->\n" +
                    "  <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh\" crossorigin=\"anonymous\">\n" +
                    "  <style>\n" +
                    "    .bd-placeholder-img {\n" +
                    "      font-size: 1.125rem;\n" +
                    "      text-anchor: middle;\n" +
                    "      -webkit-user-select: none;\n" +
                    "      -moz-user-select: none;\n" +
                    "      -ms-user-select: none;\n" +
                    "      user-select: none;\n" +
                    "    }\n" +
                    "    @media (min-width: 768px) {\n" +
                    "      .bd-placeholder-img-lg {\n" +
                    "        font-size: 3.5rem;\n" +
                    "      }\n" +
                    "    }\n" +
                    "    .card {\n" +
                    "      margin: 5px;\n" +
                    "      width: 100%;\n" +
                    "  </style>\n" +
                    "  <link href=\"css/style.css\" rel=\"stylesheet\">\n" +
                    "</head>\n" +
                    "<body data-gr-c-s-loaded=\"true\" style=\"zoom: 1;\">\n" +
                    "  <header>\n" +
                    "  <div class=\"bg-dark collapse\" id=\"navbarHeader\" style=\"\">\n" +
                    "    <div class=\"container\">\n" +
                    "      <div class=\"row\">\n" +
                    "        <div class=\"col-sm-8 col-md-7 py-4\">\n" +
                    "          <h4 class=\"text-white\">About</h4>\n" +
                    "          <p class=\"text-white\">\n" +
                    "            <a href=\"http://www.auth.gr/\" target=\"_blank\" style=\"color: #b3b3b3;\">Aristotle University of Thessaloniki</a><br>\n" +
                    "            <a href=\"http://www.csd.auth.gr/\" target=\"_blank\" style=\"color: #b3b3b3;\">School of Informatics</a><br>\n" +
                    "            <a href=\"http://dws.csd.auth.gr/\" target=\"_blank\" style=\"color: #b3b3b3;\">MSc Data & Web Science</a><br>\n" +
                    "            <a href=\"https://elearning.auth.gr/course/view.php?id=11632\" target=\"_blank\" style=\"color: #b3b3b3;\">Advanced Topics in Databases</a><br>\n" +
                    "            <a href=\"http://delab.csd.auth.gr/~tiakas/\" target=\"_blank\" style=\"color: #b3b3b3;\">Eleftherios Tiakas</a>\n" +
                    "          </p>\n" +
                    "        </div>\n" +
                    "        <div class=\"col-sm-4 offset-md-1 py-4\">\n" +
                    "          <h4 class=\"text-white\">Student</h4>\n" +
                    "          <ul class=\"list-unstyled\">\n" +
                    "            <li><a href=\"https://dimitrisap.gr\" target=\"_blank\" style=\"color: #b3b3b3;\">Dimitris Apostolou</a></li>\n" +
                    "            <li><a href=\"mailto:dimapomic@csd.auth.gr\" style=\"color: #b3b3b3;\">dimapomic@csd.auth.gr</a></li>\n" +
                    "          </ul>\n" +
                    "        </div>\n" +
                    "      </div>\n" +
                    "    </div>\n" +
                    "  </div>\n" +
                    "  <div class=\"navbar navbar-dark bg-dark shadow-sm\">\n" +
                    "    <div class=\"container d-flex justify-content-between\">\n" +
                    "      <a href=\"javascript:location.reload();\" class=\"navbar-brand d-flex align-items-center\">\n" +
                    "        <img src=\"images/logo.png\" style=\"filter: invert(100%); width: 36px;\"/>\n" +
                    "        <strong>DocSearch</strong>\n" +
                    "      </a>\n" +
                    "      <button class=\"navbar-toggler collapsed\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarHeader\" aria-controls=\"navbarHeader\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n" +
                    "        <span class=\"navbar-toggler-icon\"></span>\n" +
                    "      </button>\n" +
                    "    </div>\n" +
                    "  </div>\n" +
                    "</header>\n" +
                    "<main role=\"main\">\n" +
                    "  <div class=\"album py-5 bg-light\">\n" +
                    "    <div id=\"results\" class=\"container\">";

        var doc = "      <div class=\"row\">\n" +
                    "        <div class=\"card\">\n" +
                    "          <div class=\"card-body\">\n" +
                    "            <h5 class=\"card-title\">" + title + "</h5><br>\n" +
                    "            <p class=\"card-text\">" + content + "</p><br>\n" +
                    "          </div>\n" +
                    "        </div>\n" +
                    "      </div>";

        var second_part = "</div>\n" +
                        "  </div>\n" +
                        "</main>\n" +
                        "<footer class=\"text-muted\">\n" +
                        "  <div class=\"container\">\n" +
                        "    <p class=\"float-right\">\n" +
                        "      <a href=\"#\">Back to top</a>\n" +
                        "    </p>\n" +
                        "    <p>MSc Data & Web Science | Advanced Topics in Databases | Dimitris Apostolou | 2020</p>\n" +
                        "  </div>\n" +
                        "</footer>\n" +
                        "<script src=\"js/jquery-3.4.1.min.js\" integrity=\"sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=\" crossorigin=\"anonymous\"></script>\n" +
                        "<script>window.jQuery</script>\n" +
                        "<script src=\"js/bootstrap.bundle.min.js\" integrity=\"sha384-6khuMg9gaYr5AxOqhkVIODVIvm9ynTT5J4V1cfthmT+emCG6yVmEZsRHdxlotUnm\" crossorigin=\"anonymous\"></script>\n" +
                        "</body>\n" +
                        "</html>";

        return first_part + doc + second_part;
}