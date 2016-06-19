$(function() {

	$("#contact-btn").on("click", function () {
		$.ajax({
			type: "POST",
			url: "/contact-us",
			data: {
				"name":$("#name").val(),
				"email":$("#email").val(),
				"message":$("#message").val(),
			},
			success: function(data) {
				if (data.result == 'success') {
					alert("Message sent. We will get back to you shortly!")
					window.location.href = '/';
				} else {
					alert("Error!");
				}
				console.log(data);
			},
			dataType: 'json'
		})
	});
});