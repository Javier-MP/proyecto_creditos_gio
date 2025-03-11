document.getElementById('creditoForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Limpiar mensajes de error
    document.querySelectorAll('.error').forEach(el => el.textContent = '');

    const cliente = document.getElementById('cliente').value.trim();
    const monto = parseFloat(document.getElementById('monto').value);
    const tasa_interes = parseFloat(document.getElementById('tasa_interes').value);
    const plazo = parseInt(document.getElementById('plazo').value);
    const fecha_otorgamiento = document.getElementById('fecha_otorgamiento').value;

    let valid = true;

    // Validaciones
    if (cliente === "") {
        document.getElementById('clienteError').textContent = 'El nombre del cliente es obligatorio.';
        valid = false;
    }
    if (monto <= 0) {
        document.getElementById('montoError').textContent = 'El monto debe ser mayor a 0.';
        valid = false;
    }
    if (tasa_interes < 0) {
        document.getElementById('tasaError').textContent = 'La tasa de interés no puede ser negativa.';
        valid = false;
    }
    if (plazo <= 0) {
        document.getElementById('plazoError').textContent = 'El plazo debe ser mayor a 0.';
        valid = false;
    }
    if (!fecha_otorgamiento) {
        document.getElementById('fechaError').textContent = 'La fecha de otorgamiento es obligatoria.';
        valid = false;
    }

    if (valid) {
        const data = {
            cliente,
            monto,
            tasa_interes,
            plazo,
            fecha_otorgamiento
        };
        fetch('/creditos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Aquí puedes agregar código para actualizar la tabla
        });
    }
});