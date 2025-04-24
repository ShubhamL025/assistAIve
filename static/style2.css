
    body {
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #3b2c97, #7554d9);
      color: #fff;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .main-container {
      display: flex;
      height: 90vh;
      width: 90vw;
      max-width: 1200px;
      border-radius: 20px;
      overflow: hidden;
      background: #f3e8ff;
      box-shadow: 0 0 35px rgba(0, 0, 0, 0.1);
    }

    .sidebar {
  width: 250px;
  background: #e7d6ff;
  padding: 20px 10px;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: width 0.3s ease;
  position: relative;
}

.sidebar h2 {
  margin: 20px 0;
  font-size: 20px;
  color: #5e35b1;
  text-align: center;
}

 
.sidebar-content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  height: 100%;
}

.sidebar-inner {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  height: 100%;
  padding: 10px 8px 0 8px;  
}


.sidebar.collapsed {
  width: 0;
}

 
.history-scroll {
  flex-grow: 1;
  overflow-y: auto;
  margin-bottom: 0;
  padding-bottom: 8px;

   
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.1) transparent;
}

.history-scroll::-webkit-scrollbar {
  width: 6px;
}

.history-scroll::-webkit-scrollbar-track {
  background: transparent;
}

.history-scroll::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  transition: background 0.3s ease;
}

.history-scroll::-webkit-scrollbar-thumb:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.history-list {
  margin-top: 10px;
  gap: 12px;
  display: flex;
  flex-direction: column;
  list-style: none;  
  padding-left: 0;   
  margin: 0;
}

.history-item {
  margin-bottom: 10px;  
  padding: 12px 16px;
}


#clearBtn {
  background: #7c4dff;
  color: white;
  font-weight: bold;
  padding: 10px 24px;
  font-size: 14px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  transition: background 0.25s ease, transform 0.25s ease;
  width: 90%;
  max-width: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  box-shadow: none;  
}


#clearBtn:hover {
  background: #5e35b1;
  transform: scale(1.03);
  box-shadow: none;  
}



.clear-button-wrapper {
  position: sticky;
  bottom: 0;
  background: #e7d6ff;
  padding: 16px 0 20px;  
  display: flex;
  justify-content: center;
}

body.chatgpt-mode .clear-button-wrapper {
  background: #f5f5f5;
}

 
body.dark-mode .clear-button-wrapper {
  background: #232323;
}

    .sidebar-toggle {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 24px;
  background: #7c4dff;
  border: none;
  border-radius: 10px;
  color: #fff;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.3s;
}

body.chatgpt-mode .sidebar-toggle {
  background: #444;
  color: #fff;
}

body.dark-mode .sidebar-toggle {
  background: #555;
  color: #fff;
}

 
.sidebar.collapsed {
  overflow: hidden;
  transition: width 0.3s ease;
}

 
.sidebar + .sidebar-navigator {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

 
.main-container {
  position: relative;  
  display: flex;
  flex-direction: row;
}


 
.sidebar-navigator {
  position: absolute;
  top: 20px;  
  left: 250px;  
  width: 36px;
  height: 36px;
  background: #7c4dff;
  border-radius: 50%;  
  border: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  font-size: 18px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: left 0.3s ease, transform 0.3s ease;
  z-index: 10;
  transform: translateY(0);
  padding: 4px
  
}

 
.sidebar.collapsed ~ .sidebar-navigator {
  left:6px;
}


.sidebar.collapsed .sidebar-navigator {
  right: -16px;
}
.sidebar-navigator:hover {
  background: #5e35b1;
}



.sidebar-navigator:hover {
  background: #5e35b1;
}

body.chatgpt-mode .sidebar-navigator {
  background: #444;
  color: white;
}

body.dark-mode .sidebar-navigator {
  background: #555;
  color: white;
}

body.chatgpt-mode .sidebar-navigator:hover {
  background: #666;
}

body.dark-mode .sidebar-navigator:hover {
  background: #777;
}

#arrowIcon {
  transition: transform 0.3s ease;
  display: inline-block;
}

.sidebar.collapsed #arrowIcon {
  transform: rotate(180deg);
}


.sidebar h2,
#clearBtn,
.history-item {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.sidebar.collapsed h2,
.sidebar.collapsed #clearBtn,
.sidebar.collapsed .history-item {
  opacity: 0;
  transform: translateX(-10px);
  pointer-events: none;
}

.history-item:hover {
  background: #e5d1ff;
  transform: translateX(4px);
  transition: all 0.2s ease;
}


    .history-list::-webkit-scrollbar {
      width: 6px;
    }

    .history-list::-webkit-scrollbar-thumb {
      background-color: #7c4dff;
      border-radius: 10px;
    }

    .history-item {
      background: #fff;
      padding: 10px 15px;
      border-radius: 12px;
      margin-bottom: 10px;
      color: #5e35b1;
      font-weight: bold;
      cursor: pointer;
    }

    .chat-container {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      padding: 25px;
      background: #fff;
      border-radius: 0 20px 20px 0;
      position: relative;
    }

    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 26px;
      font-weight: bold;
      color: #5e35b1;
      margin-bottom: 15px;
    }


    .user-profile {
      position: relative;
      display: inline-block;
      background: #ded1ff;
      padding: 6px 12px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 500;
      color: #333;
      cursor: pointer;
    }


    .chat-box {
      flex-grow: 1;
      overflow-y: auto;
      padding: 12px;
      margin-bottom: 15px;
      border: 1px solid #ddd;
      border-radius: 16px;
      background: #f3e8ff;
      display: flex;
      flex-direction: column;
    }

    .message-row {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      margin: 6px 0;
    }

    .message-row.user {
      flex-direction: row-reverse;
    }

    .avatar {
      font-size: 22px;
      margin-top: 4px;
    }

    .chat-bubble {
      padding: 12px;
      border-radius: 16px;
      max-width: 75%;
      word-wrap: break-word;
      animation: slideIn 0.3s ease-in-out;
    }

    .message-row.bot .chat-bubble {
      background: #7c4dff;
      color: white;
    }

    .message-row.user .chat-bubble {
      background: #ded1ff;
      color: #333;
    }

    .input-area {
      display: flex;
    }

    .input-area input {
      flex-grow: 1;
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 12px 0 0 12px;
      outline: none;
      font-size: 15px;
      background: #f3e8ff;
    }

    .input-area button {
      background: #7c4dff;
      color: white;
      padding: 12px 24px;
      border: none;
      border-radius: 0 12px 12px 0;
      cursor: pointer;
      font-size: 15px;
      font-weight: bold;
    }

    .profile-dropdown {
      display: none;
      flex-direction: column;
      position: absolute;
      top: 38px;
      right: 0;
      background: rgba(255, 255, 255, 0.3);
      backdrop-filter: blur(15px);
      -webkit-backdrop-filter: blur(15px);
      border-radius: 16px;
      box-shadow: 0 10px 35px rgba(0, 0, 0, 0.2);
      min-width: 180px;
      border: 1px solid rgba(255, 255, 255, 0.25);
      transition: all 0.25s ease;
      opacity: 0;
      pointer-events: none;
      transform: translateY(-6px);
      z-index: 1000;
      padding: 8px 0;  
      transition: transform 0.25s ease, opacity 0.25s ease;
    }

    .profile-dropdown.show {
      display: flex;
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }

    .profile-dropdown a {
      display: block;
      padding: 10px 20px;
      font-size: 14px;
      font-weight: 500;
      color: #333;
      text-decoration: none;
      transition: all 0.25s ease;
    }

    .profile-dropdown a:hover {
      background-color: rgba(124, 77, 255, 0.12);
      color: #5e35b1;
      border-radius: 12px;
      margin: 0 8px;  
      transform: translateX(6px);
    }

    .profile-dropdown hr {
      margin: 6px 0;
      border: none;
      border-top: 1px solid rgba(255, 255, 255, 0.3);
    }

    .profile-dropdown a:hover .icon {
      transform: scale(1.1) rotate(2deg);
      transition: transform 0.3s ease;
    }

    .profile-dropdown.show {
  opacity: 0;
  transform: translateY(-10px);
  animation: dropdownFadeIn 0.3s ease forwards;
}

@keyframes dropdownFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


     
    body:not(.chatgpt-mode):not(.dark-mode) #clearBtn {
      background: #7c4dff;
      color: white;
    }
    body:not(.chatgpt-mode):not(.dark-mode) #clearBtn:hover {
      background: #5e35b1;
    }

    body:not(.chatgpt-mode):not(.dark-mode) .input-area button:hover {
  background: #5e35b1;
  transform: scale(1.03);
  box-shadow: 0 2px 10px rgba(124, 77, 255, 0.3);
}


     
    body.chatgpt-mode #clearBtn {
      background: #333;
      color: white;
    }
    body.chatgpt-mode #clearBtn:hover {
      background: #444;
    }

     
    body.dark-mode #clearBtn {
      background: #555;
      color: white;
    }
    body.dark-mode #clearBtn:hover {
      background: #666;
    }




     
     
    body.chatgpt-mode {
  background: #eeeeee;
  color: #212121;
}

body.chatgpt-mode .main-container {
  background: #fafafa;
}

body.chatgpt-mode .sidebar {
  background: #f5f5f5;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.05);
}

body.chatgpt-mode .sidebar h2 {
  color: #333;
}

body.chatgpt-mode .sidebar-toggle {
  background: #444;
  color: #fff;
}

body.chatgpt-mode .history-item {
  background: #e0e0e0;
  color: #222;
  border-radius: 12px;
  font-weight: 600;
  transition: background 0.2s ease;
}

body.chatgpt-mode .history-item:hover {
  background: #d5d5d5;
  cursor: pointer;
}

body.chatgpt-mode .chat-container {
  background: #ffffff;
}

body.chatgpt-mode .chat-box {
  background: #fdfdfd;
  border-color: #dcdcdc;
}

body.chatgpt-mode .input-area input {
  background: #f5f5f5;
  color: #000;
  border-color: #ccc;
}

body.chatgpt-mode .input-area button {
  background: #333;
  color: #fff;
}

body.chatgpt-mode .input-area button:hover {
  background: #444;
  transform: scale(1.03);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}


body.chatgpt-mode .header,
body.chatgpt-mode .user-profile,
body.chatgpt-mode .chat-bubble,
body.chatgpt-mode .profile-dropdown {
  background: #fff;
  color: #000;
}

body.chatgpt-mode .message-row.bot .chat-bubble {
  background: #e6e6e6;
  color: #000;
}

body.chatgpt-mode .message-row.user .chat-bubble {
  background: #dcdcdc;
  color: #000;
}

body.chatgpt-mode .chat-bubble a {
  color: #1a73e8;
}

body.chatgpt-mode .profile-dropdown a {
  color: #000;
}

body.chatgpt-mode .profile-dropdown a:hover {
  background: rgba(0, 0, 0, 0.05);
  color: #1a73e8;
}

 
body.dark-mode {
  background: #1e1e1e;
  color: #f5f5f5;
}

body.dark-mode .main-container {
  background: #2c2c2c;
}

body.dark-mode .sidebar {
  background: #232323;
}

body.dark-mode .sidebar h2 {
  color: #fff;
}

body.dark-mode .sidebar-toggle {
  background: #555;
  color: #fff;
}

body.dark-mode .history-item {
  background: #3a3a3a;
  color: #fff;
}

body.dark-mode .history-list::-webkit-scrollbar-thumb {
  background-color: #666;
}

body.dark-mode .chat-container {
  background: #2a2a2a;
}

body.dark-mode .chat-box {
  background: #1e1e1e;
  border-color: #444;
}

body.dark-mode .input-area input {
  background: #333;
  color: #fff;
  border-color: #555;
}

body.dark-mode .input-area button {
  background: #555;
  color: #fff;
  font-weight: bold;
  border: 1px solid #555;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  transition: background 0.3s ease, transform 0.2s ease;
}

body.dark-mode .input-area button:hover {
  background: #555;
  transform: scale(1.03);
  box-shadow: 0 6px 14px rgba(0,0,0,0.3);
}


body.dark-mode .header,
body.dark-mode .user-profile,
body.dark-mode .chat-bubble,
body.dark-mode .profile-dropdown {
  background: #2b2b2b;
  color: #fff;
}

body.dark-mode .message-row.bot .chat-bubble {
  background: #3c3c3c;
  color: #fff;
}

body.dark-mode .message-row.user .chat-bubble {
  background: #3c3c3c;
  color: #fff;
}

body.dark-mode .chat-bubble a {
  color: #90caf9;
}

body.dark-mode .profile-dropdown a {
  color: #fff;
}

body.dark-mode .profile-dropdown a:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #90caf9;
}

.admin-section + .sidebar-navigator {
  top: 20px;
}

 
.history-list::-webkit-scrollbar-thumb {
  background-color: #7c4dff;
}

 
body.chatgpt-mode .history-list::-webkit-scrollbar-thumb {
  background-color: #bbb;
}

#profileBackBtn {
  position: absolute;
  top: 14px;
  left: 16px;
  background: transparent;
  border: none;
  color: #7c4dff;
  font-size: 18px;
  cursor: pointer;
  font-weight: bold;
  transition: transform 0.2s ease;
}

body.chatgpt-mode #profileBackBtn {
  color: #333;
}
body.dark-mode #profileBackBtn {
  color: #eee;
}

#profileBackBtn:hover {
  transform: translateX(-3px);
}




.profile-details {
  padding-left: 48px;  
  padding-right: 12px;
}

.profile-title {
  margin-top: 0;
  font-size: 18px;
  color: #5e35b1;
  font-weight: bold;
  margin-left: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.profile-icon {
  color: #5e35b1;
}

 
body.chatgpt-mode .profile-title,
body.chatgpt-mode .profile-icon {
  color: #333;
}

 
body.dark-mode .profile-title,
body.dark-mode .profile-icon {
  color: #90caf9;
}

.themeBtn {
  padding: 6px 12px;
  border: none;
  border-radius: 12px;
  color: white;
  font-weight: 600;
  cursor: pointer;
  font-size: 13px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
}

.themeBtn:hover {
  transform: scale(1.05);
}

.themeBtn.classic {
  background: #fff;
  color: #000;
  border: 1px solid #333;
}

.themeBtn.classic:hover {
  background: #f2f2f2;
  transform: scale(1.05);
}

 
body {
  margin: 0;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #3b2c97, #7554d9);
  color: #fff;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-container {
  display: flex;
  height: 90vh;
  width: 90vw;
  max-width: 1200px;
  border-radius: 20px;
  overflow: hidden;
  background: #f3e8ff;
  box-shadow: 0 0 35px rgba(0, 0, 0, 0.1);
  position: relative;
}

 
.sidebar {
  width: 250px;
  background: #e7d6ff;
  padding: 20px 10px;
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: width 0.3s ease;
  position: relative;
}

.sidebar h2 {
  text-align: center;
  font-size: 20px;
  color: #5e35b1;
  margin-bottom: 14px;
}

.sidebar.collapsed {
  width: 0;
  overflow: hidden;
}

.history-scroll {
  flex-grow: 1;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.1) transparent;
}

.history-scroll::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.history-item {
  background: #fff;
  padding: 10px 15px;
  border-radius: 12px;
  margin-bottom: 10px;
  color: #5e35b1;
  font-weight: bold;
  cursor: pointer;
}

.history-item:hover {
  background: #e5d1ff;
  transform: translateX(4px);
  transition: all 0.2s ease;
}

.clear-button-wrapper {
  position: sticky;
  bottom: 0;
  background: #e7d6ff;
  padding: 12px;
  display: flex;
  justify-content: center;
}

#clearBtn {
  background: #7c4dff;
  color: white;
  font-weight: bold;
  padding: 10px 24px;
  font-size: 14px;
  border: none;
  border-radius: 14px;
  width: 90%;
  max-width: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: background 0.25s ease, transform 0.25s ease;
}

 
.sidebar-navigator {
  position: absolute;
  top: 20px;
  left: 250px;
  width: 36px;
  height: 36px;
  background: #7c4dff;
  border-radius: 50%;
  font-size: 18px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: left 0.3s ease;
  z-index: 10;
}

.sidebar.collapsed ~ .sidebar-navigator {
  left: 6px;
}

 
.chat-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  padding: 25px;
  background: #fff;
  border-radius: 0 20px 20px 0;
  position: relative;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 26px;
  font-weight: bold;
  color: #5e35b1;
  margin-bottom: 15px;
}

.input-area {
  display: flex;
  margin-top: 10px;
}

.input-area input {
  flex-grow: 1;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 12px 0 0 12px;
  background: #f3e8ff;
  font-size: 15px;
}

.input-area button {
  background: #7c4dff;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 0 12px 12px 0;
  cursor: pointer;
  font-weight: bold;
}

 
.modal-box {
  position: absolute;
  top: 65px;
  right: 20px;
  width: 300px;
  padding: 24px 20px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(124, 77, 255, 0.2);
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

#profileBackBtn,
#settingsBackBtn {
  position: absolute;
  top: 14px;
  left: 10px;
  font-size: 18px;
  font-weight: bold;
  background: transparent;
  border: none;
  color: #7c4dff;
  cursor: pointer;
  transition: transform 0.2s ease;
}

#profileBackBtn:hover,
#settingsBackBtn:hover {
  transform: translateX(-4px);
}

 
.admin-section {
  padding: 20px;
  margin-top: 30px;
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  color: #333;
}

.admin-section h3 {
  font-size: 20px;
  font-weight: bold;
  color: #5e35b1;
  margin-bottom: 20px;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
}

.admin-table th, .admin-table td {
  text-align: left;
  padding: 12px;
  border-bottom: 1px solid #e0e0e0;
  font-size: 14px;
}

.admin-table th {
  background-color: #7c4dff;
  color: #fff;
  position: sticky;
  top: 0;
  z-index: 1;
}


 
body.chatgpt-mode #profileBackBtn,
body.chatgpt-mode #settingsBackBtn {
  color: #333;
}
body.chatgpt-mode .modal-box {
  background: #f1f1f1;
  color: #111;
}
body.chatgpt-mode .admin-table td,
body.chatgpt-mode .admin-table th {
  background: #f9f9f9;
  color: #222;
  border-color: #ccc;
}

 
body.dark-mode #profileBackBtn,
body.dark-mode #settingsBackBtn {
  color: #ccc;
}
body.dark-mode .modal-box {
  background: #1f1f1f;
  color: #eee;
}
body.dark-mode .admin-table td,
body.dark-mode .admin-table th {
  background: #2c2c2c;
  color: #eee;
  border-color: #444;
}

 
#adminFeedbackSection {
  padding: 30px 25px;
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  margin-top: 24px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}

#adminFeedbackSection h3 {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 18px;
  color: #5e35b1;
}

 
#adminFeedbackSection .admin-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #ffffff;
  color: #333;
  font-size: 14px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  border-collapse: separate;       
  border-spacing: 0;  
}

#adminFeedbackSection .admin-table thead {
  background-color: #7c4dff;
  color: #fff;
}

#adminFeedbackSection .admin-table th,
#adminFeedbackSection .admin-table td {
  padding: 12px 16px;
  border: 1px solid #ddd;
  text-align: left;
  vertical-align: top;
  word-break: break-word;
}

 
#adminFeedbackSection .table-wrapper {
  max-height: 400px;
  overflow-y: auto;
  border-radius: 12px;
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.05);
}

 
#adminFeedbackSection .table-wrapper::-webkit-scrollbar {
  width: 8px;
}
#adminFeedbackSection .table-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(124, 77, 255, 0.4);
  border-radius: 4px;
}

#adminFeedbackSection .table-wrapper {
  max-height: 360px;   
  overflow-y: auto;
  border-radius: 12px;
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.05);
}

 
#adminFeedbackSection .table-wrapper::-webkit-scrollbar {
  width: 8px;
}
#adminFeedbackSection .table-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(124, 77, 255, 0.4);
  border-radius: 4px;
}

 
.table-wrapper {
  max-height: 380px;
  overflow-y: auto;
  overflow-x: auto;
  padding-right: 10px;
  margin-top: 10px;
  border-radius: 12px;
}

 
.table-wrapper::-webkit-scrollbar {
  width: 6px;
}
.table-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(128, 128, 128, 0.4);
  border-radius: 6px;
}

 
.admin-table {
  min-width: 100%;
  border-collapse: collapse;
}

.admin-table th,
.admin-table td {
  white-space: nowrap;
  padding: 10px 16px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

#adminActivitiesWrapper {
  max-height: 400px;  
  overflow-y: auto;
  margin-top: 10px;
  border-radius: 12px;
  box-shadow: inset 0 0 4px rgba(0,0,0,0.05);
}

 
#adminActivitiesWrapper::-webkit-scrollbar {
  width: 8px;
}
#adminActivitiesWrapper::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 10px;
}
#adminActivitiesWrapper::-webkit-scrollbar-track {
  background: transparent;
}


 
.themeBtn.back-btn {
  margin-bottom: 20px;
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 600;
  border-radius: 12px;
  transition: background 0.25s ease, transform 0.2s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}



 
body.dark-mode #adminFeedbackSection .admin-table tbody td {
  background-color: #1e1e1e;
  color: #eee;
}
body.chatgpt-mode #adminFeedbackSection .admin-table tbody td {
  background-color: #fff;
  color: #111;
}

.admin-section {
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 30px 25px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
  margin-top: 24px;
  color: #333;
}

.admin-section h3 {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 18px;
  color: #5e35b1;
}

.table-wrapper {
  max-height: 400px;
  overflow-y: auto;
  border-radius: 12px;
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.05);
}

.table-wrapper::-webkit-scrollbar {
  width: 8px;
}
.table-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(124, 77, 255, 0.4);
  border-radius: 4px;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  color: #333;
  font-size: 14px;
  border-radius: 14px;
  overflow: hidden;
  border-spacing: 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.admin-table th,
.admin-table td {
  padding: 12px 16px;
  border: 1px solid #ddd;
  text-align: left;
  vertical-align: top;
}

.admin-table thead {
  background: #7c4dff;
  color: white;
}

.admin-table tbody tr:nth-child(even) td {
  background-color: #faf5ff;
}

.admin-table tbody tr:hover td {
  background-color: #f1eaff;
}

 
#adminFeedbackBody:empty::after {
  content: "No feedback submitted yet.";
  display: block;
  text-align: center;
  padding: 40px;
  font-size: 15px;
  font-weight: 500;
  color: #999;
  background: #fff;
  border-radius: 0 0 14px 14px;
}

 
.themeBtn.back-btn {
  margin-bottom: 20px;
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 600;
  border-radius: 12px;
  transition: background 0.25s ease, transform 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}
body.chatgpt-mode .modal-box,
body.chatgpt-mode .admin-section {
  background: #f1f1f1;
  color: #111;
}
body.chatgpt-mode .admin-table {
  background-color: #ffffff;
  color: #222;
}
body.chatgpt-mode .admin-table thead {
  background-color: #333;
  color: #fff;
}
body.chatgpt-mode .themeBtn.back-btn {
  background: #333;
  color: white;
}
body.chatgpt-mode .themeBtn.back-btn:hover {
  background: #555;
  transform: translateX(-2px);
}

 
body.dark-mode .modal-box,
body.dark-mode .admin-section {
  background: #2c2c2c;
  color: #eee;
}
body.dark-mode .admin-table {
  background-color: #2a2a2a;
  color: #eee;
}
body.dark-mode .admin-table thead {
  background-color: #444;
  color: #fff;
}
body.dark-mode .themeBtn.back-btn {
  background: #555;
  color: white;
}
body.dark-mode .themeBtn.back-btn:hover {
  background: #777;
  transform: translateX(-2px);
}

 
body:not(.chatgpt-mode):not(.dark-mode) .themeBtn.back-btn {
  background: #7c4dff;
  color: white;
}
body:not(.chatgpt-mode):not(.dark-mode) .themeBtn.back-btn:hover {
  background: #5e35b1;
  transform: translateX(-2px);
}

 
body.chatgpt-mode .back-btn {
  background: #333;
  color: white;
}
body.chatgpt-mode .back-btn:hover {
  background: #555;
  transform: translateX(-2px);
}

 
body.dark-mode .back-btn {
  background: #555;
  color: white;
}
body.dark-mode .back-btn:hover {
  background: #777;
  transform: translateX(-2px);
}


 
.settings-title {
  margin-top: 0;
  font-size: 18px;
  color: #5e35b1;
  font-weight: bold;
  margin-left: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}

body.chatgpt-mode .settings-title,
body.chatgpt-mode #settingsBackBtn {
  color: #333;
}

body.dark-mode .settings-title,
body.dark-mode #settingsBackBtn {
  color: #90caf9;
}

#settingsBackBtn {
  position: absolute;
  top: 14px;
  left: 6px;
  background: transparent;
  border: none;
  font-size: 18px;
  cursor: pointer;
  font-weight: bold;
  transition: transform 0.2s ease;
  color: #7c4dff;
}

#settingsBackBtn:hover {
  transform: translateX(-3px);
}

#feedbackModal {
  display: none;
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  background: #fff;
  padding: 24px 20px;  
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(124, 77, 255, 0.3);
  z-index: 9999;
  width: 90%;
  max-width: 420px;
  font-family: 'Poppins', sans-serif;
  box-sizing: border-box;  
}

#feedbackModal * {
  box-sizing: border-box;
}

#profileModal,
#settingsModal,
#feedbackModal {
  z-index: 9999;
}

.modal-box {
  position: absolute;
  top: 60px;
  right: 30px;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(15px);
  padding: 24px 20px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(124, 77, 255, 0.3);
  width: 90%;
  max-width: 420px;
  font-family: 'Poppins', sans-serif;
  color: #333;
  animation: fadeIn 0.3s ease-in-out;
}

 
body.modal-open .input-area {
  display: none !important;
}


 
.profile-modal-anchored {
  position: absolute;
  top: 65px;  
  right: 20px;
  width: 260px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(16px);
  border-radius: 18px;
  padding: 20px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  z-index: 1001;
  animation: dropdownFade 0.25s ease-in-out;
}

 
body.dark-mode .profile-modal-anchored {
  background: rgba(18, 18, 18, 0.85);
  color: #eee;
}

body.chatgpt-mode .profile-modal-anchored {
  background: #f5f5f5;
  color: #111;
}

 
@keyframes dropdownFade {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}




@keyframes fadeIn {
  from { opacity: 0; transform: translate(-50%, -30%); }
  to { opacity: 1; transform: translate(-50%, 0); }
}

#feedbackModal h3 {
  font-size: 18px;
  font-weight: bold;
  color: #5e35b1;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 0;
  margin-bottom: 14px;
}

#feedbackInput {
  background: #f3e8ff;
  color: #333;
  border: 1px solid #aaa;
  padding: 10px;
  border-radius: 10px;
  font-size: 14px;
  resize: vertical;
  min-height: 100px;
}

#feedbackModal button {
  margin-top: 16px;
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
  font-weight: bold;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.3s ease;
}

#feedbackModal button:first-child {
  background: #7c4dff;
  color: white;
  margin-right: 10px;
}

#feedbackModal button:first-child:hover {
  background: #5e35b1;
}

#feedbackModal button:last-child {
  background: transparent;
  border: 1px solid #ccc;
  color: #333;
}

#feedbackModal button:last-child:hover {
  background: #eee;
}

body.chatgpt-mode #feedbackModal {
  background: #fefefe;
  color: #111;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

body.chatgpt-mode #feedbackModal h3 {
  color: #333;
  font-weight: bold;
}

body.chatgpt-mode #feedbackInput {
  background: #f1f1f1;
  color: #111;
  border: 1px solid #ccc;
}

body.chatgpt-mode #feedbackModal button:first-child {
  background: #333;
  color: #fff;
  font-weight: bold;
  border: none;
}

body.chatgpt-mode #feedbackModal button:first-child:hover {
  background: #555;
}

body.chatgpt-mode #feedbackModal button:last-child {
  background: transparent;
  color: #333;
  border: 1px solid #aaa;
}

body.chatgpt-mode #feedbackModal button:last-child:hover {
  background: #e0e0e0;
  color: #111;
}

body.dark-mode #feedbackModal {
  background: #2c2c2c;
  color: #f5f5f5;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

body.dark-mode #feedbackModal h3 {
  color: #bb86fc;
  font-weight: bold;
}

body.dark-mode #feedbackInput {
  background: #2b2b2b;
  color: #fff;
  border: 1px solid #555;
}

body.dark-mode #feedbackModal button:first-child {
  background: #7c4dff;
  color: #fff;
  font-weight: bold;
  border: none;
}

body.dark-mode #feedbackModal button:first-child:hover {
  background: #9a66ff;
}

body.dark-mode #feedbackModal button:last-child {
  background: transparent;
  color: #ccc;
  border: 1px solid #777;
}

body.dark-mode #feedbackModal button:last-child:hover {
  background: #3a3a3a;
  color: #fff;
}

 
.admin-section {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 24px;
  margin-top: 20px;
  color: #fff;
  font-family: 'Poppins', sans-serif;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.admin-section h3 {
  font-size: 22px;
  margin-bottom: 16px;
  color: #fff;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 32px;
}

.admin-table th,
.admin-table td {
  border: 1px solid #d2baff;
  padding: 10px;
  text-align: center;
}

.admin-table th {
  background-color: #7c4dff;
  color: white;
}

body.chatgpt-mode .admin-table th {
  background: #333;
  color: white;
}

body.dark-mode .admin-table th {
  background: #444;
  color: white;
}


.admin-table tbody tr:nth-child(even) {
  background-color: rgba(255, 255, 255, 0.05);
}

.admin-section {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 24px;
  color: #fff;
  font-family: 'Poppins', sans-serif;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.1);
  margin: 30px auto;
  width: 100%;
  max-width: 1000px;
}

.admin-section h3 {
  font-size: 22px;
  margin-bottom: 16px;
  color: #fff;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 32px;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  overflow: hidden;
}

.admin-table th,
.admin-table td {
  border: 1px solid #d2baff;
  padding: 10px;
  text-align: center;
  font-size: 14px;
}

.admin-table th {
  background-color: #7c4dff;
  color: white;
}

.admin-table td {
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
}

 
.admin-section {
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 24px;
  font-family: 'Poppins', sans-serif;
  margin: 30px auto;
  width: 100%;
  max-width: 1000px;
}

.admin-section h3 {
  font-size: 22px;
  margin-bottom: 16px;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 32px;
  border-radius: 12px;
  overflow: hidden;
  font-size: 14px;
}

.admin-table th,
.admin-table td {
  border: 1px solid;
  padding: 10px;
  text-align: center;
}

@media (max-width: 768px) {
  .admin-table td,
  .admin-table th {
    font-size: 12px;
    padding: 6px;
  }
}

 
body.pastel .admin-section {
  background: rgba(243, 232, 255, 0.3);
  color: #4a148c;
}

body.pastel .admin-table th {
  background-color: #7c4dff;
  color: white;
  border-color: #d2baff;
}

body.pastel .admin-table td {
  background-color: rgba(255, 255, 255, 0.3);
  color: #4a148c;
  border-color: #d2baff;
}

 
body.dark .admin-section {
  background: rgba(30, 30, 30, 0.6);
  color: #eee;
}

body.dark .admin-table th {
  background-color: #333;
  color: #fff;
  border-color: #555;
}

body.dark .admin-table td {
  background-color: rgba(255, 255, 255, 0.05);
  color: #ccc;
  border-color: #444;
}

 
body.chatgpt .admin-section {
  background: #f5f5f5;
  color: #222;
}

body.chatgpt .admin-table th {
  background-color: #2e7d32;
  color: #fff;
  border-color: #c8e6c9;
}

body.chatgpt .admin-table td {
  background-color: #ffffff;
  color: #222;
  border-color: #c8e6c9;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  font-size: 14px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.admin-table th, .admin-table td {
  padding: 10px;
  text-align: left;
  border: 1px solid #ddd;
  word-break: break-word;
}

.admin-table thead tr {
  background-color: var(--header-bg);
  color: var(--header-color);
}

body.pastel {
  --header-bg: #7c4dff;
  --header-color: white;
}

body.chatgpt {
  --header-bg: #e0e0e0;
  --header-color: #333;
}

body.dark {
  --header-bg: #222;
  --header-color: #fff;
}

.admin-table {
  overflow-x: auto;
  display: block;
}

.table-wrapper {
  max-height: 250px;
  overflow-y: auto;
  margin-bottom: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

 
.table-wrapper::-webkit-scrollbar {
  width: 8px;
}
.table-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(140, 120, 255, 0.4);
  border-radius: 4px;
}
.table-wrapper::-webkit-scrollbar-track {
  background: transparent;
}

 
.admin-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  background: var(--admin-bg);
  color: var(--admin-text);
}

.admin-table th,
.admin-table td {
  padding: 10px 12px;
  text-align: left;
  border-bottom: 1px solid var(--admin-border);
}

.admin-table thead {
  background: var(--admin-header);
  color: var(--admin-header-text);
}

 
:root {
  --admin-bg: #f5f0ff;
  --admin-text: #333;
  --admin-border: #ddd;
  --admin-header: #7c4dff;
  --admin-header-text: #fff;
}
body.theme-dark {
  --admin-bg: #1f1f1f;
  --admin-text: #e0e0e0;
  --admin-border: #333;
  --admin-header: #5e35b1;
  --admin-header-text: #fff;
}
body.theme-chatgpt {
  --admin-bg: #ffffff;
  --admin-text: #222;
  --admin-border: #ccc;
  --admin-header: #10a37f;
  --admin-header-text: #fff;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 32px;
  overflow-x: auto;
  display: block;
  border-radius: 12px;
}

.admin-table th, .admin-table td {
  padding: 12px 14px;
  border: 1px solid #ddd;
  text-align: left;
  font-size: 14px;
  color: #333;
  background: white;
}

.admin-table thead th {
  background: #7c4dff;
  color: white;
  position: sticky;
  top: 0;
  z-index: 2;
}

 
body.chatgpt-mode .admin-table th,
body.chatgpt-mode .admin-table td {
  background: #f5f5f5;
  color: #222;
  border: 1px solid #aaa;
}

 
body.dark-mode .admin-table th,
body.dark-mode .admin-table td {
  background: #2b2b2b;
  color: #eee;
  border: 1px solid #444;
}


.admin-section h3 {
  font-weight: 700;
  font-size: 20px;
  margin-bottom: 12px;
  color: #4c2b8f;
}

.table-wrapper {
  max-height: 260px;
  overflow-y: auto;
  margin-bottom: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  color: #333;
  border-radius: 10px;
  overflow: hidden;
  font-size: 14px;
}

.admin-table thead tr {
  background: #7c4dff;
  color: white;
}

.admin-table th,
.admin-table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

body.chatgpt-mode .admin-table {
  background: #f7f7f7;
  color: #000;
}

body.chatgpt-mode .admin-table thead {
  background: #333;
}

body.dark-mode .admin-table {
  background: #222;
  color: #eee;
}

body.dark-mode .admin-table thead {
  background: #444;
}


.table-wrapper {
  max-height: 400px;
  overflow-y: auto;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 32px;
}

 
.admin-table th,
.admin-table td {
  padding: 10px;
  text-align: left;
  border: 1px solid #ddd;
  font-size: 14px;
}

body.dark-mode .admin-table {
  background-color: #222;
  color: #eee;
}

body.chatgpt-mode .admin-table {
  background-color: #f9f9f9;
  color: #111;
}


@media (max-width: 768px) {
  .admin-table td, .admin-table th {
    font-size: 12px;
    padding: 6px;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 0;
  }

  .sidebar-navigator {
    left: 0 !important;
  }
}

@media (max-width: 768px) {
  .sidebar-navigator {
    top: 12px;
    width: 40px;
    height: 40px;
    font-size: 22px;
  }
}

    @keyframes slideIn {
      from { transform: translateY(10px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
