$(document).ready(function(){
	$.ajax({
		url: '/add_contents',
		type: 'POST',
		data: {},
		success:function(response){
			$('#wall_post').append(response);
		},
		error:function(){
				console.log('error');
		},
		complete:function(){
				console.log('complete');
		}


	});

});