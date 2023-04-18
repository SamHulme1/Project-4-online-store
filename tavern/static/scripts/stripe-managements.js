const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

// functionality for this comes from stripe documentation 
// https://stripe.com/docs

$( document ).ready(function() {
    let stripe = Stripe(stripePublicKey);
    let elements = stripe.elements();
    let card = elements.create("card");
    card.mount('#card-element');

    card.on('change', function(event) {
        let displayError = document.getElementById('card-errors');
        if (event.error) {
          displayError.textContent = event.error.message;
        } else {
          displayError.textContent = '';
        }
    });

    const form = document.getElementById('payment-form');
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-btn').attr('disabled', true);
        let saveInfo = Boolean($('#id-save-info').attr('checked'));
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        let url = '/checkout/cache_checkout_session/';
        $.post(url, postData).done(function() {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.first_name.value) + $.trim(form.last_name.value), 
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address: {
                            line1: $.trim(form.address.value),
                            city: $.trim(form.city.value), 
                            country: $.trim(form.country.value), 
                            state: $.trim(form.county.value)
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.first_name.value) + ' ' + $.trim(form.last_name.value), 
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.address.value),
                        city: $.trim(form.city.value), 
                        country: $.trim(form.country.value), 
                        state: $.trim(form.county.value),
                        postal_code: $.trim(form.postcode.value)
                    }
                }
            }).then(function(result) {
                if (result.error) {
                    let displayError = document.getElementById('card-errors');
                    displayError.textContent = result.error.message;
                    card.update({'disabled': false});
                    $('#submit-btn').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    } else {
    
                    }
                }
            });
        }).fail(function () {
            location.reload();
        });
    });
});