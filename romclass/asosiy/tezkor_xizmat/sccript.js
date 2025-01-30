// JavaScript fayli: sccript.js

let map;

const viloyatlar = ["Toshkent", "Andijon", "Buxoro", "Fargʻona", "Jizzax", "Namangan", "Navoiy", "Qashqadaryo", "Samarqand", "Sirdaryo", "Surxondaryo", "Xorazm", "Qoraqalpogʻiston"];
const viloyatSelect = document.getElementById("viloyat");

// Viloyat ro'yxatini yuklash
viloyatlar.forEach(v => {
    const option = document.createElement("option");
    option.value = v.toLowerCase();
    option.textContent = v;
    viloyatSelect.appendChild(option);
});

// Geolokatsiya orqali viloyatni aniqlash
function joylashuvniAniqlash() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;

                // Xaritani yaratish
                if (!map) {
                    map = L.map('map').setView([latitude, longitude], 15);
                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '© OpenStreetMap contributors'
                    }).addTo(map);
                } else {
                    map.setView([latitude, longitude], 15);
                }

                // Marker qo'shish
                L.marker([latitude, longitude]).addTo(map)
                    .bindPopup('Sizning joylashuvingiz')
                    .openPopup();

                // Viloyatni aniqlash
                fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);  // API javobini ko'rsatish
                        const location = data.address.state?.toLowerCase().trim();
                        if (viloyatlar.map(v => v.toLowerCase()).includes(location)) {
                            viloyatSelect.value = location;
                            document.getElementById("natija").textContent = `Sizning viloyatingiz: ${location.toUpperCase()}`;
                        } else {
                            document.getElementById("natija").textContent = "Joylashuv aniqlanmadi!";
                        }
                    })
                    .catch(() => {
                        document.getElementById("natija").textContent = "Ma'lumotlarni olishda xatolik!";
                    });
            },
            () => {
                alert("Geolokatsiya yoqilmagan yoki ruxsat berilmagan!");
            }
        );
    } else {
        alert("Brauzeringiz geolokatsiyani qo‘llab-quvvatlamaydi!");
    }
}
