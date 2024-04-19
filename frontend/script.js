const API_PATH = "http://ashley-ajax-clustering.westeurope.azurecontainer.io:8000/"
                    

document.addEventListener("DOMContentLoaded", function() {
    const runButton = document.getElementById("run-button");
    const dropdown = document.getElementById("endpoint-dropdown");
    const resultDisplay = document.querySelector(".result-display .big-number");
    const plotContainer = document.querySelector(".plot-container");

    runButton.addEventListener("click", function() {
        const scoreEndpoint = API_PATH + dropdown.value + "/score";
        const plotEndpoint = API_PATH + dropdown.value + "/plot";
        if (scoreEndpoint && plotEndpoint) {
            fetch(scoreEndpoint)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const roundedResult = data.result.toFixed(3);
                    resultDisplay.textContent = roundedResult;
                    // Fetch and display plot image
                    fetch(plotEndpoint)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.blob();
                        })
                        .then(blob => {
                            const imageURL = URL.createObjectURL(blob);
                            const imgElement = document.createElement('img');
                            imgElement.src = imageURL;
                            plotContainer.innerHTML = '';
                            plotContainer.appendChild(imgElement);
                        })
                        .catch(error => console.error('Error:', error));
                })
                .catch(error => console.error('Error:', error));
        }
    });
});