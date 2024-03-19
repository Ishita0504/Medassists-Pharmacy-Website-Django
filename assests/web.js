$(document).ready(function(){
$.getJSON('http://localhost:8000/fetchweb',function(data){
   htm=''
    data.data.map(item=>{

        htm+=`
        <div style=" background-color:white; border-radius:10px 70px / 50px;; margin:10px;display: flex; flex-direction: column;align-items: center; width:250px;height:300px;padding: 20px;border:1px solid #bdc3c7;box-shadow: 2px 2px #ecf0f1;elevation: below;">
          <div style='margin-top:8px;'>
          <img src="http://localhost:8000/static/${item.icon}" style='width:150px; height: 150px;' >
          </div>
          <div style="padding:5px;">
          <div style="width:200px;font-weight: bolder;text-align: left;">
${item.name}
</div>
<div style="width:200px; font-size:10px;text-align: left;">
<p>${item.des}</p>
</div>
</div>

         </div>

         `
})

  $('#pro').html(htm)

 })

})