document.addEventListener("DOMContentLoaded", function () {
    const text = "Parallel Skies";
    const target = document.getElementById("typing-title");
    let i = 0;
    const speed = 100;

    target.textContent = ""; // reset content if needed

    function typeWriter() {
        if (i < text.length) {
            target.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        } else {
            target.classList.add("done-typing"); // ✅ triggers CSS rule
        }
    }

    typeWriter();
});
