const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const points = [];

canvas.addEventListener('click', event => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    points.push({ x, y });
    drawPoint(x, y);
});

function drawPoint(x, y) {
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(x, y, 3, 0, Math.PI * 2);
    ctx.fill();
}

document.getElementById('clearBtn').addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    points.length = 0;
});

document.getElementById('addBtn').addEventListener('click', () => {
    console.log('Puntos actuales:', points);
});
