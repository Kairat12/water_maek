const roundedBarsPlugin = {
    id: 'roundedBars',
    beforeDraw: chart => {
        const {ctx} = chart;
        ctx.save();
        chart.getDatasetMeta(0).data.forEach((bar, index) => {
            const radius = 20;
            const {x, y, width, height} = bar;
            ctx.beginPath();
            ctx.moveTo(x - width / 2, y);
            ctx.lineTo(x - width / 2, y + height - radius);
            ctx.quadraticCurveTo(x - width / 2, y + height, x - width / 2 + radius, y + height);
            ctx.lineTo(x + width / 2 - radius, y + height);
            ctx.quadraticCurveTo(x + width / 2, y + height, x + width / 2, y + height - radius);
            ctx.lineTo(x + width / 2, y);
            ctx.fillStyle = bar.options.backgroundColor;
            ctx.fill();
            ctx.stroke();
        });
        ctx.restore();
    }
};

Chart.register(roundedBarsPlugin);

const createChart = (ctx, label, data, criticalLevel, criticalLevel2, criticalLevelVolume, criticalLevelVolume2) => {
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [label],
            datasets: [{
                label: 'Уровень воды (м)',
                data: [data],
                backgroundColor: data < criticalLevel ? 'rgba(255, 99, 132, 0.5)' : data < criticalLevel2 ? 'rgba(255,194,7,0.5)' : 'rgba(54, 162, 235, 0.5)',
                borderWidth: 1,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: false,
            scales: {
                x: {
                    beginAtZero: true,
                    barPercentage: 0.5,
                },
                y: {
                    beginAtZero: true,
                    max: 5,
                    ticks: {
                        stepSize: 1,
                        callback: function (value, index, values) {
                            return value + ' м'; // Метки по высоте
                        }
                    }
                },

            },
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: false,
                    text: [label],
                    font: {
                        size: 20
                    },
                },
                annotation: {
                    annotations: [
                        {
                            type: 'line',
                            scaleID: 'y',
                            value: criticalLevel, // Критический уровень
                            borderColor: criticalLevel2 === 0 ? 'red' : 'orange',
                            borderWidth: 5,
                            label: {
                                content: `${criticalLevel} м, объем ${criticalLevelVolume2} м³`,
                                enabled: true,
                                position: 'center',
                                yAdjust: -20
                            }
                        },
                        ...(criticalLevel2 !== 0 ? [{
                            type: 'line',
                            scaleID: 'y',
                            value: criticalLevel2, // Критический уровень
                            borderColor: 'red',
                            borderWidth: 5,
                            label: {
                                content: `крит. уровень ${criticalLevel2} м, объем ${criticalLevelVolume} м³`,
                                enabled: true,
                                position: 'center',
                                yAdjust: 20,
                            }
                        }] : [])
                    ]
                }
            }
        }
    });
}

function updateTime(elementId1, elementId2, volume, offset1, offset2) {
    let element1 = document.getElementById(elementId1);
    let element2 = document.getElementById(elementId2);

    if (element1) {
        let totalHours1 = ((volume * 1000 - offset1) * 3 / 2275);
        let hours1 = Math.floor(totalHours1);
        let minutes1 = Math.floor((totalHours1 - hours1) * 60);
        element1.textContent = hours1 + " час " + minutes1 + " минут";
        }
    if (element2){
        let totalHours2 = ((volume * 1000 - offset2) * 3 / 2275);
        let hours2 = Math.floor(totalHours2);
        let minutes2 = Math.floor((totalHours2 - hours2) * 60);
        element2.textContent = hours2 + " час " + minutes2 + " минут";
    }
}