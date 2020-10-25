function bodyHeight() {
	var headerHeight = $('#navbar').outerHeight(true);
	var footerHeight = $('#footer').outerHeight(true);
	document.getElementById('container-fluid').style.minHeight = window.innerHeight - (headerHeight + footerHeight) + 'px';
}

$(document).onload = bodyHeight();