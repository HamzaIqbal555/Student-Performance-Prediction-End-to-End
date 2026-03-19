// Dynamic prediction with AJAX - form persists, no reload

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictForm");
    const resetBtn = document.getElementById("resetBtn");
    const resultDiv = document.getElementById("result");

    // Reset handler
    if (resetBtn) {
        resetBtn.onclick = function () {
            form.reset();
            if (resultDiv) resultDiv.style.display = "none";
        };
    }

    // Show result if present (server-rendered)
    if (resultDiv && resultDiv.style.display !== "none") {
        resultDiv.style.display = "block";
    }

    // AJAX predict handler
    if (form) {
        form.addEventListener("submit", async function (e) {
            e.preventDefault();

            const formData = new FormData(form);
            const submitBtn = form.querySelector("button[type='submit']");
            const originalText = submitBtn.textContent;

            // Loading state
            submitBtn.textContent = "Predicting...";
            submitBtn.disabled = true;
            if (resultDiv) resultDiv.style.display = "none";

            try {
                const response = await fetch("/", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                });

                if (!response.ok) {
                    throw new Error("Prediction failed");
                }

                const data = await response.json();
                if (resultDiv) {
                    document.getElementById("scoreValue").textContent = data.results;
                    resultDiv.style.display = "block";
                }
            } catch (error) {
                alert("Prediction error: " + error.message);
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        });
    }
});
