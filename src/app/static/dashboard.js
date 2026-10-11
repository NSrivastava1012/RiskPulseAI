async function loadDashboard() {

    const summaryResponse = await fetch("/api/summary");
    const summary = await summaryResponse.json();

    const stressResponse = await fetch("/api/stress-test");
    const stressData = await stressResponse.json();

    const signalsResponse = await fetch("/api/risk-signals");
    const signals = await signalsResponse.json();

    const eventsResponse =
        await fetch("/api/top-risk-events");

    const topRiskEvents =
        await eventsResponse.json();


    // -------------------------
    // SUMMARY
    // -------------------------

    document.getElementById("portfolio-value").textContent =
        formatMoney(summary.total_portfolio_value);

    document.getElementById("stress-loss").textContent =
        formatMoney(summary.estimated_stress_loss);

    document.getElementById("stressed-value").textContent =
        formatMoney(summary.stressed_portfolio_value);

    document.getElementById("loss-percent").textContent =
        summary.portfolio_loss_percentage.toFixed(2) + "%";


    // -------------------------
    // RISK COUNTS
    // -------------------------

    const counts = {
        Critical: 0,
        High: 0,
        Medium: 0,
        Low: 0
    };

    signals.forEach(signal => {
        if (counts[signal.risk_level] !== undefined) {
            counts[signal.risk_level]++;
        }
    });

    document.getElementById("critical-count").textContent = counts.Critical;
    document.getElementById("high-count").textContent = counts.High;
    document.getElementById("medium-count").textContent = counts.Medium;
    document.getElementById("low-count").textContent = counts.Low;

    const totalSignals = signals.length;

    setBar("critical-bar", counts.Critical, totalSignals);
    setBar("high-bar", counts.High, totalSignals);
    setBar("medium-bar", counts.Medium, totalSignals);
    setBar("low-bar", counts.Low, totalSignals);


    // -------------------------
    // EXPOSURE
    // -------------------------

    const exposureContainer =
        document.getElementById("exposure-container");

    const maxLoss = Math.max(
        ...stressData.map(item => item.estimated_loss)
    );

    stressData.forEach(item => {

        const percentage =
            (item.estimated_loss / maxLoss) * 100;

        const div = document.createElement("div");

        div.className = "exposure-item";

        div.innerHTML = `
            <div class="exposure-header">
                <span>${item.company}</span>
                <strong>${formatMoney(item.estimated_loss)}</strong>
            </div>

            <div class="exposure-bar">
                <div
                    class="exposure-fill"
                    style="width: ${percentage}%">
                </div>
            </div>
        `;

        exposureContainer.appendChild(div);
    });

    // -------------------------
    // TOP RISK DRIVERS
    // -------------------------

    const riskDrivers =
        document.getElementById("risk-drivers");

    const sortedRiskData = [...stressData]
        .sort(
            (a, b) =>
                b.estimated_loss - a.estimated_loss
        );

    sortedRiskData.forEach((item, index) => {

        const div = document.createElement("div");

        div.className = "risk-driver";

        div.innerHTML = `
            <div class="risk-driver-rank">
                ${index + 1}
            </div>

            <div class="risk-driver-info">
                <strong>${item.company}</strong>

                <span>
                    ${item.risk_level} risk
                    • ${item.maximum_impact}/10 impact
                </span>
            </div>

            <div class="risk-driver-loss">
                ${formatMoney(item.estimated_loss)}
            </div>
        `;

        riskDrivers.appendChild(div);
    });

    // -------------------------
    // RISK EXPLANATIONS
    // -------------------------

    const explanationContainer =
        document.getElementById("risk-explanations");

    topRiskEvents.forEach(event => {

        const evidence =
            event.event_evidence
                ? event.event_evidence
                : "Detected from financial signal";

        const div = document.createElement("div");

        div.className = "risk-explanation";

        div.innerHTML = `
            <div class="explanation-company">
                <strong>${event.company}</strong>

                <span class="badge ${riskClass(event.risk_level)}">
                    ${event.risk_level}
                </span>
            </div>

            <div class="explanation-content">

                <div>
                    <span class="explanation-label">
                        Trigger Event
                    </span>

                    <strong>
                        ${event.event_type}
                    </strong>
                </div>

                <div>
                    <span class="explanation-label">
                        Impact
                    </span>

                    <strong>
                        ${event.impact_score}/10
                    </strong>
                </div>

                <div>
                    <span class="explanation-label">
                        Sentiment
                    </span>

                    <strong class="${
                        event.sentiment_score < 0
                            ? "negative"
                            : "positive"
                    }">
                        ${Number(event.sentiment_score).toFixed(3)}
                    </strong>
                </div>

                <div>
                    <span class="explanation-label">
                        Evidence
                    </span>

                    <strong>
                        ${evidence}
                    </strong>
                </div>

            </div>
        `;

        explanationContainer.appendChild(div);
    });

    // -------------------------
    // STRESS TABLE
    // -------------------------

    const stressTable =
        document.getElementById("stress-table");

    stressData.forEach(item => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${item.company}</td>
            <td>${item.asset_type}</td>
            <td>${formatMoney(item.value)}</td>

            <td>
                <span class="badge ${riskClass(item.risk_level)}">
                    ${item.risk_level}
                </span>
            </td>

            <td>${(item.shock_rate * 100).toFixed(0)}%</td>

            <td class="negative">
                ${formatMoney(item.estimated_loss)}
            </td>

            <td>
                ${formatMoney(item.stressed_value)}
            </td>
        `;

        stressTable.appendChild(row);
    });


    // -------------------------
    // SIGNAL TABLE
    // -------------------------

    const signalsTable =
        document.getElementById("signals-table");

    signals.forEach(signal => {

        const row = document.createElement("tr");

        const sentimentClass =
            signal.sentiment_score < 0
                ? "negative"
                : "positive";

        row.innerHTML = `
            <td>${signal.company}</td>

            <td>${signal.data_source}</td>

            <td>${signal.event_type}</td>

            <td class="${sentimentClass}">
                ${signal.sentiment_score.toFixed(3)}
            </td>

            <td>
                ${signal.impact_score}/10
            </td>

            <td>
                <span class="badge ${riskClass(signal.risk_level)}">
                    ${signal.risk_level}
                </span>
            </td>
        `;

        signalsTable.appendChild(row);
    });
}


function formatMoney(value) {

    return "$" + Number(value).toLocaleString(
        "en-US",
        {
            maximumFractionDigits: 0
        }
    );
}


function setBar(id, count, total) {

    const percentage =
        total === 0 ? 0 : (count / total) * 100;

    document.getElementById(id).style.width =
        percentage + "%";
}


function riskClass(level) {

    return "badge-" + level.toLowerCase();
}


loadDashboard();