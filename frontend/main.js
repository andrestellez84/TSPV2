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

document.getElementById('addBtn').addEventListener('click', async () => {
    if (points.length < 2) {
        alert('Debes agregar al menos dos puntos');
        return;
    }

    const coordinates = points.map(p => [p.x, p.y]);
    try {
        const response = await fetch('/api/solve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ coordinates })
        });
        const data = await response.json();
        if (data.route) {
            drawRoute(data.route);
            console.log('Ruta óptima:', data.route);
        } else {
            console.error('Respuesta inesperada de la API', data);
        }
    } catch (err) {
        console.error('Error al llamar a /api/solve', err);
    }
});

function drawRoute(route) {
    if (!route || route.length === 0) return;
    ctx.strokeStyle = 'blue';
    ctx.beginPath();
    const start = points[route[0]];
    ctx.moveTo(start.x, start.y);
    for (let i = 1; i < route.length; i++) {
        const p = points[route[i]];
        ctx.lineTo(p.x, p.y);
    }
    ctx.stroke();
}
