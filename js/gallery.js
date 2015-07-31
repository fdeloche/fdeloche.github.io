function changeImage(current, number) {
	var imagesNumber = number;
	
	for (i=1; i<=imagesNumber; i++) {	
		if (i == current) {
			document.getElementById("normal" + current).style.display = "block";
		} else {
			document.getElementById("normal" + i).style.display = "none";
		}
	}
}
