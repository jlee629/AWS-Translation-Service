const serverUrl = "http://127.0.0.1:8000";

async function displayHeadlines() {
    try {
        const response = await fetch(`${serverUrl}/news`);
        if (!response.ok) {
            throw new Error('Failed to retrieve headlines.');
        }
        const data = await response.json();

        const headlines = document.getElementById('headlines');
        if (data.headlines && data.headlines.length > 0) {
            const headlinesHTML = data.headlines.map((headline, index) => `
                <div class="headline">
                    <p><strong>Headline ${index + 1}</strong></p>
                    <p>Original Text: ${headline.original_text}</p>
                    <p>Translated Text: ${headline.translated_text}</p>
                </div>
            `).join('');

            headlines.innerHTML = headlinesHTML;
        } else {
            headlines.innerHTML = '<p>No headlines found.</p>';
        }
    } catch (error) {
        console.error('Failed to display headlines:', error);
        document.getElementById('headlines').innerHTML = '<p>Error display headlines.</p>';
    }
}

document.addEventListener('DOMContentLoaded', displayHeadlines);
