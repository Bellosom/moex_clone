const futuresData = {
    indices: [
        {code: 'MXI', name: 'Индекс МосБиржи (мини)'},
        {code: 'MIX', name: 'Индекс МосБиржи'},
        {code: 'RTS', name: 'Индекс РТС'},
        {code: 'IMOEXF', name: 'пролонг. Индекс МосБиржи'},
        {code: 'RTSM', name: 'Индекс РТС (мини)'},
        {code: 'RGBI', name: 'Индекс RGBI'},
        {code: 'IPO', name: 'Индекс МосБиржи IPO'},
        {code: 'HOME', name: 'Индекс московской недвижимости ДомКлик'},
        {code: 'OGI', name: 'Индекс Нефти и газа'},
        {code: 'CNI', name: 'Индекс Потреб. сектора'},
        {code: 'FNI', name: 'Индекс Финансов'},
        {code: 'MMI', name: 'Индекс Металлов и добычи'}
    ],
    stocks: [
        {code: 'SBRF', name: 'Сбер'},
        {code: 'GAZR', name: 'Газпром'},
        {code: 'ROSN', name: 'Роснефть'},
        {code: 'AFKS', name: 'АФК Система'},
        {code: 'AFLT', name: 'Аэрофлот'},
        {code: 'ALIBABA', name: 'Алибаба (Деп.расп.)'},
        {code: 'ALRS', name: 'АЛРОСА'},
        {code: 'ASTR', name: 'Астра'},
        {code: 'BAIDU', name: 'Байду (Деп.расп.)'},
        {code: 'BANE', name: 'Башнефть'},
        {code: 'BSPB', name: 'Банк «Санкт-Петербург»'},
        {code: 'CBOM', name: 'МОСКОВСКИЙ КРЕДИТНЫЙ БАНК'},
        {code: 'CHMF', name: 'Северсталь'},
        {code: 'FEES', name: 'ФСК-Россети'},
        {code: 'FESH', name: 'ДВМП'},
        {code: 'FLOT', name: 'Совкомфлот'},
        {code: 'GMKN', name: 'ГМК Норильский никель'},
        {code: 'HYDR', name: 'РусГидро'},
        {code: 'IRAO', name: 'Интер РАО ЕЭС'},
        {code: 'ISKJ', name: 'Артген'},
        {code: 'KMAZ', name: 'КАМАЗ'},
        {code: 'LEAS', name: 'ЛК Европлан'},
        {code: 'LKOH', name: 'ЛУКОЙЛ'},
        {code: 'MAGN', name: 'ММК'},
        {code: 'MGNT', name: 'Магнит'},
        {code: 'MOEX', name: 'ПАО Московская Биржа'},
        {code: 'MTLR', name: 'Мечел'},
        {code: 'MTSI', name: 'МТС'},
        {code: 'MVID', name: 'М.видео'},
        {code: 'NLMK', name: 'НЛМК'},
        {code: 'NOTK', name: 'НОВАТЭК'},
        {code: 'PHOR', name: 'ФосАгро'},
        {code: 'PIKK', name: 'ПИК СЗ'},
        {code: 'PLZL', name: 'Полюс'},
        {code: 'POLY', name: 'Полиметалл'},
        {code: 'POSI', name: 'Группа Позитив'},
        {code: 'RNFT', name: 'РуссНефть'},
        {code: 'RTKM', name: 'Ростелеком'},
        {code: 'RUAL', name: 'РУСАЛ'},
        {code: 'SBPR', name: 'Сбер (прив.)'},
        {code: 'SGZH', name: 'Сегежа Групп'},
        {code: 'SIBN', name: 'Газпром нефть'},
        {code: 'SMLT', name: 'Самолет'},
        {code: 'SNGP', name: 'Сургутнефтегаз (прив.)'},
        {code: 'SNGR', name: 'Сургутнефтегаз'},
        {code: 'SOFL', name: 'Софтлайн'},
        {code: 'SPBE', name: 'СПБ Биржа'},
        {code: 'SVCB', name: 'Совкомбанк'},
        {code: 'TATN', name: 'Татнефть'},
        {code: 'TATP', name: 'Татнефть (прив.)'},
        {code: 'TCSI', name: 'ТКС Холдинг'},
        {code: 'TRNF', name: 'Транснефть'},
        {code: 'VKCO', name: 'ВК'},
        {code: 'VTBR', name: 'Банк ВТБ'},
        {code: 'WUSH', name: 'ВУШ Холдинг'},
        {code: 'YDEX', name: 'ЯНДЕКС'}
    ],
    currencies: [
        {code: 'CNY', name: 'CNY/RUB'},
        {code: 'CNYRUBF', name: 'CNY/RUB (пролонг.)'},
        {code: 'Si', name: 'USD/RUB'},
        {code: 'Eu', name: 'EUR/RUB'},
        {code: 'USDRUBF', name: 'USD/RUB (пролонг.)'},
        {code: 'ED', name: 'EUR/USD'},
        {code: 'UCNY', name: 'USD/CNY'},
        {code: 'EURRUBF', name: 'EUR/RUB (пролонг.)'},
        {code: 'TRY', name: 'TRY/RUB'},
        {code: 'HKD', name: 'HKD/RUB'},
        {code: 'UCHF', name: 'CHF/RUB'},
        {code: 'GBPU', name: 'GBP/RUB'},
        {code: 'AUDU', name: 'AUD/RUB'},
        {code: 'UJPY', name: 'JPY/RUB'},
        {code: 'AED', name: 'AED/RUB'},
        {code: 'AMD', name: 'AMD/RUB'},
        {code: 'BYN', name: 'BYN/RUB'},
        {code: 'UCAD', name: 'CAD/RUB'},
        {code: 'ECAD', name: 'EUR/CAD'},
        {code: 'EGBP', name: 'EUR/GBP'},
        {code: 'EJPY', name: 'EUR/JPY'},
        {code: 'INR', name: 'INR/RUB'},
        {code: 'KZT', name: 'KZT/RUB'},
        {code: 'UKZT', name: 'USD/KZT'}
    ],
    commodities: [
        {code: 'NG', name: 'Природный газ'},
        {code: 'BR', name: 'нефть Brent'},
        {code: 'SILV', name: 'Серебро'},
        {code: 'GOLD', name: 'Золото в дол. США'},
        {code: 'GLDRUBF', name: 'пролонг. Золото в руб.'},
        {code: 'GL', name: 'Золото в руб за грамм'},
        {code: 'PLT', name: 'Платина'},
        {code: 'PLD', name: 'Палладий'},
        {code: 'WHEAT', name: 'Индекс российской пшеницы CPT Новороссийск'},
        {code: 'SUGR', name: 'Сахар-сырец'},
        {code: 'SUGAR', name: 'Сахар'},
        {code: 'Co', name: 'Медь'},
        {code: 'ALMN', name: 'Алюминий'},
        {code: 'Nl', name: 'Никель'},
        {code: 'Zn', name: 'Цинк'}
    ],
    others: [
        {code: 'SPYF', name: 'Инвест.паи SPY ETF Trust'},
        {code: 'NASD', name: 'Инвест.паи Invesco QQQ ETF Trust Unit Series 1'},
        {code: 'DJ30', name: 'Инвест.паи DJ Industrial Average ETF Trust'},
        {code: 'DAX', name: 'Инвест.паи iShares Core DAX UCITS ETF (DE)'},
        {code: 'RVI', name: 'Волатильность российского рынка'},
        {code: 'EM', name: 'Акции инвестфонда iShares MSCI Emerging Markets ETF'},
        {code: 'R2000', name: 'Акции инвестфонда iShares Russell 2000 ETF'},
        {code: 'STOX', name: 'Акции инвестфонда iShares Core EURO STOXX 50 UCITS ETF EUR (Dist)'},
        {code: 'NIKK', name: 'Акции инвестфонда iShares Core Nikkei 225 ETF'},
        {code: 'HANG', name: 'Акции инвестфонда Tracker Fund of Hong Kong ETF'},
        {code: 'RUON', name: 'Ставка однодневных кредитов RUONIA'},
        {code: '1MFR', name: 'Ставка RUSFAR'}
    ]
};


function showFutures(category) {
    const container = document.getElementById('futures-container');
    container.innerHTML = '';

    if (futuresData[category]) {
        futuresData[category].forEach(future => {
            const button = document.createElement('button');
            button.textContent = future.name; // Display name
            button.dataset.code = future.code; // Store code in a data attribute
            button.onclick = () => {
                selectFuture(future.code); // Use code for further processing
            };
            container.appendChild(button);
        });
    }
}

function selectFuture(futureCode) {
    document.getElementById('chart-buttons').innerHTML = ''; // Clear previous buttons
    document.getElementById('field-5-3').style.display = 'block'; // Show type selection

    // Store the selected future code globally
    window.selectedFutureCode = futureCode;
    console.log(`Selected future code: ${window.selectedFutureCode}`); // Fixed string interpolation

    // Hide the no-data-message and show the chart
    document.getElementById('no-data-message').style.display = 'none';
    loadChart(futureCode, 1); // Load initial chart data (you might need to adjust this depending on your requirements)
}

function showOptions(personType) {
    const chartButtons = document.getElementById('chart-buttons');
    chartButtons.innerHTML = ''; // Clear existing buttons
    document.getElementById('field-5-4').style.display = 'block'; // Show option selection

    const options = personType === 'physical'
        ? ['Чистая позиция объема покупок/продаж', 'Открытый интерес', 'Чистое количество покупателей/продавцов', 'Количество длинных/коротких позиций']
        : ['Чистая позиция объема покупок/продаж', 'Открытый интерес', 'Чистое количество покупателей/продавцов', 'Количество длинных/коротких позиций'];

    options.forEach((option, index) => {
        const button = document.createElement('button');
        button.textContent = option;
        button.onclick = () => {
            const futureCode = window.selectedFutureCode;
            loadChart(futureCode, personType === 'physical' ? index + 5 : index + 1); // Load chart based on selection
        };
        chartButtons.appendChild(button);
    });
}

const chartCache = {};  // Cache to store fetched chart data

function loadChart(futureCode, chartNumber) {
    const cacheKey = `${futureCode}-${chartNumber}`; // Fixed template literal syntax

    // Check if data is in cache
    if (chartCache[cacheKey]) {
        renderChart(chartCache[cacheKey]);  // Use cached data
    } else {
        // Fetch data from server if not cached
        fetch(`/api/get_chart_data?futureCode=${encodeURIComponent(futureCode)}&chartNumber=${chartNumber}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                chartCache[cacheKey] = data;  // Cache the data
                renderChart(data);  // Render chart with the data
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }
}

function renderChart(data) {
    const canvas = document.getElementById('myChart');
    
    if (!canvas) {
        console.error('Canvas element with id "myChart" not found.');
        return;
    }

    const ctx = canvas.getContext('2d');

    // Уничтожаем предыдущий график, если он существует
    if (window.myChart && typeof window.myChart.destroy === 'function') {
        window.myChart.destroy();
    }

    // Создаем массив данных для графика
    const datasets = [{
        label: data.label,
        data: data.values,
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
        yAxisID: 'y'
    }];

    if (data.values2) {
        datasets.push({
            label: `${data.label} - Secondary`,
            data: data.values2,
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2,
            yAxisID: 'y'
        });
    }

    // Создаем график
    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: datasets.map(dataset => ({
                ...dataset,
                pointRadius: 0,
                pointHoverRadius: 0
            }))
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'month',
                        tooltipFormat: 'MMMM yyyy',
                        displayFormats: {
                            month: 'MMMM yyyy'
                        }
                    },
                    title: {
                        display: true,
                    },
                    adapters: {
                        date: {
                            locale: window.ru // Используем импортированную локаль
                        }
                    }
                },
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                    },
                    ticks: {
                        callback: function(value) {
                            return value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}