document.getElementById('romForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Formaning standart yuborilishini to'xtatish

    // Qiymatlarni olish
    const height = parseFloat(document.getElementById('height').value);
    const width = parseFloat(document.getElementById('width').value);
    const material = document.getElementById('material').value;
    const company = document.getElementById('company').value;

    // Material va kompaniya narxlari
    const prices = {
        aluminiy: { akfa: 150000, alutex: 170000, alpro: 160000 },
        plastik: { akfa: 100000, alutex: 120000, alpro: 110000 }
    };

    // Tanlangan material va kompaniya uchun narxni olish
    const pricePerSquareMeter = prices[material][company];

    // Rom maydoni va umumiy narxni hisoblash
    const area = height * width;
    const totalPrice = area * pricePerSquareMeter;

    // Natijani ko'rsatish
    document.getElementById('result').innerHTML = `
        Rom maydoni: ${area.toFixed(2)} m²<br>
        Material: ${material.charAt(0).toUpperCase() + material.slice(1)}<br>
        Kompaniya: ${company.charAt(0).toUpperCase() + company.slice(1)}<br>
        Umumiy narx: ${totalPrice.toLocaleString()} so'm
    `;
});
