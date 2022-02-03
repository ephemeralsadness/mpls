

var getData = () => {
    $.ajax({
        url: '/plot',
        success: function(data) {
			var charts = document.getElementById('charts')
			$.each(data, function(i, data) {
				var element =  document.getElementById(i);
				if (typeof(element) != 'undefined' && element != null)
				{
				  	element.remove();
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

				var last_3_symbols = i.slice(-3)
				var map = new Map();
				map.set("age", "#7777FF")
				map.set("max", "#FD5469")
				map.set("min", "#CC8F57")
				map.set("0.1", "#2F5604")
				map.set("0.5", "#2F5604")
				map.set("0.9", "#2F5604")

				line.data.labels = data.labels;
				line.data.datasets = data.data;
				line.options.plugins.title.text = i;
				line.data.datasets[0].borderColor = '#000000';
				line.data.datasets[0].backgroundColor = map.get(last_3_symbols);
				line.data.datasets[0].tension = 0.4;
				line.data.datasets[0].fill = true;

				line.update();
			})
        }
    })
}

getData();
setInterval(getData, 1000 * 60 * 5);