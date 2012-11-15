
(function($){
    title = function() {
        $("body").append('See it works!. ');
    };

    check_videoRobot = function(jobId) {
        var start = new Date().getTime();
        var videRobURL = "http://videorobot.cnet.com/api/get_info.php?id=" + jobId + "&viewType=json";
        console.log(videRobURL);

         $.getJSON(videRobURL, function(response) {
             console.log(response);
				 });
    };

    check_videoRobot_tmp = function(jobId) {
        var start = new Date().getTime();
        var url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20rss%20where%20url%3D%22http%3A%2F%2Fnews.google.com%2Fnews%3Foutput%3Drss%22&format=json&diagnostics=true";
         
        $.getJSON(url, function(response) {
            console.log(start);
            console.log(response)
            for( var i=0 ; i < response.query.count ; i++)
					  {
						    console.log(response.query.results.item[i].title);
					      console.log(response.query.results.item[i].category);
						    console.log(response.query.results.item[i].description);
                console.log(response.query.results.item[i].pubDate); 
            }

            $('#label1').text(jobId);
        });
    };

})(jQuery);

function do_something(start){

    console.log(start);

}
