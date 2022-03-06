


$(document).ready(function(){

    $('#file').on('change',function(){
        $('#arq_selecionado').text($(this)[0].files[0].name);
    });

    $('input[type="submit"]').on('click',function (e) { 
        e.preventDefault();

        if($('#file')[0].files.length==0){
            $('#staticBackdrop').modal('show');
        }else{
            $('form').submit();
        }
     })



});

function initMap() {
    // The location of Uluru
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("mapa"), {
        zoom: 8,
        center: sorocaba,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: sorocaba,
        map: map,
        title:"Sorocaba,SP"
    });

    locations.forEach(element => {
        new google.maps.Marker({
            position: element.code,
            title:`${element.location}\nDistância de Sorocaba:${element.distancia}\nInfo:${element.info}`,
            map: map,
        });
    });
}     
