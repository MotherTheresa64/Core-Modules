// Create a new paragraph element
const newParagraph = document.createElement("p");
newParagraph.textContent = "This is a new paragraph!";
document.body.appendChild(newParagraph);

// Remove an element with ID 'remove-me' if it exists
const toRemove = document.getElementById("remove-me");
if (toRemove) {
  toRemove.remove();
}

/*
Expected HTML:
<p id="remove-me">This will be removed dynamically.</p>
<script src="dom_create_remove_elements.js"></script>
*/
