const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

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
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
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
                }
            }
        });
    });
});