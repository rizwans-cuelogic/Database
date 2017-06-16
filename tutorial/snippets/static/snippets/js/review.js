$(document).ready(function() {
	$("#reviewform").submit(function (e){
   rate=$('#ratebar:selected').val();
   desc=$('#ratebar').val();
   email=$('#email1').val();
   datastring=rate+""+desc+""+email
   $.ajax({
      type: "POST",
      url: 'review_submit/',
      data: datastring ,  
      dataType:"JSON",
      processData: false,
      contentType: false,
      success: function(result){

      }
    });
});
})