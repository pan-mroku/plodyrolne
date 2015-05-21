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

//Po namyśle to chyba średni pomysł
//http://stackoverflow.com/questions/5884644/calculate-the-current-location-longtitude-and-latitude
// navigator.geolocation.getCurrentPosition(
//		function(pos){
//				init_lat = pos.coords.latitude;
//				init_lng = pos.coords.longitude;
//				// send coordinates to server, or display on map, if you wish
//				//buildMarker(map, lat, long, "TEST", 'red');
//				//alert("your position is:"+lat+";"+long);
//				$('#id_Adres').val(init_lat+", "+init_lng);
//				geocode();
//		},
//		function(){
//				/* Handler if location could not be found */
//		});

map = new GMaps({
		div: '#gmap',
		lat: init_lat,
		lng: init_lng,
		zoom: 6
});

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
