$(function(){
	var timer=null,interval=2000,value=0;
	var n=0;
var takephoto= function() {
	    $.ajax({
		type : 'POST',
		url : 'takephoto.php',
		success : function(data){
		  $("#photo").attr("src", "cam.jpg?timestamp=" + new Date().getTime());
			n+=1;
			$('#msg').html(n+' photos taken');

		},
	    });
	};

$('#takephoto').click(function(){
	timer=setInterval(function(){
		takephoto();
	},2000);
	});


$('#stoptakingphoto').click(function(){
	clearInterval(timer);
	timer=null;
	});

$('#go').click(function(){
	$('#msgmove').html('moving');
	  $.ajax({
		type : 'POST',
		url : 'move.php?M=F&T=1&P=0.5',
		success : function(data){
			$('#msgmove').html('moved');

		},
	    });


});

$('#back').click(function(){
	$('#msgmove').html('moving');
	  $.ajax({
		type : 'POST',
		url : 'move.php?M=B&T=1&P=0.5',
		success : function(data){
			$('#msgmove').html('moved');

		},
	    });


});
$('#left').click(function(){
	$('#msgmove').html('moving');
	  $.ajax({
		type : 'POST',
		url : 'move.php?M=L&T=0.2&P=0.4',
		success : function(data){
			$('#msgmove').html('moved');

		},
	    });


});

$('#right').click(function(){
	$('#msgmove').html('moving');
	  $.ajax({
		type : 'POST',
		url : 'move.php?M=R&T=0.2&P=0.4',
		success : function(data){
			$('#msgmove').html('moved');

		},
	    });


});




});
