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

    const saveInfo = $('#id-save-info').is('checked');
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    const url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        postal_code: $.trim(form.postcode.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
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
    }).fail(function () {
        // Reload page to show the error from Django messages
        location.reload();
    });
});