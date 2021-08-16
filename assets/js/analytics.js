var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: '',
    data: {
        labels: ['personal_loans_value', 'personal_loans_payments', 'personal_loans_profit', 'group_loans_value', 'group_loans_payments', 'group_loans_profit'],
        datasets: [{
            label: '# Loan Data 2021 # Amounts in KES',
            data: [
              {% for item in loan_values %}
                  {{item}},
              {% endfor %}
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});