const apiKey = "pub_58294d7dd9146c79712185714243c955c82c7";
const baseUrl = "https://newsdata.io/api/1/news";

async function fetchNews() {
    const languages = Array.from(document.getElementById("language-select").selectedOptions).map(option => option.value);
    const newsContainer = document.getElementById("news-container");
    newsContainer.innerHTML = ""; // Clear previous results

    if (languages.length === 0) {
        newsContainer.innerHTML = "<p>Please select at least one language.</p>";
        return;
    }

    for (let language of languages) {
        try {
            const response = await fetch(`${baseUrl}?apikey=${apiKey}&language=${language}&country=in`);
            const data = await response.json();

            if (data.results && data.results.length > 0) {
                const languageTitle = document.createElement("h2");
                languageTitle.textContent = `Top News in ${language}`;
                newsContainer.appendChild(languageTitle);

                data.results.forEach(article => {
                    const newsItem = document.createElement("div");
                    newsItem.classList.add("news-item");

                    const title = document.createElement("h3");
                    title.textContent = article.title;
                    newsItem.appendChild(title);

                    const description = document.createElement("p");
                    description.textContent = article.description || "No description available.";
                    newsItem.appendChild(description);

                    const link = document.createElement("a");
                    link.href = article.link;
                    link.textContent = "Read more";
                    link.target = "_blank";
                    newsItem.appendChild(link);

                    newsContainer.appendChild(newsItem);
                });
            } else {
                newsContainer.innerHTML += `<p>No news articles available for language: ${language}</p>`;
            }
        } catch (error) {
            console.error("Error fetching news:", error);
            newsContainer.innerHTML += `<p>Failed to fetch news for language: ${language}</p>`;
        }
    }
}
