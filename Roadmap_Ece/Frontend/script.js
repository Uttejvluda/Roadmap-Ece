const API_BASE = "http://127.0.0.1:5000/api";

const rolesContainer = document.getElementById("rolesContainer");
const searchInput = document.getElementById("searchInput");
const domainFilter = document.getElementById("domainFilter");
const searchBtn = document.getElementById("searchBtn");

async function loadRoles() {
  const search = searchInput.value.trim();
  const domain = domainFilter.value;

  let url = `${API_BASE}/roles?domain=${domain}`;
  if (search) url += `&search=${search}`;

  const res = await fetch(url);
  const roles = await res.json();

  rolesContainer.innerHTML = "";

  if (roles.length === 0) {
    rolesContainer.innerHTML = `<p style="text-align:center;">No roles found ❌</p>`;
    return;
  }

  roles.forEach(role => {
    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `
      <h2>${role.title}</h2>
      <p><b>Domain:</b> ${role.domain}</p>
      <p>${role.description}</p>
      <a href="role.html?id=${role.id}">View Roadmap →</a>
    `;
    rolesContainer.appendChild(div);
  });
}

searchBtn.addEventListener("click", loadRoles);
window.addEventListener("load", loadRoles);
