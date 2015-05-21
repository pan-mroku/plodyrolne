function setAddress(point)
{
		map.panTo(point);
		$('#id_Adres').val(point.lat()+", "+point.lng());
}
function geocode() {
		GMaps.geocode({
				address: $('#id_Adres').val().trim(),
				callback: function(results, status){
						if(status=='OK'){
								var latlng = results[0].geometry.location;
                map.setCenter(latlng.lat(), latlng.lng());
                marker.setPosition(latlng);
						};
				}
		});
}

var init_lat = 52;
var init_lng = 20;

//http://stackoverflow.com/questions/5884644/calculate-the-current-location-longtitude-and-latitude
//Nie pytaj o położenie, jeśli coś zostało wpisane (czyli nie przyszliśmy getem) ^^
if ($('#id_Adres').val() == '') {
		navigator.geolocation.getCurrentPosition(
				function(pos){
						init_lat = pos.coords.latitude;
						init_lng = pos.coords.longitude;
						// send coordinates to server, or display on map, if you wish
						//buildMarker(map, lat, long, "TEST", 'red');
						//alert("your position is:"+lat+";"+long);
						$('#id_Adres').val(init_lat+", "+init_lng);
						geocode();
				},
				function(){
						/* Handler if location could not be found */
				});
}

map = new GMaps({
		div: '#gmap',
		lat: init_lat,
		lng: init_lng,
		zoom: 6
});

$('#id_Adres').val(init_lat+", "+init_lng);

var marker = map.addMarker({
		lat: init_lat,
		lng: init_lng,
		draggable:true,
});

google.maps.event.addListener(marker, 'dragend', function(mouseEvent) {
    setAddress(mouseEvent.latLng);
});

google.maps.event.addListener(map, 'click', function(mouseEvent){
    marker.setPosition(mouseEvent.latLng);
    setAddress(mouseEvent.latLng);
});

geocode();

$("#id_Adres").keypress(function(){
		geocode();
});

$('tr[rolnik_url]').each(function(){
    var $el = $(this);

		var latlng = geocode($el.attr('rolnik_adres'));
		GMaps.geocode({
				address: $el.attr('rolnik_adres'),
				callback: function(results, status){
						if(status=='OK'){
								var latlng = results[0].geometry.location;
								map.addMarker({
										lat: latlng.lat(),
										lng: latlng.lng(),
										icon: $el.attr('rolnik_icon'),
										infoWindow: {
												content: "<a href="+$el.attr('rolnik_url')+">"+$el.attr('rolnik_etykieta')+"</a>"
										}
								});
						};
				}
		});
});
