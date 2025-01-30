// Elementlarni tanlab olish
const locateBtn = document.getElementById("locateBtn");
const statusText = document.getElementById("status");
const latitudeText = document.getElementById("latitude");
const longitudeText = document.getElementById("longitude");
const locationNameText = document.getElementById("locationName");
const resultDiv = document.getElementById("result");
const mapIframe = document.getElementById("map");

// Geolokatsiyani aniqlash
locateBtn.addEventListener("click", () => {
    statusText.textContent = "Joylashuvingiz aniqlanmoqda...";
    statusText.style.color = "#3498db";

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            async (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                // Koordinatalarni ko'rsatish
                latitudeText.textContent = latitude;
                longitudeText.textContent = longitude;

                // Joy nomini aniqlash (Reverse Geocoding)
                try {
                    const locationName = await getLocationName(latitude, longitude);
                    locationNameText.textContent = locationName;
                } catch (error) {
                    locationNameText.textContent = "Joy nomini aniqlab bo'lmadi.";
                    console.error("Xatolik:", error);
                }

                // Xaritani yuklash
                mapIframe.src = `https://maps.google.com/maps?q=${latitude},${longitude}&z=15&output=embed`;

                // Natijani ko'rsatish
                resultDiv.style.display = "block";
                statusText.textContent = "Joylashuvingiz muvaffaqiyatli aniqlandi!";
                statusText.style.color = "#27ae60";
            },
            (error) => {
                // Geolokatsiya xatoliklari
                let errorMessage = "Joylashuvingizni aniqlashda xatolik yuz berdi.";
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        errorMessage = "Geolokatsiya ruxsati rad etildi. Iltimos, brauzer sozlamalaridan ruxsat bering.";
                        break;
                    case error.POSITION_UNAVAILABLE:
                        errorMessage = "Joylashuv ma'lumotlari mavjud emas.";
                        break;
                    case error.TIMEOUT:
                        errorMessage = "Joylashuvni aniqlash vaqti tugadi.";
                        break;
                }
                statusText.textContent = errorMessage;
                statusText.style.color = "#c0392b";
                console.error("Xatolik:", error);
            }
        );
    } else {
        statusText.textContent = "Brauzeringiz geolokatsiyani qo'llab-quvvatlamaydi.";
        statusText.style.color = "#c0392b";
    }
});

// Reverse Geocoding (Joy nomini aniqlash)
async function getLocationName(latitude, longitude) {
    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`;
    const response = await fetch(url);
    const data = await response.json();

    if (data.display_name) {
        return data.display_name;
    } else {
        throw new Error("Joy nomi topilmadi.");
    }
}