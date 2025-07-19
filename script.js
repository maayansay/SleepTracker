function saveId() {
  const id = document.getElementById('participantId').value;
  if (id) {
    localStorage.setItem('participantId', id);
    showSleepSection();
  }
}

function showSleepSection() {
  const id = localStorage.getItem('participantId');
  if (id) {
    document.getElementById('idInputSection').style.display = 'none';
    document.getElementById('sleepSection').style.display = 'block';
    document.getElementById('storedId').innerText = id;
  }
}

function goToSleep() {
  const id = localStorage.getItem('participantId');
  const timestamp = new Date().toISOString();
  fetch('https://api.github.com/repos/YOUR_USERNAME/sleep-tracker/issues', {
    method: 'POST',
    headers: {
      'Authorization': 'token YOUR_GITHUB_TOKEN',
      'Accept': 'application/vnd.github+json'
    },
    body: JSON.stringify({
      title: `Sleep Entry: ${id}`,
      body: JSON.stringify({ participant_id: id, timestamp: timestamp })
    })
  }).then(() => alert("Sleep time logged."));
}

window.onload = showSleepSection;
