 $(function() {

       var sum_UNPAID_total_data = 0;
       var sum_PAID_total_data = 0;
    

       $("tr #UNPAID").each(function(index,value){
         getEachRow = parseFloat($(this).text());
         sum_UNPAID_total_data += getEachRow
       });
        
       $("tr #PAID").each(function(index,value){
         getEachRow = parseFloat($(this).text());
         sum_PAID_total_data += getEachRow
       });
       document.getElementById('UNPAID_total').innerHTML = sum_UNPAID_total_data;
       document.getElementById('PAID_total').innerHTML = sum_PAID_total_data;
       document.getElementById('total').innerHTML = sum_UNPAID_total_data + sum_PAID_total_data ;

});