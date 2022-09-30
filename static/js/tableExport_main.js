
function exportTo(type) {

	$('.table').tableExport({
		filename: 'table_%DD%-%MM%-%YY%',
		format: type,
		cols: '2,3,4'
	});

}

function exportAll(type) {

	$('.table').tableExport({
		filename: 'FSL_%DD%-%MM%-%YY%',
		format: type
	});

}