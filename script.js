function getRecommendations() {
    const talkContent = document.getElementById("talkInput").value;

    if (talkContent.trim() === "") {
        alert("Please enter a TED talk description.");
        return;
    }

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ talkContent: talkContent })
    })
    .then(response => response.json())
    .then(data => {
        const recommendationsDiv = document.getElementById("recommendations");
        recommendationsDiv.innerHTML = "<h2>Recommended TED Talks:</h2>";

        if (data.recommendations.length === 0) {
            recommendationsDiv.innerHTML += "<p>No recommendations found.</p>";
        } else {
            data.recommendations.forEach(talk => {
                recommendationsDiv.innerHTML += `<p><strong>${talk.main_speaker}</strong>: ${talk.details}</p>`;
            });
        }
    })
    .catch(error => console.error("Error:", error));
}
