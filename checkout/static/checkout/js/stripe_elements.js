const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#32325d"
        }
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};
const card = elements.create('card', {
    style: style
});
card.mount('#card-element');

card.addEventListener('change', function (event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        console.log(event.error.message)
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>
                ${event.error.message}
            </span>
            `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// When form is submitted
const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    console.log('0')
    ev.preventDefault();
    console.log('1')
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    console.log('2')
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        console.log('3')
        if (result.error) {
            console.log('4')
            const errorDiv = document.getElementById('card-errors');
            const html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            console.log('5')
            if (result.paymentIntent.status === 'succeeded') {
                console.log('6')
                form.submit();
            }
        }
    });
});