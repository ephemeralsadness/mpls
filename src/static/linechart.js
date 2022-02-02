

var getData = () => {
    $.ajax({
        url: '/plot',
        success: function(data) {
			var charts = document.getElementById('charts')
			$.each(data, function(i, data) {
				if ($('#' + i).length > 0) {
					$('#' + i).remove();
				}
				
				var canvas = document.createElement('canvas');
				canvas.id = i;
				charts.appendChild(canvas);
				var ctx = document.getElementById(i).getContext("2d");
				var line = new Chart(ctx, {
					type: 'line',
					data: {
						labels: [],
						datasets: []
					},
					options: {
						responsive: true,
						plugins: {
							title: {
								display: true,
								text: ''
							},
							legend: {
								position: null,
							}
						},
					}
				})

				line.data.labels = data.labels;
				line.data.datasets = data.data;
				line.options.plugins.title.text = i;
				line.data.datasets[0].borderColor = '#ff4747';
				line.data.datasets[0].backgroundColor = '#ff4747';
				line.data.datasets[0].tension = 0.4;
				line.data.datasets[0].fill = true;

				line.update();
			})
        }
    })
}

getData();
setInterval(getData, 10000);