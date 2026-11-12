function fetchWithTimeout(url, timeout) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(
      () => reject(new Error("Request timed out")),
      timeout
    );

    fetch(url)
      .then(response => response.json())
      .then(data => {
        clearTimeout(timer);
        resolve(data);
      })
      .catch(error => {
        clearTimeout(timer);
        console.log("Request failed:", error);
        reject(error);
      });
  });
}

fetchWithTimeout("https://example.com/data", 2000)
  .then(data => console.log(data))
  .catch(error => console.error(error));
