def returnJs(scoreList: dict):
    score = {}
    averageScore = 0
    averageRank = ''

    for s in scoreList:
        replyScore = s['replyScore']

        for key, value in s.items():
            if key == 'replyScore':
                continue
            elif key in score.keys():
                score[key][0] += replyScore * value
                score[key][1] += value
            else:
                score[key] = [replyScore * value, value]
    
    for key in score.keys():
        score[key][0] /= score[key][1]
        averageScore += score[key][0]

    averageScore /= len(score)
    averageScore = round(averageScore)

    if averageScore == 100:
        averageRank = 'S+'
    elif averageScore >= 90:
        averageRank = 'S'
    elif averageScore >= 80:
        averageRank = 'A+'
    elif averageScore >= 70:
        averageRank = 'A'
    elif averageScore >= 60:
        averageRank = 'B+'
    elif averageScore >= 50:
        averageRank = 'B'
    elif averageScore >= 40:
        averageRank = 'C+'
    elif averageScore >= 30:
        averageRank = 'C'
    elif averageScore >= 20:
        averageRank = 'D+'
    elif averageScore >= 10:
        averageRank = 'D'
    else:
        averageRank = 'F'

    result = """
<script type="text/javascript" src="https://fastly.jsdelivr.net/npm/echarts@5.3.3/dist/echarts.min.js"></script>
<script type="text/javascript">
    var radarDom = parent.document.getElementById('radar');
    var radarChart = echarts.init(radarDom, null, {
    renderer: 'canvas',
    useDirtyRect: false
    });
    
    var radarOption;

    radarOption = {
        color: [
            '#5595e8'
        ],
        textStyle: {
            fontFamily: 'Open Sans',
            fontSize: 14,
            color: '#587cac',
            fontStyle: 'normal',
            fontWeight: 'normal'
        },
        radar: {
            // shape: 'circle',
            indicator: ["""

    for i, key in enumerate(score.keys()):
        if key == 'replyScore':
            continue

        result += """
            { name: '""" + key + """', max: 100 }"""
        
        if i != len(score):
            result += ","

    result += """
                ]
        },
        series: [
            {
            type: 'radar',
            data: [
                {
                value: ["""

    for i, key in enumerate(score.keys()):
        if key == 'replyScore':
            continue

        result += str(score[key][0])

        if i != len(scoreList) - 1:
            result += ","

    result += """],
                name: 'Score'
                }
            ]
            }
        ]
    };

    var gaugeDom = parent.document.getElementById('gauge');
    var gaugeChart = echarts.init(gaugeDom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    
    var gaugeOption;

    gaugeOption = {
        series: [
            {
            type: 'gauge',
            startAngle: 180,
            endAngle: 0,
            min: 0,
            max: 100,
            radius: '100%',
            center: ["50%", "65%"],
            splitNumber: 10,
            axisLine: {
                lineStyle: {
                width: 6,
                color: [
                    [0.1, '#9e0142'],
                    [0.2, '#d53e4f'],
                    [0.3, '#f46d43'],
                    [0.4, '#fdae61'],
                    [0.5, '#fee08b'],
                    [0.6, '#e6f598'],
                    [0.7, '#abdda4'],
                    [0.8, '#66c2a5'],
                    [0.9, '#3288bd'],
                    [1.0, '#5e4fa2']
                ]
                }
            },
            pointer: {
                icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
                length: '12%',
                width: 20,
                offsetCenter: [0, '-60%'],
                itemStyle: {
                color: 'auto'
                }
            },
            axisTick: {
                length: 12,
                lineStyle: {
                color: 'auto',
                width: 2
                }
            },
            splitLine: {
                length: 20,
                lineStyle: {
                color: 'auto',
                width: 5
                }
            },
            axisLabel: {
                color: '#464646',
                fontSize: 20,
                distance: -65,
                formatter: function (value) {
                if (value === 100) {
                    return 'S+';
                } else if (value === 90) {
                    return 'S ';
                } else if (value === 80) {
                    return 'A+';
                } else if (value === 70) {
                    return 'A ';
                } else if (value === 60) {
                    return 'B+';
                } else if (value === 50) {
                    return 'B ';
                } else if (value === 40) {
                    return 'C+';
                } else if (value === 30) {
                    return 'C ';
                } else if (value === 20) {
                    return 'D+';
                } else if (value === 10) {
                    return 'D ';
                } else if (value === 0) {
                    return 'F ';
                }
                return '';
                }
            },
            title: {
                offsetCenter: [0, '-20%'],
                fontSize: 100,
                valueAnimation: true,
                color: 'auto'
            },
            detail: {
                fontSize: 40,
                offsetCenter: [0, '40%'],
                valueAnimation: true,
                formatter: function (value) {
                return Math.round(value) + ' Points';
                },
                color: 'auto'
            },
            data: [
                {
                value: """ + str(averageScore) + """,
                name: '""" + averageRank + """'
                }
            ]
            }
        ],
        title: {
            text: 'Grade Rating',
            left: 'center',
            top: '71%',
            textStyle: {
            fontSize: 20
            }
        }
    };

    if (gaugeOption && typeof gaugeOption === 'object') {
        gaugeChart.setOption(gaugeOption);
    }
    if (radarOption && typeof radarOption === 'object') {
        radarChart.setOption(radarOption);
    }

    parent.window.addEventListener('resize', gaugeChart.resize);
    parent.window.addEventListener('resize', radarChart.resize);
</script>"""

    return result