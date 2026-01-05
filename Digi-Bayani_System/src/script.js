document.addEventListener('DOMContentLoaded', function() {
    const tweetInput = document.getElementById('tweetInput');
    const classifyBtn = document.getElementById('classifyBtn');
    const resultSection = document.getElementById('resultSection');
    const resultContent = document.getElementById('resultContent');
    const errorSection = document.getElementById('errorSection');
    const errorMessage = document.getElementById('errorMessage');
    const btnText = document.querySelector('.btn-text');
    const spinner = document.querySelector('.spinner');

    classifyBtn.addEventListener('click', async function() {
        const tweetText = tweetInput.value.trim();

        // Clear previous results
        resultSection.style.display = 'none';
        errorSection.style.display = 'none';

        // Validate input
        if (!tweetText) {
            showError('Please enter a tweet to classify.');
            return;
        }

        // Show loading state
        classifyBtn.disabled = true;
        btnText.style.display = 'none';
        spinner.style.display = 'inline';

        try {
            // Send request to Flask backend
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ tweet: tweetText })
            });

            const data = await response.json();

            if (response.ok) {
                showResult(data.prediction, tweetText);
            } else {
                showError(data.error || 'An error occurred during classification.');
            }
        } catch (error) {
            showError('Failed to connect to the server. Make sure the Flask backend is running on port 5000.');
            console.error('Error:', error);
        } finally {
            // Reset button state
            classifyBtn.disabled = false;
            btnText.style.display = 'inline';
            spinner.style.display = 'none';
        }
    });

    function showResult(prediction, originalTweet) {
        resultContent.innerHTML = `
            <div class="result-card">
                <div class="result-label">
                    <strong>Original Tweet:</strong>
                    <p class="tweet-text">${escapeHtml(originalTweet)}</p>
                </div>
                <div class="prediction-box ${getPredictionClass(prediction)}">
                    <div class="prediction-label">Informativeness Level</div>
                    <div class="prediction-value">${escapeHtml(prediction)}</div>
                </div>
                <div class="prediction-description">
                    ${getPredictionDescription(prediction)}
                </div>
            </div>
        `;
        resultSection.style.display = 'block';
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorSection.style.display = 'block';
        errorSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function getPredictionClass(prediction) {
        const pred = prediction.toLowerCase();
        if (pred.includes('high') || pred.includes('informative')) {
            return 'high-info';
        } else if (pred.includes('low') || pred.includes('not informative')) {
            return 'low-info';
        } else {
            return 'medium-info';
        }
    }

    function getPredictionDescription(prediction) {
        const pred = prediction.toLowerCase();
        if (pred.includes('high') || pred.includes('informative')) {
            return '<p>✅ This tweet contains valuable information about typhoons/floods.</p>';
        } else if (pred.includes('low') || pred.includes('not informative')) {
            return '<p>ℹ️ This tweet has limited informational value about typhoons/floods.</p>';
        } else {
            return '<p>📊 Classification complete.</p>';
        }
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Allow Enter key to submit (with Shift+Enter for new line)
    tweetInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            classifyBtn.click();
        }
    });
});
