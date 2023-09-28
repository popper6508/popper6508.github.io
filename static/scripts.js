const apiKeyInput = document.getElementById('api-key-input');
const topicInput = document.getElementById('topic-input');
const numChapterInput = document.getElementById('num-chapter-input');
const makeForWhoInput = document.getElementById('make-for-who-input');
const generateButton = document.getElementById('generate-button');

// Add event listener to the Generate Book button
generateButton.addEventListener('click', () => {
  // Get the input values
  const apiKey = apiKeyInput.value;
  const topic = topicInput.value;
  const numChapter = numChapterInput.value;
  const makeForWho = makeForWhoInput.value;

  // Call the generate_pdf function with the input values
  gpt_for_book(apiKey, topic, numChapter, makeForWho);
});

function gpt_for_book(apiKey, topic, numChapter, makeForWho) {
  // Make the necessary API calls or perform any other logic here
  // You can use the apiKey, topic, numChapter, and makeForWho variables to make the API call

  // Example output
  const chapters = ['Chapter 1', 'Chapter 2', 'Chapter 3'];
  const books = ['Book 1', 'Book 2', 'Book 3'];

  // Display the result or perform further actions with the chapters and books data
  console.log(chapters);
  console.log(books);
}