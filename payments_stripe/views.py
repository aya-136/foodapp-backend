import stripe
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from firebase_config import db

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def process_payment(request):
    order_id = request.data.get('order_id')
    payment_method_id = request.data.get('payment_method_id')

    if not order_id or not payment_method_id:
        return Response({"error": "order_id and payment_method_id required"}, status=400)

    order_ref = db.collection('orders').document(order_id)
    order_doc = order_ref.get()
    if not order_doc.exists:
        return Response({"error": "Order not found"}, status=404)

    order = order_doc.to_dict()
    amount = int(order.get('total', 0) * 100)

    try:
        intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
        payment_method=payment_method_id,
        confirm=True,
        automatic_payment_methods={
            "enabled": True,
            "allow_redirects": "never"
        },
        metadata={'order_id': order_id}

        )
        if intent.status == 'succeeded':
            order_ref.update({"paymentStatus": "completed"})
            return Response({"success": True, "payment_id": intent.id, "message": "Payment successful"})
        else:
            return Response({"success": False, "payment_id": intent.id, "message": f"Payment status: {intent.status}"}, status=400)
    except stripe.error.StripeError as e:
        return Response({"success": False, "message": str(e)}, status=400)

@api_view(['POST'])
def create_payment_intent(request):
    amount = request.data.get("amount")
    if not amount:
        return Response({"error": "amount required"}, status=400)

    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        return Response({"success": True, "client_secret": intent.client_secret})
    except stripe.error.StripeError as e:
        return Response({"success": False, "message": str(e)}, status=400)
