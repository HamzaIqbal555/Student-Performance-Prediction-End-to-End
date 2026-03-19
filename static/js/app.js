// Simple working JS - reset & show result

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("resetBtn").onclick = function () {
        document.querySelector("form").reset();
        document.getElementById("result").style.display = "none";
    };
    // Show result if present
    const result = document.getElementById("result");
    if (result) result.style.display = "block";
});
