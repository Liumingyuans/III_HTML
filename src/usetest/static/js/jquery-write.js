/* 淡入 淡出 */
$(document).ready(function(){
					$('#clickMe_one').css('opacity',0.7);
					$('#clickMe_one').mouseover(function(){
						$(this).fadeTo(50,1.5);
					});
					$('#clickMe_one').mouseout(function(){
						$(this).fadeTo(50,0.7);
					});
				});	
$(document).ready(function(){
					$('#clickMe_two').css('opacity',0.7);
					$('#clickMe_two').mouseover(function(){
						$(this).fadeTo(50,1.5);
						$('#clickMe_two').not(this).fadeTo(50,0.7);
					});
					$('#clickMe_two').mouseout(function(){
						$(this).fadeTo(50,0.7);
					});
				});	
$(document).ready(function(){
					$('#clickMe_thrid').css('opacity',0.7);
					$('#clickMe_thrid').mouseover(function(){
						$(this).fadeTo(50,1.5);
						$('#clickMe_thrid').not(this).fadeTo(50,0.7);
					});
					$('#clickMe_thrid').mouseout(function(){
						$(this).fadeTo(50,0.7);
					});
				});
$(document).ready(function(){
					$('#clickMe_fourth').css('opacity',0.7);
					$('#clickMe_fourth').mouseover(function(){
						$(this).fadeTo(50,1.5);
						$('#clickMe_fourth').not(this).fadeTo(50,0.7);
					});
					$('#clickMe_fourth').mouseout(function(){
						$(this).fadeTo(50,0.7);
					});
				});	
$(document).ready(function(){
					$('#Result').css('opacity',0.7);
					$('#Result').mouseover(function(){
						$(this).fadeTo(50,1.5);
						$('#Result').not(this).fadeTo(50,0.7);
					});
					$('#Result').mouseout(function(){
						$(this).fadeTo(50,0.7);
					});
				});	
$(document).ready(function(){
					$('.Conditions input[type="Conditions"]+label').css('opacity',0.8);
					$('.Conditions input[type="Conditions"]+label').mouseover(function(){
						$(this).fadeTo(50,2);
						$('#Result').not(this).fadeTo(50,0.8);
					});
					$('.Conditions input[type="Conditions"]+label').mouseout(function(){
						$(this).fadeTo(50,0.8);
					});
				});	
/* 顯示 隱藏 */
$(document).ready(function(){
	
	$('#clickMe_fourth').click(function(){
		$('#Conditions_fourth').slideToggle(1000);
	});

});

$(document).ready(function(){
	
	$('#clickMe_thrid').click(function(){
		$('#Conditions_thrid').slideToggle(1000);
	});

});

$(document).ready(function(){
	
	$('#clickMe_two').click(function(){
		$('#Conditions_two').slideToggle(1000);
	});

});


$(document).ready(function(){
	
	$('#clickMe_one').click(function(){
		$('#Conditions_one').slideToggle(1000);
	});

});
$(document).ready(function(){
	
	$('#Result').click(function(){
		$('#Conditions_fifth').slideToggle(1000);
	});

});

/* $(document).ready(function(){
	
	$('#name_one').click(function(){
		$('#Drawing_one').slideToggle(500);
		$('#Drawing_two').slideToggle(500);
		$('#Drawing_three').slideToggle(500);
	});

}); */
/* 移動改變 字體大小 */

$(document).ready(function(){
$('#money_title').bind('mouseenter mouseleave',function(){
	$(this).toggleClass('blod');
});
$('#money_title1').bind('mouseenter mouseleave',function(){
	$(this).toggleClass('blod');
});
$('#money_title2').bind('mouseenter mouseleave',function(){
	$(this).toggleClass('blod');
});

});


/* By jQuery http://jqueryui.com/tabs/*/
$(function() {
    $( "#tabs" ).tabs();
  });
  
/* By jQuery 12_animation */
  
$(function() {
    $( "#dialog" ).dialog({
      autoOpen: false,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "explode",
        duration: 1000
      }
    });
 
    $( "#opener" ).click(function() {
      $( "#dialog" ).dialog( "open" );
    });
  });