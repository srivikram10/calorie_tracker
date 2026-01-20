document.getElementById("intakeForm").onsubmit = async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    const response = await fetch("/add_intake", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("alert").innerText = data.message;

    loadGraphs();
};

async function loadGraphs() {
    const res = await fetch("/graph_data");
    const data = await res.json();

    drawChart("dailyChart", data.daily, "Daily Calories");
    drawChart("weeklyChart", data.weekly, "Weekly Calories");
    drawChart("monthlyChart", data.monthly, "Monthly Calories");
}

function drawChart(canvasId, data, label) {
    const ctx = document.getElementById(canvasId).getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: data.map(d => d[0]),
            datasets: [{
                label: label,
                data: data.map(d => d[1]),
                borderWidth: 2
            }]
        }
    });
}

loadGraphs();
