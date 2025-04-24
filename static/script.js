
function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar');
  const clearBtn = document.getElementById('clearBtn');
  const h2 = sidebar.querySelector('h2');
  const historyItems = sidebar.querySelectorAll('.history-item');
  const toggleBtn = document.getElementById('sidebarToggleBtn');

  const isCollapsed = sidebar.classList.toggle('collapsed');
  sidebar.style.width = isCollapsed ? '0' : '250px';
  document.getElementById('arrowIcon').textContent = isCollapsed ? '❯' : '❮';
  h2.style.display = isCollapsed ? 'none' : 'block';
  clearBtn.style.display = isCollapsed ? 'none' : 'block';
  historyItems.forEach(item => item.style.display = isCollapsed ? 'none' : 'block');
  toggleBtn.setAttribute('aria-expanded', !isCollapsed);
}

function toggleProfileMenu() {
  const menu = document.getElementById("profileMenu");
  menu.classList.toggle("show");
  menu.style.display = menu.classList.contains("show") ? "flex" : "none";
}

function showProfileModal() {
  const menu = document.getElementById('profileMenu');
  menu.style.display = 'none';
  menu.classList.remove('show');
  document.getElementById('profileModal').style.display = 'block';
  document.body.classList.add('modal-open');
}

function showSettingsModal() {
  const menu = document.getElementById('profileMenu');
  menu.style.display = 'none';
  menu.classList.remove('show');
  document.getElementById('settingsModal').style.display = 'block';
  document.body.classList.add('modal-open');
}

function sendFeedback() {
  const menu = document.getElementById('profileMenu');
  menu.style.display = 'none';
  menu.classList.remove('show');
  document.getElementById('feedbackModal').style.display = 'block';
  document.body.classList.add('modal-open');
}

function submitFeedback(event) {
  if (event) event.stopPropagation();
  const feedbackInput = document.getElementById('feedbackInput');
  const feedback = feedbackInput.value.trim();
  if (!feedback) return showToast("Please write something!");
  fetch('/submit_feedback', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ feedback })
  }).then(res => res.json())
    .then(() => {
      showToast("🙏 Thanks for your feedback!");
      feedbackInput.value = '';
      closeFeedback();
    });
}

function closeFeedback(event) {
  if (event) event.stopPropagation();
  document.getElementById('feedbackModal').style.display = 'none';
  document.body.classList.add('modal-open');
}

function backToDropdown(event) {
  if (event) event.stopPropagation();

  // Hide all modals
  const modals = ['profileModal', 'settingsModal', 'feedbackModal'];
  modals.forEach(id => {
    const modal = document.getElementById(id);
    if (modal) modal.style.display = 'none';
  });

  // Show dropdown menu
  const menu = document.getElementById('profileMenu');
  menu.style.display = 'flex';
  menu.classList.add('show');

  // Remove modal-open state
  document.body.classList.remove('modal-open');
}

function surpriseMe() {
  fetch('/surprise')
    .then(res => res.json())
    .then(tool => {
      const chatBox = document.getElementById('chatBox');
      const bubble = `
        <div class="message-row bot">
          <div class="avatar">🤖</div>
          <div class="chat-bubble">
            🎁 <strong>Surprise Tool:</strong><br><br>
            <strong>Name:</strong> ${tool.name}<br>
            <strong>Description:</strong> ${tool.description}<br>
            <strong>URL:</strong> <a href="${tool.url}" target="_blank">🔗 Visit</a>
          </div>
        </div>
      `;
      chatBox.insertAdjacentHTML('beforeend', bubble);
      chatBox.scrollTop = chatBox.scrollHeight;
    });
}


function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.style.display = 'none';
  document.body.classList.remove('modal-open');
}

function setTheme(mode) {
  const body = document.body;
  body.classList.remove('chatgpt-mode', 'dark-mode');
  if (mode === 'chatgpt') body.classList.add('chatgpt-mode');
  else if (mode === 'dark') body.classList.add('dark-mode');
}

function toggleTheme() {
  const body = document.body;
  const isChatGPT = body.classList.contains('chatgpt-mode');
  const isDark = body.classList.contains('dark-mode');
  if (!isChatGPT && !isDark) body.classList.add('chatgpt-mode');
  else if (isChatGPT) {
    body.classList.remove('chatgpt-mode');
    body.classList.add('dark-mode');
  } else {
    body.classList.remove('dark-mode');
  }
}

function loadSidebarHistory() {
  fetch('/get_history')
    .then(res => res.json())
    .then(data => {
      const historyList = document.getElementById('historyList');
      historyList.innerHTML = '';
      const seen = new Set();
      data.forEach(chat => {
        const msg = chat.user_message.trim();
        if (msg && !seen.has(msg)) {
          seen.add(msg);
          const li = document.createElement('li');
          li.className = 'history-item';
          li.textContent = msg.length > 30 ? msg.slice(0, 30) + '...' : msg;
          li.title = msg;
          li.onclick = () => {
            const bubbles = document.querySelectorAll('.chat-bubble');
            for (let bubble of bubbles) {
              if (bubble.textContent.trim().startsWith(msg)) {
                bubble.scrollIntoView({ behavior: 'smooth', block: 'center' });
                bubble.style.boxShadow = '0 0 12px #7c4dff';
                setTimeout(() => bubble.style.boxShadow = 'none', 1500);
                break;
              }
            }
          };
          historyList.appendChild(li);
        }
      });
    });
}

function clearHistory() {
  fetch('/clear_history', { method: 'POST' })
    .then(res => res.json())
    .then(data => {
      if (data.status === 'success') {
        document.getElementById('historyList').innerHTML = '';
        showToast("Chat history cleared!");
      }
    });
}

function showToast(message) {
  const toast = document.createElement('div');
  toast.textContent = message;
  toast.style.position = 'fixed';
  toast.style.top = '20px';
  toast.style.left = '50%';
  toast.style.transform = 'translateX(-50%)';
  toast.style.color = 'white';
  toast.style.padding = '10px 20px';
  toast.style.borderRadius = '12px';
  toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.2)';
  toast.style.zIndex = '9999';
  toast.style.opacity = '0';
  toast.style.transition = 'opacity 0.3s ease-in-out';
  toast.style.background = '#7c4dff';
  document.body.appendChild(toast);
  requestAnimationFrame(() => toast.style.opacity = '1');
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 2000);
}

function askBot() {
  const input = document.getElementById('promptInput');
  const prompt = input.value.trim();
  if (!prompt) return;
  const chatBox = document.getElementById('chatBox');
  const userMsgWrap = document.createElement('div');
  userMsgWrap.className = 'message-row user';
  userMsgWrap.innerHTML = `<div class="avatar">👤</div><div class="chat-bubble">${prompt}</div>`;
  chatBox.appendChild(userMsgWrap);
  chatBox.scrollTop = chatBox.scrollHeight;
  input.value = '';
  const typingRow = document.createElement('div');
  typingRow.className = 'message-row bot';
  typingRow.id = 'typingRow';
  typingRow.innerHTML = `<div class="avatar">🤖</div><div class="chat-bubble">assistAIve is typing<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></div>`;
  chatBox.appendChild(typingRow);
  chatBox.scrollTop = chatBox.scrollHeight;
  fetch('/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  }).then(res => res.json())
    .then(data => {
      document.getElementById('typingRow')?.remove();
      data.forEach(tool => {
        const botMsgWrap = document.createElement('div');
        botMsgWrap.className = 'message-row bot';
        botMsgWrap.innerHTML = `<div class="avatar">🤖</div><div class="chat-bubble"><strong>assistAIve:</strong><br><br><strong>Name:</strong> ${tool.name}<br><br><strong>Description:</strong> ${tool.description}<br><br><strong>URL:</strong> <a href="${tool.url}" target="_blank">🔗 Visit</a></div>`;
        chatBox.appendChild(botMsgWrap);
        chatBox.scrollTop = chatBox.scrollHeight;
      });
      loadSidebarHistory();
    });
}

function handleKey(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    askBot();
  }
}

function showAdminActivities() {
  fetch('/admin/activities')
    .then(res => res.json())
    .then(data => {
      document.getElementById('adminActivitiesSection').style.display = 'block';
      document.getElementById('adminFeedbackSection').style.display = 'none';
      document.getElementById('chatBox').style.display = 'none';
      document.querySelector('.input-area').style.display = 'none';
      document.getElementById("profileMenu").style.display = "none";
      const tableBody = document.getElementById('chatActivityBody');
      tableBody.innerHTML = "";
      if (data.chats.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="5">No activity yet.</td></tr>`;
      } else {
        data.chats.forEach(chat => {
          tableBody.innerHTML += `<tr><td>${chat.username}</td><td>${chat.email}</td><td>${chat.message}</td><td>${chat.response}</td><td>${new Date(chat.timestamp).toUTCString()}</td></tr>`;
        });
      }
    });
}

function showAdminFeedback() {
  if (window.sessionRole !== 'admin') return;
  document.getElementById('chatBox').style.display = 'none';
  document.querySelector('.input-area').style.display = 'none';
  document.getElementById('adminActivitiesSection').style.display = 'none';
  document.getElementById('adminFeedbackSection').style.display = 'block';
  document.getElementById("profileMenu").style.display = "none";
  fetch('/get_feedback')
    .then(res => res.json())
    .then(data => {
      const tbody = document.getElementById('adminFeedbackBody');
      tbody.innerHTML = "";
      data.forEach(item => {
        tbody.innerHTML += `<tr><td>${item.id}</td><td>${item.name || "—"}</td><td>${item.user_email}</td><td>${item.message}</td><td>${item.submitted_at}</td></tr>`;
      });
    });
}

function returnToChat() {
  document.getElementById('chatBox').style.display = 'block';
  document.querySelector('.input-area').style.display = 'flex';
  document.getElementById('adminFeedbackSection').style.display = 'none';
  document.getElementById('adminActivitiesSection').style.display = 'none';
}

document.addEventListener("click", function (event) {
  const profile = document.querySelector(".user-profile");
  const dropdown = document.getElementById("profileMenu");
  const feedbackModal = document.getElementById("feedbackModal");
  const settingsModal = document.getElementById("settingsModal");
  const profileModal = document.getElementById("profileModal");

  const isClickInsideDropdown = profile.contains(event.target) || dropdown.contains(event.target);
  const isClickInsideModal = feedbackModal?.contains(event.target) || settingsModal?.contains(event.target) || profileModal?.contains(event.target);

  if (!isClickInsideDropdown && !isClickInsideModal) {
    dropdown.classList.remove("show");
    dropdown.style.display = "none";
  }
});

window.onload = () => {
  loadSidebarHistory();
  fetch('/get_user_role')
    .then(res => res.json())
    .then(data => {
      window.sessionRole = data.role;
    });
};
