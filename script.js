document.getElementById('scanForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const urlInput = document.getElementById('urlInput').value;
    const scanBtn = document.getElementById('scanBtn');
    const resultsSection = document.getElementById('resultsSection');
    
    // UI Loading State
    scanBtn.innerText = "Analyzing...";
    scanBtn.disabled = true;

    try {
        // Send request to FastAPI backend
        const response = await fetch('http://127.0.0.1:8000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: urlInput })
        });

        if (!response.ok) {
            throw new Error('Network response failure.');
        }

        const data = await response.json();
        
        // Render Output Results
        document.getElementById('targetUrlDisplay').innerText = data.url;
        document.getElementById('timestamp').innerText = `TIMESTAMP: ${data.scanned_at}`;
        document.getElementById('scoreNumber').innerText = data.risk_score;
        
        const verdictText = document.getElementById('verdictText');
        verdictText.innerText = data.verdict;
        
        // Reset dynamic indicator colors
        verdictText.className = "verdict-banner"; 
        if(data.verdict === "Safe") {
            verdictText.classList.add('safe');
        } else if(data.verdict === "Suspicious") {
            verdictText.classList.add('suspicious');
        } else {
            verdictText.classList.add('dangerous');
        }

        // Build Diagnostic Flags UI
        const flagsList = document.getElementById('flagsList');
        flagsList.innerHTML = ""; // Clear old rules

        for (const [flagName, triggered] of Object.entries(data.details)) {
            const li = document.createElement('li');
            li.innerHTML = `
                <span>${flagName}</span>
                <span class="status-flag ${triggered ? 'dangerous' : 'safe'}">
                    ${triggered ? '⚠️ FAIL' : '✓ CLEAN'}
                </span>
            `;
            flagsList.appendChild(li);
        }

        // Unhide the analysis layout
        resultsSection.classList.remove('hidden');

    } catch (error) {
        alert("Could not connect to scanner core. Make sure backend is active!");
        console.error(error);
    } finally {
        scanBtn.innerText = "Execute Scan";
        scanBtn.disabled = false;
    }
});