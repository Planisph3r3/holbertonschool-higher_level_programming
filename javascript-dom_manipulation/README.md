## DOM Manipulation in JavaScript

DOM manipulation means using JavaScript to change how a webpage looks and behaves. With it, we can make websites more interactive and dynamic.

### Why it's Important:

- **Interactivity**: We can make elements on a webpage respond to user actions like clicks or typing.
- **Updating Content**: JavaScript can add, remove, or change elements on the page without needing to reload.
- **Handling Events**: We can make things happen when users interact with the page, like showing a popup when a button is clicked.
- **Binding Data**: JavaScript can connect data to parts of the webpage, so when the data changes, the page updates too.

### Example:

```javascript
// Find a button with an ID 'update_header'
const button = document.querySelector('#update_header');

// When the button is clicked, change the header text
button.addEventListener("click", function() {
    const header = document.querySelector('header');
    header.textContent = "New Header Text";
});
