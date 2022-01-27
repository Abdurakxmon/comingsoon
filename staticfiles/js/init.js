// Edit the date here

$(document).ready(function() {
						   
	$("#countdown").countdown({
				date: "20 November 2020 10:10:10",
				format: "on"
			},
			
			function() {
				// callback function
			});

});	
