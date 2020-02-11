$(function() {
    console.log("in stripe.js: ");
    $("#payment-form").submit(function() {
        console.log("submitting payment");
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
        alert("before card");
        for(let item in card) {
            alert(item + item.val());
        }
        alert("after card");
        Stripe.createToken(card, function(status, response) {
            console.log('In stripe create token: ' + status);
            if(status === 200) {
                console.log("in the 200");
                $("#credit-card-errors").hide();
                $("#id_stripe_id").val(response.id);

                // Prevent the credit card details from being submitted to our server
                $("#id_credit_card_number").removeAttr('name');
                $("#id_cvv").removeAttr('name');
                $("#id_expiry_month").removeAttr('name');
                $("#id_expiry_year").removeAttr('name');

                form.submit();
            } else {
                console.log("in the else");
                $("#stripe-error-message").text(response.error.message);
                $("#credit-card-errors").show();
                $("#validate_card_btn").attr("disabled", false);
            }
        });
        return false;
    });
    console.log("at the end")
});