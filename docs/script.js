const { get } = require("express/lib/response");

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
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';
        const getResultsButton = document.getElementById('get_results');
        getResultsButton.disabled = true;
        getResultsButton.classList.add('opacity-50', 'cursor-not-allowed');
        // DISABLE BUTTON
        getResultsButton.innerHTML = `
        <div class="flex items-center justify-center space-x-4 py-1">
            <div class="w-3 h-3 bg-gray-100 rounded-full animate-bounce shadow-md shadow-gray-400"></div>
            <div class="w-3 h-3 bg-gray-200 rounded-full animate-bounce200 shadow-md shadow-gray-400"></div>
            <div class="w-3 h-3 bg-gray-300 rounded-full animate-bounce400 shadow-md shadow-gray-400"></div>
        </div>
        <style>
        @keyframes bounce {
            0%, 100% {
            transform: translateY(-25%);
            animation-timing-function: cubic-bezier(0.8,0,1,1);
            }
            50% {
            transform: translateY(0);
            animation-timing-function: cubic-bezier(0,0,0.2,1);
            }
        }
        .animate-bounce {
            animation: bounce 1s infinite;
        }
        .animate-bounce200 {
            animation: bounce 1s infinite 200ms;
        }
        .animate-bounce400 {
            animation: bounce 1s infinite 400ms;
        }
        </style>
        `;
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
            getResultsButton.disabled = false;
            getResultsButton.classList.remove('opacity-50', 'cursor-not-allowed');
            getResultsButton.innerHTML = 'Get Results';
            resultsContainer.innerHTML = 'Error fetching data. Please try again.';
        }
        const data = await response.json();
        getResultsButton.disabled = false;
        getResultsButton.classList.remove('opacity-50', 'cursor-not-allowed');
        getResultsButton.innerHTML = 'Get Results';


        // Dynamically creating and appending elements for each result
        data.results.forEach((result, index) => {
            const resultElement = document.createElement('div');
            resultElement.innerHTML = `
            <div class="max-w-4xl mx-auto bg-gray-800 text-white p-4 my-4 rounded-lg shadow-lg">
                <div class="flex justify-between items-start mb-4">
                    <h3 style="width: 70%;" class="text-xl font-semibold">${result.project.title}</h3>
                    <div style="width: 25%;" class="bg-gray-700 rounded-full h-2.5">
                        <div class="bg-blue-500 h-2.5 rounded-full" style="width: ${Math.max(result.comparison.score, 5)}%;"></div>
                        <p class="text-center text-sm text-gray-500">${result.comparison.score}/100</p>
                    </div>
                </div>
                <p class="mb-4">${result.comparison.summary}</p>
                <details class="bg-gray-800 p-4 rounded-lg shadow-md">
                    <summary class="font-semibold cursor-pointer hover:bg-gray-700 text-lg rounded-md p-2 transition-colors duration-300 ease-in-out">
                        Details
                    </summary>
                <div class="text-gray-300 mt-4 space-y-3">
                    <div class="p-3 bg-gray-700 rounded-lg">
                        <span class="font-semibold block mb-2">Similarity</span>
                        <div class="p-2 bg-gray-600 rounded">${result.comparison.similarity}</div>
                    </div>
                    <div class="p-3 bg-gray-700 rounded-lg">
                        <span class="font-semibold block mb-2">Difference</span>
                        <div class="p-2 bg-gray-600 rounded">${result.comparison.difference}</div>
                    </div>
                    <div class="p-3 bg-gray-700 rounded-lg">
                        <span class="font-semibold block mb-2">Score reasoning</span>
                        <div class="p-2 bg-gray-600 rounded">${result.comparison.reason}</div>
                    </div>
                    <div class="p-3 bg-gray-700 rounded-lg">
                        <span class="font-semibold block mb-2">Original objective</span>
                        <div class="p-2 bg-gray-600 rounded">${result.project.objective}</div>
                    </div>
                    <div class="p-3 bg-gray-700 rounded-lg">
                        <span class="font-semibold block mb-2">Vector similarity</span>
                        <div class="p-2 bg-gray-600 rounded">${result.project.score}</div>
                    </div>
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
