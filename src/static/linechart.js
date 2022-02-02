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
			display: false,
			text: "TesT",
		},
		plugins: {
      		title: {
        		display: true,
        		text: 'Test'
      		},
			legend: {
				position: null,
			}
    	},
	}
})

var getData = () => {
    $.ajax({
        url: '/plot',
        success: function(data) {
            line.data.labels = data.test.labels;
            line.data.datasets = data.test.data;
			line.data.datasets[0].borderColor = '#ff4747';
			line.data.datasets[0].backgroundColor = '#ff4747';
			line.data.datasets[0].tension = 0.4;
			line.data.datasets[0].fill = true;

			line.update();
        }
    })
}

getData()