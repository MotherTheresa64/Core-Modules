const toggleBtn = document.getElementById("toggle-btn");
let toggled = false;

toggleBtn.addEventListener("click", function () {
  const title = document.getElementById("title");
  const desc = document.querySelector(".description");

  if (!toggled) {
    title.textContent = "New Title";
    desc.textContent = "This is the new description.";
    toggleBtn.textContent = "Revert Content";
  } else {
    title.textContent = "Original Title";
    desc.textContent = "This is the original description.";
    toggleBtn.textContent = "Change Content";
  }

  toggled = !toggled;
});

/*
Expected HTML:
<h1 id="title">Original Title</h1>
<p class="description">This is the original description.</p>
<button id="toggle-btn">Change Content</button>
<script src="dom_toggle_content.js"></script>
*/
