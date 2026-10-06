let direction = "en-te";

const englishToTelugu = document.getElementById("englishToTelugu");
const teluguToEnglish = document.getElementById("teluguToEnglish");

const inputText = document.getElementById("inputText");
const translateButton = document.getElementById("translateButton");
const result = document.getElementById("result");


englishToTelugu.addEventListener("click", function () {

    direction = "en-te";

    englishToTelugu.classList.add("active");
    teluguToEnglish.classList.remove("active");

    inputText.placeholder = "Enter an English sentence...";

});


teluguToEnglish.addEventListener("click", function () {

    direction = "te-en";

    teluguToEnglish.classList.add("active");
    englishToTelugu.classList.remove("active");

    inputText.placeholder = "తెలుగు వాక్యాన్ని ఇక్కడ నమోదు చేయండి...";

});


translateButton.addEventListener("click", async function () {

    const text = inputText.value.trim();

    if (!text) {
        result.textContent = "Please enter a sentence.";
        return;
    }

    result.textContent = "Translating...";

    try {

        const response = await fetch("/translate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text,
                direction: direction
            })

        });

        const data = await response.json();

        if (data.error) {
            result.textContent = data.error;
        } else {
            result.textContent = data.translation;
        }

    } catch (error) {

        result.textContent =
            "Something went wrong. Please try again.";

    }

});