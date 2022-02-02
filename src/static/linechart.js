var ctx = document.getElementById('line')

var line = new Chart(ctx, {
    type: 'line',
	data: {
		labels: [],
		datasets: []
	},
	options: {
		responsive: true,
		title: {
			display: true,
			text: "",
		},
		plugins: {
			legend: {
				position: null,
			}
		}
	}
})

var getData = () => {
    $.ajax({
        url: '/plot',
        success: function(data) {
            line.data.labels = data.labels;
            line.data.datasets = data.data;
        }
    })
}

setInterval(getData, 300000)