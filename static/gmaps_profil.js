GMaps.geocode({
		address: $('#Adres').text().trim(),
		callback: function(results, status){
				if(status=='OK'){
						var latlng= results[0].geometry.location;
						map = new GMaps({
								lat: latlng.lat(),
								lng: latlng.lng(),
								div: '#gmap',
								zoom: 6
						});
						map.addMarker({
								lat: latlng.lat(),
								lng: latlng.lng(),
						});
				}
		}
});
