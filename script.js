function goToSleep() {
  const id = localStorage.getItem("participantId");
  const timestamp = new Date().toISOString();

  fetch("https://sleeptrackerproxy.sleeptracker.workers.dev", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ participant_id: id, timestamp })
  })
  .then(() => alert("Sleep time logged"))
  .catch(() => alert("Failed to log sleep"));
}
