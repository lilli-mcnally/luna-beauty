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
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    $('#lb-loading').fadeToggle(100);

    const saveInfo = Boolean($('#id-save-info').attr('checked'));
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                first_name: $.trim(form.first_name.value),
                last_name: $.trim(form.last_name.value),
                email: $.trim(form.email.value),
                phone: $.trim(form.phone.value),
                address: {
                    street_address1: $.trim(form.street_address1.value),
                    street_address2: $.trim(form.street_address2.value),
                    town_or_city: $.trim(form.town_or_city.value),
                    county: $.trim(form.county.value),
                    country: $.trim(form.country.value),
                }
            }
        },
        shipping: {
            first_name: $.trim(form.first_name.value),
            last_name: $.trim(form.last_name.value),
            phone: $.trim(form.phone.value),
            address: {
                street_address1: $.trim(form.street_address1.value),
                street_address2: $.trim(form.street_address2.value),
                town_or_city: $.trim(form.town_or_city.value),
                county: $.trim(form.county.value),
                postcode: $.trim(form.postcode.value),
                country: $.trim(form.country.value),
            }
        }
    }).then(function (result) {
        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            const html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#lb-loading').fadeToggle(100);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});