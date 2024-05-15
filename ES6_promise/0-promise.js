function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Response from API");
    }, 1000); 
  });
}

export default getResponseFromAPI;

