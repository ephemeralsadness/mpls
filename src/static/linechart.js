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
            line.data.datasets[0] = data.data;
			line.data.datasets[0].backgroundColor = '#ff4747';
			line.data.datasets[0].tension = 0.4;
        }
    })
}

setInterval(getData, 300000)