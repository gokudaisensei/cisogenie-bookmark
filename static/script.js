const API_BASE = "http://localhost:8000/api";
let token = "";

function showResponse(id, data) {
  document.getElementById(id).innerText =
    typeof data === "string" ? data : JSON.stringify(data, null, 2);
}

async function register() {
  const email = document.getElementById("reg-email").value;
  const password = document.getElementById("reg-password").value;

  const res = await fetch(`${API_BASE}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  const data = await res.json();
  showResponse("register-response", data);
}

async function login() {
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  const data = await res.json();
  token = data.access_token;
  showResponse("login-response", data);
}

async function getBookmarks() {
  const res = await fetch(`${API_BASE}/bookmarks/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  const data = await res.json();
  showResponse("bookmarks-response", data);
}

async function createBookmark() {
  const url = document.getElementById("bm-url").value;
  const title = document.getElementById("bm-title").value;
  const description = document.getElementById("bm-description").value;
  const category = document.getElementById("bm-category").value;

  const res = await fetch(`${API_BASE}/bookmarks/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ url, title, description, category }),
  });

  const data = await res.json();
  showResponse("create-response", data);
}

async function updateBookmark() {
  const id = document.getElementById("update-id").value;
  const title = document.getElementById("update-title").value;
  const description = document.getElementById("update-description").value;
  const category = document.getElementById("update-category").value;

  const res = await fetch(`${API_BASE}/bookmarks/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ title, description, category }),
  });

  const data = await res.json();
  showResponse("update-response", data);
}

async function deleteBookmark() {
  const id = document.getElementById("delete-id").value;

  const res = await fetch(`${API_BASE}/bookmarks/${id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });

  showResponse(
    "delete-response",
    res.status === 204 ? "Deleted successfully" : await res.json(),
  );
}
