async function fetchData() {
    const projectDescription = document.getElementById('project_description').value;
    const model = document.getElementById('model').value;
    const topK = parseInt(document.getElementById('top_k').value, 10);

    // Constructing the request payload
    const payload = {
        project_description: projectDescription,
        model: model,
        top_k: topK
    };

    try {
        // Fetching data from the API
        const response = await fetch('http://127.0.0.1:8000/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        // Clearing previous results

        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';

        // Dynamically creating and appending elements for each result
        data.results.forEach((result, index) => {
            const resultElement = document.createElement('div');
            resultElement.innerHTML = `
            <div class="max-w-3xl mx-auto bg-gray-800 text-white p-4 my-4 rounded-lg shadow-lg">
                <div class="flex justify-between items-start mb-2">
                    <h3 class="text-xl font-semibold">${result.project.title}</h3>
                    <p class="text-gray-400">Comparison score: ${result.comparison.score}</p>
                </div>
                <p class="mb-4">${result.comparison.summary}</p>
                <details class="bg-gray-700 p-3 rounded">
                    <summary class="font-semibold cursor-pointer hover:text-blue-400">Details</summary>
                    <div class="text-gray-300 space-y-2 mt-2">
                        <p><strong>Similarity:</strong> ${result.comparison.similarity}</p>
                        <p><strong>Difference:</strong> ${result.comparison.difference}</p>
                        <p><strong>Score reasoning:</strong> ${result.comparison.reason}</p>
                        <p><strong>Vector similarity:</strong> ${result.project.score}</p>
                        <p><strong>Original objective:</strong> ${result.project.objective}</p>
                    </div>
                </details>
            </div> 
    `;
            resultsContainer.appendChild(resultElement);
        });
    } catch (error) {
        console.error('Error fetching data: ', error);
        document.getElementById('results').textContent = 'Failed to fetch data.';
    }
}
